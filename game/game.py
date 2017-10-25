#!/usr/bin/python3
from os import system 
import msvcrt
from map import *
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

	output('Type HELP to see all available commands and their usage',player.sobriety)
	
	output("What do you want to do?",player.sobriety)


def is_valid_exit(exits, chosen_exit):

	return chosen_exit in exits

def execute_go(direction,player):



	if is_valid_exit(player.current_room.exits, direction):
		player.current_room = move(player.current_room.exits, direction)

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
	if victim == npc_kirill:
		output('You realise your mistake as soon as you make it. Kirill gracefully dodges your swing, dancing behind you. "Nothing personal kid" he whispers as he chokes you unconscious.')
		player.hp = 0
		anykey()

	your_weapon = get_item_from_inventory(item,player)
	if (your_weapon == None):
		pass
	elif (victim.hp // your_weapon.mass) + 1 < (player.hp // victim.inventory[0].mass) + 1:
		output('You have knocked out ' + npc + '. The following items: ' +  list_of_items(victim.inventory) + ' spill to the floor. Emptying their pockets reveals £'+str(round(victim.money,2)) , player.sobriety)
		player.money += victim.money
		player.current_room.items +=  player.current_room.npcs.pop(npc).inventory
		
		anykey()
	else:
		print(npc)
		output('The last thing you see is '+npc+' wielding '+victim.inventory[0].name+' before you are knocked unconscious',player.sobriety)
		player.hp = 0
	return player


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

def execute_help():
	print(''' 
GO PLACE to move
TAKE ITEM to take an item that is in a room
DROP ITEM to drop an item
FIGHT NPC ITEM to fight an npc with an item in your inventory (try something heavy)
TALK NPC to talk to an npc
LOOK ITEM to inspect an item in your inventory
USE ITEM to use an item in your inventory
ID to list the ids of the items in the room and your inventory''')
	anykey()

def execute_id(player):
	output('\nIn the room:',player.sobriety)
	for item in player.current_room.items:
		output(item.id,player.sobriety)
	output('\nIn your inventory:',player.sobriety)
	for item in player.inventory:
		output(item.id,player.sobriety)

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

	elif command[0] == 'id':
		execute_id(player)
		anykey()
	elif command[0] == 'help':
		execute_help()

	else:
		output("This makes no sense.", player.sobriety)
		anykey()
	return player

def menu(player):
	print_room(player)


	output("You can go " + ', '.join([direction + ' to '+exit_leads_to(player.current_room.exits, direction) for direction in player.current_room.exits]) + ".\n", player.sobriety)

	items = list_of_items(player.inventory)
	if items != '':
		print('You have ' + items +'. ',end = '',flush = True)
	output("You're carrying " + str(inventory_mass(player.inventory))+ "kg.\n", player.sobriety) 
	output('You have £'+ str(player.money)+'\n', player.sobriety)
		
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
			anykey()
			return True
		else:
			print('Without your id you are forced to go home, it\'s too late to go out again so you cry yourself to sleep')
			anykey()
			return True
	elif player.drugged:
		system('cls')
		print('Whoa this is wicked!') 
		psychedelic()
		anykey()
		return True
	elif player.hp <= 0:
		print("You died.")
		anykey()
		return True
	elif player.current_room == room_river:
		print("You wake up at the bay the next morning cold and covered in bits of plastic and fecal matter")
		anykey()
		return True


	elif player.hp == 0:
		print('You awaken in a police cell, you dread to imagine what fate awaits you')
		anykey()

	#elif kirill disco biscuit:
	#	anykey()
	#	return True
	elif (cheeseburger or chucken_nuggets or mayo_chicken or wrap_of_the_day or chips or bigmac or mcflurry or kebab) in player.inventory:
		print("You purchased some food and stumbled home while eating it, a rather successful night.")

	elif player.current_room == room_bed:
		print('''You are now known amongst your friends as the flaker, passive aggressive 
messages spam your messenger all night. 'enjoying netflix?!?!?!??!'
This wasn't your wisest choice.''')
		anykey()
		return True


	#elif: #lose fight
	#elif: #drown
	#elif: #takeaway
	#else: #kiril irish
	#	return False





	
	return False




# This is the entry point of our program
def main():

	player = player_obj()
	# Main game loop
	while not win_condition(player):
		# Display game status (room description, inventory etc.)
		system('cls')


		# Show the menu with possible actions and ask the player
		command = menu(player)

		# Execute the player's command

		player = execute_command(command,player)
	print('Game over')
	anykey()



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
	system('mode con: cols=100 lines=40')
	main()

