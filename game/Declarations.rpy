######################################
#####Declarations##############
#######################################



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
define lucille = Character('Lucille',ctc="ctc_blink",
        ctc_position="fixed")
define n = Character('???',ctc="ctc_blink",
        ctc_position="fixed")
define nr = Character(None,ctc="ctc_blink",
        ctc_position="fixed")
define gd = Character('Goddess',ctc="ctc_blink",
        ctc_position="fixed")


#Background
image BG_City = "images/BG/City.png"
image BG_City_BW= im.Sepia("images/BG/City.png")
image BG_City_Invert= im.MatrixColor("images/BG/City.png", im.matrix.invert())
image BG_Modern_Room = "images/BG/ModernRoom.png"
image BG_Sky = "images/BG/Sky.png"
image BG_Forest Day= "images/BG/Forest_Day.png"
image BG_ForestPath Day= "images/BG/ForestPath_Day.png"


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
        yalign 3.0

image Lisa Smile2:
        "images/Elisabeth/ElisabethPose02-1.png"
        yalign 1.0

image Lisa Sad:
        "images/Elisabeth/ElisabethPose01-3.png"
        yalign 0.7

image Lisa Smirk:
        "images/Elisabeth/ElisabethPose02-2.png"
        yalign 1.0

#Guild master
image GuildMaster:
        "images/GuildMaster/Guild Master.png"
        yalign -2.0


#CG


#Music
define audio.music_refresh = "sounds/Innocent-Years_Looping.mp3"
define audio.music_heaven = "sounds/Random-Processes_Looping.mp3" 



