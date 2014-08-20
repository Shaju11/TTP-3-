__author__ = 'michael.chambers'

import web
import xml.etree.ElementTree as ET
import json
import mimerender
import sqlite3
from flask import Flask

db_user_conn = sqlite3.connect('user.db')
db_project_conn = sqlite3.connect('projectinfo.db')

mimerender = mimerender.FlaskMimeRender()

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/fish', 'fish',
    '/users/(.*)', 'get_user',
    '/test', 'test'
)


app = web.application(urls, globals())

def removeUnicodeChars(list):
    newlist = []
    for item in list:	#iterate over the individual tuples
        try:
            item = item.decode('unicode_escape').encode('ascii','ignore') # remove the unicode
        except AttributeError: # catch for non-unicode chars
            item = item
        newlist.append(item) # append to the new list (does not seem to like it when trying to change it in the old list)
    return newlist

#class list_users:
#    def GET(self):
#        output = 'users:['
#        for child in root:
#            print 'child', child.tag, child.attrib
#            output += str(child.attrib) + ', '
#        output += ']'
#        return output


class fish:
    def GET(self):
        return self.doEverything()

    def doEverything(self):
        """get all the info as lists"""
        #get skills
        #turn into objects

        #get categories
        #turn into objects

        #get persons
        personsString = self.getAllPersons()
        personsList = self.makePersonsStringIntoObjects(personsString)

        #get personSkills
        personSkillsString = self.getAllPersonSkills()
        personSkillsList = self.makePersonSkillsStringIntoObjects(personSkillsString)

        #get projects
        projectsString = self.getAllProjects()
        projectsList = self.makeProjectsStringIntoObjects(projectsString)

        #get projectSkills
        projectSkillsString = self.getAllPersonSkills()
        projectSkillsList = self.makeProjectSkillsStringIntoObjects(projectSkillsString)

        #get the skills for the person

        for person in personsList:
            person.setPersonSkills(personSkillsList)

        for project in projectsList:
            project.setProjectSkills(projectSkillsList)

        #for each project, find people with skills
        self.match(projectsList, personsList)

        #return everything in a nice format
        return self.displayInfo(projectsList)

    def displayInfo(self, projectsList):
        output = ''
        for project in projectsList:
            output += project.outputInfo()
        return output

    def match(self, projectsList, personsList):
        """by this point we have all the info in objects and we want to match people to projects"""
        for project in projectsList:
            for person in personsList:
                if ((person.availability is None) or (person.availability == 0))\
                   and (person.compare(project.skills)):
                    project.capablePersons.append(person)

    def splitObjects(self, string):
        string = string[2:(len(string)-2)]  # deletes first and last brackets
        stringList = string.split('), (')  # splits on ')'
        return stringList

    def getAllPersons(self):
        return "[(1, u'Rob', 1, 1, 2013-10-07, 0), (2, u'Adam', NULL, 3, 2014-12-08, 1), (3, u'Stephen', 1, 5, 2006-07-05, 0)]"

    def makePersonsStringIntoObjects(self, personsString):
        """takes a sting with the person info then turns it into a list of objects"""

            #personAttribList = removeUnicodeChars(AttribList)
        personList = self.splitObjects(personsString)

        personObjList = []
        for item in personList:
            personAttribList = item.split(', ')

            personObj = Person()
            personObj.id = personAttribList[0]
            personObj.name = personAttribList[1]
            personObj.availability = personAttribList[2]
            personObj.position = personAttribList[3]  # as in, rank, I think?
            personObj.availabilitydate = personAttribList[4]
            personObj.employeetype = personAttribList[5]  # not relevant (yet??)
            personObjList.append(personObj)

        return personObjList

    ###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###STUB###
    #def makePersonsStringIntoObjects(self, personsString):
    #    """takes a sting with the person info then turns it into a list of objects"""
    #    dave = Person()
    #    dave.id = 1
    #    dave.name = 'Clive (nee dave)'
    #    dave.availability = 0
    #    dave2 = Person()
    #    dave2.id = 2
    #    dave2.name = 'Clive2 (nee dave2)'
    #    dave2.availability = None
    #    return [dave, dave2]

    def getAllPersonSkills(self):
        return "[(2, 8, 0, 0, 5, 5), (4, 9, 3, 1, 4, 6), (3, 11, 7, 3, 3, 7)]"

    def makePersonSkillsStringIntoObjects(self, personSkillsString):
        """takes a sting with the person skill info then turns it into a list of objects"""
        skillList = self.splitObjects(personSkillsString)
        skillObjList = []
        for item in skillList:
            skillAttribList = item.split(', ')
            skillObj = PersonSkill()
            skillObj.id = skillAttribList[0]
            skillObj.categoryId = skillAttribList[1]
            skillObj.level = skillAttribList[2]
            skillObj.skillId = skillAttribList[3]  # as in, rank, I think?
            skillObj.personId = skillAttribList[4]
            skillObjList.append(skillObj)
        return skillObjList
       # personSkill = PersonSkill()
       # personSkill.id = 1
        #personSkill.categoryId = 1
        #personSkill.level = 3
        #personSkill.skillId = 1
        #personSkill.personId = 1

       # personSkill2 = PersonSkill()
       # personSkill2.id = 1
       # personSkill2.categoryId = 1
       # personSkill2.level = 3
       # personSkill2.skillId = 1
       # personSkill2.personId = 2
       # return [personSkill, personSkill2]

    def getAllProjects(self):
        return "[(8, u'Mileyproject', u'Disney', 2014-07-03, 2014-07-23, u'Active', 20), (9, u'Frozen', u'Disney', 2011-09-09, 2011-09-29, u'Completed', 3), (11, u'Ilovechoc', u'Rachelscompany', 2010-10-20, 2011-10-20, u'Future', 1)]"

    def makeProjectsStringIntoObjects(self, projectsString):
        """takes a string with the project info then turns it into a list of objects"""

        projectList = self.splitObjects(projectsString)
        projectObjList = []
        for item in projectList:
            projectAttribList = item.split(', ')
            projectObj = PersonSkill()
            projectObj.id = projectAttribList[0]
            projectObj.name = projectAttribList[1]
            projectObj.client = projectAttribList[2]
            projectObj.status = projectAttribList[3]
            projectObj.numberOfPeople = projectAttribList[4]
            projectObj.startDate = projectAttribList[5]
            projectObj.endDate = projectAttribList[6]
            projectObjList.append(projectObj)
        return projectObjList

    #STUB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #def makeProjectsStringIntoObjects(self, projectsString):
    #    projectX = Project()
    #    projectX.id = 2
    #    projectX.client = 'Dr. Death'
    #    projectX.name = 'Project X'
    #    return [projectX]

    def getAllProjectSkills(self):
        return 'ignore'

    def makeProjectSkillsStringIntoObjects(self, projectSkillsString):

        projectSkillsList = self.splitObjects(projectSkillsString)
        projectSkillsObjList = []
        for item in projectSkillsList:
            projectSkillsAttribList = item.split(', ')
            projectSkillsObj = ProjectSkills()
            projectSkillsObj.id = projectSkillsAttribList[0]
            projectSkillsObj.projectId = projectSkillsAttribList[1]
            projectSkillsObj.skillId = projectSkillsAttribList[2]
            projectSkillsObj.levelMin = projectSkillsAttribList[3]
            projectSkillsObj.levelMax = projectSkillsAttribList[4]
            projectSkillsObj.categoryId = projectSkillsAttribList[5]
            projectSkillsObjList.append(projectSkillsObj)
        return projectSkillsObjList


        """stub
        projSkill = ProjectSkill()
        projSkill.skillId = 1
        projSkill.levelMin = 1
        projSkill.levelMax = 4
        projSkill.categoryId = 1
        projSkill.projectId = 2
        projSkill.id = 1
        return [projSkill]


def getRidOfUnicode(*input):
#Get rid of unicode loop
    for attribute in input:
        try:
            attribute = attribute.decode('unicode_escape').encode('ascii', 'ignore')
        except AttributeError:
            continue
    return attribute
"""

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)


class Person:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.availability = None
        #this will be a list of PersonSkills
        self.skills = []

    def createFromString(self):
        """turn the string into an object"""
        return ''

    def setPersonSkills(self, personSkillsList):
        """creates a list of skills that this person has"""
        for personSkill in personSkillsList:
            # personSkillsList
            if self.id == personSkill.personId:
                self.skills.append(personSkill)

    def compare(self, skillList):
        """if the person has the required skills return True, skillList will be a list of projectSkills"""
        for projectSkill in skillList:
            gotSkill = False
            for personSkill in self.skills:
                if (personSkill.categoryId == projectSkill.categoryId)and(personSkill.skillId == projectSkill.skillId)\
                    and (projectSkill.levelMin <= personSkill.level) and (projectSkill.levelMax >= personSkill.level):
                    gotSkill = True
            if gotSkill == False:
                return False
        return True


class Skill:
    def __init__(self):
        self.id = -1
        self.name = ''


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
        self.skills = []
        self.capablePersons = []

    def setProjectSkills(self, projectSkillsList):
        """sets all the skills for this project, puts a list of projectSkills on each project object"""
        for projectSkill in projectSkillsList:
            if self.id == projectSkill.projectId:
                self.skills.append(projectSkill)

    def outputInfo(self):
        output = 'Project ID: ' + str(self.id) + '\n'
        output += 'Project: ' + self.name + '\n'

        output += 'Client: ' + self.client + '\n\n'
        output += 'Capable people:\n'
        if len(self.capablePersons) < 1:     ######project.numberNeeded: # for underavailability
            output += 'Not enough capable people available'
        for person in self.capablePersons:
            output += person.name + '\n'
        return output

class ProjectSkill:
    def __init__(self):
        self.id = -1
        self.projectId = -1
        self.skillId = -1
        self.levelMin = 0
        self.levelMax = 5
        self.categoryId = -1

    def createFromString(self):
        return 'go'


class Category:
    def __init__(self):
        self.categoryId = -1
        self.name = ''


if __name__ == "__main__":
    app.run()