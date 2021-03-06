"""
Django settings for XSproject project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import logging
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from logging import FileHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 引入sources root目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'extapps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xi)8*x8c@7=(om%+0_2r-tk_fw@eu)=l+*6$70tci&^_-=8$kv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'xadmin',
    'crispy_forms',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artapp',
    'userapp',
    'DjangoUeditor',
    'djcelery',  # django-celery的应用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'XSproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'XSproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 静态文件存放的位置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 多媒体文件（图片、视频、音频、表格等文件）
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/ups')

# 多媒体文件资源请求的路径位置
MEDIA_URL = '/static/ups/'

# 配置session方案(默认存在数据库中)


# 配置Cache缓存方案－Redis
# 安装 django-redis: pip install django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# 配置django 日志输出
LOGGING = {
    'version': 1.0,
    'disable_existing_loggers': False,
    'formatters': {  # 日志格式化
        'verbose': {
            'format': '[%(asctime)s %(module)s %(funcName)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '[%(asctime)s %(funcName)s -> %(lineno)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {  # 日志处理器
        'console': {  # 控制台输出
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file_log': {  # 将日志写入到文件中
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'xs_app.log',
            'level': 'INFO',
            'formatter': 'verbose',
        }
    },
    'loggers': {  # 日志对象
        'inf': {
            'handlers': ['console', 'file_log'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# 获取inf 日志对象
logger = logging.getLogger('inf')


##### Django-Celery配置 #####
import djcelery
from celery.schedules import crontab, timedelta

# 装载当前项目中的celery任务
djcelery.setup_loader()

BROKER_URL = 'redis://127.0.0.1:6379/10'  # 任务中间代理地址－任务队列

# 导入celery任务
CELERY_IMPORTS = ('artapp.tasks',)

# 设置celery的时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 设置celery计划类型
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# 设置定时任务
CELERYBEAT_SCHEDULE = {
    u'发送邮件': {
        'task': 'artapp.tasks.sendMail',
        'schedule': timedelta(seconds=2),
        'args': ('610039018@qq.com', '测试'),
    }
}

######--- Django-Celery配置 end----- #######