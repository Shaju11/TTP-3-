__author__ = 'adam.cummings'

import unittest
import test_main as main



class MyTestCase(unittest.TestCase):
	def test_doEverything(self):
		cat = main.fish()
		self.assertEqual('Woooo!',cat.doEverything())

	def test_displayInfo(self):
		cat = main.fish()
		self.assertEqual('display info!',cat.displayInfo())

	def test_getAllPersons(self):
		cat = main.fish()
		self.assertEqual('NO!',cat.getAllPersons())

	def test_sendAllPersons(self):
		cat = main.fish()
		self.assertEqual('no!',cat.sendAllPersons())

	def test_getAllPersons(self):
		cat = main.fish()
		self.assertEqual('get all persons',cat.getAllPersons())

	def test_getAllPersonSkills(self):
		cat = main.fish()
		self.assertEqual('get all personSkills',cat.getAllPersonSkills())

if __name__ == '__main__':
	unittest.main()
