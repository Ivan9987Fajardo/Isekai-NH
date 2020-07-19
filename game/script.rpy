## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.
init:
    $ sshake = Shake((0, 0, 0, 0), 5.0, dist=15)
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))
    image red = Solid("#ff0000")
    image white = Solid("#ffffff")

    $ world = 0
    $ playerName = "Hayato"


screen world:
    imagebutton:
        xalign 0.9 yalign 0.5
        idle im.Scale("images/BG/Forest_Selection.png" , 280, 600)
        hover im.Scale("images/BG/Forest_Selection.png" , 310, 640)
        action (SetVariable("world", "Adventure"),Return())
    imagebutton:
        xalign 0.1 yalign 0.5
        idle im.Scale("images/BG/Castle_Selection.png" , 280, 600)
        hover im.Scale("images/BG/Castle_Selection.png" , 350, 640)
        action (SetVariable("world", "Demon"),Return())
## The game starts here.
label splashscreen:
    scene black
    show splash with dissolve
    with Pause (3) 
    hide splash with dissolve
    return
    
label start:
    show image "images/MenuItems/MainMenuV2.png":
        ease 2 zoom 1.2
    stop music fadeout 2.0
    
    
    
    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    ## These display lines of dialogue.

# label intro:
#     show image "images/MenuItems/MainBG.jpg": 
#         ease 3 zoom 1.2
#     $ renpy.pause(3,hard=True)
#     # scene black with Dissolve(5)
#     # play music "Sounds/08 - South-Facing Window.mp3" loop
#     n "Makoto-kun… Makoto-kun…"
#     m "What?"
#     $ renpy.vibrate(1)
#     n "Let’s make a promise…"

# label select_world:
#     nr "A promise huh?..."
#     nr "I wonder if I can still fulfill a promise after all that happened."
#     nr "I don’t want to see her cry again."
#     nr "I want to protect that smile that she was wearing moments ago."
#     nr "Will I ever see that smile of hers again?"
#     m "A promise?"
#     call screen world with dissolve
#     nr "I’ll just hope that this promise of ours will make us both happy…"
#     n "Let’s make a promise to each other…"
#     n "A promise that will be fulfilled when I woke up from this illusionary dream…"

label intro:
    $ renpy.pause(2,hard=True)
    scene black with Dissolve(2)
    $ renpy.pause(2,hard=True)
    play music music_refresh
    scene BG_Modern_Room with dissolve
    mc "Morning already??"
    mc "Do I have classes today? or is it a weekend? "
    nr "Ohh, I have morning classes…"
    mc "Darn… I did nothing on both weekends"
    mc "I hope we don’t have a pop quiz, I didn’t study the whole weekend"
    nr "I hope I can finish college by next year. I can’t endure listening to boring lectures everyday."
    nr "I just want to have my college diploma and have a stable job. Nothing else.."
    mc "Oh well, Time to fix myself and go to school.."
    scene BG_City with dissolve
    # *otw to school*
    nr "It’s already summer, everyone is wearing thin clothes because of the heat"
    mc "Feels like it will be sunny all day"
    nr "As I walk through the crowd of people, thirst starts to kick in"
    mc "Damn, I forgot to bring my water bottle"
    mc "I can’t stay outside in this kind of heat"
    mc "Better buy some refreshments in the next convenience store…"
    # *screen flicker*
    stop music fadeout 0.5
    scene BG_City_Invert
    $ renpy.pause(2,hard=True)
    scene BG_City_BW with Dissolve(1)
    mc "….."
    mc "Wait what?"
    mc "What’s happening?"
    mc "Where’s everybody??"
    # *Truck horn*
    play music "sounds/Horn.mp3"
    nr "What?"
    nr "Is this how am I going to die?"
    stop music
    play sound "sounds/Crash.mp3"
    scene BG_City_BW with sshake
    $ renpy.pause(5,hard=True)
    scene red with Dissolve(1)
    $ renpy.pause(1,hard=True)
    scene black with Dissolve(2)
    $ renpy.pause(2,hard=True)
    scene white with Dissolve(2)
    $ renpy.pause(2,hard=True)
    pause(1)
label test:
    # *crashhhhhh*
    # *red background opacity*
    # Fade to black
    # Flicker screen 
    # From blurred to hd
    # Heaven screen
    scene BG_Sky with dissolve
    show Snow
    play music music_heaven
    # hide Snow with dissolve
    mc "What?"
    
    # Screen left right (Look around)
    scene BG_Sky:
        # show Snow
        ease 1.0 zoom 1.5
        pause(0.5)
        ease 1.0 zoom 1.0
        pause(0.5)
        ease 1.0 xalign 0.8 yalign 0.2 zoom 1.5 
        pause(0.5)
        ease 1.0 zoom 1.0
    show Snow
    mc "Where am I?"
    nr "Those are the kind of questions that are going through my head.."
    show Goddess_Wings
    show Goddess 
    with dissolve
    
    gd "Heyyyyy!"
    mc "Who are you?!"
    mc "What the hell happened to me??"
    gd "You had a horrible death.. So Saaaad"
    mc "Death? How???"
    mc "I’m just on my way to school then everybody is gone.."
    mc "The next thing I know is I’m already here…"
    gd "Hmm…. Nopeee."
    gd "The details of your death are the least important now.."
    gd "What you need to do right now is think on where you’re going to go in your next life."
    nr "She must be joking."
    nr " but wait… Next life??"
    nr "am I not going to heaven??"
    gd "I’m going to give you another chance to relive your life.."
    gd "But not in your previous world, You already died on that."
    gd "I’ll give you 2 different worlds to choose from."
    show Selection_Forest:
        xalign 0.9 yalign 0.5
    show Selection_Castle:
        xalign 0.1 yalign 0.5
    with dissolve
    mc "What kind of world?"
    hide Selection_Castle
    show Selection_Castle2:
        xalign 0.1 yalign 0.5
    gd "The first one is the Demon World…"
    gd "This is where the demon queen Lucille resides."
    gd "She is one of a cheeky girl so be careful."
    hide Selection_Castle2
    show Selection_Castle:
        xalign 0.1 yalign 0.5
    show Selection_Forest2:
        xalign 0.9 yalign 0.5
    hide Selection_Forest
    
    gd "The other one is the Adventure World"
    gd "This is where the horrible goblins are lurking around, beware of those goblins because they might attack you anytime."
    gd "There is an elf who will support you in your battles, her name is Elisabeth"
    # gd "And the last one is the Human World.."
    # gd "This is just like your previous world... but it is not. Nobody knows you and you don’t know anyone."
    # gd "You will start your life as a regular college student."
    hide Selection_Forest2
    show Selection_Forest:
        xalign 0.9 yalign 0.5
    gd "Sooo, That’s all. Any questions?"
    mc "Hmm.. If I die again in those worlds, will I have a new set of worlds to choose from?"
    gd "Nope. You will go straight to heaven… I think?"
    gd "So, What world do you want to go to?"
    call screen world with dissolve
    # -WORLD CHOICE-
    gd "You have chosen {i}{b}[world] World{/b}{/i}, What name do you want to use in this world?"
    python:
        playerName = renpy.input("Enter your name: ")
        playerName = playerName.strip()

        if not playerName:
            playerName = "Hayato"
    gd "Okay! Good luck [playerName]!"




label world1:
    return
    n "welcome to world1"







    show BG_Bedroom 
    with Dissolve(3.0)
    stop music fadeout 1
    m "Ughh… It’s morning already?"
    m "I don’t think I have slept at all…"
    nr "My body feels heavy…"
    play music "Sounds/21 - Route I.mp3" loop
    nr "What is this pain that I’m feeling on my chest?"
    nr "Every time I wake up in the morning, this pain never leaves my chest."
    nr "I wonder when did it started?"
    nr "Is it when I was still a child?"
    nr "As I remember, we were once called a “Happy Family”."
    nr "My family only consists of 3 members… Mom, Dad, and me."
    nr "Dad is such a funny person, He tells hilarious jokes, that was never been funny at all."
    nr "Even though his jokes are corny, we always laugh at it until we chase our breaths."
    nr "And Mom, she was always a klutz."
    nr "She never created a single edible dish."
    nr "As a result, we always eat our meals at a near family restaurant."
    nr "I can say that our family is not perfect…"
    nr "We also have faults and problems that every other family have."
    nr "But these problems what makes us stronger and happier."
    nr "We created many memories and bonded to each other…"
    nr "-but all of these memories are now history…"
    nr "They were all in the past now..."
    nr "We will never create any memories anymore."
    m "Haaa…"
    m "It’s time to go to school."
    m "Better fix up myself."
    show BG_Street
    with Dissolve(2.5)
    hide BG_Sky
    nr "Same day… Same Scenery…"
    nr "As I walk up straight ahead, I saw students wearing the same uniform as I am."
    nr "Chatting with their friends, making different kinds of expressions."
    m "Must be nice.."
    nr "I wasn’t particularly enjoying my so called “youth” to the fullest like most people my age."
    nr "I wasn’t an outcast or anything, I can communicate with other people just fine but I don’t really have anyone who I get along well with or to call a friend."
    nr "Was there something wrong with me?"
    nr "I stopped walking when I saw a group of students playing some kind of video game on their phones."
    nr "*pew* *pew* *pew*"
    m "…"
    nr "Who needs friends anyway? They’re just annoying people who’ll keep bothering me every day."
    stop music fadeout 1
    play sound "Sounds/Horn.mp3" 
    queue sound "Sounds/Horn.mp3"
    nr "*BEEEEEEEEEP!!!*" 
    m "Uwaahh!"
    nr "Startled by the loud noise, I stopped and covered my hurting ears."
    nr "When I looked to my side there was a speedy truck heading my way."
    play sound "Sounds/Horn.mp3"
    nr "*BEEEEEP!!!*"
    nr "The moment I saw it, I knew I couldn’t move away in time."
    nr "It was like the grim reaper’s scythe was coming to strike my neck and all I could do was watch in awe."
    nr "So this is how it ends.."
    n "Look Out!"
    nr "*push* *shove*"
    m "Eh!?"
    play sound "Sounds/Crash.mp3"
    nr "*crash*" with sshake
    #########################
    #########################
    nr "W-Why!?"
    nr "She pushed me out of the way?"
    nr "Why did she do that?"
    scene black 
    with fade
    hide BG_Street
    ###########
    show BG_Hospital
    with fade
    play music "Sounds/04 - Lamune 79's (Narcissu 2nd version).mp3"
    nr "We were brought to the hospital in an ambulance. "
    nr "They made me go through a few tests to ensure my safety but that was the least of my worries."
    nr "I was waiting outside of the operation room where they were treating the girl who saved me."
    #############
    m "Damn it.."
    play sound "Sounds/DoorOpen.mp3"
    nr "*Door sound*"
    nr "*Doctors chatter*"
    m "Uhh-Uhhmmm.."
    m "I-Is that girl also all right?"
    nr "I immediately and nervously asked the nurse who just got out of the room."
    nr "She probably wasn’t all right seeing as how badly injured she was after being hit by that truck."
    nr "The doctors have been treating her for hours and I wanted to know if she was okay or more specifically, I wanted to know if she survived."
    'Nurse' "We managed to save her life at least."
    nr "I breathe a sigh of relief upon hearing that she was still alive."
    'Nurse' "But she isn’t exactly in a good state right now."
    'Nurse' "The damage to her head was severe and she has been…--"
    scene black
    with dissolve
    hide BG_Hospital
    show BG_Hospital 
    with fade
    pause(1.0)
    show BG_Hospital
    with fade
    nr "It’s been a few days since the accident happened"
    nr "The nurse told me that she was put in a comatose state."
    nr "That means she will not wake up anytime soon."
    nr "No one knows when or if she will ever wake up."
    nr "I returned to the hospital asking about her condition, but the doctors said that nothing had changed since then."
    m "…"
    ####################
    m "Haah.."
    nr "The truck driver was fined a huge amount for the incident, but honestly, it was not his fault that I was spacing out on the road crossing."
    nr "When I went back to school the next day, my classmates were all worried about me after word got out that I was involved in an accident."
    nr "But I don’t think they even actually cared, it was more like a passing trend to talk about something."
    nr "No one even greeted me the day after that, but I didn’t really care about that."
    nr "I was worrying about something else."
    show CG_Setsuna_Sleeping
    stop music fadeout 1
    play music "Sounds/05 - For Whose Sake.mp3" fadeout 1
    m "When are you going to wake up?"
    nr "She was still alive but…."
    m "Ugh.."
    nr "I was the one who put her in this predicament."
    nr "This is all my fault, If I only wasn’t thinking about stupid stuff back then.."
    m "…"
    #################
    nr "The quietness of the room calmed me down."
    nr "But other than that, the quietness made me wonder about something regarding the girl."
    nr "Why am I the only one visiting her? Shouldn’t she at least have a family member watching over her? It’s been a few days since that accident…"
    nr "She was also alone during the time that she was being treated, I haven’t met anyone to apologize to for everything that happened."
    nr "There was no trace of any visitors having come to her room, anyone would expect flowers or something in the room of a girl who is sick."
    nr "Maybe she’s just like me.."
    ######################
    hide CG_Setsuna_Sleeping with dissolve
    play sound "Sounds/DoorOpen.mp3"
    'Nurse' "Oh it’s you again..."
    m "You’re that nurse from before..."
    'Nurse' "Are you worried about her? "
    m "Yeah.."
    m "(Everything was my fault anyway; it’s only natural for me to worry)"
    'Nurse' "Don’t look so sad, I’m sure she saved you because she wanted to."
    m "Well she’s a weird girl for wanting to save me."
    m "By the way miss nurse, if it’s not too rude… "
    m "Can I ask for her name?"
    'Nurse' "Actually even we don’t know who she is yet."
    'Nurse' "She had no phone, ID, or anything we could identify her with."
    m "What!?"
    nr "That would explain why she’s been alone all this time since the accident"
    nr "I feel even more pity for the girl and guilt to myself after realizing that her loved ones probably had no idea of the state she’s in."
    'Nurse' "Don’t worry too much about it; we’ll do our best to find out who she is."
    m "Okay.."
    nr "The nurse finishes her business and exits the room after saying goodbye."
    m "It’s getting pretty late, I should get going too.."
    nr "I decided to go home for the day, but before heading out, I took one last look at the girl who was sleeping rather peacefully."
    ###########################
    m "I hope she’s having a nice dream."
    stop music
    scene white with dissolve
    show Snow
    pause(5.0)
    show BG_Hospital with dissolve
    hide Snow with dissolve
    show Setsuna_Smile
    
    m "What the?"
    play music "Sounds/09 - The Emerald Sea.mp3" fadeout 1
    m "You’re awake!"
    nr "A girl suddenly appeared before me and was awake, but after looking closely, there was also another girl who was still sleeping in the bed."
    m "Wha?? No you’re not.. But you look just like her.."
    s "Eh?"
    m "W-Who are you?"
    s "Mmmm…"
    s "I don’t know?"
    m "Huh?!" 
    scene black with Dissolve(5.0)
    hide BG_Hospital
    hide Setsuna_Smile
    $ renpy.movie_cutscene('Opening1.ogg')


    


    


    

    
    

    

    

    
    



    




    

    
       
    
    
    ## This ends the game.

    return
