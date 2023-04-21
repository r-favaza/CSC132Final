#########################################################################
#   Project class
#   Project represents a project at the expo
#   Contains information pertaining to the project such as members, description, name
#   Also contains the section the project belongs to, if any
#########################################################################

import Section

class Project:

    def __init__(self, name:str, members:str, desc:str, categories:str) -> None:
        self.name = name
        self.members = members
        self.desc = desc
        self.categories = categories
        self.section = None

    def setSection(self, section:Section):
        self.section = section