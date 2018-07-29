from player import Player
from constants import MatchInitializer

FIRST_BALL = 1
LAST_BALL = 6
OUTCOME_FOR_WICKET = 'Out'
ONE_BALL = 1

class Match:
	def __init__(self, overs_remaining, runs_required, wickets_remaining, batting_team, bowling_team):
		
		self.overs = overs_remaining
		self.runs = runs_required
		self.wickets = wickets_remaining
		self.batting_team = batting_team
		self.bowling_team = bowling_team

	def createBatsmen(self):
		
		batsmen = []
		Kirat_Boli   = Player("Kirat Boli",   [0.05, 0.30, 0.25, 0.10, 0.15, 0.01, 0.09, 0.05])
		batsmen.append(Kirat_Boli)
		N_S_Nodhi    = Player("N. S. Nodhi",  [0.10, 0.40, 0.20, 0.05, 0.10, 0.01, 0.04, 0.10])
		batsmen.append(N_S_Nodhi)
		R_Rumrah     = Player("R. Rumrah",    [0.20, 0.30, 0.15, 0.05, 0.05, 0.01, 0.04, 0.20])
		batsmen.append(R_Rumrah)
		Shashi_Henra = Player("Shashi Henra", [0.30, 0.25, 0.05, 0.00, 0.05, 0.01, 0.04, 0.30])
		batsmen.append(Shashi_Henra)
		
		return batsmen

	def startMatch(self, striker, non_striker, current_batsmen, batsmen_played):
		match_won = False
		for i in range(MatchInitializer.OVERS_IN_MATCH):
			if not match_won:
				print ()
				print (self.overs, "overs left.", self.runs, "runs to win")
				for j in range(FIRST_BALL,LAST_BALL+1):
					if not match_won:
						outcome = striker.getOutcome()[0]
						if outcome != OUTCOME_FOR_WICKET:
							striker.runs += outcome
							striker.balls_faced += ONE_BALL
							self.runs -= outcome
							print (str(i)+"."+str(j),striker, "scored", outcome)
							#Check for batting win here
							if self.runs > 0:
								if self.isOddScore(outcome):
									temp = striker
									striker = non_striker
									non_striker = temp
							else:
								match_balls_played = (i*6) + j
								balls_remaining = (MatchInitializer.OVERS_IN_MATCH*6) - match_balls_played
								print ("\n<---"+ self.batting_team.name ,"won by", self.wickets, "wicket(s) and", balls_remaining, "balls remaining--->")
								match_won = True
						else:
							print (str(i)+"."+str(j),striker, "is out")
							self.wickets -= 1
							striker.status = "Out"
							striker.balls_faced += 1
							if self.wickets > 0:
								striker = current_batsmen.pop(0)
								batsmen_played.append(striker)
							else:
								print ("\n<---"+ self.bowling_team.name ,"won by", self.runs - 1 ,"runs--->")
								match_won = True
				self.overs -= 1
				temp = striker
				striker = non_striker
				non_striker = temp 
		if not match_won:
			print ("\n<---"+ self.bowling_team.name ,"won by", self.runs - 1 ,"runs--->")
		print ()

	def isOddScore(self, outcome):
		return outcome%2 != 0
