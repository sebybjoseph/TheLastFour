from constants import MatchInitializer
from match import Match
from player import Player
from team import Team
from helper import HelperFunctions


def the_last_four():

	Lengaburu = Team("Lengaburu")
	Enchai = Team("Enchai")

	the_match = Match(MatchInitializer.OVERS_IN_MATCH, MatchInitializer.RUNS_REQUIRED, MatchInitializer.WICKETS_REMAINING, Lengaburu, Enchai)

	lengaburu_batsmen = the_match.createBatsmen()
	Lengaburu.batsmen_list = lengaburu_batsmen

	#List to keep track of players yet to bat
	current_batsmen = lengaburu_batsmen

	#List to track the batsmen who have played in the innings
	batsmen_played = []

	striker = current_batsmen.pop(0)
	non_striker =current_batsmen.pop(0)

	batsmen_played.append(striker)
	batsmen_played.append(non_striker)


	HelperFunctions.getUserChoice(the_match, striker, non_striker, current_batsmen, batsmen_played)

	


the_last_four()