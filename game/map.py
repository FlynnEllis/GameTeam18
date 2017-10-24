from items import *
from npcs import *

class room():
    def __init__(self,name,exits,items,npcs,description):
        self.name = name                    #Name of the room (string e.g.'glam')
        self.exits = exits                  #exits from the room (dict e.g. {'north':'glam'})
        self.items = items                  #items in the room (list of objects)
        self.npcs = npcs                    #non-player characters in the room (list of objects)
        self.description = description      #description str

room_pre_drinks =  room( 
    "pre drinks",
    {"south": "student union", "east": "tiger tiger", "west": "pryzm"},
    [],
    [],
    """You arrive at pre drinks, the room is full of vodka, testosterone and bad life decisions. 
    Apart from everyone having a crippling university debt the room seems to be in good spirits. 
    The music in the room appears to be Grime Time, which you should have expected by now. 
    From across the room you see your squad and go over to get this party started. 
    Now do you choose to go hard and drink an alcoholic concoction or stay sober and have a coke?
    """)

room_pre_pre_drinks = room(
    "pre pre drinks",
    {"out": 'pre drinks'},
    [],
    {'john':npc_john},
    """Welcome to the start of the greatest night of your life. 
    You have received an invitation to the biggest bar crawl in Cardiff which includes such nightlife as the SU, Pryzm and even Tiger Tiger. 
    Before you leave you should select some belongings that will help you along the way.""")
    
    


room_student_union =  room(
    "student union",
    { "west": "tiger tiger", "east": "pryzm", "south": "glam"},
    [],
    [],
    """You have arrived at the Student Union. 
    After queueing for what seemed 3 decades you have arrived at the main dance floor. 
    It appears that a foam party is happening on this particular night. 
    From across the room you can see half the people trying not to suffocate from the foam and the other half trying to not look like a cardboard cut-out.
    The music appears to be 80s hits, which you seem to enjoy.
    Do you make your way to the bar or leave to go to another club?""")

room_tiger_tiger =  room(
    "tiger tiger",
    {"north": "student union", "east": "glam", "south": "revs"},
    [],
    [],
    """You arrive at the ever hyped but always a huge disappointment called Tiger Tiger. 
    The queue is as short as your life expectancy so you enter straight away. 
    Much to your surprise the normally barren and empty dancefloor much like your soul is full of people. 
    The atmosphere seems to have a sort of life to it although what that life is you are never sure. You can choose to enter this uncommon occurrence or leave for yet another cesspool. """)

room_pryzm =  room(
    "pryzm",
    {"north": "student union", "west": "glam", "south": "clwb ifor bach"},
    [],
    [],
    """You arrive at Pryzm. 
    You join the queue that was so long you started to question your life decisions. 
    As you finally get into the club, you see two things: 
    The club is packed and there is a lot of creepy guys grabbing girls everywhere without consent. 
    If you would like to join in and lose all sense of pride and eventually enter the depths of hell, proceed and enter to the bar or leave for another club.""")

room_glam =  room(
    "glam",
    {"north": "student union", "west": "tiger tiger", "southeast": "clwb ifor bach", "southwest": "revs", "east": "pryzm"},
    [],
    [],
    """Welcome to Glam. 
    (I am trying to hype this place up but we all really know how bad it is). 
    The party is electrifying and its one of the best places you haveve ever been. 
    (can you smell that sarcasm or is that the toilets). 
    What am I joking this place is normally barren with somewhat decent drinks. 
    You can choose to enter and forever question why you entered, or leave for another life of luxury?""")

room_revs =  room(
    "revs",
    {"north": "tiger tiger", "west": "glam", "south": "clwb ifor bach"},
    [],
    [],
    """Welcome to a club that tries to look posh and sophisticated but is anything but. 
    The queue is relatively normal and will not have you dying of thirst by the end. 
    Once your ID has been checked by 50 machines you finally get in. 
    It appears that the majority of people have been herded toward the back or upstairs like cattle. 
    Although the music seems decent you are aware that the drinks taste cheaper than that guy across the room in his Ralph Lauren shirt and Rebook tracksuit bottoms. 
    Do you enter at your own risk or leave for another club?""")

room_clwb_ifor_bach = room(
    "clwb ifor bach",
    {"north": "pryzm", "west": "glam", "south": "revs"},
    [],
    [],
    """Welcome to the hottest club on the map. No, it is not full of Britains next top models. 
    It is more like a sauna full of sweaty men trying to dance. 
    The floor looks more like an Olympic swimming pool than somewhere you would bust and move and make those shapes to impress that girl who always rejects you. 
    Do you pull up your swimming trunks and doggy paddle in or leave before you get soaked?""")

room_chip_alley =  room(
    "chip alley",
    {"home": "home"},
    [],
    [],
    "Insert description here")

room_mc_donalds =  room(
    "mc donalds",
    {"home": "home"},
    [],
    [],
    "Insert description here")

room_burger_guy =  room(
    "burger guy",
    {"home": "home"},
    [],
    [],
    "Insert description here")

#ENDINGS BELOW
room_ending =room(
     "home",
     {},
    [],
    [],
    "Insert description here")


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
   
