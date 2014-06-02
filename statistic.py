#Statistic properties and observation types

class Statistic(Object)
	'Properties of a statistic'
	
	def __init__(self, id, name, type, scale):
		self.id = id
		self.name = name
		self.type = type
		self.scale = scale

class Observation(Object)
	'One observation of a statistic'
	
	def __init__(self, date, value, statistic):
		self.date = date
		self.value = value
		self.statistic = statistic