from django.conf import settings


settings.configure(
    DEBUG=True,
    TEMPLATE_DEBUG=True,
    SECRET_KEY='s3cr3t',
    # INSTALLED_APPS=[],
)


import django

if hasattr(django, 'setup'):
    django.setup()


SECRET_KEY = 's3cr3tssds'