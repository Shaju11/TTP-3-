__author__ = 'adam.cummings'

import unittest
import test_main as main

class MyTestCase(unittest.TestCase):

    def test_availability_default_yes_with_None(self):
        projectsList = ['Project X']
        personsList = ['1', u'Clive', None]  # ID, name, availability
        compare = True  # if the person is capable enough for the project
        capablePersons = []
        for project in projectsList:
            #for person in personsList:
            if ((personsList[2] is None) or (personsList[2] == '0')) and compare:
                capablePersons.append(personsList[1])
        self.assertEqual(capablePersons, ['Clive'])

    def test_availability_default_yes_with_0(self):
        projectsList = ['Project Y']
        personsList = ['1', u'Clive2', '0']
        compare = True
        capablePersons = []
        for project in projectsList:
            #for person in personsList:
            if ((personsList[2] is None) or (personsList[2] == '0')) and compare:
                capablePersons.append(personsList[1])
        self.assertEqual(capablePersons, ['Clive2'])

    def test_availability_no_with_string_not_0(self):
        projectsList = ['Project Z']
        personsList = ['1', u'Clive3', '1']
        compare = True
        capablePersons = []
        for project in projectsList:
            #for person in personsList:
            if ((personsList[2] is None) or (personsList[2] == '0')) and compare:
                capablePersons.append(personsList[1])
        self.assertEqual(capablePersons, [])

    def test_availability_no_with_integer_value(self):
        """Availability is now an integer rather than a string"""
        projectsList = ['Project M']
        personsList = ['1', u'Clive4', 0]
        compare = True
        capablePersons = []
        for project in projectsList:
            #for person in personsList:
            if ((personsList[2] is None) or (personsList[2] == '0')) and compare:
                capablePersons.append(personsList[1])
        self.assertEqual(capablePersons, [])

    def test_incapable_but_available(self):
        """Clive99's capability is False rather than True - he is not listed, despite being available"""
        projectsList = ['Project A']
        personsList = ['1', u'Clive99', '0']
        compare = False
        capablePersons = []
        for project in projectsList:
            #for person in personsList:
            if ((personsList[2] is None) or (personsList[2] == '0')) and compare:
                capablePersons.append(personsList[1])
        self.assertEqual(capablePersons, [])

    def test_incapable_and_unavailable(self):
        """Clive99's capability is False rather than True - he is not listed, despite being available"""
        projectsList = ['Project A']
        personsList = ['1', u'Clive99', '1']
        compare = False
        capablePersons = []
        for project in projectsList:
            #for person in personsList:
            if ((personsList[2] is None) or (personsList[2] == '0')) and compare:
                capablePersons.append(personsList[1])
        self.assertEqual(capablePersons, [])

    def test_multiple_projects_for_multiple_capable_and_available_persons(self):
        projectsList = ['Project A', 'Project B']
        personsList = [['1', u'Clive99', '0'], ['2', 'Clive98', '0']]
        compare = True
        capablePersons = []
        for project in projectsList:
            for person in personsList:
                if ((person[2] is None) or (person[2] == '0')) and compare:
                    capablePersons.append(person[1])
        self.assertEqual(capablePersons, ['Clive99', 'Clive98', 'Clive99', 'Clive98'])

    def test_multiple_projects_for_multiple_capable_and_available_persons_2(self):
        projectsList = ['Project A', 'Project B']
        personsList = [['1', u'Clive99', '0', True], ['2', 'Clive98', '0', False]]
        capablePersons = []
        for project in projectsList:
            for person in personsList:
                if ((person[2] is None) or (person[2] == '0')) and person[3] is True:
                    capablePersons.append(person[1])
        self.assertEqual(capablePersons, ['Clive99', 'Clive99'])












"""

    def availability_default_yes(self):
        cat = main.match.doEverything()
        for project in cat.projectsList:
            for person in cat.doEverything.personsList:
                if ((person.availability is None) or (person.availability == '0'))\
                   and (person.compare(project.skills)):
                    project.capablePersons.append(person)
        return cat.project.capablePersons


	def doEverything(self):
		cat = main.match()
		self.assertEqual('Woooo!',cat.doEverything())

	def displayInfo(self):
		cat = main.match()
		self.assertEqual('display info!',cat.displayInfo())

	def getAllPersons(self):
		cat = main.match()
		self.assertEqual('NO!',cat.getAllPersons())

	def sendAllPersons(self):
		cat = main.match()
		self.assertEqual('no!',cat.sendAllPersons())

	def getAllPersons(self):
		cat = main.match()
		self.assertEqual('get all persons',cat.getAllPersons())

	def getAllPersonSkills(self):
		cat = main.match()
		self.assertEqual('get all personSkills',cat.getAllPersonSkills())
"""


if __name__ == '__main__':
    unittest.main()
