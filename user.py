#Demographic information and tracking for a user

from enum import Enum

class User(object):
	'Demographic information and tracking data'
	
	def __init__(self, id, first_name, last_name, age=None, gender=None
				, tracked_observations=None):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.tracked_observations = tracked_observations
		
class Gender(Enum):
	male = 1
	female = 2