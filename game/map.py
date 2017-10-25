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
    {"back":'pre pre drinks', "bed":'your bed'},
    [wallet, your_id, keys],
    {},
    """You sit on your bed contemplating your outfit for the night, the walls are shaking from
    the predrinks occuring next door. It is time to grace them with your presence.

    """)

room_bed = room(
    "your bed",
    {},
    [],
    {},
    """You are now known amongst your friends as the flaker, passive aggressive messages spam your messenger all night. 'enjoying netflix?!?!?!??!'
    This wasn't your wisest choice.

    """)

room_student_union =  room(
    "student union",
    { "tiger": "tiger tiger", "pryzm": "pryzm", "dancefloor": "student union dancefloor", "bar":"student union bar"},
    [],
    {'jill' : npc_jill},
    """You have arrived at the Student Union. 
    After queueing for what seemed 3 decades you have arrived at the main dance floor. 
    It appears that a foam party is happening on this particular night. 
    From across the room you can see half the people trying not to suffocate from the foam and the other half trying to not look like a cardboard cut-out.
    The music appears to be 80s hits, which you seem to enjoy.
    Do you make your way to the bar or leave to go to another club?""")

room_student_union_dancefloor =  room(
    "student union dancefloor",
    {"bar": "student union bar","exit":"student union"},
    [],
    {},
    """The floor is sticky with less fortunate VK's than yours, they have a good owner. You awkwardly sway to the tunes, swigging on your VK occaisionally to blend in.
    You are not quite sure why anyone drinks VK's.
    """)

room_student_union_bar =  room(
    "student union bar",
    {"dancefloor": "student union dancefloor", "exit":"student union"},
    [],
    {'bartender': npc_su_bar},
    """After queing for at least half an hour you make it to the bar. As the pressure of the people pushing on you grows
    you manage to shout VK breathlessly at the bartender. He asks what colour and you desperately gesture at the fridge.
    Luckily VK's only only cost 1 tonight. Perfect.
    """)

room_tiger_tiger =  room(
    "tiger tiger",
    {"su": "student union", "pryzm": "pryzm", "upstairs": "tiger tiger main"},
    [],
    {},
    """You arrive at the ever hyped but always dissapointing Tiger Tiger. 
    The queue is as short as your life expectancy so you enter straight away. 
    The atmosphere seems to have a sort of life to it although what that life is you are never sure. You can choose to enter this uncommon occurrence or leave for yet another cesspool. """)

room_tiger_tiger_main =  room(
    "tiger tiger main",
    {"downstairs": "tiger tiger", "bar": "tiger tiger bar", "tiger2":"tiger tiger second"},
    [],
    {},
    """You are in the main room of tiger tiger!
    Much to your surprise the normally barren and empty dancefloor is full of people, 
    however floors are a bit sticky so dancing will require a bit more effort than you would like.

    """)

room_tiger_tiger_bar =  room(
    "tiger tiger bar",
    {"exit":"tiger tiger", "south": "tiger tiger main", "tiger2":"tiger tiger second"},
    [],
    {'Bartender': npc_tiger_tiger_bar},
    """

    """)

room_tiger_tiger_second =  room(
    "tiger tiger second",
    {"north": "tiger tiger main", "toilet": "tiger tiger toilet", "bar":"tiger tiger bar"},
    [],
    {},
    """You enter the second room in tiger tiger.
    its kinda like the other one but the floors arent as sticky this time.

    """)

room_tiger_tiger_toilet =  room(
    "tiger tiger toilet",
    {"tiger2": "tiger tiger second", "south":"tiger tiger main","bar":"tiger tiger bar"},
    [],
    {},
    """

    """)


room_pryzm =  room(
    "pryzm",
    {"su": "student union", "tiger": "tiger tiger", "upstairs": "pryzm main"},
    [],
    {},
    """You arrive at Pryzm. 
    The queue was so long you started to question your life decisions. 
    As you finally get into the club, you see two things: 
    The club is packed and there is a lot of creepy guys grabbing girls everywhere without consent. 
    If you would like to join in and lose all sense of pride and eventually enter the depths of hell, proceed and enter to the bar or leave for another club.""")

room_pryzm_bar =  room(
    "pryzm bar",
    {"south": "pryzm main", "disco":"pryzm disco", "toilet":"pryzm toilet", "exit":"pryzm"},
    [],
    {'Bartender': npc_pryzm_bar},
    """You hope you brought enough gold bullion with you as you approach the pryzm bar. The bartender spins bottles around fancily whilst pouring the
    last order. I guess spirits are the order of the night here.
    """)

room_pryzm_main =  room(
    "pryzm main",
    {"disco": "pryzm disco", "bar":"pryzm bar", "toilet":"pryzm toilet","exit":"pryzm"},
    [],
    {'Barry Chuckle' : npc_Chuckle_1, 'Paul Chuckle' : npc_Chuckle_2},
    """Welcome to the main floor where the bass is giving you heart palputations and the lights elevating you to a new plane of being,
    in the corner you spot two odd looking men with moustaches taking pictures with everyone.
    """)

room_pryzm_disco =  room(
    "pryzm disco",
    {"north":"pryzm main", "bar":"pryzm bar", "exit":"pryzm"},
    [],
    {},
    """The sound of High School Musical greets your ears as you enter the disco room, you take one last deep breath before proceeding to belt
    out the lyrics to the best of your ability. Perhaps you should work on those high notes.

    """)

room_pryzm_toilet=  room(
    "pryzm toilet",
    {"smoke":"pryzm smoke", "north": "pryzm main", "exit":"pryzm"},
    [],
    {},
    """The smell of piss and other delights greets you as you walk into the toilets. They are packed as usual and you have to wait for your time to shine.
    """)


room_pryzm_smoking_area =  room(
    "pryzm smoke",
    {"toilets": "pryzm toilet", "exit":"pryzm"},
    [],
    {},
    """You walk into the smoking area and reach for your pockets for a cigarette, it is then you remember that smoking shortens your life expectancy by ten years,
    you won't be smoking today.

    """)

room_welsh_pub =  room(
    "welsh pub",
    {"bar": "pub bar", "ouside": "river"},
    [],
    {},
    """You have somehow ended up in a welsh pub. The delights of Delilah fill your ears, along with the cacophony of
    a room full of balding middle aged men singing along, they all seem to be glaring at you.
    They know you dont belong here. 
    You know you dont belong here.

    """)

room_pub_bar =  room(
    "pub bar",
    {"south": "welsh pub"},
    [],
    {'Bartender': npc_welsh_bar},
    """It looks like a pint of Brains is the favourite drink here. Maybe it will help you blend in.
    The welsh national anthem comes on and you try your best to move your mouth to match the funny sounds whilst you wait
    for your order.

    """)

room_river = room(
    "river",
    {},
    [],
    {},
    """It appears whilst drunk you stumbled and fell in the river Taff, the water seeps into your clothes as your feet touch a number of foreign objects.
    Was that a shopping trolley?
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
room_endings = {
"your bed": room_bed,
"river": room_river,
}


rooms = {
"your room": room_your_room,
"your bed": room_bed,
'pre pre drinks': room_pre_pre_drinks,
"pre drinks": room_pre_drinks,
"student union": room_student_union,
"student union bar": room_student_union_bar,
"student union dancefloor": room_student_union_dancefloor,
"tiger tiger": room_tiger_tiger, 
"tiger tiger main": room_tiger_tiger_main,
"tiger tiger bar": room_tiger_tiger_bar,
"tiger tiger second": room_tiger_tiger_second,
"tiger tiger toilet": room_tiger_tiger_toilet,
"pryzm smoke": room_pryzm_smoking_area,   
"pryzm":room_pryzm,
"pryzm bar": room_pryzm_bar,
"pryzm main": room_pryzm_main,
"pryzm disco": room_pryzm_disco,
"pryzm toilet": room_pryzm_toilet,
"welsh pub": room_welsh_pub,
"pub bar": room_pub_bar,
"river": room_river,

#"glam":room_glam, 
#"revs":room_revs,  
#"clwb ifor bach":room_clwb_ifor_bach,
    
#"chip alley":room_chip_alley,  
    
"mc donalds":room_mc_donalds, 
"burger guy":room_burger_guy}


