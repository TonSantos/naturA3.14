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

    @try_connection
    def list_processos(self):
        login_response = http_request.get(SemaceConnection.SEMACE_LOGIN_URL)
        data = {
                "form_nav": SemaceConnection.SEMACE_FORM_NAV,
                "j_idt36": SemaceConnection.SEMACE_CHECKLIST_ID,
                "javax.faces.ViewState": SemaceConverter(login_response.content).javax_faces_view_state
                }
       
        cookies={SemaceConnection.SEMACE_COOKIE_ID:login_response.cookies[SemaceConnection.SEMACE_COOKIE_ID]}
        
        semace_response = http_request.post(SemaceConnection.SEMACE_LOGIN_URL, data=data, cookies=cookies)
        
        if semace_response.status_code != 200:
            return (SemaceConnection._connection_error_messages, semace_response.status_code)
        else:
            return (SemaceConverter(semace_response.content).processos, 200)

    @try_connection
    def list_grupos(self):
        login_response = http_request.get(SemaceConnection.SEMACE_LOGIN_URL)
        data = {
                "form_nav": SemaceConnection.SEMACE_FORM_NAV,
                "j_idt36": SemaceConnection.SEMACE_CHECKLIST_ID,
                "javax.faces.ViewState": SemaceConverter(login_response.content).javax_faces_view_state
                }
       
        cookies={SemaceConnection.SEMACE_COOKIE_ID:login_response.cookies[SemaceConnection.SEMACE_COOKIE_ID]}
        
        semace_response = http_request.post(SemaceConnection.SEMACE_LOGIN_URL, data=data, cookies=cookies)
        
        if semace_response.status_code != 200:
            return (SemaceConnection._connection_error_messages, semace_response.status_code)
        else:
            return (SemaceConverter(semace_response.content).grupos_atividades, 200)