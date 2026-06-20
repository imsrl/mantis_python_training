from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible("administrator", "root")

        if projects is None:
            return []

        return [
            Project(
                id=str(project.id),
                name=project.name
            )
            for project in projects
        ]