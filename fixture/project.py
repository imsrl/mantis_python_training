from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        self.app.wd.find_element(By.LINK_TEXT, "Manage").click()

    def open_manage_projects_page(self):
        self.open_manage_page()
        self.app.wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def create(self, project):
        self.open_manage_projects_page()
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        self.fill_project_form(project)
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element(By.NAME, field_name).click()
            self.app.wd.find_element(By.NAME, field_name).clear()
            self.app.wd.find_element(By.NAME, field_name).send_keys(text)

    def get_project_list(self):
        self.open_manage_projects_page()
        projects = []

        rows = self.app.wd.find_elements(By.CSS_SELECTOR, "table.width100 tr.row-1, table.width100 tr.row-2")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            link = cells[0].find_element(By.TAG_NAME, "a")
            name = link.text
            href = link.get_attribute("href")
            id = href.split("project_id=")[1]
            projects.append(Project(id=id, name=name))

        return projects

    def delete_project_by_id(self, id):
        self.open_manage_projects_page()
        self.app.wd.find_element(By.CSS_SELECTOR, "a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()