from storages.backends.s3boto3 import S3Boto3Storage
from utils import generate_presigned_url
from django.conf import settings
from django.utils.encoding import filepath_to_uri


class MediaStorage(S3Boto3Storage):
    file_overwrite = False

    def url(self, name, parameters=None, expire=None, http_method=None):
        # Not sure what http_method will give, so default to https in all cases (there's not many reasons to use http).
        if expire is None:
            expire = 3600
        response = generate_presigned_url(name, 600)
        return response

