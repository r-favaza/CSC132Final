#########################################################################
#   Section class
#   Section represents a section of the expo
#   Contains a list of projects that belong to that section
#   Sections can represent floors, rooms, etc.
#########################################################################

from project import Project

class Section:

    # Init section with a name that represents the section
    def __init__(self, name:str) -> None:
        self.name = name
        self.projects = []

    def addProject(self, index:int, project:Project):
        self.projects[index] = project
        project.setSection(self)

