__author__ = 'adam.cummings'

import unittest
import test_main
from mock import patch

class MyTestCase(unittest.TestCase):

"""
	@patch("test_main.match.getAllPersons")
	def test_defaultAvailability(self,mock_getAllPersons):
		mock_getAllPersons.return_value = "[(10, u'PersonName',, 2014-08-20, 1, 0)]"
"""
if __name__ == '__main__':
	unittest.main()
