from random import choice
from model.project import Project
import time


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(
            name="Project for delete %s" % int(time.time()),
            description="Project for delete description"))
    old_projects = app.project.get_project_list()
    project = choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects,key=Project.id_or_max)