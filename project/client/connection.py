"""
    dados de acesso ao sistema Natuur
"""
class SemaceConnection:
    SEMACE_LOGIN_URL = "http://natuur.semace.ce.gov.br/login.faces"
    SEMACE_CHECKLIST_URL  = "http://natuur.semace.ce.gov.br/paginas/checkList/formSimuladorCheckList.faces?cid=1"
    SEMACE_COOKIE_ID = "JSESSIONID"
    SEMACE_CHECKLIST_ID = "j_idt36"
    SEMACE_FORM_NAV = "form_nav"
    SEMACE_FORM_SIMULADOR_CHECKLIST = "formSimuladorCheckList"

    _connection_error_messages = {
        'connection_error' : 'Não foi possível estabeler uma conexão com o sistema NATUUR ONLINE'
    }