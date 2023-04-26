#import floor
import project
from project import Project
import spreadsheet
#import lights

########
    # Shared manager
    # Contains shared variables and functions for the program
########

class SharedManager:

    def __init__(self) -> None:
        self.floor = 1
        self.activeProject : Project = None

    def onProjectSelected(self, project:Project):
        self.activeProject = project
        print(project, self.activeProject)

manager = SharedManager()

projectInfo = spreadsheet.returnProjects()
projects = []

for proj in projectInfo:
    newProj = project.Project(proj.name, proj.members, proj.desc, "Default")
    projects.append(newProj)

print(projects)

import gui

gui.generateFromProjects(projects, manager)
gui.startUI()