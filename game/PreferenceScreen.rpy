## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences(inMain=False):
    
    tag menu
    add "images/MenuItems/OptionsBG.png"
    add "Snow"
    vbox:
        style_prefix "slider"
        xpos 587
        ypos 275
        bar value Preference("text speed")
        
    vbox:
        style_prefix "slider"
        xpos 587
        ypos 360
        bar value Preference("auto-forward time")
        
    vbox:
        style_prefix "slider"
        xpos 587
        ypos 440
        bar value Preference("music volume")
    
    vbox:
        style_prefix "slider"
        xpos 587
        ypos 520
        bar value Preference("sound volume")
    
    imagebutton:
            xpos 1036 ypos 598
            idle "images/buttons/Exit_Idle.png"
            hover "images/buttons/Exit_Hover.png"
            activate_sound "sounds/Quirky33.mp3"
            action If(inMain,Show('main_menu',transition=dissolve),Return())
    imagebutton:
            xpos 600 ypos 190
            idle "images/buttons/Seen_Idle.png"
            hover "images/buttons/Seen_Hover.png"
            selected_idle "images/buttons/Seen_Selected.png"
            selected_hover "images/buttons/Seen_Selected.png"
            action Preference("skip", "seen")
            
    imagebutton:
            xpos 860 ypos 190
            idle "images/buttons/All_Idle.png"
            hover "images/buttons/All_Hover.png"
            selected_idle "images/buttons/All_Selected.png"
            selected_hover "images/buttons/All_Selected.png"
            action Preference("skip", "all")
            
    
    




    
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 494

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450
