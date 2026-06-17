from model.project import Project
import time


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(
        name="Test project %s" % int(time.time()),
        description="Test project description")
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects,key=Project.id_or_max)