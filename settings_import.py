#!/usr/bin/python
from os import getenv
import locale

# Read list of admins from $DOCKER_CRYPT_ADMINS env var
if getenv('DOCKER_CRYPT_ADMINS'):
    ADMINS = getenv('DOCKER_CRYPT_ADMINS').split(',')
else:
    ADMINS = (
                ('Admin User', 'admin@test.com')
             )

# Read the preferred time zone from $DOCKER_CRYPT_TZ, use system locale or
# set to 'America/New_York' if neither are set
if getenv('DOCKER_CRYPT_TZ'):
    if '/' in getenv('DOCKER_CRYPT_TZ'):
        TIME_ZONE = getenv('DOCKER_CRYPT_TZ')
    else: TIME_ZONE = 'America/New_York'
elif getenv('TZ'):
    TIME_ZONE = getenv('TZ')
else:
    TIME_ZONE = 'America/New_York'

# Read the preferred language code from $DOCKER_CRYPT_LANG, use system locale or
# set to 'en_US' if neither are set
if getenv('DOCKER_CRYPT_LANG'):
    if '_' in getenv('DOCKER_CRYPT_LANG'):
        LANGUAGE_CODE = getenv('DOCKER_CRYPT_LANG')
    else:
        LANGUAGE_CODE = 'en_US'
elif locale.getdefaultlocale():
    LANGUAGE_CODE = locale.getdefaultlocale()[0]
else:
    LANGUAGE_CODE = 'en_US'

# Read the list of allowed hosts from the $DOCKER_CRYPT_ALLOWED env var, or
# allow all hosts if none was set.
if getenv('DOCKER_CRYPT_ALLOWED'):
    ALLOWED_HOSTS = getenv('DOCKER_CRYPT_ALLOWED').split(',')
else:
    ALLOWED_HOSTS = ['*']
