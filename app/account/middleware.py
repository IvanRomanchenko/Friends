from django.conf import settings

from loguru import logger

from .views import get_client_ip


logger.add(
    settings.BASE_DIR / 'logs' / '{time:YYYY-MM-DD}.log',
    format='{time:YYYY-MM-DD HH:mm:ss} | {message}',
    rotation="1 week",
    compression="zip",
    # serialize=True,
    level='INFO',
    filter=lambda rcd: rcd if rcd.get('name') == 'account.middleware' else None
)


class StoresMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.log_user_login(request)
        return self.get_response(request)

    @staticmethod
    def log_user_login(request):
        """ Records user authentication to log """
        if request.method == 'POST' and request.path == '/login/':
            logger.info(
                f"{get_client_ip(request)} | {request.POST.get('username')}"
            )
