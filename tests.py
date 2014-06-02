#! /usr/bin/env python3

import unittest
import statistic
import user
import cli

class TestUser(unittest.TestCase):
	
	def setUp(self):
		self.id = '1'
		self.first_name = 'Fred'
		self.last_name = 'Flintstone'
		self.age = 32
		self.gender = user.Gender.male

	def test_create_user_no_observations(self):
		self.user = user.User(self.id, self.first_name, self.last_name, self.age, self.gender)
		self.assertEqual(self.user.id, self.id)
		self.assertEqual(self.user.first_name, self.first_name)
		self.assertEqual(self.user.last_name, self.last_name)
		self.assertEqual(self.user.age, self.age)
		self.assertEqual(self.user.gender, self.gender)

if __name__ == '__main__':
	unittest.main()