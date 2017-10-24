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
    {"south": "student union", "east": "tiger tiger", "west": "pryzm", "home": "your room"},
    [], #items
    {}, #npcs
    """You arrive at pre drinks, the room is full of vodka, testosterone and bad life decisions. 
    Apart from everyone having a crippling university debt the room seems to be in good spirits. 
    The music in the room appears to be Grime Time, which you should have expected by now. 
    From across the room you see your squad and go over to get this party started. 
    Now do you choose to go hard and drink an alcoholic concoction or stay sober and have a coke?
    """)

room_pre_pre_drinks = room(
    "pre pre drinks",
    {"out": 'pre drinks', "in": "your room"},
    [],
    {'john':npc_john},

    """Welcome to the start of the greatest night of your life. 
    You have received an invitation to the biggest bar crawl in Cardiff which includes such nightlife as the SU, Pryzm and even Tiger Tiger. 
    Before you leave you should select some belongings that will help you along the way.""")
    
room_your_room = room(
    "your room",
    {"back":'pre pre drinks'},
    [wallet, your_id, keys],
    {},
    """You return to your room, sad and alone.
    You crash onto your bed ands start crying.
    WHY WOULD YOU GO HOME! 
    WHO DOES THAT!
    Game Over, you never go home after pre drinks!""")

room_student_union =  room(
    "student union",
    { "leave1": "tiger tiger", "leave2": "pryzm", "north": "student union bar"},
    [],
    {'Jill' : npc_jill},
    """You have arrived at the Student Union. 
    After queueing for what seemed 3 decades you have arrived at the main dance floor. 
    It appears that a foam party is happening on this particular night. 
    From across the room you can see half the people trying not to suffocate from the foam and the other half trying to not look like a cardboard cut-out.
    The music appears to be 80s hits, which you seem to enjoy.
    Do you make your way to the bar or leave to go to another club?""")

room_student_union_bar =  room(
    "student union bar",
    {"south": "student union"},
    [],
    {},
    """As you lean over the bar to peer into the mini fridge, 
    you find that the only drinks on offer tonight are VKs and they only cost 1. Perfect.
    """)

room_tiger_tiger =  room(
    "tiger tiger",
    {"leave1": "student union", "leave2": "pryzm", "upstairs": "tiger tiger main"},
    [],
    {},
    """You arrive at the ever hyped but always dissapointing Tiger Tiger. 
    The queue is as short as your life expectancy so you enter straight away. 
    The atmosphere seems to have a sort of life to it although what that life is you are never sure. You can choose to enter this uncommon occurrence or leave for yet another cesspool. """)

room_tiger_tiger_main =  room(
    "tiger tiger main",
    {"leave1": "student union", "leave2": "pryzm", "downstairs": "tiger tiger entrance", "east": "tiger tiger second"},
    [],
    {},
    """You are in the main room of tiger tiger!
    Much to your surprise the normally barren and empty dancefloor is full of people, 
    however floors are a bit sticky so dancing will require a bit more effort than you would like.

    """)

room_tiger_tiger_second =  room(
    "tiger tiger second",
    {"leave1": "student union", "leave2": "pryzm", "west": "tiger tiger main", "east": "smoking area", "south": "tiger tiger toilet"},
    [],
    {},
    """You enter the second room in tiger tiger.
    its kinda like the other one but the floors arent as sticky this time.

    """)

room_tiger_tiger_toilet =  room(
    "tiger tiger toilet",
    {"leave1": "student union", "leave2": "pryzm", "north": "tiger tiger second"},
    [],
    {},
    """

    """)

room_smoking_area =  room(
    "smoking area",
    {"west": "tiger tiger second"},
    [],
    {},
    """You dont want to do that do you? Smoking is bad remember!

    """)

room_pryzm =  room(
    "pryzm",
    {"leave1": "student union", "leave2": "tiger tiger", "upstairs": "pryzm main"},
    [],
    {},
    """You arrive at Pryzm. 
    The queue was so long you started to question your life decisions. 
    As you finally get into the club, you see two things: 
    The club is packed and there is a lot of creepy guys grabbing girls everywhere without consent. 
    If you would like to join in and lose all sense of pride and eventually enter the depths of hell, proceed and enter to the bar or leave for another club.""")

room_pryzm_bar =  room(
    "pryzm bar",
    {"leave1": "student union", "leave2": "tiger tiger", "south": "pryzm main"},
    [],
    {},
    """ 
    """)

room_pryzm_main =  room(
    "pryzm main",
    {"leave1": "student union", "leave2": "tiger tiger", "west": "pryzm disco", "north": "bar", "south": "toilet","downstairs": "pryzm"},
    [],
    {'Barry Chuckle' : npc_Chuckle_1, 'Paul Chuckle' : npc_Chuckle_2},
    """Welcome to the main floor 
    (something funny), in the corner you spot two odd looking men with moustaches taking pictures with everyone.
    """)

room_pryzm_disco =  room(
    "pryzm disco",
    {"leave1": "student union", "leave2": "tiger tiger", "east": "pryzm main", "north": "bar"},
    [],
    {},
    """

    """)

room_pryzm_toilet=  room(
    "pryzm toilet",
    {"leave1": "student union", "leave2": "tiger tiger", "north": "pryzm main"},
    [],
    {},
    """

    """)

room_welsh_pub =  room(
    "welsh pub",
    {"north": "pub bar", "ouside": "river"},
    [],
    {},
    """You have somehow ended up in a welsh pub.
    The room is full of balding middle aged men that all seem to be glaring at you.
    They know you dont belong here. 
    You know you dont belong here.

    """)

room_pub_bar =  room(
    "pub bar",
    {"south": "welsh pub"},
    [],
    {},
    """

    """)


#room_glam =  room(
#    "glam",
#    {"north": "student union", "west": "tiger tiger", "southeast": "clwb ifor bach", "southwest": "revs", "east": "pryzm"},
#    [],
#    [],
#    """Welcome to Glam. 
#    (I am trying to hype this place up but we all really know how bad it is). 
#    The party is electrifying and its one of the best places you haveve ever been. 
#    (can you smell that sarcasm or is that the toilets). 
#    What am I joking this place is normally barren with somewhat decent drinks. 
#    You can choose to enter and forever question why you entered, or leave for another life of luxury?""")

#room_revs =  room(
#    "revs",
#    {"north": "tiger tiger", "west": "glam", "south": "clwb ifor bach"},
#    [],
#    [],
#    """Welcome to a club that tries to look posh and sophisticated but is anything but. 
#    The queue is relatively normal and will not have you dying of thirst by the end. 
#    Once your ID has been checked by 50 machines you finally get in. 
#    It appears that the majority of people have been herded toward the back or upstairs like cattle. 
#    Although the music seems decent you are aware that the drinks taste cheaper than that guy across the room in his Ralph Lauren shirt and Rebook tracksuit bottoms. 
#    Do you enter at your own risk or leave for another club?""")

#room_clwb_ifor_bach = room(
#    "clwb ifor bach",
#    {"north": "pryzm", "west": "glam", "south": "revs"},
#    [],
#    [],
#    """Welcome to the hottest club on the map. No, it is not full of Britains next top models. 
#    It is more like a sauna full of sweaty men trying to dance. 
#    The floor looks more like an Olympic swimming pool than somewhere you would bust and move and make those shapes to impress that girl who always rejects you. 
#    Do you pull up your swimming trunks and doggy paddle in or leave before you get soaked?""")

#room_chip_alley =  room(
#    "chip alley",
#    {"home": "home"},
#    [],
#    [],
#    """ Welcome to Chip Alley, the aroma of different smells hits you from kebabs to cheesey chips to even pizza?
#    None the less this seems like a fine place to finish the night and get food before you head home. 
#    Do you enter the wonderfully endulging takeaways or go home hungry and sad""")

room_mc_donalds =  room(
    "mc donalds",
    {"home": "home"},
    [],
    [],
    """ Welcome to Mc Donalds, what many people consider is the root of all evil. 
    This fine establishjment is packed, the bouncers are making you queue and most people are sat on the floor.
    Do you choose to risk your colon and ventuire in or go home hungry?""")

room_burger_guy =  room(
    "burger guy",
    {"home": "home"},
    [],
    [],
    """ As you leave the SU you notice the usual guy flipping his burgers, with as much finese as your night out.
    He appears to stare at you like you are his next biggest catch, coiled like a spring he waits for you.
    Do you endulge thew coiled spring and eat here, or go home starving?""")

#ENDINGS BELOW
#NEED MORE ENDINGS!
room_ending =room(
     "home",
     {},
    [],
    [],
    "Insert description here")


rooms = {
"your room": room_your_room,
'pre pre drinks': room_pre_pre_drinks,
"pre drinks": room_pre_drinks,
"student union": room_student_union,
"student union bar": room_student_union_bar,
"tiger tiger": room_tiger_tiger, 
"tiger tiger main": room_tiger_tiger_main,
"tiger tiger second": room_tiger_tiger_second,
"tiger tiger toilet": room_tiger_tiger_toilet,
"smoking area": room_smoking_area,   
"pryzm":room_pryzm,
"pryzm bar": room_pryzm_bar,
"pryzm main": room_pryzm_main,
"pryzm disco": room_pryzm_disco,
"pryzm toilet": room_pryzm_toilet,
"welsh pub": room_welsh_pub,
"pub bar": room_pub_bar,

#"glam":room_glam, 
#"revs":room_revs,  
#"clwb ifor bach":room_clwb_ifor_bach,
    
#"chip alley":room_chip_alley,  
    
"mc donalds":room_mc_donalds, 
"burger guy":room_burger_guy}


