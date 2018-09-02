import requests as http_request
from requests.exceptions import ConnectionError

from .connection import SemaceConnection
from .converter import SemaceConverter

class SemaceApiClient:

    def try_connection(access):
        def wrapper(*args, **kwargs):
            try:
                return access(*args, **kwargs)
            except ConnectionError as conn_error:
                return (SemaceConnection._connection_error_messages, 500)
        return wrapper

    @try_connection
    def login_page(self):
        semace_response = http_request.get(SemaceConnection.SEMACE_LOGIN_URL)

        if semace_response.status_code != 200:
            return (SemaceConnection._connection_error_messages, semace_response.status_code)
        else:
            return (SemaceConverter(semace_response.content).processos, 200)
