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

class fish:
    def GET(self):
        return self.doEverything()

    def doEverything(self):
        """get all the info as lists"""
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
        projectSkillsString = self.getAllProjectSkills()
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
                if ((person.availability is None) or (person.availability == '0'))\
                   and (person.compare(project.skills)):
                    project.capablePersons.append(person)

    def splitObjects(self, string):
        string = string[2:(len(string)-2)]  # deletes first and last brackets
        stringList = string.split('), (')  # splits on ')'
        return stringList

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

    def makePersonSkillsStringIntoObjects(self, personSkillsString):
        """takes a sting with the person skill info then turns it into a list of objects"""
        skillList = self.splitObjects(personSkillsString)
        skillObjList = []
        for item in skillList:
            skillAttribList = item.split(', ')
            skillObj = PersonSkill()
            skillObj.id = skillAttribList[0]
            skillObj.personId = skillAttribList[1]
            skillObj.skillId = skillAttribList[2]
            skillObj.level = skillAttribList[3]
            skillObj.categoryId = skillAttribList[4]
            skillObjList.append(skillObj)
        return skillObjList

    def makeProjectsStringIntoObjects(self, projectsString):
        """takes a string with the project info then turns it into a list of objects"""
        projectList = self.splitObjects(projectsString)
        projectObjList = []
        for item in projectList:
            projectAttribList = item.split(', ')
            projectObj = Project()
            projectObj.id = projectAttribList[0]
            projectObj.name = projectAttribList[1]
            projectObj.client = projectAttribList[2]
            projectObj.status = projectAttribList[3]
            projectObj.numberOfPeople = projectAttribList[4]
            projectObj.startDate = projectAttribList[5]
            projectObj.endDate = projectAttribList[6]
            projectObjList.append(projectObj)
        return projectObjList

    def makeProjectSkillsStringIntoObjects(self, projectSkillsString):

        projectSkillsList = self.splitObjects(projectSkillsString)
        projectSkillsObjList = []
        for item in projectSkillsList:
            projectSkillsAttribList = item.split(', ')
            projectSkillsObj = ProjectSkill()
            projectSkillsObj.id = projectSkillsAttribList[0]
            projectSkillsObj.projectId = projectSkillsAttribList[1]
            projectSkillsObj.skillId = projectSkillsAttribList[2]
            projectSkillsObj.levelMin = projectSkillsAttribList[3]
            projectSkillsObj.levelMax = projectSkillsAttribList[4]
            projectSkillsObj.categoryId = projectSkillsAttribList[5]
            projectSkillsObjList.append(projectSkillsObj)
        return projectSkillsObjList

#def getRidOfUnicode(*input):
#Get rid of unicode loop
    #for attribute in input:
    #    try:
    #        attribute = attribute.decode('unicode_escape').encode('ascii', 'ignore')
    #    except AttributeError:
    #        continue
    #return attribute

    def getAllProjectSkills(self):
        return "[(40, 39, 30, 2, 4, 31)]"

    def getAllProjects(self):
        return "[(39, u'testproject30s', u'adamisclient', 0, 3, 2013-05-12, 2013-05-20)]"

    def getAllPersons(self):
        return "[(33, u'James', 0, 2011-05-05, 7, 0), (34, u'Rachel', 0, 2012-05-05, 6, 0), (35, u'Karim', 0, 2012-06-06, 5, 0)]"

    def getAllPersonSkills(self):
        return "[(35, 33, 30, 3, 31), (37, 34, 30, 4, 31)]"

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
            if (projectSkill.levelMin == '0') and not (self.haveSkillAtAnyLevel(projectSkill)):
                gotSkill = True
            for personSkill in self.skills:
                if self.isRightSkill(projectSkill, personSkill)\
                    and (projectSkill.levelMin <= personSkill.level) and (projectSkill.levelMax >= personSkill.level):
                    gotSkill = True
            if gotSkill == False:
                return False
        return True

    def isRightSkill(self, projectSkill, personSkill):
        return (personSkill.categoryId == projectSkill.categoryId) and (personSkill.skillId == projectSkill.skillId)

    def haveSkillAtAnyLevel(self, projectSkill):
        """ returns true if the person has the skill"""
        retVal = False
        for personSkill in self.skills:
            if self.isRightSkill(projectSkill, personSkill):
                retVal = True
        return retVal


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

    def setProjectSkills(self, projectSkillsList):
        """sets all the skills for this project, puts a list of projectSkills on each project object"""
        for projectSkill in projectSkillsList:
            if self.id == projectSkill.projectId:
                self.skills.append(projectSkill)

    def outputInfo(self):
        output = '-----------------------------------------\n'
        output += 'Project ID: ' + str(self.id) + '\n'
        output += 'Project: ' + self.name + '\n'

        output += 'Client: ' + self.client + '\n\n'
        output += 'Capable people:\n'
        if len(self.capablePersons) < 1:     ######project.numberNeeded: # for underavailability
            output += 'Not enough capable people available\n\n'
        for person in self.capablePersons:
            output += person.name + '\n\n'
        return output

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

if __name__ == "__main__":
    app.run()