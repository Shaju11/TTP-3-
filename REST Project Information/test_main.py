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
        output = 'users:[';
        for child in root:
            print 'child', child.tag, child.attrib
            output += str(child.attrib) + ', '
        output += ']';
        return output


class fish:
    def GET(self):
        return self.doEverything()

    def doEverything(self):
        return 'Hello'
        """get all the info as lists"""
        #get skills
        #turn into objects

        #get categories
        #turn into objects

        #get persons
        personsString = self.getAllPersons()
        personsList = 'personsString as a list'

        #get projects
        projectsList = 'df'

        #get the skills for the person
        for person in personsList:
            person.getSkills()

        for project in projectsList:
            project.getSkills()

        #for each project, find people with skills
        match()

        #print out everything in a nice format

        return 'go!'

    def getAllPersons(self):
        """returns all the rows in the Person table to send to another comp, in a nice format (to be determined)"""
        return 'NO!'

    def sendAllPersons(self):
        """returns all the rows in the Person table to send to another comp, in a nice format (to be determined)"""
        return 'no!'

    def match(self, projectList, personList):
        """by this point we have all the info in objects and we want to match people to projects"""
        for project in projectList:
            for person in personList:
                #compare person skills to requirements
                if person.compare(project.skill):
                    project.capablePersons.append(person)

        return 'go!'



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

    def getSkill(self):
        """creates a list of skills that this person has"""
        return 'go'

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

    def getSkills(self):
        """get all the skills for this project"""
        self.skills


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