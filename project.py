#########################################################################
#   Project class
#   Project represents a project at the expo
#   Contains information pertaining to the project such as members, description, name
#   Also contains the section the project belongs to, if any
#########################################################################

class Project:

    def __init__(self, name:str, members:str, desc:str, categories:str) -> None:
        self.name = name
        self.members = members
        self.desc = desc
        self.categories = categories
        self.section = None
        self.floor = 0

    def setSection(self, section:'Section'):
        self.section = section

    def setFloor(self, floor:int):
        self.floor = floor

#########################################################################
#   Section class
#   Section represents a section of the expo
#   Contains a list of projects that belong to that section
#   Sections can represent floors, rooms, etc.
#########################################################################

class Section:

    # Init section with a name that represents the section
    def __init__(self, name:str) -> None:
        self.name = name
        self.projects = []

    def addProject(self, index:int, project:Project):
        self.projects[index] = project
        project.setSection(self)