from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the error response
        response.data['status_code'] = response.status_code
        response.data['error'] = str(exc)
        response.data['message'] = response.data.get('detail', '')

        # Remove 'detail' as it’s redundant
        if 'detail' in response.data:
            del response.data['detail']
    else:
        # Handle unexpected errors that don’t trigger DRF’s exception handler
        response = Response({
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "error": "Unexpected error",
            "message": str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
