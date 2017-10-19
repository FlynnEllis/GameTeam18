from items import *
from npcs import *

class room():
    def __init__room(self,name,exits,items,npcs):
        self.name = name                    #Name of the room (string e.g.'glam')
        self.exits = exits                  #exits from the room (dict e.g. {'north':'glam'})
        self.items = items                  #items in the room (list of objects)
        self.npcs = npcs                    #non-player characters in the room (list of objects)

room_pre_pre_drinks = room(
    "pre pre drinks",
    {"leave flat": "pre drinks"},
    [npc_john],
    [])
    
room_pre_drinks =  room( 
    "pre drinks",
    {"south": "student union", "east": "tiger tiger", "west": "pryzm"},
    [],
    [])

room_student_union =  room(
    "student union",
    { "west": "tiger tiger", "east": "pryzm", "south": "glam"},
    [],
    [])

room_tiger_tiger =  room(
    "tiger tiger",
    {"north": "student union", "east": "glam", "south": "revs"},
    [],
    [])

room_pryzm =  room(
    "pryzm",
    {"north": "student union", "west": "glam", "south": "clwb ifor bach"},
    [],
    [])

room_glam =  room(
    "glam",
    {"north": "student union", "west": "tiger tiger", "south east": "clwb ifor bach", "south west": "revs", "east": "pryzm"},
    [],
    [])

room_revs =  room(
    "revs",
    {"north": "tiger tiger", "west": "glam", "south": "clwb ifor bach"},
    [],
    [])

room_clwb_ifor_bach = room(
    "clwb ifor bach",
    {"north": "pryzm", "west": "glam", "south": "revs"},
    [],
    [])

room_chip_alley =  room(
    "chip alley",
    {"home": "home"},
    [],
    [])

room_mc_donalds =  room(
    "mc donalds",
    {"home": "home"},
    [],
    [])

room_burger_guy =  room(
    "burger guy",
    {"home": "home"},
    [],
    [])

#ENDINGS BELOW
room_ending =room(
     "home",
     {},
    [],
    []
)

rooms = {
'pre pre drinks': room_pre_pre_drinks,
"pre drinks":room_pre_drinks,
   "student union":room_student_union, 
"tiger tiger":room_tiger_tiger, 
    
"pryzm":room_pryzm, 
 "glam":room_glam, 
"revs":room_revs,  
 "clwb ifor bach":room_clwb_ifor_bach,
    
"chip alley":room_chip_alley,  
    
"mc donalds":room_mc_donalds, 
"burger guy":room_burger_guy}
   
