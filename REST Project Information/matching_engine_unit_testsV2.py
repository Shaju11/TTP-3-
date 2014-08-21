__author__ = 'adam.cummings'

import unittest
import test_main
from mock import patch

class MyTestCase(unittest.TestCase):

	def test_rankOrder(self):
		# people["name",skill,rank]
		people = [["charlie",3,7],["bertie",3,4],["albert",3,4]] # placeholder for people
		order = main.orderList() # placeholder for sort function
		self.assertEqual("bertie, albert, charlie", order)
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
