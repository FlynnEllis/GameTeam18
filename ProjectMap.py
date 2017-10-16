Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
room_pre_pre_drinks = (
    "name": "pre pre drinks"
    "exits": ("leave flat": "pre drinks")
    )
room_pre_drinks = (
    "name": "pre drinks"
    "exits": ("south": "student union", "east": "tiger tiger", "west": "pryzm")
    )
room_student_union = (
    "name": "student union"
    "exits":( "west": "tiger tiger", "east": "pryzm", "south": "glam")
    )
room_tiger_tiger = (
    "name": "tiger tiger"
    "exits": ("north": "student union", "east": "glam", "south": "revs")
    )
room_pryzm = (
    "name": "pryzm"
    "exits": ("north": "student union", "west": "glam", "south": "clwb ifor bach")
    )
room_galm = (
    "name": "glam"
    "exits": ("north": "student union", "west": "tiger tiger", "south east": "clwb ifor bach", "south west": "revs", "east": "pryzm")
    )
room_revs = (
    "name": "revs"
    "exits": ("north": "tiger tiger", "west": "glam", "south": "clwb ifor bach")
    )
room_clwb_ifor_bach = (
    "name": "clwb ifor bach"
    "exits": ("north": "pryzm", "west": "glam", "south": "revs")
    )
room_chip_alley = (
    "name": "chip alley"
    "exits": ("home": "home")
    )
room_mc_donalds = (
    "name": "mc donalds"
    "exits": ("home": "home")
    )
room_burger_guy = (
    "name": "burger guy"
    "exits": ("home": "home")
#ENDINGS BELOW
room_ending =(
    "name": "home"
    )
