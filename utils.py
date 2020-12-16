import datetime
import hashlib
import hmac
import urllib
from django.conf import settings


def fix_hk_s3_url(url):
    """This method fixes the url returned by the boto3 library because the library is buggy when dealing with ap-east-1
    (Hong Kong) S3 buckets.

    Parameters:
        url (str): the original url

    Returns:
        url (str): the fixed url
    """
    if settings.AWS_S3_REGION_NAME == 'ap-east-1':
        url = url[:url.find('.amazon')] + '.ap-east-1' + url[url.find('.amazon'):]
    return url


# Taken form https://stackoverflow.com/questions/50213740/aws-s3-presigned-urls-with-boto3-signature-mismatch.
# just some rant. The boto3 signing function did work. Spent countless of hours reading boto3's documentation,
# googleing stuff, debug and debug and trying to look for workaround. Turns out the boto3 library itself is broken!!!!

ENCODING = 'utf8'
SEVEN_DAYS = 604800

def sign(key, msg):
    return hmac.new(key, msg.encode(ENCODING), hashlib.sha256).digest()



def get_signature_key(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode(ENCODING), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning


def generate_presigned_s3_get(bucket, object_key, region, expires_in, access_key, secret_key):
    """The function that signs S3 get url. Should use this instead of the one in the boto3 library because the one
     signed by boto3 is buggy

     Parameters:
         bucket (str): The name of teh S3 bucket
         object_key (str): The key (as in the path) of the object in S3 to get
         region (str): The region name of the S3 bucket
         expires_in (int): The expire time of the signature in seconds
         access_key (str): S3 Access Key
         secret_key (str): S3 Secret Key

     Returns:
         The signed S3 url.

     """
    METHOD = 'GET'
    SERVICE = 's3'
    host = bucket + '.s3.' + region + '.amazonaws.com'
    endpoint = 'https://' + host
    t = datetime.datetime.utcnow()
    amz_date = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d')
    canonical_uri = '/' + object_key
    canonical_headers = 'host:' + host + '\n'
    signed_headers = 'host'
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = datestamp + '/' + region + '/' + SERVICE + '/' + 'aws4_request'
    canonical_querystring = '?X-Amz-Algorithm=AWS4-HMAC-SHA256'
    canonical_querystring += '&X-Amz-Credential=' + urllib.parse.quote_plus(access_key + '/' + credential_scope)
    canonical_querystring += '&X-Amz-Date=' + amz_date
    canonical_querystring += '&X-Amz-Expires=' + str(expires_in)
    canonical_querystring += '&X-Amz-SignedHeaders=' + signed_headers
    canonical_request = METHOD + '\n' + canonical_uri + '\n' + canonical_querystring[1:] + '\n' + canonical_headers + '\n' + signed_headers + '\nUNSIGNED-PAYLOAD'
    string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + '\n' + hashlib.sha256(canonical_request.encode(ENCODING)).hexdigest()
    signing_key = get_signature_key(secret_key, datestamp, region, SERVICE)
    signature = hmac.new(signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256).hexdigest()
    canonical_querystring += '&X-Amz-Signature=' + signature
    url = endpoint + canonical_uri + canonical_querystring
    return url
