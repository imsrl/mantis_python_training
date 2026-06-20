from random import choice
from model.project import Project
import time


def test_delete_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.session.ensure_login("administrator", "root")
        app.project.create(Project(
            name="Project for delete %s" % int(time.time()),
            description="Project for delete description"
        ))

    old_projects = app.soap.get_project_list()
    project = choice(old_projects)

    app.session.ensure_login("administrator", "root")
    app.project.delete_project_by_id(project.id)

    new_projects = app.soap.get_project_list()

    old_projects.remove(project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)