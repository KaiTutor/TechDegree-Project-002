import copy
import time
from constants import TEAMS, PLAYERS # localfile


def clean_data():
	"""Return a cleaned copy of the player data."""
	cleaned_players = copy.deepcopy(PLAYERS)


	for player in cleaned_players:
		# cleaning height
		player['height'] = int(player['height'].split()[0])
		# clean experience to bool T/F
		player['experience'] = True if player['experience'] == 'YES' else False
	
	return cleaned_players


def assign_teams(cleaned_players):
	"""Distribute players evenly across all teams."""
	balanced = {team : [] for team in TEAMS}
	num_players_team = len(cleaned_players) // len(TEAMS)
	player_index = 0


	for team in TEAMS:
		balanced[team] = cleaned_players[player_index : player_index + num_players_team]
		player_index += num_players_team

	return balanced


def display_stats(team_name, players):
	"""Display stats for a single team."""
	print(f"\nTeam: {team_name} Stats")
	print("-----")
	print(f"Total Players: {len(players)}\n")
	print("Players on team:")
	player_names = ",".join([player['name'] for player in players])
	print(f" {player_names}\n")
	input("Press ENTER to continue...")


def main_menu(balanced_teams):
	"""Run the menu for the Basketball Team Stats."""
	while True:
		print("\nBASKETBALL TEAM STATS TOOL")
		print("---- MENU----\n")
		print("Here are your choices:")
		print("  A) Display Team Stats")
		print("  B) Quit\n")

		choice = input("Enter an option: ")
		time.sleep(.5)


##### Working unsure about this 

		if choice.upper() == "A":
			#add letters to teams
			team_options = {chr(ord('A') + i): team for i, team in enumerate(TEAMS)}

			print("\nSelect a team to view stats:")
			for letter, team in team_options.items():
				print(f"  {letter}) {team}")

			team_choice = input("\nEnter an option: ").strip().upper()
			selected_team = team_options.get(team_choice)

			if selected_team:
				display_stats(selected_team, balanced_teams[selected_team])
			else:
				print("Invalid option. Try again.")

#####
		elif choice.upper() == "B":
			print("Exiting the program...")
			break
		else:
			print("Invalid option. Try again.")





if __name__ == "__main__":
    result = clean_data()
    result2 = assign_teams(result)
    main_menu(result2)
    

    # for team, players in result2.items():
    # 	print(f"\nTEAM: {team}")
    # 	for player in players:
    # 		print(" -", player["name"])
