__author__ = 'team3.aka.the.best.team'

import web
import xml.etree.ElementTree as ET
import json
import mimerender
import sqlite3
from flask import Flask
import urllib2
import unpacker

mimerender = mimerender.FlaskMimeRender()

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/match', 'match',
    '/getPerson', 'getPerson',
    '/getPersonSkill', 'getPersonSkill',
    '/getProject', 'getProject',
    '/getProjectSkill', 'getProjectSkill'
)

app = web.application(urls, globals())


class getPerson:
    def GET(self):
        return '[{"EmployeeID":"33", "Name":"James", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"7", "EmploymentType":"0"}]'
        #"[(10, u'Sharrrrrjuuuu', 0, 2014-08-20, 1, 0), (11, u'Nick', 1, 2014-12-08, 3, 1), (12, u'Frank', 1, 2014-09-09, 5, 0), (200, u'Marcus', 0, 2012-10-01, 1, 0), (201, u'Odrey', 0, 2013-12-01, 3, 1), (202, u'Jacob', 0, 2013-10-01, 5, 0), (33, u'James', 0, 2011-05-05, 7, 0), (34, u'Rachel', 0, 2012-05-05, 6, 0), (35, u'Karim', 0, 2012-06-06, 5, 0)]"


class getPersonSkill:
    def GET(self):
        return '[{"EmployeeSkillID":"35", "EmployeeID":"33", "SkillID":"30", "SkillLevel":"3", "CategoryID":"31"}]'
        #"[(1 , 10 , 10 , 5 , 15), (2, 11, 11, 4, 16), (3, 12, 12, 3, 17), (300, 200 , 25 , 6, 20), (301, 201, 26, 4, 21), (302, 202, 26, 5, 21), (35, 33, 30, 3, 31), (37, 34, 30, 4, 31), (38, 35, 30, 5, 31)]"


class getProject:
    def GET(self):
        return '[{"ProjectID":"39", "Name":"testproject30s", "Client":"adamisclient", "Status":"0", "NumberOfPeople":"3", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}]'
        #return "[(10, u'YeahBoi', u'TheLads', u'Active', 5, 2014-07-03, 2014-08-23), (11, u'GoingOnTour', u'Completed', 3, u'TheLads', 2011-09-09, 2011-09-29), (12, u'Ilovechoc', u'Rachelscompany', u'Future', 2014-10-20, 2015-10-20, 5), (400, u'AwsomeProject', u'Asda', u'Future', 4, 2014-02-01, 2015-02-01), (401, u'RoseProject', u'Asda', u'Future', 4,  2014-03-01, 2015-03-01), (401, u'LithuaniaProject', u'LTGovernment', u'Future', 2, 2014-04-01, 2015-04-01), (39, u'testproject30s', u'adamisclient', 0, 3, 2013-05-12, 2013-05-20)]"


class getProjectSkill:
    def GET(self):
        return '[{"ProjectSkillID":"40", "ProjectID":"39", "SkillID":"30", "LevelMin":"3", "LevelMax":"5", "CategoryID":"31"}]'
        #"[(10, 10, 10, 0, 4, 15), (11, 11, 11, 1, 4, 16), (12, 12, 12, 1, 2, 17), (500, 400, 25, 0, 5, 20), (501, 401, 26, 1, 4, 21), (502, 402, 27, 3, 4, 22), (40, 39, 30, 3, 5, 31)]"


def removeUnicodeChars(list):
    newlist = []
    for item in list:	#iterate over the individual tuples
        try:
            item = item.decode('unicode_escape').encode('ascii','ignore') # remove the unicode
        except AttributeError: # catch for non-unicode chars
            item = item
        newlist.append(item) # append to the new list (does not seem to like it when trying to change it in the old list)
    return newlist


class match:
    def GET(self):
        return self.doEverything()

    def doEverything(self):
        """get all the info as lists"""
        #get persons
        personsString = self.getAllPersons()
        personsList = unpacker.makePersonsStringIntoObjects(personsString)
        #get personSkills
        personSkillsString = self.getAllPersonSkills()
        personSkillsList = unpacker.makePersonSkillsStringIntoObjects(personSkillsString)
        #get projects
        projectsString = self.getAllProjects()
        projectsList = unpacker.makeProjectsStringIntoObjects(projectsString)
        #get projectSkills
        projectSkillsString = self.getAllProjectSkills()
        projectSkillsList = unpacker.makeProjectSkillsStringIntoObjects(projectSkillsString)

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

    def getAllPersons(self):
        return urllib2.urlopen('http://localhost:8080/getPerson').read()

    def getAllPersonSkills(self):
        return urllib2.urlopen('http://localhost:8080/getPersonSkill').read()

    def getAllProjects(self):
        return urllib2.urlopen('http://localhost:8080/getProject').read()

    def getAllProjectSkills(self):
        return urllib2.urlopen('http://localhost:8080/getProjectSkill').read()


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


class Category:
    def __init__(self):
        self.categoryId = -1
        self.name = ''

if __name__ == "__main__":
    app.run()