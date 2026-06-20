from model.project import Project
import time


def test_add_project(app):
    old_projects = app.soap.get_project_list()

    project = Project(
        name="Test project %s" % int(time.time()),
        description="Test project description"
    )

    app.session.ensure_login("administrator", "root")
    app.project.create(project)

    new_projects = app.soap.get_project_list()

    old_projects.append(project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)