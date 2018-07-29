
class HelperFunctions:
	def getUserChoice(the_match, striker, non_striker, current_batsmen, batsmen_played):
		print ("\nWhat do you wish to do? Please enter a choice")
		print ("1. Play match without commentary")
		print ("2. Play match with commentary")
		user_choice = int(input())
		if user_choice == 1:
			the_match.playMatch(striker, non_striker, current_batsmen, batsmen_played)
			the_match.printSummary(batsmen_played)
		elif user_choice == 2:
			the_match.playMatch(striker, non_striker, current_batsmen, batsmen_played)
			the_match.printSummary(batsmen_played)
			the_match.printCommentary()
		else:
			print ("Please enter a valid choice. Either 1 or 2")