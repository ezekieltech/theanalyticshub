from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from whitenoise.storage import CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(ManifestStaticFilesStorage):
    manifest_strict = False