    ###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###
    #def makePersonsStringIntoObjects(self, personsString):
    #    """takes a sting with the person info then turns it into a list of objects"""
#import test_main
class Person:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.availability = None
        self.availabilityDate = ''
        self.position = -1
        self.employeeType = ''
        #this will be a list of PersonSkills
        self.skills = []

class Skill:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.categoryId = -1


class PersonSkill:
    def __init__(self):
        self.id = -1
        self.personId = -1
        self.skillId = -1
        self.level = -1
        self.categoryId = -1


class Project:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.client = ''
        self.startdate = ''
        self.enddate = ''
        self.status = ''
        self.numberOfPeople = 1
        self.skills = []
        self.capablePersons = []

class ProjectSkill:
    def __init__(self):
        self.id = -1
        self.projectId = -1
        self.skillId = -1
        self.levelMin = 0
        self.levelMax = 5
        self.categoryId = -1


class Category:
    def __init__(self):
        self.categoryId = -1
        self.name = ''


personList = []
Person1 = Person()
Person1.id = 1
Person1.name = 'Albert'
Person1.availability = 0
personList.append(Person1)
Person2 = Person()
Person2.id = 2
Person2.name = 'Bertie'
Person2.availability = None
personList.append(Person2)
Person3 = Person()
Person3.id = 2
Person3.name = 'Charles'
Person3.availability = 1
personList.append(Person3)




        #def makePersonSkillsStringIntoObjects(self, personSkillsString):

personSkillList = []
personSkill = PersonSkill()
personSkill.id = 1
personSkill.categoryId = 1
personSkill.level = 3
personSkill.skillId = 1
personSkill.personId = 1
personSkillList.append(personSkill)
personSkill2 = PersonSkill()
personSkill2.id = 1
personSkill2.categoryId = 1
personSkill2.level = 3
personSkill2.skillId = 1
personSkill2.personId = 2
personSkillList.append(personSkill2)
personSkill3 = PersonSkill()
personSkill3.id = 1
personSkill3.categoryId = 1
personSkill3.level = 3
personSkill3.skillId = 1
personSkill3.personId = 3
personSkillList.append(personSkill3)

           #STUB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #def makeProjectsStringIntoObjects(self, projectsString):
projectList = []
projectX = Project()
projectX.id = 1
projectX.client = 'Dr. Death'
projectX.name = 'Project X'
projectList.append(projectX)

        #####stub

projSkillList = []
projSkill = ProjectSkill()
projSkill.skillId = 1
projSkill.levelMin = 0
projSkill.levelMax = 5
projSkill.categoryId = 1
projSkill.projectId = 2
projSkill.id = 1
projSkillList.append(projSkill)
