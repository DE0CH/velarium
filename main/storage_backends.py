from storages.backends.s3boto3 import S3Boto3Storage
from utils import generate_presigned_s3_get
from django.conf import settings
from django.utils.encoding import filepath_to_uri


class MediaStorage(S3Boto3Storage):
    file_overwrite = False

    def url(self, name, parameters=None, expire=None, http_method=None):
        # Not sure what http_method will give, so default to https in all cases (there's not many reasons to use http).
        if expire is None:
            expire = 3600
        response = generate_presigned_s3_get(self.bucket.name, filepath_to_uri(name), settings.AWS_S3_REGION_NAME, expire, settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        return response

