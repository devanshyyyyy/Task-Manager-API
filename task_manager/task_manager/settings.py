INSTALLED_APPS = [
    # Default Django apps...
    'rest_framework',
    'tasks',
    'rest_framework.authtoken'
    'rest_framework_simplejwt',
    'djangorestframework_simplejwt'
    'django_filters'
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'tasks.utils.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'PAGE_SIZE': 10,
}
