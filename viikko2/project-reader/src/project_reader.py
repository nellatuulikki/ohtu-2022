from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = toml.loads(content).get('tool').get('poetry')
        
        name = toml_dict.get('name')
        description = toml_dict.get('description ') 
        dependencies = list(toml_dict.get('dependencies').keys())
        dev_dependencies = list(toml_dict.get('dev-dependencies').keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
