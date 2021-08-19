######################################
#####Declarations##############
#######################################


#InteractiveDirector
define director.show_tags = ("Lucille Smile" "Lucille Smug" "Lucille Mad" "Lucille Normal" "Lucille Normal 2" "Demon Maid")
define director.transitions = [ "Dissolve(0.5)", "Pixellate" ]
define director.spacing = 0


#Effects
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')



#InteractiveDirector
define director.show_tags = ("Lucille" "Demon" "Lisa" "GuildMaster")
define director.transitions = [ "Dissolve(0.5)", "Pixellate", "flashbulb", "vpunch" ]
define director.spacing = 0


#ClickToContinue
image ctc_blink:
       "GUI/arrow.png"
       yalign 0.91 xalign 0.86
       linear 0.75 alpha 0.0
       linear 0.75 alpha 1.0
       repeat



#SplashScreen
image splash = "MenuItems/CompanyScreen.png"

#Main Menu
image Snow = Snow("images/MenuItems/Snowflake.png")





#In Game
define mc = Character('[playerName]',ctc="ctc_blink",
        ctc_position="fixed")
define lisa = Character('Elisabeth',ctc="ctc_blink",
        ctc_position="fixed")
define lisa2 = Character('Elisabeth',ctc="ctc_blink",
        ctc_position="fixed", who_color="#ff4d94")        
define lucille = Character('Lucille',ctc="ctc_blink",
        ctc_position="fixed")
define n = Character('???',ctc="ctc_blink",
        ctc_position="fixed")
define nr = Character(None,ctc="ctc_blink",
        ctc_position="fixed")
define gd = Character('Goddess',ctc="ctc_blink",
        ctc_position="fixed")


#Background
image BG_Castle_Bedroom= "images/BG/Castle Bedroom.png"
image BG_Castle_Bedroom_Day= "images/BG/Castle Bedroom Day.png"
image BG_Castle_Hall_Day= "images/BG/CastleHall_Day.png"
image BG_City = "images/BG/City.png"
image BG_City_BW= im.Sepia("images/BG/City.png")
image BG_City_Invert= im.MatrixColor("images/BG/City.png", im.matrix.invert())
image BG_Dining_Room = "images/BG/Dining Room.png"
image BG_Garden_Day = "images/BG/Garden Day.png"
image BG_Garden_Day_2 = "images/BG/Garden Day 2.png"
image BG_Garden_Night_2 = "images/BG/Garden Night 2.png"
image BG_Library = "images/BG/Library.png"
image BG_Modern_Room = "images/BG/ModernRoom.png"
image BG_Sky = "images/BG/Sky.png"
image BG_Throne_Room = "images/BG/Throne room.png"
image BG_Forest Day= "images/BG/Forest_Day.png"
image BG_ForestPath Day= "images/BG/ForestPath_Day.png"
image CG_Goddess = "images/CG/Goddess.png"
image BG_ForestPath Night= "images/BG/ForestPath_Night.png"
image BG_Rustic_Room Day = "images/BG/rustic room morning.png"
image BG_Rustic_Room Night = "images/BG/rustic room gabi.png"
image BG_Training = "images/BG/Training Grounds.png"


image Selection_Forest = im.Scale("images/BG/Forest_Selection.png" , 280, 600)
image Selection_Forest2 = im.Scale("images/BG/Forest_Selection.png" , 350, 640)
image Selection_Castle = im.Scale("images/BG/Castle_Selection.png" , 280, 600)
image Selection_Castle2 = im.Scale("images/BG/Castle_Selection.png" , 350, 640)




#Sprite#####################################################################

#Goddess
image Goddess:
        "images/Goddess/Goddess2.png"
        xalign 0.5 yalign 0.7
        linear 1.0 xalign 0.45 yalign 0.5
        linear 2.0 xalign 0.40 yalign 0.55
        linear 2.0 xalign 0.45 yalign 0.6
        linear 1.0 xalign 0.50 yalign 0.55
        linear 1.5 xalign 0.55 yalign 0.45
        linear 1.0 xalign 0.60 yalign 0.55
        linear 1.5 xalign 0.55 yalign 0.65
        linear 2.0 xalign 0.5 yalign 0.7
        repeat
image Goddess_Wings:
        "images/Goddess/Wings.png"
        xalign 0.5 yalign 0.7
        linear 1.2 xalign 0.45 yalign 0.55
        linear 1.8 xalign 0.40 yalign 0.53
        linear 2.2 xalign 0.45 yalign 0.55
        linear 0.8 xalign 0.50 yalign 0.50
        linear 1.7 xalign 0.55 yalign 0.44
        linear 0.8 xalign 0.60 yalign 0.55
        linear 1.7 xalign 0.55 yalign 0.60
        linear 1.8 xalign 0.5 yalign 0.7
        repeat

#Goblin
image Goblin_Weak:
        "images/Goblin/Goblin.png"
        yalign 0.7

#Lisa
image Lisa Smile:
        "images/Elisabeth/ElisabethPose01-1.png"
        yalign 0.5

image Lisa Smile2:
        "images/Elisabeth/ElisabethPose02-1.png"
        yalign 0.5
        ypos 1.08

image Lisa Shy1:
        "images/Elisabeth/ElisabethPose01-2.png"
        ypos 1.08

image Lisa Shy2:
        "images/Elisabeth/ElisabethPose02-3.png"
        ypos 1.08

image Lisa Normal:
        "images/Elisabeth/ElisabethPose01-4.png"
        ypos 1.08

image Lisa Smile2:
        "images/Elisabeth/ElisabethPose02-1.png"
        ypos 1.08

image Lisa Smile3:
        "images/Elisabeth/ElisabethPose03-1.png"
        ypos 1.08

image Lisa Smile4:
        "images/Elisabeth/ElisabethPose03-3.png"
        ypos 1.08

image Lisa Sad:
        "images/Elisabeth/ElisabethPose01-3.png"
        ypos 1.13

image Lisa Smirk:
        "images/Elisabeth/ElisabethPose02-2.png"
        ypos 1.08

image Lisa Angry:
        "images/Elisabeth/ElisabethPose03-2.png"
        ypos 1.08

#Guild master
image GuildMaster:
        "images/GuildMaster/Guild Master.png"
        yalign -2.0

#Lucille
image Lucille Smile:
        "images/Lucille/LucillePose01-1.png"
        yalign 0.5

image Lucille Smug:
        "images/Lucille/LucillePose01-2.png"
        yalign 0.5

image Lucille Mad:
        "images/Lucille/LucillePose01-3.png"
        yalign 0.5

image Lucille Normal:
        "images/Lucille/LucillePose01-4.png"
        yalign 0.5

image Lucille Normal 2:
        "images/Lucille/LucillePose02-1.png"
        yalign 0.5

image Lucille Happy:
        "images/Lucille/LucillePose02-2.png"
        yalign 0.5

image Lucille Embarassed:
        "images/Lucille/LucillePose02-3.png"
        yalign 0.5

image Lucille Pose:
        "images/Lucille/LucillePose03-1.png"
        yalign 0.5

image Lucille Shocked:
        "images/Lucille/LucillePose03-2.png"
        yalign 0.5


image Lucille Normal 2:
        "images/Lucille/LucillePose02-1.png"
        yalign 0.5

image Lucille Happy:
        "images/Lucille/LucillePose02-2.png"
        yalign 0.5

image Lucille Embarassed:
        "images/Lucille/LucillePose02-3.png"
        yalign 0.5

image Lucille Pose:
        "images/Lucille/LucillePose03-1.png"
        yalign 0.5

image Lucille Shocked:
        "images/Lucille/LucillePose03-2.png"
        yalign 0.5

image Lucille HappyBlush:
        "images/Lucille/LucillePose01-5.png"
        yalign 0.5

image Lucille Angry:
        "images/Lucille/LucillePose01-6.png"
        yalign 0.5

image Lucille MadBlush:
        "images/Lucille/LucillePose02-4.png"
        yalign 0.5

image Lucille Sad:
        "images/Lucille/LucillePose02-5.png"
        yalign 0.5

#DemonMaid
image Demon Maid:
        "images/DemonMaid/DemonMaid-1.png"
        yalign 0.5

image Demon Maid 2:
        "images/DemonMaid/DemonMaid-1-2.png"
        yalign 0.5

image Demon Maid Sword:
        "images/DemonMaid/DemonMaid-2.png"
        yalign 0.5


#CG
image CG_Goddess = "images/CG/Goddess.png"


#Music
define audio.music_refresh = "sounds/Innocent-Years_Looping.mp3"
define audio.music_heaven = "sounds/Random-Processes_Looping.mp3"
