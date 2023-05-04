#import floor
import html
import project
from project import Project
import spreadsheet
#import lights

########
    # Shared manager
    # Contains shared variables and functions for the program
########

class SharedManager:

    def __init__(self, projects) -> None:
        self.floor = 1
        self.activeProject : Project = None
        self.projects = projects

    def onProjectSelected(self, index):
        self.activeProject = self.projects[index]
        print(self.projects[index], self.activeProject, self.activeProject.floor)

projectInfo = spreadsheet.returnProjects()
projects = []

manager = SharedManager(projects)

for proj in projectInfo:
    newProj = project.Project(html.unescape(proj.name), html.unescape(proj.members), html.unescape(proj.desc), "Default")
    newProj.floor = proj.floor
    projects.append(newProj)

print(projects)

import gui

gui.generateFromProjects(projects, manager)
gui.startUI()