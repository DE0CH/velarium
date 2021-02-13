from abc import ABC
from storages.backends.s3boto3 import S3Boto3Storage
from utils import generate_presigned_url


class MediaStorage(S3Boto3Storage, ABC):

    def url(self, name, parameters=None, expire=None, http_method=None):
        if expire is None:
            expire = 3600
        response = generate_presigned_url(name, 600)
        return response

