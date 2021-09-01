## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
#image Shit:
    #"images/ingameshit.png"
    #xalign -0.03
    #ypos 0.6
    #rotate 0
    #linear 5.0 rotate 360
    #repeat
    
screen quick_menu():

    #key "mouseup_3" action Quit()
    # Ensure this appears on top of other screens.
    zorder 100
    #add "Shit"
    # Add an in-game quick menu.
    imagemap:
        ground "images/MenuItems/Quick_Menu_Ground.png"
        idle "images/MenuItems/Quick_menu.png" 
        hover "images/MenuItems/Quick_Menu_Hover.png"
        selected_idle "images/MenuItems/Quick_Menu_Hover.png"
        selected_hover "images/MenuItems/Quick_Menu_Hover.png"
        
        hotspot (423, 1, 80, 76) action ShowMenu('save')
        hotspot (509, 0, 79, 75) action ShowMenu('load')
        hotspot (603, 0, 74, 77) action ShowMenu('text_history')
        hotspot (9, 11, 71, 67) action ShowMenu('preferences')
        hotspot (685, 1, 89, 78) action Preference("auto-forward","toggle")
        hotspot (773, 0, 88, 75) action Skip() alternate Skip(fast=True, confirm=True)
        hotspot (1196, 13, 68, 72) action MainMenu()
        
   

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
