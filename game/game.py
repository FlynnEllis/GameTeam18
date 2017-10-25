#!/usr/bin/python3
from os import system 
import msvcrt
from map import rooms
from player import *
from items import *
from gameparser import *
from helperfunctions import *

def get_item_from_inventory(item_id):
	try:
		return inventory[[item.id for item in inventory].index(item_id)]

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
	print("You're carrying", inv_mass, "kg.") 
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


def print_menu(exits, room_items, inv_items):

	print("You can:")
	# Iterate over available exits
	for direction in exits:
		# Print the exit name and where it leads to
		print_exit(direction, exit_leads_to(exits, direction))
	for item in current_room.items:
		print("TAKE " + item.id.upper() + " to take " + item.name)
	for item in inv_items:
		print("DROP " + item.id.upper() + " to drop your " + item.name)
	for npc in current_room.npcs:
		print("FIGHT " + current_room.npcs[npc].name.upper() + " to fight " + current_room.npcs[npc].name.upper())
	
	print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):

	return chosen_exit in exits

def execute_go(direction):

	global current_room

	if is_valid_exit(current_room.exits, direction):
		current_room = move(current_room.exits, direction)
		print("You are in", current_room.name)
	else:
		print("You cannot go there.")
		anykey()

def execute_take(item_id):
	try:
		item_id = [item.id for item in current_room.items].index(item_id)
		if (current_room.items[item_id].mass +  inventory_mass(inventory)) > 20:
			print(("Inventory full!").upper())
			anykey()
		else:
			inventory.append(current_room.items.pop(item_id))

	except ValueError:
		print('You cannot take that')
		anykey()

	

def execute_drop(item_id):
	try:
		current_room.items.append(inventory.pop([item.id for item in inventory].index(item_id)))
	except ValueError:
		print('You cannot drop that')
		anykey()

def execute_fight(npc,item):
	try:
		victim = current_room.npcs[npc]
	except KeyError:
		print(npc[0].upper() + npc[1:] + ' is not in the room')
		anykey()
		return
	your_weapon = get_item_from_inventory()
	if (your_weapon == None):
		return
	elif (victim.hp // your_weapon.mass) + 1 < (hp // victim.inventory[0].mass) + 1:
		print('You have knocked out ' + npc +' emptying their pockets reveals ' + list_of_items(victim.inventory))
		current_room.items +=  current_room.npcs.pop(npc).inventory
		
		anykey()
	else:
		return

	

	#return npc



<<<<<<< HEAD

=======
def print_chat_options(options,cursor):
	for index in range(len(options)):
		if index == cursor:
			print('{ '+ options[index] +' }')
		else:
			print('  ' + options[index])
 
def navigate_chat_options(options,cursor):
	system('cls')
	print_chat_options(options,cursor)
	key = getkey()
	while 1:
		if key == 'up':
			return navigate_chat_options(options,cursor -1)
		elif key == 'down':
			return navigate_chat_options(options,cursor +1)
		else:
			return cursor
		key = getkey()
 
 
 
def getkey():
	while True:
		if msvcrt.kbhit():        
			char = msvcrt.getch()

			if char in [b'\xe0']:
				char = msvcrt.getch()
				return {b'H': 'up', b'P': 'down'}[char]
			else:
				return char
>>>>>>> a36ab898f6d3de80fe6165a42bdd812f86e61de6
def anykey():
	print('Press any key to continue')
	while True:
		if msvcrt.kbhit():
			return

def execute_talk(npc):
	npc.talk()
   

def execute_look(item):
	item = get_item_from_inventory(item)
	if item != None:
		print(item.name)
		print(item.desc)
		anykey()

def execute_use(item):
	inventory,sobriety = item.use(inventory,sobriety) 
	anykey()

def execute_survey():
	pass

def execute_command(command):

	if 0 == len(command):
		return
	if command[0] == "go":
		if len(command) > 1:
			execute_go(command[1])
		else:
			print("Go where?")
			anykey()

	elif command[0] == "take":
		if len(command) > 1:
			execute_take(command[1])
		else:
			print("Take what?")
			anykey()

	elif command[0] == "drop":
		if len(command) > 1:
			execute_drop(command[1])
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
			execute_fight(command[1],command[2])

			
	elif command[0] == "talk":
		if len(command) > 1:
			execute_talk(command[1])
		else:
			print("Talk to who?")
			anykey()

	elif command[0] == 'look':
		if len(command) > 1:
			execute_look(command[1])
		else:
			print("Look at what?")
			anykey()

	elif command[0] == 'use':
		if len(command) > 1:
			execute_use(command[1])
		else:
			print("Use what?")
			anykey()

	elif command[0] == 'survey':
		execute_survey()

	else:
		print("This makes no sense.")
		anykey()


def menu(exits, room_items, inv_items):

	print_menu(exits, room_items, inv_items)


	user_input = input("> ")

	normalised_user_input = normalise_input(user_input)

	return normalised_user_input


def move(exits, direction):

	return rooms[exits[direction]]

def win_condition():
	return False
 #   if current_room == rooms["Office"]:
  #      print("Congratualations you have won!")
   #     return True
	#else:
	 #   return False


# This is the entry point of our program
def main():

	# Main game loop
	while not win_condition():
		# Display game status (room description, inventory etc.)
		system('cls')
		print_room(current_room)
		print_inventory_items(inventory)

		# Show the menu with possible actions and ask the player
		command = menu(current_room.exits, current_room.items, inventory)

		# Execute the player's command
		execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
	main()

