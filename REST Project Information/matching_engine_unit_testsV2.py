__author__ = 'adam.cummings'

import unittest
import test_main
from mock import patch

class MyTestCase(unittest.TestCase):

	def test_connecttoAPI_PeopleGET(self):
		urlGet = test_main.match().getAllPersons() # gets from URL
		allPeople = test_main.getPerson().GET() # people in the dummy API
		self.assertEqual(allPeople,urlGet)
	def test_connecttoAPI_PersonSkillsGET(self):
		urlGet = test_main.match().getAllPersonSkills() # gets from URL
		allPeopleSkills = test_main.getPersonSkill().GET() # people in the dummy API
		self.assertEqual(allPeopleSkills,urlGet)
	def test_connecttoAPI_ProjectsGET(self):
		urlGet = test_main.match().getAllProjects() # gets from URL
		allProjects = test_main.getProject().GET() # people in the dummy API
		self.assertEqual(allProjects,urlGet)
	def test_connecttoAPI_ProjectSkillsGET(self):
		urlGet = test_main.match().getAllProjectSkills() # gets from URL
		allProjectSkills = test_main.getProjectSkill().GET() # people in the dummy API
		self.assertEqual(allProjectSkills,urlGet)


"""
	def test_rankOrder(self):
		# people["name",skill,rank]
		people = [["charlie",3,7],["bertie",3,4],["albert",3,4]] # placeholder for people
		order = main.orderList() # placeholder for sort function
		self.assertEqual("bertie, albert, charlie", order)
"""
if __name__ == '__main__':
	unittest.main()

"""
@patch("test_main.match.getAllPersons")
	def test_defaultAvailability(self,mock_getAllPersons):
		mock_getAllPersons.return_value = "[(10, u'PersonName', None, 2014-08-20, 1, 0)]"
		match = test_main.match()
		result = match.doEverything()

		self.assertEqual(match.getAllPersons(),result)


	def test_Availability(self):
		match = test_main.match()
		self.assertEqual(match.doEverything(),1)
"""
