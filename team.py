class Team:
	def __init__(self, name, batsmen_list = []):
		self.name = name
		self.batsmen_list = batsmen_list

	def __str__(self):
		return self.name