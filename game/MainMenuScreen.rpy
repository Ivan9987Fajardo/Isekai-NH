## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu
#Main Menu
image Frame:
    "images/MenuItems/Mainmenu_Frame.png"
    xpos 580
    ypos -60
    zoom 0.4

screen main_menu():
    #$ renpy.transition(dissolve)
    # This ensures that any other menu screen is replaced.
    tag menu
    add gui.main_menu_background
    style_prefix "main_menu"

    add "Snow"
    add "Frame"

    # add "images/MenuItems/Header.png" xpos 60 ypos 40

    # This empty frame darkens the main menu.

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    # use navigation

    imagebutton:
        xpos 860 ypos 209
        idle "images/buttons/Start_Idle.png"
        hover "images/buttons/Start_Hover.png"
        #hover_sound "Sounds/hover1.ogg"
        # activate_sound "sounds/PowerUp9.mp3"
        action (Start('start'),Hide("main_menu"))

    imagebutton:
        xpos 860 ypos 303
        idle "images/buttons/Load_Idle.png"
        hover "images/buttons/Load_Hover.png"
        #hover_sound "Sounds/hover1.ogg"
        activate_sound "sounds/Quirky33.mp3"
        action (Show('load',inMain=True,transition=dissolve))

    imagebutton:
        xpos 860 ypos 397
        idle "images/buttons/Options_Idle.png"
        hover "images/buttons/Options_Hover.png"
        #hover_sound "Sounds/hover1.ogg"
        activate_sound "sounds/Quirky33.mp3"
        action (Show('preferences',inMain=True,transition=dissolve))



    imagebutton:
        xpos 860 ypos 491
        idle "images/buttons/Quit_Idle.png"
        hover "images/buttons/Quit_Hover.png"
        #hover_sound "Sounds/hover1.ogg"
        activate_sound "sounds/Quirky33.mp3"
        action (Quit())







style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text


style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size
