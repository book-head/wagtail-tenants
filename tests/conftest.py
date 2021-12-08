import os

from django.conf import settings
from wagtail import VERSION as WAGTAIL_VERSION

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pytest_plugins = 'tests.fixtures'


def pytest_configure():
    wagtail_apps = [
        'wagtail.contrib.forms',
        'wagtail.contrib.redirects',
        'wagtail.embeds',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.snippets',
        'wagtail.documents',
        'wagtail.images',
        'wagtail.search',
        'wagtail.admin',
        'wagtail.core',
    ]
    if WAGTAIL_VERSION >= (2, 9):
        wagtail_middleware = [
            'wagtail.contrib.redirects.middleware.RedirectMiddleware',
        ]
    else:
        wagtail_middleware = [
            'wagtail.core.middleware.SiteMiddleware',
            'wagtail.contrib.redirects.middleware.RedirectMiddleware',
        ]

    settings.configure(
        SECRET_KEY="secret_for_testing_only",
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        },
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

        ] + wagtail_apps + [

            'modelcluster',
            'taggit',

            'tests',
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ] + wagtail_middleware,
        ROOT_URLCONF='tests.urls',
        ALLOWED_HOSTS='*',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(BASE_DIR, 'templates'),
                ],
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                    'loaders': [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ]
                },
            },
        ],
        WAGTAIL_SITE_NAME='Wagtail Tenants',
    )