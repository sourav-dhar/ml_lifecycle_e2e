from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
import logging

from starlette.responses import Response

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        logging.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logging.info(f'Response: {response.status_code}')
        return response

