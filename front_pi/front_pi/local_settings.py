from pathlib import Path

DJANGO_SECRET_KEY = 'django-insecure-mws8w#9=8i)twc#hvw1*t1j2nc!p^#11#a=j8&ac64m%$3ll37'

API_URL = 'http://localhost:8080'

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE_CONN = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MYSQL_CONN = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pi-front',
        'USER': 'doadmin',
        'PASSWORD': 'AVNS_HgycckrPE9yG15Kx71b',
        'HOST': 'db-pi-ifsc-do-user-12216598-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

AWS_ACCESS_KEY_ID = "AKIA33NCIWARIHVMKVVA"

AWS_SECRET_ACCESS_KEY = "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"

AWS_STORAGE_BUCKET_NAME = "s3-ifsc"

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_S3_FILE_OVERWRITE = False  

AWS_DEFAULT_ACL = None  

AWS_S3_ADDRESSING_STYLE = "virtual"