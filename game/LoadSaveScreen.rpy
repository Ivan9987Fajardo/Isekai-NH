## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load
init:
    $ style.slot_time_text.size = 22
    $ style.slot_time_text.color = "#363636"
    $ style.slot_time_text.antialias = True
    # $ style.slot_time_text.hover_color = "#363636"
    # $ style.slot_button_text.color = "#959595"


define gui.button_text_font = gui.interface_font 
define gui.button_text_size = gui.interface_text_size

screen save():

    add "images/MenuItems/SaveBG.png"
    add "Snow"
    use file_slots(_("Save"))


screen load(inMain=False):

    tag menu
    add "images/MenuItems/LoadBG.png"
    add "Snow"
    use file_slots(_("Load"),inMain)


screen file_slots(title,inMain=False):

    default page_name_value = FilePageNameInputValue()

   

    fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.
            
            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.55

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("%B %d, %H:%M"), empty=_("Empty Slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing
                imagemap:
                    ground "images/MenuItems/LoadPage_Idle.png"
                    idle "images/MenuItems/LoadPage_Idle.png"
                    hover "images/MenuItems/LoadPage_Hover.png"
                    selected_idle "images/MenuItems/LoadPage_Ground.png"
                    selected_hover "images/MenuItems/LoadPage_Ground.png"
        
                    alpha True
                    hotspot (60, 629, 70, 71) action FilePage(1)
                    hotspot (131, 629, 70, 67) action FilePage(2)
                    hotspot (202, 629, 70, 67) action FilePage(3)
                    hotspot (273, 630, 71, 66) action FilePage(4)
                    hotspot (346, 630, 68, 68) action FilePage(5)
                    hotspot (416, 631, 69, 65) action FilePage(6)
                    hotspot (487, 630, 69, 68) action FilePage(7)
                    hotspot (557, 630, 71, 68) action FilePage(8)
                    hotspot (630, 631, 68, 66) action FilePage(9)
                    hotspot (699, 630, 71, 68) action FilePage(10)

            imagebutton:
                xpos 1000 ypos 620 ##ypos 648
                idle "images/buttons/Back_Idle.png"
                hover "images/buttons/Back_Hover.png"
                activate_sound "sounds/Quirky33.mp3"
                action If(inMain,Show('main_menu',transition=dissolve),Return())
                
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

# style page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")