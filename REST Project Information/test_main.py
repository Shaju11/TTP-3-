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


class list_users:
    def GET(self):
        output = 'users:['
        for child in root:
            print 'child', child.tag, child.attrib
            output += str(child.attrib) + ', '
        output += ']'
        return output


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
            person.setSkills(personSkillsList)

        for project in projectsList:
            project.setSkills(projectSkillsList)

        #for each project, find people with skills
        self.match(projectsList, personsList)

        #print out everything in a nice format
        return self.displayInfo(projectsList)

    def displayInfo(self, projectsList):
        output = ''
        for project in projectsList:
            output += project.outputInfo()
        return output

    def getAllPersons(self):
        """returns all the rows in the Person table to send to another comp, in a nice format (to be determined)"""
        return 'NO!'

    def sendAllPersons(self):
        """returns all the rows in the Person table to send to another comp, in a nice format (to be determined)"""
        return 'no!'

    def match(self, projectsList, personsList):
        """by this point we have all the info in objects and we want to match people to projects"""
        for project in projectsList:
            for person in personsList:
                #compare person skills to requirements
                if person.compare(project.skills):
                    project.capablePersons.append(person)

    def getAllPersons(self):
        return 'get all persons'

    def makePersonsStringIntoObjects(self, personsString):
        """takes a sting with the person info then turns it into a list of objects"""
        dave = Person()
        dave.id = 1
        dave.name = 'Clive (nee dave)'
        dave.availability = True
        return [dave]

    def getAllPersonSkills(self):
        return 'get all personSkills'

    def makePersonSkillsStringIntoObjects(self, personSkillsString):
        personSkill = PersonSkill()
        personSkill.id = 1
        personSkill.categoryId = 1
        personSkill.level = 3
        personSkill.skillId = 1
        personSkill.personId = 1
        return [personSkill]

    def getAllProjects(self):
        return 'blah!'

    def makeProjectsStringIntoObjects(self, projectsString):
        projectX = Project()
        projectX.id = 2
        projectX.client = 'Dr. Death'
        projectX.name = 'Project X'
        return [projectX]

    def getAllPersonSkills(self):
        return 'stuff'

    def makeProjectSkillsStringIntoObjects(self, projectSkillsString):
        projSkill = ProjectSkill()
        projSkill.skillId = 1
        projSkill.levelMin = 1
        projSkill.levelMax = 4
        projSkill.categoryId = 1
        projSkill.projectId = 2
        projSkill.id = 1
        return [projSkill]


class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)


class Person:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.availability = -1
        #this will be a list of PersonSkills
        self.skills = []

    def createFromString(self):
        """turn the string into an object"""
        return ''

    def setSkills(self, personSkillsList):
        """creates a list of skills that this person has"""
        for personSkill in personSkillsList:
            if self.id == personSkill.personId:
                self.skills.append(personSkill)

    def compare(self, skillList):
        """if the person has the required skills return True, skillList will be a list of projectSkills"""
        for projectSkill in skillList:
            gotSkill = False
            for personSkill in self.skills:
                if (personSkill.categoryId == projectSkill.categoryId)and(personSkill.skillId == projectSkill.skillId)\
                    and (projectSkill.levelMin < personSkill.level) and (projectSkill.levelMax > personSkill.level):
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

    def setSkills(self, projectSkillsList):
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
            output += 'No enough capable people available'
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