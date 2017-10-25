#!/usr/bin/python3
from os import system 
import msvcrt
from map import rooms
from player import *
from items import *
from gameparser import *
from helperfunctions import *


def get_item_from_inventory(item_id,player):
	try:
		return player.inventory[[item.id for item in player.inventory].index(item_id)]

	except ValueError:
		output('You don\'t have ' + item_id, player.sobriety)
		anykey()
		return None

def list_of_items(items):

	return ', '.join([item.name for item in items])

def inventory_mass(inventory):
	inv_mass = 0
	for item in inventory:
		inv_mass = inv_mass + float(item.mass)
	inv_mass = round(inv_mass, 3)    
	return inv_mass

def list_of_npcs(npcs):

	return ', '.join([npcs[npc].name for npc in npcs])






def print_room(player):

	blank_line = "\n"
	output(blank_line + player.current_room.name.upper() + blank_line, player.sobriety)
	# Display room description
	output(player.current_room.description + blank_line, player.sobriety)
	# Display items in room
	
	if len(player.current_room.items) != 0:
		output("There is " + list_of_items(player.current_room.items) + " here.\n", player.sobriety)

	if len(player.current_room.npcs) != 0:
		output("There is " + list_of_npcs(player.current_room.npcs) + " here.\n", player.sobriety)


def exit_leads_to(exits, direction):

	return rooms[exits[direction]].name



	


def print_menu(player):

	output("You can:",player.sobriety)
	# Iterate over available exits
	for direction in player.current_room.exits:
		# Print the exit name and where it leads to
	
		output("GO " + direction.upper() + " to " + exit_leads_to(player.current_room.exits, direction) + ".", player.sobriety)
	for item in player.current_room.items:
		output("TAKE " + item.id.upper() + " to take " + item.name, player.sobriety)
	for item in player.inventory:
		output("DROP " + item.id.upper() + " to drop your " + item.name, player.sobriety)
	for npc in player.current_room.npcs:
		output("FIGHT " + player.current_room.npcs[npc].name.upper() + " to fight " + player.current_room.npcs[npc].name.upper(), player.sobriety)
	
	output("What do you want to do?",player.sobriety)


def is_valid_exit(exits, chosen_exit):

	return chosen_exit in exits

def execute_go(direction,player):



	if is_valid_exit(player.current_room.exits, direction):
		player.current_room = move(player.current_room.exits, direction)
		output("You are in "+ player.current_room.name, player.sobriety)
	else:
		output("You cannot go there. ", player.sobriety)
		anykey()
	return player

def execute_take(item_id,player):
	try:
		item_id = [item.id for item in player.current_room.items].index(item_id)
		if (player.current_room.items[item_id].mass +  inventory_mass(player.inventory)) > 20:
			output(("Inventory full!").upper(), player.sobriety)
			anykey()
		else:
			player.inventory.append(player.current_room.items.pop(item_id))

	except ValueError:
		output('You cannot take that', player.sobriety)
		anykey()
	return player
	

def execute_drop(item_id,player):
	try:
		player.current_room.items.append(player.inventory.pop([item.id for item in player.inventory].index(item_id)))
	except ValueError:
		output('You cannot drop that', player.sobriety)
		anykey()
	return player

def execute_fight(npc,item,player):
	try:
		victim = player.current_room.npcs[npc]
	except KeyError:
		output(npc[0].upper() + npc[1:] + ' is not in the room', player.sobriety)
		anykey()
		return player
	your_weapon = get_item_from_inventory(item,player)
	if (your_weapon == None):
		pass
	elif (victim.hp // your_weapon.mass) + 1 < (player.hp // victim.inventory[0].mass) + 1:
		output('You have knocked out ' + npc + '. The following items: ' +  list_of_items(victim.inventory) + ' spill to the floor. Emptying their pockets reveals £'+str(round(victim.money,2)) , player.sobriety)
		player.money += victim.money
		player.current_room.items +=  player.current_room.npcs.pop(npc).inventory
		
		anykey()
	else:
		pass
	return player

	

	#return npc




def execute_talk(npc,player):

	try:
		player =  player.current_room.npcs[npc].talk(player)
	except KeyError:
		output(npc[0].upper() + npc[1:] + ' is not in the room', player.sobriety)
		anykey()
	return player
   

def execute_look(item,player):
	item = get_item_from_inventory(item,player)
	if item != None:
		output(item.name, player.sobriety)
		output(item.desc, player.sobriety)
		anykey()
	return player

def execute_use(item,player):
	item_to_use = get_item_from_inventory(item,player)
	if item_to_use != None:
		player = item_to_use.use(player) 
		anykey()
	return player

def execute_survey():
	pass

def execute_command(command,player):

	if 0 == len(command):
		return player
	if command[0] == "go":
		if len(command) > 1:
			player = execute_go(command[1],player)
		else:
			output("Go where?", player.sobriety)
			anykey()

	elif command[0] == "take":
		if len(command) > 1:
			player = execute_take(command[1],player)
		else:
			output("Take what?", player.sobriety)
			anykey()

	elif command[0] == "drop":
		if len(command) > 1:
			player = execute_drop(command[1],player)
		else:
			output("Drop what?", player.sobriety)
			anykey()

	elif command[0] == "fight":
		if len(command) ==1:
			output('Fight who?', player.sobriety)
			anykey()
		elif len(command) == 2:

			output('Fight '+ command[1] +' with what?', player.sobriety)
			anykey()
		else:
			player = execute_fight(command[1],command[2],player)

			
	elif command[0] == "talk":
		if len(command) > 1:
			player = execute_talk(command[1],player)
		else:
			output("Talk to who?", player.sobriety)
			anykey()

	elif command[0] == 'look':
		if len(command) > 1:
			player = execute_look(command[1],player)
		else:
			output("Look at what?", player.sobriety)
			anykey()

	elif command[0] == 'use':
		if len(command) > 1:
			player = execute_use(command[1],player)
		else:
			output("Use what?", player.sobriety)
			anykey()

	elif command[0] == 'survey':
		execute_survey()

	else:
		output("This makes no sense.", player.sobriety)
		anykey()
	return player

def menu(player):

	print_menu(player)


	user_input = input("> ")

	normalised_user_input = normalise_input(user_input)

	return normalised_user_input


def move(exits, direction):

	return rooms[exits[direction]]

def win_condition(player):
	if (player.current_room in [room_student_union,room_tiger_tiger,room_pryzm]) and (your_id not in player.inventory):
		if (keys not in player.inventory) or (phone not in player.inventory):
			print('With neither an id to enter a club or your keys or phone to get home, you spend the night on the streets')
		else:
			print('Without your id you are forced to go home, it\'s too late to go out again so you cry yourself to sleep')
	elif player.drugged:
		print('') 
		pyshedelic()
	#drugs
	elif: #lose fight
	elif: #drown
	elif: #takeaway
	else: #kiril irish
		return False



 #   if player.current_room == rooms["Office"]:
  #      output("Congratualations you have won!")
   #     return True
	#else:
	 #   return False



# This is the entry point of our program
def main():

	player = player_obj()
	# Main game loop
	while not win_condition(player):
		# Display game status (room description, inventory etc.)
		system('cls')
		print_room(player)
		output("You're carrying " + str(inventory_mass(player.inventory))+ "kg.", player.sobriety) 
		output('You have £'+ str(player.money), player.sobriety)
		

		# Show the menu with possible actions and ask the player
		command = menu(player)

		# Execute the player's command

		player = execute_command(command,player)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
	main()

