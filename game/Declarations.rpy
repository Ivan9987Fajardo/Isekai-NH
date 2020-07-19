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
image BG_City = im.Scale("images/BG/City.png",1280,720)
image BG_City_BW= im.Sepia(im.Scale("images/BG/City.png",1280,720))
image BG_City_Invert= im.MatrixColor(im.Scale("images/BG/City.png",1280,720), im.matrix.invert())
image BG_Modern_Room = im.Scale("images/BG/ModernRoom.png",1280,720)
image BG_Sky = im.Scale("images/BG/Sky.png",1280,720)
image Selection_Forest = im.Scale("images/BG/Forest_Selection.png" , 280, 600)
image Selection_Forest2 = im.Scale("images/BG/Forest_Selection.png" , 350, 640)
image Selection_Castle = im.Scale("images/BG/Castle_Selection.png" , 280, 600)
image Selection_Castle2 = im.Scale("images/BG/Castle_Selection.png" , 350, 640)

image BG_Street = "BG/Street.jpg"
image BG_School = "BG/School.jpg"
image BG_Hall = "BG/Hall.jpg"
image BG_Hospital = "BG/Hospital.jpg"
image BG_Bedroom = "BG/Bedroom.png"
#Sprite

image Goddess:
        im.Scale("images/Goddess/Goddess2.png",700,700)
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
        im.Scale("images/Goddess/Wings.png",700,700)
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



image Lizette_Smile = "Lizette/Lizette_Smile.png"
image Lizette_Smile2 = "Lizette/Lizette_Smile2.png"
image Lizette_Angry = "Lizette/Lizette_Angry.png"
image Lizette_Confused = "Lizette/Lizette_Confused.png"
image New = "Lizette/Heroine.png"

image Setsuna_Angry = "Setsuna/FS1-angry1.png"
image Setsuna_Normal = "Setsuna/FS1-smile1.png"
image Setsuna_Smile = "Setsuna/FS1-smile3.png"
image Setsuna_Wink = "Setsuna/FS1-wink3.png"

#CG
image CG_Lizette= "CG/Lizette.jpg"
image CG_Sylvie= "CG/Sylvie.jpg"
image CG_Setsuna_Sleeping = "CG/Sleeping_Setsuna.jpg"

#Music
define audio.music_refresh = "sounds/Innocent-Years_Looping.mp3"
define audio.music_heaven = "sounds/Random-Processes_Looping.mp3" 



