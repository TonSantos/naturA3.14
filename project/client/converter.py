from bs4 import BeautifulSoup

class SemaceConverter:

    def __init__(self, content):
        self.soup = BeautifulSoup(content,'html.parser')
        self.__content = content
        self.__processos = None
        self.__grupos_atividades = None
        self.__javax_faces_view_state = None
        self.__subtipos_processos = None
        self.__get_processos()
        self.__get_javax_faces_view_state()
        self.__get_grupos_atividades()
        self.__get_subtipos_processos()

    @property
    def content(self):
        return self.__content

    @property
    def processos(self):
        return self.__processos

    @property
    def javax_faces_view_state(self):
        return self.__javax_faces_view_state

    @property
    def grupos_atividades(self):
        return self.__grupos_atividades

    @property
    def subtipos_processos(self):
        return self.__subtipos_processos

    def __get_processos(self):
        find_elements = self.soup.find(id="select_tipo_processo")
       
        processos = []
        if find_elements:
            for option in find_elements.find_all('option'):
                if option['value']:
                    processos.append({'opcao': option.text, 'valor': option['value']})

        self.__processos = processos

    def __get_javax_faces_view_state(self):
        javax_faces_view_state = self.soup.find_all(id="javax.faces.ViewState")
        if javax_faces_view_state:
            self.__javax_faces_view_state = javax_faces_view_state[-1].get('value')
        else:
            javax_faces_view_state
    
    def __get_grupos_atividades(self):
        find_elements = self.soup.find(id="select_grupo_atividade")
        grupos_atividades = []
        if find_elements:
            for option in find_elements.find_all('option'):
                if option['value']:
                    grupos_atividades.append({'opcao': option.text, 'valor': option['value']})

        self.__grupos_atividades = grupos_atividades

    def __get_subtipos_processos(self):
        subtipos_processos = []
        self.__subtipos_processos = subtipos_processos