"""
Django settings for main project.
"""

from pathlib import Path
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key-for-development')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Для красивых форм
    'crispy_forms',
    'crispy_bootstrap5',

    # Your apps
    'auth_app',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'auth_app.User'

# ============================================
# AUTHENTICATION & ALLAUTH
# ============================================
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Django Sites Framework
SITE_ID = 1

# ============================================
# ALLAUTH КОНФИГУРАЦИЯ
# ============================================

# Методы аутентификации
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Верификация email
ACCOUNT_EMAIL_VERIFICATION = 'optional' # или 'mandatory'

# Максимум email адресов на пользователя (опционально)
ACCOUNT_MAX_EMAIL_ADDRESSES = 2

# Настройки сессий
ACCOUNT_SESSION_REMEMBER = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30 дней
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ============================================
# РЕДИРЕКТЫ
# ============================================

# Основные редиректы
LOGIN_REDIRECT_URL = 'auth_app:profile'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

# ============================================
# EMAIL НАСТРОЙКИ (только один раз!)
# ============================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = "hubaibohdan258@gmail.com"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[MyApp] "

# ============================================
# SOCIALACCOUNT НАСТРОЙКИ
# ============================================

# Кастомные адаптеры
SOCIALACCOUNT_ADAPTER = 'auth_app.adapter.CustomSocialAccountAdapter'

# Автоматически связывать аккаунты по email
SOCIALACCOUNT_AUTO_SIGNUP = True

SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'

# КРИТИЧНО: Связывать существующие аккаунты по email
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True  # Использовать email для поиска существующего аккаунта
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True  # Автоматически связывать

# Требовать email от провайдера
SOCIALACCOUNT_QUERY_EMAIL = True

# Убрать промежуточную страницу OAuth
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'VERIFIED_EMAIL': True,  # Google email всегда подтверждён
    }
}

# ============================================
# ЛОГИРОВАНИЕ
# ============================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}