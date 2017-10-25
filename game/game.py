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
		print('You don\'t have ' + item_id)
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

def print_room_npcs(room):
	if len(room.npcs) != 0:
		print("There is " + list_of_npcs(room.npcs) + " here.\n")

def print_room_items(items):
	if len(items) != 0:
		print("There is " + list_of_items(items) + " here.\n")

def print_inventory_items(items):

	if len(items) !=0:
		print("You have " + list_of_items(items) + ".\n")


def print_room(room):

	blank_line = "\n"
	print(blank_line + room.name.upper() + blank_line)
	# Display room description
	print(room.description + blank_line)
	# Display items in room
	print_room_items(room.items)
	print_room_npcs(room)



def exit_leads_to(exits, direction):

	return rooms[exits[direction]].name


def print_exit(direction, leads_to):

	print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, room_npcs):

	print("You can:")
	# Iterate over available exits
	for direction in exits:
		# Print the exit name and where it leads to
		print_exit(direction, exit_leads_to(exits, direction))
	for item in room_items:
		print("TAKE " + item.id.upper() + " to take " + item.name)
	for item in inv_items:
		print("DROP " + item.id.upper() + " to drop your " + item.name)
	for npc in room_npcs:
		print("FIGHT " + room_npcs[npc].name.upper() + " to fight " + room_npcs[npc].name.upper())
	
	print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):

	return chosen_exit in exits

def execute_go(direction,player):



	if is_valid_exit(player.current_room.exits, direction):
		player.current_room = move(player.current_room.exits, direction)
		print("You are in", player.current_room.name)
	else:
		print("You cannot go there.")
		anykey()
	return player

def execute_take(item_id,player):
	try:
		item_id = [item.id for item in player.current_room.items].index(item_id)
		if (player.current_room.items[item_id].mass +  inventory_mass(player.inventory)) > 20:
			print(("Inventory full!").upper())
			anykey()
		else:
			player.inventory.append(player.current_room.items.pop(item_id))

	except ValueError:
		print('You cannot take that')
		anykey()
	return player
	

def execute_drop(item_id,player):
	try:
		player.current_room.items.append(player.inventory.pop([item.id for item in player.inventory].index(item_id)))
	except ValueError:
		print('You cannot drop that')
		anykey()
	return player

def execute_fight(npc,item,player):
	try:
		victim = player.current_room.npcs[npc]
	except KeyError:
		print(npc[0].upper() + npc[1:] + ' is not in the room')
		anykey()
		return player
	your_weapon = get_item_from_inventory(item,player)
	if (your_weapon == None):
		return
	elif (victim.hp // your_weapon.mass) + 1 < (player.hp // victim.inventory[0].mass) + 1:
		print('You have knocked out ' + npc + '.' +  list_of_items(victim.inventory) + ' spills to the floor. Emptying their pockets reveals £'+str(victim.money) )
		player.money += victim.money
		player.current_room.items +=  player.current_room.npcs.pop(npc).inventory
		
		anykey()
	else:
		pass
	return player

	

	#return npc




def execute_talk(npc,player):

	try:
		player.inventory =  player.current_room.npcs[npc].talk(player.inventory)
	except KeyError:
		print(npc[0].upper() + npc[1:] + ' is not in the room')
		anykey()
	return player
   

def execute_look(item,player):
	item = get_item_from_inventory(item,player)
	if item != None:
		print(item.name)
		print(item.desc)
		anykey()
	return player

def execute_use(item,player):
	player.inventory,player.sobriety = item.use(player.inventory,player.sobriety) 
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
			print("Go where?")
			anykey()

	elif command[0] == "take":
		if len(command) > 1:
			player = execute_take(command[1],player)
		else:
			print("Take what?")
			anykey()

	elif command[0] == "drop":
		if len(command) > 1:
			player = execute_drop(command[1],player)
		else:
			print("Drop what?")
			anykey()

	elif command[0] == "fight":
		if len(command) ==1:
			print('Fight who?')
			anykey()
		elif len(command) == 2:

			print('Fight '+ command[1] +'with what?')
			anykey()
		else:
			player = execute_fight(command[1],command[2],player)

			
	elif command[0] == "talk":
		if len(command) > 1:
			player = execute_talk(command[1],player)
		else:
			print("Talk to who?")
			anykey()

	elif command[0] == 'look':
		if len(command) > 1:
			player = execute_look(command[1],player)
		else:
			print("Look at what?")
			anykey()

	elif command[0] == 'use':
		if len(command) > 1:
			player = execute_use(command[1],player)
		else:
			print("Use what?")
			anykey()

	elif command[0] == 'survey':
		execute_survey()

	else:
		print("This makes no sense.")
		anykey()
	return player

def menu(exits, player):

	print_menu(exits, player.current_room.items, player.inventory,player.current_room.npcs)


	user_input = input("> ")

	normalised_user_input = normalise_input(user_input)

	return normalised_user_input


def move(exits, direction):

	return rooms[exits[direction]]

def win_condition():
	return False
 #   if player.current_room == rooms["Office"]:
  #      print("Congratualations you have won!")
   #     return True
	#else:
	 #   return False


# This is the entry point of our program
def main():
	player = player_obj()
	# Main game loop
	while not win_condition():
		# Display game status (room description, inventory etc.)
		system('cls')
		print_room(player.current_room)
		print("You're carrying", inventory_mass(player.inventory), "kg.") 
		print_inventory_items(player.inventory)

		# Show the menu with possible actions and ask the player
		command = menu(player.current_room.exits,player)

		# Execute the player's command
		player = execute_command(command,player)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
	main()

