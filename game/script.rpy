## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.
init:
    $ sshake = Shake((0, 0, 0, 0), 5.0, dist=15)
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))
    image flashback = Solid((62, 39, 13, 150))
    image reddish = Solid((255, 25, 25, 150))
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
    scene CG_Goddess:
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
    nr "but wait… Next life??"
    nr "am I not going to heaven??"
    mc "Will you tell me who you are?? You're weirding me out"
    gd "I'm the goddess who will guide you to your next life"
    mc "What the hell is this {i}Next Life{/i} you're talking about??"
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

    if world == "Demon":

        jump demonWorld
    if world == "Adventure":
        show Selection_Forest:
            xalign 0.9 yalign 0.5
            ease 2 zoom 1.2
        jump adventureWorld

label adventureWorld:
    scene black with fade
    scene BG_Forest Day
    show Snow
    with Dissolve(1)
    hide Snow with Dissolve(3)

    mc "Where Am I?"
    nr "The scenery here is good.."
    nr "I feel the chills when the cold breeze hits my skin"
    mc "Is this the Adventure world she’s talking about??"
    mc "It’s beautiful in here"
    nr "So where do I go next?"
    # *Grawlll*
    show Goblin_Weak with moveinbottom
    "Goblin" "Gwrawwwllll!!"
    nr "A Goblin! "
    mc "Hey! Stay away from me! "
    show Goblin_Weak with vpunch
    pause(0.5)
    show Goblin_Weak with vpunch
    mc "AAAAGGGHHH"
    show Goblin_Weak with hpunch
    pause(0.5)
    show Goblin_Weak with hpunch
    pause(0.5)
    show Goblin_Weak with hpunch
    pause(0.5)
    # *Scratch* *Scratch*
    # *scratch* *scratch*
    # *hpunch*
    lisa "Light Arrows!"
    show Goblin_Weak at Shake((0.5, 1.1, 0.5, 1.0), 1.0, dist=5)
    pause(1.0)
    hide Goblin_Weak with moveoutbottom
    # *Goblin death*
    mc "Woaah, What was that??"
    nr "That shiny thing was awesome!"
    show Lisa Smile with Dissolve(0.5)
    lisa "Those are goblin monsters. There are different kinds of goblins lurking in this world."
    mc "No, I mean that light something that kills the goblin"
    nr "This is the first time I see that kind of weapon"
    lisa "Ohh, Those are light arrows. One of the basic types of magic. Never used one before?"
    nr "Ohh, so this world uses magic.."
    mc "Actually, I never used magic before.."
    mc "I just got reincarnated in this world then this goblin attacked me out of nowhere"
    show Lisa Smile2 with Dissolve(0.5)
    lisa "Really? So you’re a new gen?"
    mc "New Gen?"
    lisa "Yes, New Gen are the ones who’s sent by god to help fight the goblins."
    lisa "They relatively have more magic capacity than the old gen."
    lisa "Old gen are beings who originally lived in this world."
    mc "So you’re an old gen or a new gen? I’m [playerName] by the way."
    lisa "I originally lived in this world so you can categorize me as  an old gen."

    show Lisa Smile3 with Dissolve(0.5)
    lisa "I’m Elisabeth from the Elf clan, but you can call me Lisa."
    nr "So I’m a new gen and I have magic powers??"
    mc "Okay Lisa, Can you explain to me this magic thing?"
    lisa "Okay, First, There are 4 types of magic: Light, Dark, Nature, and Spirit."
    lisa "Light magic uses the attributes of light to create an object from nothing."
    lisa "Earlier, I used light magic to create arrows."
    lisa "Dark Magic uses the attributes of darkness to destroy objects into nothingness."
    lisa "Nature Magic controls the 4 elements of nature: Earth, Water, Air, and Fire."
    lisa "And the Spirit Magic increases the physical strength of one’s individual."
    lisa "So, any Questions?"
    nr "The only thing I need to remember is the 4 types of magic: Light, Dark, Nature and Spirit."
    nr "I wonder if I can use one of those type of magic"
    mc "Is there a way to know what kind of magic to use?"
    show Lisa Smile2 with Dissolve(0.5)
    lisa "There is a crystal at the guild hall where you can see what type of magic is suitable for you."
    lisa "The Guild Hall is just 5 minutes walk from here."
    lisa "There’s also a Mission board, where you can find suitable jobs for you."
    lisa "You wanna come with me?"
    mc "Yeah sure, I’ll be happy to"
    hide Lisa with Dissolve(0.5)
    scene BG_ForestPath Day with Dissolve(2.0)
    nr "As we walked through the grassy land, I started to remember the things that I did in my previous life."
    nr "I realized that living that kind of life is very boring"
    nr "That thought somehow gave me motivation to do better in this life."
    show Lisa Smile with Dissolve(0.5)
    lisa "Okay here we are. The Adventurers Guild."
    lisa "This is where all the Adventurers in this kingdom find work."
    lisa "Come, I’ll introduce you to the guild master"
    hide Lisa
    show GuildMaster
    with Dissolve(0.5)
    "Guild Master" "You must be [playerName], a New Gen right?"
    mc "Ahh, Yess, I just came into this world today. Exploring the things that I can do here."
    mc "Is there anything I can do here to earn some money?"
    nr "I need to do work so I can live by myself.."
    "Guild Master" "Ahh! Before anything else, Let me measure your magic capacity first.. Maybe you can help in defeating the Elder Goblin."
    "Guild Master" "Just hold this magic crystal in your hand and wait for the light to appear"
    nr "This magic crystal is kinda cold.."

    nr "Feels like it’s sucking up some energy in my body.."
    show GuildMaster with move:
        xpos 0.3
    show Lisa Smile:
        xpos 0.4

    with Dissolve(0.5)
    lisa " Grandmaster, I forgot to mention."
    lisa "We fought a Goblin monster on the way here. Just the weak ones though"
    "Guild Master" "You need to go back there, Maybe there’s a Goblin General lurking there."

    mc "Uhmm.. Guys?"
    mc "There’s a light coming from the crystal."
    "Guild Master" "Oh, It must be the--"
    window hide
    show white with Dissolve(2)
    pause(1)
    hide white with Dissolve(2)
    window show
    # *Super Light*
    # *crack*
    nr "The Crystal broke.."
    "Guild Master" "Oh my god… That crystal has been used for generations, and no one has ever reached beyond the crystal’s limit"
    mc "What does it mean??"
    show Lisa Smile2:
        xpos 0.4
    with Dissolve(0.2)
    lisa "It means you have an unlimited supply of magic capacity. An endless potential I guess.."
    "Guild Master" "I must report this to the council.."
    "Guild Master" "Maybe you can even free us all in the shackles of the Goblin Lord.."
    hide GuildMaster with moveoutleft
    show Lisa Smile2 with move:
        xalign 0.5
    with Dissolve(0.5)
    mc "Goblin Lord?"
    lisa "Yes. There are 3 types of Goblin."
    show Lisa Normal at center
    lisa "The first one is the {i}Goblin Monster{/i}, the one that we have defeated earlier. "
    show Lisa Normal
    lisa "The weakest among the three."
    lisa "The next one is the {i}Goblin General{/i}."
    lisa "They are the one who gives orders to the Goblin Monsters."
    lisa "And the last one is the {i}Goblin Lord{/i}."
    lisa "The Goblin Lord is the one who corrupts and controls this world."
    lisa "No one has ever dared to challenge the Goblin Lord because of his tremendous amount of mana in him."

    lisa "But you, You have the potential to defeat and free us from the evil goblins."
    show Lisa Smile2
    lisa "Will you help us defeat the Goblin Lord?"
    nr "I have the power to defeat the Goblin Lord?"
    nr "The power to free the people of this world?"
    mc "Wait, This is too much information for me.."
    mc "Can I think for a while before giving you my answer?"
    nr "I don’t think I can handle this big of a responsibility"
    show Lisa Sad
    lisa "Oh Sure… Take your time."
    lisa "I’ll show you where you’ll be staying for the night"
    scene black with fade
    # *Room*
    show Lisa Smile with Dissolve(0.5)
    lisa "This will be your room"
    lisa "Tomorrow I’ll show you how to accept quest in the mission board"
    mc "Okay Thanks! Good Night Lisa."
    lisa "Good Night [playerName]"
    hide Lisa with Dissolve(0.5)

    nr "..."
    scene BG_ForestPath Day
    show GuildMaster:
        xalign 0.1
    show Lisa Smile:
        xalign 0.9
    show flashback
    show white
    with Dissolve(1)
    pause(1)
    hide white with Dissolve(1)


    # *flashback*
    # *shining light*
    # *crack*
    lisa "It means you have an unlimited supply of magic capacity. An endless potential I guess.."
    lisa "You have the potential to defeat and free us from the evil goblins."
    mc "Unlimited potential huh.."
    lisa "Will you help us defeat the Goblin Lord?"
    scene black with Dissolve(1)
    # End Flashback
    nr "Maybe this is why I am sent here.."
    nr "To defeat and free the people from the Goblin Lord…"
    scene black with Dissolve(3)
    # Scene to Black
    # *alarm clock*
    scene BG_Rustic_Room Day with Dissolve(1)
    nr "Ohh, That was good sleep"
    nr "Better fix myself"
    # *knock knock*
    show Lisa Smile2
    lisa "[playerName]?"
    mc "Oh Hey Lisa."
    lisa "Are you ready to take some quests?"
    # *Flashback*
    scene BG_ForestPath Day
    show Lisa Smile2 with Dissolve(0.5)
    show flashback
    with Dissolve(1)
    lisa "Will you help us defeat the Goblin Lord?"
    scene black with Dissolve(1)
    scene BG_Rustic_Room Day with Dissolve(1)
    show Lisa Smile2 with Dissolve(0.5)
    # End Flashback
    mc "Before that…"
    mc "About defeating the Goblin King.. I think I have an answer.."
    show Lisa Sad with Dissolve(0.5)
    lisa "Wait, First I need to apologize to you…"
    lisa "Sorry for asking you to save the world hastily.."
    lisa "I know that you’re still new to this world and need more time and experience…"
    show Lisa Smile4 with Dissolve(0.5)
    lisa "But don’t worry, I’m here to train you to maximize the use of your potential."
    lisa "I’ll help you polish your skills and techniques so you will be ready for any battle…"
    lisa "We will have a lot of adventures together.. "
    nr "Do I really have the power to free the people?"
    show Lisa Smile2 with Dissolve(0.5)
    lisa "So [playerName], Will you help us defeat the Goblin Lord?"
    lisa "Will you be our hero in this world?"
    menu:
        "What will I do?"
        "I’ll be the one who will protect you and everyone":
            $ adventureWorld_Choice1 = True
        "I don’t think I am capable of carrying that responsibility":
            $ adventureWorld_Choice1 = False

    if adventureWorld_Choice1 == True:
        mc "I’ll be the one who will protect you and everyone"
        mc "Even though it is kinda scary, I know that you and everyone else will always be in my back right?"
        nr "Maybe this is my destiny after all. That goddess gave me this power to help everyone else."
        mc "Thank you Lisa. For making me realize that I can do more in my life."
        show Lisa Sad with Dissolve(0.5)
        lisa "No, I must be the one who’s giving you thanks. For helping us free this world."
        lisa "Besides, Don’t thank me yet. Our training has not yet started"
        show Lisa Smirk with Dissolve(0.5)
        lisa "I hope you don’t regret your decision. So prepare yourself!"
        mc "I’ll never regret this.. "
        nr "I hope so…"
    elif adventureWorld_Choice1 == False:
        mc "I don’t think I am capable of carrying that responsibility"
        mc "I still can’t imagine myself killing the Goblin Lord.."
        mc "I still need to learn a lot to have the courage of carrying that kind of task"
        nr "I can’t do it… I can’t fight someone like that.."
        show Lisa Sad with Dissolve(0.5)
        lisa "Really? Too bad.. But I really think that you can defeat him"
        lisa "But I don’t want to force you in doing something half heartedly"
        mc "I need to train and be familiar in this world first."
        show Lisa Smile4 with Dissolve(0.5)
        lisa "Don’t worry, I’ll still train so you will be prepared to do quests"
        show Lisa Angry
        lisa "So prepare yourself! "
        mc "Really? Thank you Lisa."
        nr "Lisa is really a great girl."

    ##Training
    scene BG_Training with Dissolve(1)
    show Lisa Smile3 with Dissolve(0.5)
    lisa "So this is where we’re going to train every day until you can defeat a single goblin"
    mc "This place is spacious"
    nr "The scenery and atmosphere here is also good"
    lisa "We need to train in a large place so no one will get hurt if you can’t control your powers."
    mc "I’ll try my best not to destroy things. Hehehe"

    lisa "Okay! Since you have unlimited magic potential, I guess you can use all 4 types of magic right?"
    mc "I think so? I don’t have an idea."
    show Lisa Smile with Dissolve(0.5)
    lisa "Let’s try it out! First, try to create a light arrow."
    lisa "Do a pose like you’re shooting an arrow"
    lisa "Hold your imaginary bow in your right hand, then the arrow on the left"
    mc "Am I doing this right?"
    show Lisa Normal
    lisa "Hold your bow higher.."
    lisa "Then focus all your energy in your left hand.."
    lisa "Imagine yourself holding an arrow.."


    # *Close eyes*
    scene black with Dissolve(0.2)
    nr "Arrow… Arrow.."
    nr "Imagine yourself holding an arrow.."
    nr "My hands feel warm.."
    # *Opens eyes*
    scene BG_Training with Dissolve(0.5)
    mc "Woaahhh!"
    show Lisa Smile with Dissolve(0.5)
    lisa "You did it! Now, Aim it on that rock.."
    lisa "Then release!"
    # *Arrow Sound*
    mc "Light Arrow!"
    scene white with Dissolve(0.2)
    pause(1.0)
    scene BG_Training with Dissolve(0.2)
    show Lisa Smile
    nr "I missed.."
    show Lisa Smile4 with Dissolve(0.5)
    lisa "It’s fine! We have a lot of time to practice!"
    lisa "Next one, We need to test if you can use dark magic"
    lisa "Since I’m an elf, Light magic is the only thing that I can use"
    show Lisa Smile3 with Dissolve(0.5)
    lisa "But I’ll do my best to support you in practicing the different types"
    mc "Thank you. So how can I use dark magic?"
    show Lisa Normal with Dissolve(0.5)
    lisa "Hmm. The asic type of dark magic is the void."
    lisa "It’s like creating a small black hole in your palms that sucks everything"
    lisa "Open your hands, and imagine holding a mini black hole."
    # *close eyes*
    scene black with Dissolve(0.5)
    nr "A black hole…. In my palm…"
    nr "It feels cold.."
    scene BG_Training with Dissolve(0.5)
    show Lisa Normal
    # *Openm eyes*
    mc "I did it!"
    lisa "Now throw it on that rock. Be careful not to touch it. It can suck your fingers."
    scene black with Dissolve(0.2)
    scene BG_Training with Dissolve(0.2)
    show Lisa Normal
    nr "I missed it.. Again."
    show Lisa Smile4 with Dissolve(0.5)
    lisa "We have a whole day to practice so don’t worry!"
    lisa "For today, You will only focus practicing Light and Dark Magic."
    mc "How about Nature and Spirit Magic?"
    show Lisa Smile with Dissolve(0.5)
    lisa "We can practice those on some other day, but today, Light and Dark Magic first."
    lisa "Are you ready for your intense magic training??"
    mc "Yeah.. I think so.."
    lisa "Let’s Goooo!"
    scene black with Dissolve(1.0)
    pause(0.5)
    scene BG_Training with Dissolve(0.5)
    # *dark screen*

    mc "Haaahhh… Haaahhh.."
    mc "I can’t do more…"
    show Lisa Smile2 with Dissolve(0.5)
    lisa "Okay! That’s it for today."
    lisa "You’re a fast learner! You already mastered all the basics of light and dark magic."
    lisa "It took me weeks to master light magic.."
    lisa "Tomorrow, I’m going to train you in using Nature and spirit magic, so be sure to have a lot of rest."
    lisa "Good work today [playerName]. I’m so proud of you.."
    mc "It’s all because my trainer is so great and caring.."
    nr "She’s so sweet and caring"
    show Lisa Shy2 with Dissolve(0.5)
    lisa "Thank you. Let’s go back to the guild hall?"
    mc "Let’s go!"
    scene black with Dissolve(0.5)
    if adventureWorld_Choice1 == True:
        # *dining hall*
        scene BG_Dining_Room with Dissolve(0.5)
        show Lisa Smile2 with Dissolve(0.5)
        lisa "[playerName]! Are you alone?"
        mc "Yeah, Just having a quick dinner then I’m off to bed."
        lisa "Me too! Can I eat with you? "
        mc "Yeah sure! No problem!"
        nr "It will be an honor for me to eat with a beautiful girl."
        lisa "Good work today! I can’t believe you mastered all those spells in just a single day"
        mc "Thanks! It’s all because of you. You explained all the theories behind those spells really well."
        mc "Just like a mom teaching her child!"
        show Lisa Sad with Dissolve(0.5)
        lisa "…"
        mc "Lisa? Did I say something wrong?"
        lisa "No.. it’s just that…"
        mc "What’s the matter?"
        lisa "I just miss my parents.."
        lisa "They died 10 years ago.. "
        lisa "Because of me… "
        lisa "They protected me… From the Goblins!"
        scene BG_ForestPath Night
        show flashback
        with Dissolve(1.0)
        # *Lisa Flashback*
        "Goblin" "Wrayayayys"
        show Goblin_Weak
        show flashback
        with Dissolve(0.5)
        lisa "\"Nooooo!\""
        # *Vpunch to viewer* *Vpunch*
        # *Magic sound effect*
        # *vpunch to goblin*
        # *goblin die*
        with hpunch
        with vpunch
        lisa2 "\"Mama! Papa!\" "
        with hpunch
        with vpunch
        # *More Goblins appear*
        # *screen to dark*
        scene black with Dissolve(1.0)
        lisa "That was the last time they ever hugged me.. To protect me from the goblins"
        lisa2 "\"No!!!\""
        scene red with Dissolve(1.0)
        pause(1.0)
        scene black with Dissolve(0.5)
        scene BG_Dining_Room
        show Lisa Sad
        with Dissolve(0.5)
        # *goblin sounds*
        # *hit sounds*
        # *screen to red*
        # *back to reality*
        lisa "On that day, I swear to myself."
        lisa "That I’m going to be strong enough so I can avenge my parents from those goblins."
        lisa "And now that you’re here, I can feel that It will only take days before I fulfill that promise."
        mc "I promise that your parents will get the justice that they deserve"
        mc "I will not waste the trust that you have given me. I will make sure that the Goblin Lord will be gone."
        nr "I never knew Lisa had a tragic past."
        show Lisa Smile with Dissolve(1.0)
        lisa "Thank you [playerName]. You’re the light that I’m waiting for."
        lisa "Okay! It’s time to rest!, We have a long day tomorrow."
        lisa "Thank you for listening to me. Good Night [playerName]"
        lisa "Sweet Dreams <3"
        mc "Okay! Good Night Lisa!"
        nr "I really am a lucky guy…"
        # *Fade to black*
    if adventureWorld_Choice1 == False:
        # *room*
        scene BG_Rustic_Room Night with Dissolve(0.5)
        nr "Do I really deserve this kind of training?"
        nr "After I rejected her to help in defeating the goblin lord..."
        mc "I really am a terrible person.."
        # *flashback*
        scene BG_Training
        show Lisa Smile2
        show flashback
        with Dissolve(1.0)
        lisa "Good work today [playerName]. I’m so proud of you.."
        scene BG_Rustic_Room Night with Dissolve(0.5)
        # *reality*
        nr "Do I deserve this kind of treatment?"
        mc "Maybe if I try hard enough, I can help her with the Goblin Lord?"
        nr "I really don’t know…"
        mc "I need more time to think…"
        # *Fade to black*
    scene black with Dissolve(0.5)
    # *knock* knock*
    lisa "[playerName]? Are you awake?"
    mc "Mmmmm…"
    lisa "Wake up [playerName]... It’s time for training.."
    # *Opens eyes*
    scene BG_Rustic_Room Day with Dissolve(1.0)
    # Knock knock
    lisa "[playerName]? [playerName]?"
    show Lisa Angry with Dissolve(0.5)
    mc "Oh hey Lisa, What’s up?"
    lisa "Do you know what time is it?"
    mc "Oh, I’m sorry, I just replenished my energy from yesterday’s training through sleep"
    nr "Did I really sleep that long?"
    nr "Well, Sleeping for 10 hours is not bad though."
    show Lisa Smile2 with Dissolve(0.5)
    lisa "Anyways, Just eat your breakfast and meet me in the training ground okay?"

    if adventureWorld_Choice1 == True:
        mc "How about you? Wanna have breakfast with me?"
        lisa "I would love to, but I already ate earlier. I’ll take that offer on another day okay?"
        lisa "Your treat!"
    if adventureWorld_Choice1 == False:
        mc "Okay! I’ll be done in a bit."

    # *Fade to black*
    scene black with Dissolve(1.0)
    scene BG_Training with Dissolve(0.5)
    show Lisa Smile3 with Dissolve(0.5)
    lisa "Okay today we’re going to test if you can use Nature and Spirit magic."
    lisa "But your performance yesterday is really good, so I think that you’re the first person who can use all 4 types of magic"
    mc "Is it really possible? To use all types of it? Doesn’t it have any drawback to battle or in my body?"
    lisa "Well, Casting different types of magic consecutively can be really tiresome."
    lisa "There is a single person before that is now a legend who can use the 3 types."
    lisa "Light, Dark and Nature. "
    lisa "Shifting different types at a time can really drain your magic energy, so casting a single type is the ideal way of it."
    lisa "This is why I only let you practice Light and Dark magic yesterday.."
    mc "How about in battle? Is it effective to change magic type on every attack?"
    show Lisa Smile2 with Dissolve(0.5)
    lisa "Well, It is a yes and no."
    lisa "Yes, because firing different types of magic consecutively can really throw off your enemy’s defense."
    lisa "And a No because, there’s a small delay to throw your next attack if they’re from a different magic type."
    mc "What do you mean small delay? And how long is it?"
    lisa "About 2 seconds, For example, Try to cast Light Arrows and Light Ball."
    # *show light  ball and arrow*
    nr "I can cast them at the same time.. "
    show Lisa Smile3 with Dissolve(0.5)
    lisa "You can easily cast light arrows right after a light ball.."
    lisa "Then try to cast a Dark Void and a Light ball at the same time."
    # *Show light ball…
    # 4 seconds
    # *Show Dark Void
    mc "There’s a 4 second delay in casting Dark Void.."
    nr "It feels like there’s something that’s blocking the magic to pass through."
    show Lisa Smile1 with Dissolve(0.5)
    lisa "Well, It’s just your 2nd day of training. 2 seconds casting delay is the fastest that you can do."
    lisa "So now, Let’s start your training!"
    mc "Yeah, sure!"
    show Lisa Normal with Dissolve(0.5)
    lisa "Okay, You’re going to try Nature magic.."
    lisa "Nature Magic is just like controlling things in your surroundings. "
    lisa "See this glass of water?"
    nr "I don’t have an idea why she spilled the water on the floor…"
    lisa "Now, Try to put back the water I spilled into the glass."
    nr "Ohh, That’s why she did that"
    lisa "Focus on the flow of the water.."
    lisa "Guide the water into the glass.."
    nr "It starts moving on my will…"
    mc "Just a little more…"
    mc "I did it!"
    show Lisa Smile2 with Dissolve(0.5)
    lisa "Okay Good. Now you have an idea how to move nature elements around you.."
    lisa "You’re going to try moving rocks, fire and air next…"
    scene black with Dissolve(1.0)
    scene BG_Training with Dissolve(0.5)
    show Lisa Smile3 with Dissolve(0.5)
    # *black screen*
    lisa "Okay Good. You finished all 4 Nature elements."
    mc "I only have Spirit Magic right??"
    lisa "Yes.. This is also the magic that the Goblin Lord uses."
    lisa "There’s a rumor that the Goblin Lord can use nature magic but nobody has confirmed it."
    mc "So I must find a way to counter Spirit magic…"
    nr "But first I must learn how to use this magic…"
    lisa "Spirit Magic is strengthening your mind and body way beyond its limits."
    lisa "It gives you physical strength and confidence."
    lisa "There’s a trick in activating it.."
    lisa "You just need to believe in yourself.."
    lisa "Focus all your energy in your body, and believe that you can do anything."
    lisa "Be confident in yourself."
    scene black with Dissolve(0.5)
    # *Eyes closed*
    nr "I can do this… The power…"
    nr "I'm the strongest person in this world…"
    nr "I can do anything.."
    show Lisa Smile2
    show flashback
    with Dissolve(0.5)
    # *show Lisa Smile Flashback*
    nr "For her…"
    # *Open eyes Reddish screen*
label test:
    scene BG_Training
    show reddish
    with Dissolve(0.5)

    mc "I can see some reddish aura around me"
    show Lisa Smile3 with Dissolve(0.5)
    lisa "That reddish aura is the sign that Spirit magic is currently activated"
    lisa "Your mana drains up fast when Spirit Magic is activated, so use it wisely"
    nr "My body feels so light.."
    lisa "Try to lift that boulder over there.. "
    # *rock sounds*
    nr "This is 50x lighter than it looks.. Or maybe I’m just too strong right now"
    lisa "Great! It is confirmed that you can use all 4 types of magic."
    lisa "Today, I’ll let you practice any type of magic you want to enhance."
    mc "Really? Nice!"
    lisa "We have the whole day to practice so let’s go!"
    # *screen to black*
    mc "Phew! I think I'm getting used to the intensity of our training."
    lisa "Since you’re a fast learner, It looks like you’re ready…"
    mc "Ready for what?"
    lisa "Ready to kill a goblin."
    nr "A goblin?! "
    lisa "Just the goblin monster though"
    lisa "So, Are you ready?"
    mc "I think I Am, but where can we find a goblin monster?"
    nr "I’m sure they’re hiding right now.."
    lisa "Remember the place where we fought a goblin monster?"
    lisa "I think their nest is just near there.."
    nr "I hope we only find a single one"
    lisa "What are you waiting for? Let’s go!!!"
    # Screen to black
    nr "So Lisa and started our hunt for a goblin"
    nr "To be honest, I have mixed emotions about this."
    nr "I'm scared and excited at the same time.."
    nr "But I know, Lisa will always be in my back."
    # Flashback
    nr "For her…"
    # End Flashback
    nr "Why did I have thoughts of her that time?"
    nr "I don’t understand.."
    lisa "[playerName], Do you hear that?"
    lisa "Sounds like it’s coming from her--"
    "Goblin" "Wraaaaaaa!"
    nr "It happens so fast that the goblin is already at Lisa’s shoulder"
    mc "I can’t use Light Arrow at this moment, I might hit her"
    nr "I have an idea"
    mc "Lisa! Close your eyes!"
    mc "BLINDING LIGHT! "
    nr "The moment I cast that spell, I rapidly grabbed Lisa’s arm and punched the hell out of that creepy goblin."
    # *Punch sound
    mc "Take this! DARK NEBULA!"
    # *Goblin dying sounds*
    nr "The goblins body has been turned into nothingness"
    mc "Lisa! Are you okay?"
    lisa "I was just surprised when the goblin suddenly jumped on me.."
    lisa "Thank you [playerName]."
    mc "I’m just glad that nothing bad happened to you"
    lisa "I’m amazed [playerName], You defeated a goblin despite having some unexpected events"
    lisa "You have now completed the basic training for the 4 magic types! Yaaayyyy!"

    if adventureWorld_Choice1 == False:
        lisa "You can now start doing quests at the mission board and earn a lot of gold"
        lisa "or you can help us in defeating the goblin lord"
        lisa "With your talent and power, Defeating the goblin lord will definitely be possible."
        lisa "Maybe you’ve changed your mind after experiencing your power?"
        nr "What do I really want to do?"
        # *flashback*
        nr "Do I deserve this kind of treatment?"
        lisa "You just need to believe in yourself.."
        # *end flashback*
        nr "Can I really defeat the goblin lord?"

        menu:
            "What do I need to do?"
            "I just want to enjoy my life and do some quests":
                $ normal_end = False
                jump adventureWorld_Bad
            "Defeat the Goblin Lord and free the people":
                $ normal_end = True

    if adventureWorld_Choice1 == False and normal_end == True:
        lisa "Really? You’ll help us now defeat the Goblin Lord?"
        mc "Yeah, I realized that maybe that goddess gave me this power to help the people in this world."
        nr "I don’t need to be selfish. This is the right thing to do."
        lisa "Thank you very much [playerName]! I owe you a lot."

    lisa "Now let’s head back to the guild and have some rest.."
    lisa "We still have a lot of training to do tomorrow so have enough rest okay?"
    mc "Okay, You too Lisa! Thanks for today!"
    # *screen to rooml*
    if adventureWorld_Choice1 == False and normal_end == True:
        nr "That was the right thing to do right? To help and save this world from the goblins"
        nr "I need to do this not just for the people, also for myself."
        nr "Thank you Lisa, for making me realize my worth in this world."
        # *sleep*
    if adventureWorld_Choice1 == True:
        nr "What is this thing that I’m feeling?"
        nr "My chest tightens whenever Lisa is near me.. I don’t understand.."
        # *Lisa flash back*
        lisa "Mama! Papa! "
        # *End Flashback
        nr "I don’t want that to happen to her ever again.."
        # *sleep*

    # *Knock Knock*
    lisa "[playerName]! [playerName]! "
    lisa "Wake uppp! We need to train!"
    mc "Good Morning Lisa! You’re Energetic today."
    nr "She looks cute when she’s like this"
    lisa "I just realized that we still lack experience and power in ourselves."
    mc "So what do you plan to do?"
    lisa "Since we’re going to fight the Goblin Lord, I suggest that we increase our training hours"
    lisa "We’re going to train from morning to night everyday."
    mc "We’re going to spend the whole day only for training?"
    mc "How about quests? How are we going to live without money??"
    lisa "Well, I do have a lot of savings, so I’ll let you borrow a little."
    lisa "I think if we’re going to follow my training schedule, we might be able to defeat the Goblin Lord in just 3 months."
    mc "I don’t even think we’re going to survive a month doing that schedule."
    nr "The training is too intense.."
    lisa "Just trust me okay? We can do this."
    mc "Well, If you say so.."
    lisa "Okay! Then it’s a deal!"
    lisa "Fix up yourself and meet me up at the Training Hall."
    mc "Okay! See you."
    # *Training hall*
    lisa "Okay [playerName], For the next few days, What we’re going to train is our stamina, power, and our Killer move."
    mc "What is this Killer Move?"
    lisa "Killer Move is a type of magic that you’ve invented and perfected by yourself."
    lisa "A killer move must be powerful enough to 1 hit kill an enemy, so take time to think about it."
    mc "I might 1 hit kill myself by doing that."
    nr "Powerful magic huh.."
    mc "Can it be a combination of different magic types?"
    lisa "Yes. As long as it can kill goblins.."
    lisa "So are you ready to start our training?"
    mc "Always Ready"
    lisa "Trainingggg Start!"
    # *white screen*
    # ---- 2 Weeks later ---
    mc "HAAAAAAA!!!!"
    # *explosions*
    lisa "Wow! You really have mastered that kind of killer move in just a few days."
    lisa "I’m quite jealous of how fast your progress is.."
    lisa "But I’m also relieved because I know that you’ll always be in my back, protecting me."
    mc "Yeah, but you’ll also protect me right?"
    lisa "We’ll protect each other, because we’re partners."
    nr "partners huh…"
    lisa "Since we both mastered our killer moves, You know what we’re going to do next?"
    lisa "It’s time for us to celebrateee!"
    lisa "it’s your treat right?"
    mc "Ahhh. I guess so?"
    mc "Oh well, Let’s go!"
    # *screen to guild hall*
    lisa "What do you want to drink? Beer or Vodka?"
    mc "Water is fine"
    lisa "Ohh, Don’t be shy. We are both adults so it’s fine"
    lisa "Hey Mister! 2 bottles of beer please."
    nr "I’m not really in the mood to drink right now"
    nr "But Lisa looks so happy…"
    nr "I’ll just go with the flow"
    lisa "Okay [playerName]! You didn’t actually tell me how you died in your previous world."
    lisa "Maybe spilling a little bit of detail to me? If it’s fine for you"
    mc "I don’t really want to talk about my previous life.."
    lisa "Everytime I look into your face, It feels like you’re in deep thoughts.."
    nr "So Lisa is always watching over me"
    lisa "I thought that maybe I can help you just a little bit?"
    mc "Okay, Since you’re a close friend of mine, I’ll tell you something about my past"
    # *black screen to bar*
    nr "We stayed up all night drinking and talking. Just the two of us."
    nr "In the end, I did tell everything about myself to Lisa"
    nr "How I lost interest in the world, and just spending my time doing what life gives me"
    # drunk lisa
    lisa "You’reee Actuallyyyy not a bad guyy, and you’re face is not bad.."
    mc "What do you mean not bad? "
    lisa "I meaaaan, You’re handsome and always look out for othersss."
    lisa "Still remember what you did to me a few days ago. Kyaaaa. You naughty boyy"
    lisa "You hold on to me like I’m you most important person hihihi."
    mc "That was because of that stupid Goblin!"
    lisa "I’ll give you a reward because of that.. *Smooochhhh*"
    mc "Lisaaaa! You’re drunk. I’ll carry you to your room."
    lisa "Noooo! I’m still fin-- *Blurghhh*"
    mc "Ughhh. Okay, Let’s go to your room."
    # *screen to black
    # *Lisa’s room*
    mc "Hey lisa.. Lisa.. Wake up.."
    lisa "Ohh, *zzzzz*"
    mc "Lisa??"
    lisa "You know…. I love you-- *zzzz*"
    mc "What?? Lisa?"
    lisa "Zzzzzzz.."
    nr "She’s fast asleep."
    nr "I’ll just lay her down in the bed then go back in my room."
    mc "Okay. Done! "
    mc "Good Night Lisa.."
    lisa "Goo-- *Zzzzzz*"
    # *screen to mc room*
    nr "Lisa likes me?"
    nr "She looks so cute when half asleep.."
    nr "Did she mean it when she said she likes me?"
    nr "My mind is full of questions right now…"
    nr "Well, I do think of her a lot this past few days.."

    if adventureWorld_Choice1 == False and normal_end == True:
        mc "I’ll better clear this up tomorrow.."
        mc "I don’t deserve any kind of these feelings.."
        mc "Not Yet. Not until we defeated that Goblin Lord."
        # *Sleep*
    if adventureWorld_Choice1 == True:
        mc "Am I…?"
        mc "In love with LiSA?"
        nr "No, No, No… This can’t be.."
        nr "She only sees me as a friend.. Right?"
        # *flash back*
        lisa "We’ll protect each other, because we’re partners."
        # *end flashback*
        nr "I need to clear things up to Lisa…"
        mc "I can’t hide my feelings anymore."
        mc "Tomorrow, I’ll tell her about my feelings."
        nr "I hope this doesn’t break our friendship.."
        nr "I want to see her smile and laugh everyday…"
        nr "I want her to be the happiest girl in this world…"
        mc "I’ll do anything to make that a reality."
        mc "I really love Lisa…."
        # *sleep*
    # Black screen
    # *knock knock*
    lisa "[playerName]?"
    mc "Good Morning Lisa, Is it time for our training?"
    lisa "No, It’s about yesterday.."
    lisa "I just want to say thank you for taking care of me last night.."
    lisa "My alcohol resistance is just too weak.."
    mc "It’s fine, I don’t mind.. "
    mc "Besides, You’re cute when you say some random things."
    lisa "About the thing that I said yesterday.."
    nr "She remembered?!"
    lisa "I want to clear things up…"
    lisa "Come with me, I’ll show you something…"
    # *screen forest*
    lisa "Do you know this place?"
    mc "Yeah…"
    lisa "This is where we first met.."
    lisa "This is the place where our adventure started."
    nr "She saved me in this place… "
    mc "I still remember how you killed that goblin here.."
    lisa "I know we only knew each other for less than a month.. But it feels like we knew each other for years.."
    lisa "I remember how gentle and caring you are.."
    nr "Wait.. It feels like she’s…"
    lisa "How you always lookout for me.."
    lisa "You always listen to all my problems.."
    lisa "This past few days, I started to notice how my heart beats fast when I’m with you.."
    lisa "[playerName]..."
    lisa "I think that I have fallen in--"
    "Goblin" "Rawwrrrr!"
    "Goblin" "Raaawrsss!!"
    mc "Lisa! Lookout!"
    # *hpunch* *vpunch*
    mc "TORNADO SPIN!! "
    nr "I casted multiple small versions of tornado to blow the goblins away, but they are too many.."
    nr "Their quantity is around 20 - 30."
    mc "We can’t beat them like this.."
    mc "Lisa!"
    mc "We need to run! "
    nr "As I prepare to run, I saw Lisa had her ankle broken..."
    lisa "Go run! Ask the guild for some help.."
    mc "No! I will not leave you behind!"
    mc "Hold tight!"
    nr "As I carry her in my back and prepare to run, A Goblin Commander appears in our sight."
    lisa "A Goblin Commander!"
    "Goblin Commander" "Where do you think you’re going?"
    lisa "[playerName]! Put me down! You can still make it to the guild hall when you’re not carrying me!"
    mc "No!, I will defeat him here."
    "Goblin Commander" "Do you think you’re strong enough boy??"
    # *Hpunch*
    mc "GAH!"
    nr "I tried blocking his attack, but it’s no use. My balance is slightly off because of Lisa in my back."
    "Goblin Commander" "What’s wrong boy?? Can’t even block that type of attack??"
    lisa "You’ll pay for this you ugly bastard!"
    "Goblin Commander" "Oh wait! Is that an Elf I’m seeing??"
    "Goblin Commander" "Never seen an elf for a while.."
    "Goblin Commander" "Soldiers! Capture the Elf! ALIVE!"
    "Goblins" "Gyaaaa!!!"
    "Goblin Commander" "The lord will be in an endless joy because of this gift for him."
    "Goblin Commander" "The place for the next Goblin Lord will be mine Bwahahaha!"
    lisa "KYAAA! NO!! Stop!!!"
    mc "NO!!!! STOPPP!"
    nr "I tried to stop them from taking Lisa away from me.."
    nr "But I failed…"
    nr "They are too many.. "
    "Goblin Commander" "Okay Boys, Let’s move out! "
    "Goblin Commander" "We already got what we need.. To the palace!"
    # *goblin gone*
    nr "The goblins take their leave fast"
    mc "…."
    mc "Wh- What happened? "
    mc "Lisa?"
    mc "Wait… Don’t take her from me…"
    mc "Wait..."
    nr "As I am in a state of shock, I suddenly remember…"
    # *flashback*
    lisa "I know that you’ll always be in my back, protecting me."
    # *flashback end*
    mc "This is not the time to be sad! I can still make it!"
    mc "I need to follow them, I can also know the whereabouts of the Goblin Lord!"
    # *Forest*
    nr "because of my incredible magic capacity, I already catched up to them in no time."
    nr "Thank goodness Lisa is fine.. "
    nr "I still can’t show myself to them.. Not yet.."
    nr "Not until I’ve seen the Goblin Lord.."
    # *goblin Lord hideout*
    nr "In just a few hours stalking them, I already found out their hideout.."
    mc "I can’t hear what they’re saying.."
    mc "I gotta make sure Lisa is safe.."
    mc "I need to get closer.."
    # *screen flicker*
    "Goblin Commander" "My Lord, I brought you a rare gift.."
    "Goblin Commander" "I saw her in the forest on my way here.."
    "Goblin Lord" "This is amazing! An Elf!"
    lisa "Stay away from me you monsters!"
    "Goblin Commander" "Shut up!"
    # *hpunch*
    "Goblin Lord" " Don’t worry I’ll make sure to tame her up tonight.."
    "Goblin Lord" "We’ll be having a lot of fun HAHAHAHAHA!"
    "Goblin Commander" "Uhmm. My Lord.. Since I’m the one who got you this gift…"
    "Goblin Lord" "What is it that you want?"
    "Goblin Commander" "Maybe… The place for the next Goblin Lord is reserved for me??"
    "Goblin Lord" "You want to be a lord is that what you say?"
    "Goblin Commander" "YES!"
    "Goblin Lord" "HAHAHAHAHAHA!"
    # *HPUNCH*
    nr "He didn’t hesitate even a little bit!"
    nr "He smashed the hell out of that commander resulting in his instant death"
    "Goblin Lord" "No one can ever take this place from me! No One! HAHAHAHAHAHA!!"
    "Goblin Lord" "I’m the only one who is ever worthy of being called the Goblin Lord!"
    lisa "You will never be worthy of anything!"
    lisa "You are a trash in this world! "
    "Goblin Lord" "You have the guts to talk to me like that ehh?"
    "Goblin Lord" "Do you know what I do to people like you???"
    lisa "Stop doing this to innocent people! Stop stealing all the goods in this world!"
    lisa "We can all live this world in harmony!"
    "Goblin Lord" "Why do I need to live equally With all of you weakling if I can have all of this all by myself? HAHAHAHAHA"
    lisa "You being so full of yourself will soon be your downfall."
    "Goblin Lord" "Nobody can ever defeat me in this world!"
    lisa "I know someone who can defeat you! Someone who’s physically and mentally stronger than you.."
    lisa "Maybe he’s already here waiting for the right time to kill you.."
    nr "Thank you Lisa, for believing in me.."
    nr "I just need the perfect time to kill this monster.."
    "Goblin Lord" "No one will ever come to save you! HAHAHA"
    "Goblin Lord" "Now let’s come to my room… I’ll teach you a lot of things.."
    mc "Not yet…"
    lisa "Let Go of me!"
    # *Hpunch*
    nr "While Lisa is resisting so much, she sees an opening for a one big uppercut."
    lisa "[playerName]! NOW!"
    mc "BLINDING LIGHT! "
    nr "Blinding light is the perfect spell, to steal Lisa from the Goblin Lord and blind him."
    mc "Hold on to me Lisa!"
    nr "Now I just need something that can 1 hit kill him"
    lisa "Use your Killer move!"
    nr "Not yet. I need to meet the 3 conditions before casting that spell."
    mc "DARK NEBULA!"
    nr "That spell must have dealt a lot of damage to him.."
    "Goblin Lord" "HAHAHAHAH! Is that it??"
    "Goblin Lord" "Is this the guy you’re telling me??"
    mc "Lisa, Stay behind me."
    nr "as the blind takes off, this monster already covers himself with Spirit Magic"
    mc "What a tremendous aura…"
    "Goblin Lord" "You have the guts surprising me like that"
    "Goblin Lord" "I hope you’re prepared to take the consequences"
    "Goblin Lord" "I can’t wait to hang your head in the wall of my room"
    mc "Goblin Lord! I’ll give you a chance!"
    mc "A chance to change!"
    mc "Surrender now, and I’ll spare your head"
    "Goblin Lord" "How about… NO!"
    nr "He’s slowly walking towards me, holding his big o’l bat"
    nr "This is my chance to strike.."
    mc "METEOR SHOWER!"
    nr "The meteors can’t even penetrate his Spirit Aura.."
    lisa "LIGHT ARROWS!"
    lisa "That Aura is stronger than any kind of metal in this world"
    nr "I need to fight him hand by hand"
    mc "Lisa, Back me up, I’ll go near him."
    lisa "BLINDING LIGHT"
    nr "As soon as Blinding Light shines, I covered myself with spirit aura."
    mc "Spirit Aura… Engaged!"
    nr "I feel the vast amount of power flowing through my veins."
    mc "I can do this…"
    nr "as the blinding light wears off, I instantly throw a powerful punch into his jaw."
    mc "TAKE THIS! JAWBREAKER!"
    # *HPUNCH*
    nr "I heard a few bones of his cracked."
    mc "It’s working…"
    mc "Lisa! It’s working!"
    mc "Cast a Light Cloak on me!"
    nr "Blinding Light Cloak is Lisa’s special spell that covers your whole body with light that blinds everyone around you."
    lisa "BLINDING LIGHT CLOAK!"
    mc "We can do this! "
    # *hpunch vpunch*
    nr "I can feel every punch that I throw is taking him a lot of damage"
    mc "This one is for hurting Lisa!"
    # *Hpunch*
    mc "and this one is for making the people suffer!"
    # *Vpunch*
    # Black screen
    # *punch sounds
    nr "I punched him a lot until I satisfied myself. "
    mc "Maybe this is the time to give you my final blow…"
    mc "Any last words?"
    "Goblin Lord" "Wait! I’ll do what you want!"
    "Goblin Lord" "I’ll free the people, and help them rebuild this world.."
    mc "Really?"
    mc "Are you sure you’re going to do that?"
    "Goblin Lord" "Ofcourse…. NOT! HAHAHAHA!"
    "Goblin Lord" "TREE BIND!"
    # *Bind sounds
    nr "What the?!"
    mc "What kind of magic is this??"
    lisa "Ughh! Get this off me!"
    mc "Lisa!"
    lisa "This is ancient magic, Tree Magic…"
    "Goblin Lord" "You’re right! HAHAHA I kept this magic hidden for a long time"
    "Goblin Lord" "So I congratulate you both for making me use my secret magic"
    "Goblin Lord" "As a reward, I’ll make death easy for the both of you!"
    mc "FIRE SURGE!"
    mc "Ugh! I can’t use my magic"
    lisa "You can’t use any type of magic once a tree magic has been casted to you.."
    lisa "We don’t have any choice now…"
    mc "No! Don’t lose hope! We can still do this!"
    nr "I cannot let this happen"
    "Goblin Lord" "I think I’ll finish first off is the elf."
    "Goblin Lord" "I’ll let you join your ancestors now!"
    lisa "I’m glad I fought alongside you MC…"
    lisa "Thank you"
    mc "NOOOO!"

    if adventureWorld_Choice1 == False and normal_end == True:
        lisa "I lov--"
        # *SLASH*
        # *red screen*
        mc "Lisa? Lisa?"
        "Goblin Lord" "Your Lisa is Dead! HAHAHAHA"
        mc "Dead?"
        # *Flash back Lisa Faces*
        mc "NOOOO!!!!"
        # *FLashing Negative screen*
        # *turn into demon*
        nr "Lisa.."
        nr "Lisa…"
        "Goblin Lord" "What the??"
        "Goblin Lord" "A-A Demon!"
        mc "You will pay for what you’ve done…"
        mc "I’ll show you what hell looks like"
        mc "Hell’s Fire!"
        "Goblin Lord" "YOU CANNOT DEFEAT ME! AAAAAAHHHHH"
        # *Blibk*
        "Goblin Lord" "Wha-? Where did he go?"
        # *Vpunch*
        # *cpunch*
        "Goblin Lord" "Ughhh! Where are you??"
        # *Hpunch*
        # &Hopunch*
        # *Hpunch*
        "Goblin Lord" "STOP!"
        # *Slash*
        # *slash*
        mc "Any last words?"
        "Goblin Lord" "All of you people in this world are trash!"
        "Goblin Lord" "You don’t deserve to live in my kingdom!"
        "Goblin Lord" "You must be --"
        # *black slash*
        # *Demonic slash*
        "Goblin Lord" "Farewell."
        "Goblin Lord" "You had the choice to become a leader, but you chose to die."


        "Goblin Lord" "I hope this makes you happy Lisa…"
        "Goblin Lord" "I still have a lot of things to say to you.."
        "Goblin Lord" "But that will be for the next timeline I guess.."
        "Goblin Lord" "I’m sorry I failed to protect you.."
        "Goblin Lord" "Please come back.."
        # *fade to black*

        # *Screen to forest*
        nr "I did save this world from the reign of the evil Goblin"
        nr "I had a lot of training adventures with Lisa"
        nr "If I can just rewind the time, I’ll make sure that Lisa will make it out alive"

    return

label adventureWorld_Bad:
    mc "This is now my 2nd life and I just want to enjoy the rest of it."
    mc "I know you’ve trained me to defeat the Goblin Lord, but I really don’t have the strength and confidence to defeat a Lord."
    mc "I hope you understand.."
    nr "Maybe she hates me now.."
    lisa "It’s fine. You’re free to do what you want. Just forget what I said."
    lisa "I’ll help you pick some quest that suits you tomorrow."
    lisa "Let’s just head back now to the guild and have some rest."
    # *screen black
    # *room
    nr "What am I thinking?"
    nr "I really am a coward.."
    nr "Maybe that’s why I died in my previous world.."
    nr "I can’t face my fears.."
    nr "I’ll always be like this…"
    # *screen to black*
    # *knock knock*
    mc "Good Morning Lisa, What’s up?"
    lisa "Good Morning [playerName], I’ve found a suitable quest for you"
    lisa "I thought you might be interested in them.."
    mc "Ohh, Thank you Lisa, I’ll check them down the stairs in a bit."
    lisa "Okay, I’ll wait for you there."
    # *Lisa gone*
    nr "She even cares for me even though I rejected helping her.."
    mc "Maybe I made the wrong decision.."
    nr "I promise I’ll help her once I get strong enough"
    mc "Well, Time to check that quest.."
    # *screen black to quest board*
    lisa "[playerName]! Look!, This is the quest I found for you"
    lisa "It’s a 1 week escort type quest"
    lisa "You’ll just escort the city mayor in and out of this city for a week."
    lisa "Pretty easy quest for a big reward…"
    nr "This is not bad.."
    mc "How about you Lisa? Found any quest for yourself?"
    lisa "Ohh, No. I’ll be staying in the training hall for 2 weeks.."
    lisa "After seeing your performance, I realized that I’m still weak"
    lisa "I need to fill all the gaps in my technique. This is also the best time for me to explore my magic."
    nr "Just wait for me Lisa.. I’ll be strong enough to be able to help you."
    mc "Okay! Good luck on your training Lisa!"
    lisa "So, Are you going to take the Escort Quest?"
    mc "Yeah! This is not a bad quest after all.."
    lisa "Just fill up that form and give it to the quest manager."
    mc "Sure!"
    # *Blinds transition*
    mc "Okay I’m all done! I’ll head now to the City Hall and escort the mayor."
    lisa "Okay! Have a safe trip! I’ll see you in a week!"
    mc "Byeee!"
    # *Screen transition to white*
    # ----AFTER 1 WEEK------
    # *Sceen Otw to Guild Hall*
    nr "Ughhh.. I’m starving.."
    nr "I didn’t have any proper meal since last week"
    nr "But the pay is still good so it’s all worth it.."
    nr "I wonder what Lisa’s doing right now?"
    mc "Maybe I’ll go to the training hall to surprise her."
    # *training hall*
    mc "Lisa??"
    nr "I wonder why she’s not here. It’s still training hours."
    mc "Maybe she got back to the guild hall to rest."
    mc "I’ll better go check it out."
    # *Guild hall*
    nr "What happened here?"
    nr "Where did everyone go?"
    # *Some sounds*
    mc "Lisa??"
    "Goblin" "Uwaarrrrr!"
    mc "Light arrows!"
    # *shoot sounds*
    "Goblin" "Bleghhh"
    # *Goblin dead*
    mc "Where did that come from?"
    "Goblin" "Uweehhhh!"
    # 3 Goblin Uwehhh!!!
    nr "A goblin commander!"
    "Goblin Commander" "Kill him!"
    "Goblin" "Uwehhh!"
    # *Attack sounds*
    # *vpunch* *hpunch*
    mc "AAAAGHHHHhH!!!!"
    mc "HELP!!!! ANYONE!!!!!"
    mc "ACKKK…"
    # *Fade to Red*
    # --- YOU ARE DEAD----
    # *Go to main menu*
    return


label demonWorld:
    # Black Screen
    # Fade to background
    scene BG_Garden_Day
    mc "Woah..."
    nr "So this is the demon world."
    nr "This place looks really fantasy like."
    nr "Is this place a castle?"
    show Lucille Normal with Dissolve(0.5)
    lucille "…."
    mc "…."
    nr "It’s a cute demon girl."
    mc "Um.. hello there…"
    lucille "Th-This is the future demon king?"
    show Lucille Mad with Dissolve(0.5)
    lucille "How could I have summoned such a weak looking mongrel."
    lucille "A human nonetheless."
    nr "Wow she looks really disappointed."
    mc "Sorry for being a weak human I guess."
    show Lucille Normal with Dissolve(0.5)
    lucille "Well whatever, I can probably work with this."
    lucille "State thy name human."
    mc "Oh.. I’m [playerName] "
    mc "By the way what's going on?"
    mc "Why am I in some weird circle on the floor?"
    show Lucille Pose with Dissolve(0.5)
    lucille "Welcome to the Demon World."
    lucille "I am the Demon Queen Lucille and I have summoned you from the realm of the dead to serve in my kingdom."
    mc "Serve you? Wait does that mean I was summoned as a demon’s slave."
    lucille "As much as I’d like for you to be a slave your summoning ritual was actually somewhat special."
    lucille "I used the royal summoning spell  to summon a soul worthy of being the demon king. ."
    mc "Demon King? Me?"
    mc "Hell yeah I’m the demon king!"
    show Lucille Normal 2 with Dissolve(0.5)
    lucille "Not yet you are!"
    lucille "Don’t act so conceited mongrel, you are still far from being worthy of the title demon king."
    lucille "I can sense your weakness you know."
    nr "I guess I’m not much of a great person here like in my world."
    mc "You wouldn’t replace me with another by doing another summon ritual would you?"
    lucille "Unfortunately I can only perform the sacred ritual once."
    lucille "So I guess I’ll have to make do with you."
    mc "What am I supposed to do here then?"
    show Lucille Pose with Dissolve(0.5)
    lucille "You will learn to be a proper demon and earn the right to be demon king."
    lucille "Until then you shall be following my every instruction."
    lucille "Would you accept the responsibility?"
    lucille "Or would you prefer for me to send you back to the realm of the dead?"
    nr "Honestly, becoming the demon king… that actually sounds like a lot of fun."
    mc "Fine.. I’ll become the demon king. It’s not like I have anything else to do."
    show Lucille Smile with Dissolve(0.5)
    lucille "Okay then, from now you are on the path of becoming demon king."
    lucille "I shall be your partner on this endeavor."
    mc "Pleasure to be working with you."
    lucille "Yes but umm..."
    lucille "Please restrain yourself a bit around me first."
    lucille "I’m still quite inexperienced."
    mc "Huh? Okay..."
    nr "What does she mean restrain myself?"
    # Hallway
    scene BG_Castle_Hall_Day
    nr "She brings inside the castle to a fancy looking hallway."
    show Lucille Normal with Dissolve(0.5)
    lucille "Stay close to me, you don’t want to get lost in these halls"
    mc "Um… Miss Lucille…"
    lucille "You needn’t use honorifics when addressing me."
    show Lucille Happy with Dissolve(0.5)
    lucille "I grant you permission to just call me Lucille."
    mc "Okay then Lucille."
    mc "What exactly am I gonna be learning about."
    show Lucille Smile with Dissolve(0.5)
    lucille "Well… mostly the basic things like demon economics,demon etiquette,demon vision and mission."
    mc "Don’t those things sound too fancy for a demon to be studying about."
    show Lucille Normal 2 with Dissolve(0.5)
    lucille "We demons are a proud and noble race."
    lucille "It is only right for us to act in an elegant and dignified manner."
    nr "These are not the kind of demons I would imagine back in my world."
    mc "Would I at least be able to learn magic or something."
    show Lucille Smile with Dissolve(0.5)
    lucille "Of course you would."
    lucille "As future demon king you have access to use royal magic."
    mc "Royal magic… You mean like the magic you used to summon me?"
    mc "What kind of magic is that?"
    show Lucille Normal with Dissolve(0.5)
    lucille "Royal Magic in a way is like domination in the form of magic."
    lucille "Using royal magic one can bend the rules of mind and matter by dominating and commanding them."
    mc "Wait.. how does magic like that summon me to this world?"
    show Lucille Smug with Dissolve(0.5)
    lucille "That was the highest level of royal magic."
    lucille "I merely commanded the force controlling your soul to bring you to me."
    nr "So in a way she kind of commanded the goddess to bring me here."
    show Lucille Normal with Dissolve(0.5)
    lucille "Usually royal magic is mostly used to command lower level demons and open magically sealed mechanisms."
    nr "Just as she was saying that we arrive and stop at a closed door."
    show Lucille Smile with Dissolve(0.5)
    lucille "Oh.. perfect we’re here."
    lucille "Observe."
    show Lucille Pose with Dissolve(0.5)
    lucille "Open!"
    # Whoosh
    play sound "sounds/PowerUp9.mp3"
    nr "The doors in front of us suddenly open like an automatic door."
    nr "This kinda reminds me of mall doors."
    show Lucille Happy with Dissolve(0.5)
    lucille "Well? Amazing right?"
    mc "Well…."
    nr "I can tell she wants me to be impressed by that, guess I’ll pretend."
    mc "Wow! That was amazing, your magic is awesome!"
    lucille "No, that was just easy, especially for someone like me."
    mc "I never would have thought someone so small could do that."
    show Lucille Embarassed with Dissolve(0.5)
    lucille "Wha!?"
    # Angry
    show Lucille Mad with Dissolve(0.5)
    lucille "You mongrel! How dare you call me small!"
    lucille "Thou shall inflict harm upon himself!"
    mc "Excuse me?"
    nr "Then suddenly my fist came crashing down on my face."
    # Punch
    mc "Ouchie!"
    mc "I’m guessing that was royal magic."
    show Lucille Normal 2 with Dissolve(0.5)
    lucille "Do not treat me lightly! I am still the queen of this kingdom."
    nr "Oops.. she must not like being called small."
    mc "Sorry bout that, won’t happen again."
    show Lucille Normal with Dissolve(0.5)
    lucille "Whatever.. "
    lucille "Let’s just go inside already."
    # Bedroom
    scene BG_Castle_Bedroom
    mc "This place is?"
    show Lucille Smile with Dissolve(0.5)
    lucille "This is where you shall be staying."
    nr "That’s a really comfortable looking bed."
    mc "Can I sleep for today? "
    mc "I’ve been through a lot today, dying and everything."
    show Lucille Normal with Dissolve(0.5)
    lucille "I suppose you can rest for now."

    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "We shall start your demon studies first thing tomorrow morning."
    lucille "Make sure to wake up early."
    mc "Yeah yeah.."
    mc "Time to sleep then."
    hide Lucille
    nr "I fall asleep almost immediately as I lay into the soft bed more comfortable than any bed I’ve used back in my past world."
    # Fade to black
    lucille "Good night my demon king..."
    # Sleep tone music
    # Roaaar
    scene BG_Castle_Bedroom_Day
    mc "Gyaaah!"
    mc "What the frick was that!"
    show Lucille Smile with Dissolve(0.5)
    lucille "Oh.. did you not have roostergons in your previous world."
    lucille "They crow during mornings to start the day."
    mc "I’m pretty sure that was more roaring than crowing."
    mc "…"
    mc "Wait a minute… were you just sleeping in the same bed as me?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Well of course, this is my bed after all."
    mc "This is your room?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Yes."
    mc "Why did you make me stay here?"
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Well.. you are my future spouse after all."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "We might as well get used to it."
    mc "Future spouse? Me?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "You are the future demon king are you not?"
    mc "Now that you mention it… "
    mc "The demon king and queen would be married right?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Yes, exactly!"
    mc "Wait hold on! I’m not so sure about this yet."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "What do you mean you're not sure?"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "You said you would become the demon king right, did your determination then mean so little."
    mc "I didn’t realize being demon king entailed that."
    mc "I just got reincarnated, I don’t think I'm ready for that kind of lifelong commitment."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "What!?"
    show Lucille Mad
    with Dissolve(0.5)
    lucille "Are you saying you won’t take responsibility for me?"
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Do you dislike me that much?"
    # nr "I don’t dislike her but..."

    menu:
        "I don’t dislike her but..."
        "Maybe I can consider it":
            $ demonWorld_Choice1 = 1
        "I'm not ready for this.":
            $ demonWorld_Choice1 = 0

    if demonWorld_Choice1 == 1:
        mc "Now that I think about it, maybe I’d like being with you"
        mc "Let’s just get to know each other better first."
        show Lucille Smug
        with Dissolve(0.5)
        lucille "Hoh.. did you change your mind?"
        lucille "Have you come to realize what a great opportunity this is for you?."
        lucille "Smart move mongrel."
        show Lucille Smile
        with Dissolve(0.5)
        mc "I don’t feel like we’re going to get closer with you calling me mongrel all the time though."
        lucille "Oh… Is that so?"
        show Lucille Normal
        with Dissolve(0.5)
        lucille "…"
        show Lucille Embarassed
        with Dissolve(0.5)
        lucille "Okay then… [playerName]...."
        mc "..."
        show Lucille Embarassed
        with Dissolve(0.5)
        lucille "Well?"
        show Lucille Normal 2
        with Dissolve(0.5)
        lucille "Say something!"
        nr "So cute… I’m so glad I came to this world."
    if demonWorld_Choice1 == 0:
        mc "This is just too soon for me."
        mc "Sorry, but I can't promise to go through with a relationship like that yet."
        lucille "What!? But you have already given your word."
        lucille "You cannot just simply walk away now."
        lucille "Are you that much of a coward?"
        mc "Well... I guess I did give my word."
        nr "I should at least try to commit to something."
        nr "Am I really just gonna give up again so easily even in this world?"
        mc "I apologize... you're right, I promised that I would become the demon king."
        mc "I shouldn't be fazed by something like this."
        lucille "Hmph! Looks like you've finally come to your senses."
        lucille "Stupid mongrel…"
        nr "I’ll try for now but…"
        nr "Can I really become the demon king?"

    # Hallway
    scene BG_Castle_Hall_Day
    show Demon Maid at right
    with Dissolve(0.5)
    "Demon Maid" "Good morning milady."
    nr "We’re suddenly approached by what looks to be a demon servant of this castle."
    show Lucille Smile at left
    with Dissolve(0.5)
    lucille "Good morning."
    "Demon Maid" "Oh, Milady is that finally him?"
    mc "Oh, hello."
    "Demon Maid" "After all this time you have successfully summoned him."
    "Demon Maid" "Now you won’t be alone anymore."
    show Lucille Normal 2
    lucille "Hey!"
    mc "Did you need a demon king king that badly?"
    "Demon Maid" "Demon king? Milady just wanted to summon her soulma---"
    show Lucille Mad
    with Dissolve(0.5)
    lucille "Waah!!"
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Look at the time! We better hurry up, we're already behind schedule."
    "Demon Maid" "See you later then milady."
    # Footsteps
    hide Demon
    mc "Um.. where are we going anyway?"
    show Lucille Normal at center
    with Dissolve(0.5)
    lucille "We’re headed to where all the great powers of the world are stored."
    lucille "You shall absorb as much power as you can today."
    mc "Oohhh that sounds exciting!"
    nr "It sounds like we're gonna be going to some magical training room today."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "You sound ecstatic, I can see why."
    lucille "Personally, It is also my favorite place in the castle."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "I spend almost all of my time there."
    mc "No wonder you’re so powerful."
    # Library
    scene BG_Library
    nr "Goddamnit it’s just the library."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Pretty amazing isn't it?"
    mc "Yeah… Pretty cool..."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I secured most of these books myself."
    lucille "This library’s selection has grown bigger and better throughout the years."
    lucille "This section here in particular is full of rare texts defining ancient financial practices."
    lucille "While this shelf here is full of demon historical records written by the great demon authors."
    lucille "And over there is..."
    nr "She seems to really like literature."
    nr "She probably would've loved surfing the internet back in my past world."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Hey, are you listening?"
    mc "Yeah I’m listening."
    mc "What do I have to study about here?"
    show Lucille Smug
    with Dissolve(0.5)
    lucille "All of them."
    mc "What? You can't possibly expect me to finish all these books. There’s like a million of them."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Of course not. Even I’m not that unreasonable"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I’ll prepare a set of books for you which will greatly summarize all the topics you need to learn in this library."
    mc "Oh.. Okay then."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Wait here."
    nr "She’ll have to pick from a lot of books."
    nr "Lucille is a pretty nice person to do that for me."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Hmm…"
    nr "She’s also really damn cute to boot."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Oh, this one is good."
    nr "So small though, I wonder if she’s even legal to marry yet?"
    nr "I bet she’s one those 5000 year old demon lolis."
    nr "No problem with me though."
    show Lucille Smug
    with Dissolve(0.5)
    lucille "Here you go."
    # Table slam SE
    mc "That was fast, and wow that a lot of books to read."
    nr "Laid out on the table were about twenty really thick books."
    show Lucille Smile
    with Dissolve(0.5)
    mc "This looks a bit too hard for me."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "But you’ll finish them all wouldn't you. Right?"
    mc "Yeah… Okay then."
    nr "I lifelessly start reading the first book while knowing I'll have to finish a mountain of other books."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "..."
    lucille "Hey um…"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Do your best [playerName]. I’m rooting for you."
    nr "That was absurdly cute. I suddenly feel full of energy."
    mc "Dorya! I’m gonna finish all of these in one sitting!"
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Hey!? Don't try that hard."
    # Library Afternoon
    mc "Ughh.. This is never gonna end."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "…"
    nr "Lucille seems to have been reading some books herself for the past few hours."
    lucille "Mhmm.."
    nr "Her books seem way more fun than mine."
    mc "Hey, Lucille whatcha readin’."
    mc "Are you reading fiction or something?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Well yes, one would call it that."
    mc "Can we trade? Mine’s boring."
    show Lucille Mad
    with Dissolve(0.5)
    lucille "No."
    mc "Why’s that, lemme see that."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Oh!? Hey."
    nr "I grabbed the one of the books she had and checked the title."
    mc "“My Demon Romantic Comedy is Going Perfectly Well, As I Expected of the Great Me Vol. 3” "
    mc "What the hell is this??"
    nr "It’s like one of those romcom light novels with a really long title."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "That’s DemoRoma."
    lucille "It’s only one of the most popular series here in the demon world."
    mc "You don’t say. "
    show Lucille Happy
    with Dissolve(0.5)
    lucille "You can read that if you’re interested."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I guess you could take a break from your studies for now. "
    lucille "That is actually one of my favorite series."
    mc "Really? What are some other series you like?"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Mmmm… it’s hard to say, there are alot of novel series I like."
    lucille "There’s “A Specific Mystical Demon Indicant”."
    lucille "“That Time I Was Summoned As a Demon Goblin” was also pretty cool."
    nr "Sorry Lucille, but I don’t think the authors here are very original."
    mc "You sure know a lot of series Lucille."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Probably because I have a lot of free time here. It’s not like there’s much to do.."
    mc "Aren’t you kept busy by taking care of the demon community?"
    show Lucille Smug
    with Dissolve(0.5)
    lucille "As I said before, we demons are a proud and noble race."
    show Lucille Smile
    lucille "The people are well behaved, there’s really not much problems to take care of in this country."
    nr "That’s not fantasy like at all, usually there’d be wars or something."
    mc "Don’t you have any looming threats in this world though?"
    mc "Like an evil demon king that’s plotting to rule the worl---"
    mc "Nevermind."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Oh! Do you desire world conquest?"
    lucille "You can do as you wish once you are demon king, I will not object."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I would even support you If that is what you truly want to do."
    mc "I’m not so sure about doing something that crazy."
    mc "What about you Lucille? What do you wanna do?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Me!?"
    lucille "Well… I do love reading romance novels."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I was thinking maybe I could write one as well."
    mc "Oh cool! You're aspiring to be an author."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Maybe... Aspire is a big word."
    show Lucille Normal 2
    mc "Don’t worry, I’m gonna support you all the way."
    mc "I’ll buy one hundred copies of your book and I’m gonna line up for every future autograph session you hold."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "That’s too much support!"
    mc "What are gonna name this great romance novel of yours?"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "I was thinking of calling it something like “My Tiny Demon Wife can’t be this Cute”."
    mc "Do not use that name!"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Wha!?"
    # Dining Room
    scene BG_Dining_Room
    nr "After finishing up at the library, Lucille invited me to eat dinner with her."
    # Small Sprite
    mc "…"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "…"
    lucille "You don’t have to sit so far away you know."
    lucille "We’re the only two people here."
    mc "Sorry, I didn’t know where to sit."
    mc "I’m just not used to such a big dining table."
    # Chair SE
    # Zoom Sprite
    mc "Ah, This is much better."
    mc "Now I can talk to you more easily."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "It’s not like I wanted to talk more with you or anything."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "It’s just proper manners to eat with other people on the table."
    mc "I could barely see you from the other end of the table."
    mc "You looked even smaller than usual from over there."
    show Lucille Mad
    with Dissolve(0.5)
    lucille "What was that?"
    nr "Oh crap! Why did I say that?"
    lucille "Thou shall bite his tongue."
    mc "No wait owwwwlll!!"
    mc "Ouchie…"
    lucille "You shouldn't mess with a woman with royal magic."
    mc "Noted."
    show Lucille Normal
    with Dissolve(0.5)
    mc "By the way, when am I gonna learn to use royal magic."
    lucille "You’ve only just begun your studies, royal magic is still leaps and bounds ahead for you."
    mc "Yeah… Nothing’s ever easy."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "…"
    mc "..."
    mc "Where’s the food anyway? Should I go get it or something?"
    lucille "No need, It will be arriving shortly."
    lucille "My demon maid shall be serving it to the table."
    mc "Hope she doesn't put it on the other side of this strangely long table."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "This table is actually big because it was supposed to house the entire extended royal demon family."
    mc "Come to think of it, Where are all of the other demons in your family?"
    mc "I’ve only ever seen you and a bunch of servants here in this castle"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "About that..."
    show Lucille Normal
    lucille "They’re no longer here anymore."
    nr "Looks like I may have asked about a sensitive topic."
    mc "Sorry for asking about that. You don’t have to tell me more if you don’t want to."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Sorry? For what?"
    mc "Huh? Didn't your family die?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "No they aren’t dead."
    mc "Where are they then?"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "They just went on a vacation to Borakingdom where it’s warm all year long."
    show Lucille Mad
    with Dissolve(0.5)
    lucille "Leaving me behind here in the cold north."
    mc "Why didn't you just go with them then."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Because I hate going outside."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I’d rather prefer staying here all alone with all my books."
    nr "Oh she’s kind of like a shut-in then."
    lucille "What about you [playerName]?"
    lucille "Would you prefer to travel around the world than stay here with me?"
    mc "I guess I’m cool with staying here."
    nr "If I wanted to go on an adventure I would've just picked the adventure world."
    show Demon Maid at left
    with Dissolve(0.5)
    "Demon Maid" "Dinner is served."
    hide Demon
    with Dissolve(0.5)
    mc "Oh! That looks appetizing."
    lucille "I assure you, the meals served here are all top notch."
    mc "Munch munch."
    mc "Yeah no kidding, this is delicious."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Hey, mind your manners here on the dining table."
    mc "By the way what kind of meat is this?"
    mc "Are we eating dragon meat or something?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Yuck no, Why would we eat filthy monster meat."
    lucille "That would be disgusting."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "This is beef steak."
    mc "Yeah, actually that would be pretty disgusting."
    nr "I guess they don't eat monsters here like they do in those “different world” stories from my world."
    nr "This world really isn’t fantasy like in that sense."
    mc "I’m assuming the beef here came from farmed cattle?"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "You mean cattlegons?"
    mc "..."
    nr "The naming sense in this world though…"
    # Bedroom
    scene BG_Castle_Bedroom
    mc "Man I’m pooped, I’ve never worked this hard in my life."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Yes, even I have to admit today felt more tiring with you around."
    nr "Oh right I have to sleep in the same room as Lucille."
    lucille "Are you not going to bed yet?"
    mc "Uhhh yeah I’ll go to sleep in a while."
    lucille "Okay…"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Say.. I’ve put you through a lot today haven’t I."
    mc "Yeah, I’ll say."
    lucille "I wasn’t being too hard on you was I?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Do you regret coming to this world now?"
    # nr "Lucille looks like she’s serious."

    menu:
        "Lucille looks like she’s serious."
        "Regret is for the weak.":
            $ demonWorld_Choice2 = 1
        "Maybe I do regret it after all.":
            $ demonWorld_Choice2 = 0

    if demonWorld_Choice2 == 1:
        show Lucille Smile
        with Dissolve(0.5)
        lucille "Really?"
        show Lucille Normal
        with Dissolve(0.5)
        lucille "But I have been making you follow my selfish requests ever since you got here."
        mc "It wasn’t anything too hard."
        mc "Besides, I gave my word right?"
        mc "Just keep em’ coming, I’ll take on any challenge."
        show Lucille Embarassed
        with Dissolve(0.5)
        lucille "…"
        show Lucille Smile
        with Dissolve(0.5)
        lucille "Really? You would go that far for me?"
        show Lucille Normal 2
        with Dissolve(0.5)
        lucille "Aren’t I being a burden to you?"
        mc "Of course not."
        mc "Today’s been really fun."
        show Lucille Smile
        with Dissolve(0.5)
        lucille "That’s good then."
        mc "I’m gonna become the best damn demon king ever."
        lucille "Yes, and I’ll be with you every step through the way."
        mc "I wouldn't want it any other way."
        show Lucille Happy
        with Dissolve(0.5)
        lucille "Thank goodness, I’ve only known you for a while but..."
        lucille "I’m glad you were the one whom I summoned."
        mc "Thanks, I’m glad you were the one who summoned me as well."
        show Lucille Smile
        with Dissolve(0.5)
        nr "I can feel that she trusts me a little bit now."
        lucille "It’s pretty late, let us go to sleep already."
        show Lucille Smug
        with Dissolve(0.5)
        lucille "I’m gonna make sure to work even harder tomorrow."
        mc "You wouldn't want it to be too easy now would you."

    if demonWorld_Choice2 == 0:
        mc "This is kinda too much for me to handle."
        mc "I’ve never been really someone to take on a difficult challenge."
        lucille "Is that so."
        lucille "Sorry for making you put up with me today then."
        mc "Nevermind that, what’s done is done."
        lucille "I kind of expected you to be a better person."
        mc "Nah, I’ve never been anything special."
        mc "I’ll just keep doing the things I can do but I’ll never try too hard in the things I can't do."
        lucille "You believe in such a thing…"
        lucille "Such morals should be considered wrong."
        lucille "How disappointing."

    # Sleep Tone Music
    # Library
    scene BG_Library
    nr "A few weeks have gone ever since I came to this world."
    nr "I’ve grown accustomed to life here but still leagues away from becoming the demon king."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "…"
    nr "The best thing about this world is being with Lucille."
    nr "I have to admit, I’ve grown quite fond of her."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Hey, stop staring at me."
    lucille "You should really focus on your work."
    mc "But I’ve already learned enough."
    mc "I wanna do more demon-like things."
    mc "When am I gonna start learning royal magic?"
    show Lucille Smug
    with Dissolve(0.5)
    lucille "Oh really you've learned enough?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Who was the first president of the demon kingdom?"
    mc "Trick question! The demon kingdom has a monarchy."
    lucille "What is the demon kingdom’s gross domestic product."
    mc " 330.9 billion demon dollars."
    lucille "Who was the first demon to travel to the demon moon?"
    mc "Demon Armstrong!"
    show Lucille Pose
    lucille "What is my favorite kind of animal in the world?"
    mc "Dogons!"
    lucille "What kind?"
    mc "Pug dogons!!"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I see.. You have learned quite a lot already."
    mc "Was that last question even relevant?"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Very well then, we shall study royal magic starting tomorrow."
    mc "All right!"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "For now, we can take a breather for once."
    lucille "Do you have anything you wish to do?"
    mc "I don’t really know… "
    mc "Are there any interesting places here in the castle?"
    show Lucille Normal 2
    lucille "Now that you mention it, there is a special part of the castle I haven’t shown you yet."
    mc "A special part of the castle? That seems interesting."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "C’mon follow me."
    scene BG_Castle_Hall_Day
    mc "Say Lucille.."
    mc "Have you been working on your novel recently?"
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Wha!? How did you know that?"
    mc "I’ve seen you staying up late at night writing something."
    mc "We stay in the same room after all."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "You saw that?"
    lucille "Yes, I admit I have been trying to write my novel these past few nights."
    lucille "I was thinking writing a novel would be easy for a demon as great as me."
    mc "So? Was it easy?"
    show Lucille Mad
    with Dissolve(0.5)
    lucille "No it is not!"
    lucille "Writing a story isn't actually as easy as it seems."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Creativity is especially hard to grasp."
    lucille "I already had a clear image of the story in my mind but it was so difficult to put it into words."
    mc "Maybe writing novels just isn’t for you then."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "No, I will continue."
    lucille "It’s hard but I want to finish writing my story regardless."
    mc "That’s some determination. "
    show Lucille Happy
    with Dissolve(0.5)
    lucille "I just kinda felt inspired to write it."
    mc "Oh? Why so inspired all of a sudden?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "It’s probably because I’ve recently been watching some hopeless idiot strive to achieve things far beyond his capabilities."
    nr "That guy must be some idiot for Lucille to call him hopeless."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "…"
    mc "Hey! Wait a minute!"
    # Throne Room
    scene BG_Throne_Room
    mc "This place is.."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "This place is the very heart of the castle itself"
    lucille "The royal throne room."
    mc "Cool!"
    mc "Can I sit on the throne?"
    show Lucille Smug
    with Dissolve(0.5)
    lucille "Sorry, But only a noble demon crowned with the highest title such as me may sit on the throne."
    mc "Wouldn't our titles be basically the same when I become demon king?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Oh… Good point, I never thought about that."
    lucille "Maybe we should add one more throne here for the future."
    mc "Are throne rooms even supposed to have two thrones?"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Probably not, but it’s not like I have to follow some rule."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "I’m the queen after all, rules shall bend to my will."
    mc "If you say so."
    mc "What are you even supposed to do in a throne room anyway?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Theoretically, It’s for holding an audience with the queen or something."
    lucille "But most of the time it is left unused."
    lucille "It’s still an important part of the castle regardless."
    mc "What a waste of a beautiful throne to be unused though."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Sometimes I like to just sit on it and strike a confident pose."
    mc "Really?"
    lucille "I don’t know why exactly but it feels pretty empowering."
    nr "A small demon on a throne would be so cute."
    nr "I would love to see her just sitting there all smug."
    mc "You should try it now."
    show Lucille Mad
    with Dissolve(0.5)
    lucille "No."
    mc "Why not?"
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Because it’s embarrassing."
    mc "You said you do it sometimes."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Yeah but it’s different with you watching."
    lucille "I can sense that you have some strange expectation from me."
    mc "Oh c’mon."
    # Dining Room
    scene BG_Dining_Room
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "Dinner is served."
    hide Demon
    with Dissolve(0.5)
    nr "I’ve been fed meals here countless times already."
    nr "I kinda feel like I’m freeloading."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "What's wrong? You look worried about something?"
    mc "I just thought it’s pretty weird of me to suddenly come live here and eat for free."
    lucille "You've been here for a few weeks already, why let that bother you now?"
    lucille "You are the future demon king after all."
    mc "Yeah, you’re right."
    mc "It’s just that the meals here are always so delicious."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Did you not have delicious food back in your previous world?"
    mc "We had tons of delicious food back in my previous world."
    mc "I just never had the budget to try them."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "No worries, I can make them serve you any food you like."
    lucille "Feel free to request any dish you wish to have tried then."
    mc "Seriously? Can I request wagyu beef then?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Wagyu beef?"
    mc "Oh, do you not have that in this world?"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Not that I can recall. What kind of beef is this wagyu?"
    mc "It’s just really fatty and tender beef made from specially breeding cattle."
    mc "I mean cattlegons."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Really? That sounds alot like how our demonyu beef is made."
    mc "..."
    mc "Of course it does…."
    nr "Demonyu beef? Godamnit, how did I not see that coming."
    # Bedroom
    scene BG_Castle_Bedroom
    show Lucille Normal
    lucille "Hey [playerName]... I have something I want to talk about."
    mc "What is it?"
    lucille "You’ll finally be learning royal magic tomorrow."
    lucille "It is powerful magic but not exactly easy to handle."
    mc "Don’t worry I can probably handle myself well enough."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "That’s not the problem."
    lucille "Royal magic… It may consume you."
    lucille "Mortals were never meant to use domination on others."
    show Lucille Normal
    mc "But we’re different right? That’s why you can use it."
    mc "And why I need to be able to use it."
    mc "Because I was summoned here to be the demon king."
    show Lucille Normal
    lucille "No…"
    show Lucille Normal 2
    lucille "That’s not the purpose I summoned you for."
    show Lucille Smile
    lucille "Please whatever happens, just promise me you'll always be yourself."
    mc "Okay… I promise."
    lucille "Don’t break that promise."
    show Lucille Smug
    with Dissolve(0.5)
    lucille "If you do, I’ll personally be the one to lay down your punishment."
    mc "C’mon, That’s scary."
    # Sleep Tone Music
    # Hallway
    scene BG_Castle_Hall_Day
    nr "Today’s finally the day I learn royal magic."
    nr "The most important step in becoming the demon king."
    mc "This is bound to be an eventful day."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Indeed, just make sure you don’t mess up."
    mc "Is learning royal magic going to be that hard?"
    lucille "No, it is actually quite easy once you understand the concept behind it."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "But I still worry you might mess up something so simple."
    mc "I’m not that unskilled."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Joking aside, I’m sure you’ll grasp it quickly, you were summoned to be the future demon king after all."
    mc "Does that mean I was already summoned with magical talent?"
    show Lucille Smug
    with Dissolve(0.5)
    lucille "No, but you have been studying all this time haven’t you."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "You’ve greatly increased your intelligence thus greatly increasing your magical capabilities."
    mc "Was that what all that studying was for?"
    lucille "Royal magic should be easier to activate now with your high intelligence."
    lucille "It should come as second nature to you after getting used to it."
    mc "Cool."
    mc "By the way, Where in the castle are we gonna practice?"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "We won’t be practicing inside the castle."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "You may create a big mess considering it’s still your first time using royal magic."
    nr "Actually, It’s gonna be my first time using any kind of magic."
    mc "Yeah good point. Are we going outside then?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Yes, the castle gardens shall suffice as a training area."
    mc "Oh, I’ve never been there before."
    nr "Now that I think about it, I haven’t even really left the castle building since I got here."
    # Gardens
    scene BG_Garden_Day
    nr "This is a nice looking garden."
    mc "Are we really gonna make a mess here?"
    show Lucille Smug
    with Dissolve(0.5)
    lucille "Not If you follow my instruction properly."
    mc "Kay’ boss."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "First of all, if you want to cast royal magic, you should fix your manner of speaking."
    lucille "Try to use more formal speech like me."
    mc "Speaking formally will help me cast magic?"
    mc "Seriously? How does that make any sense?"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Formality is a sign of self control and discipline after all."
    lucille "Both of which are essential to control magic, especially royal magic."
    mc "Oh I get it, It’s kinda like the saying “knowledge is power”."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "In this case it’s more like “words are power”."
    mc "Affirmative! What is the next step sir!."
    show Lucille Mad
    with Dissolve(0.5)
    lucille "Who the hell are calling sir! I don’t mean talk like a soldier."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Sigh…  Let’s just try it out already."
    lucille "Try using it on a magically powered object first."
    lucille "They are built to take magic commands so they will be easier to control."
    mc "Just like the magical doors in the castle."
    show Lucille Pose
    with Dissolve(0.5)
    lucille "That fountain over there is powered by magic."
    lucille "Turn Off fountain!"
    nr "The water in the fountain suddenly stops flowing by her command."
    lucille "Try to command the fountain to turn on."
    lucille "Gather the magical energy in your body."
    lucille "Then simply describe what you want in words and the fountain will follow."
    mc "Okay then I’ll try."
    mc "..."
    mc "Go Fountain Water!!"
    show Lucille Mad
    with Dissolve(0.5)
    lucille "Formal speech!!"
    mc "Oh right…"
    mc "Turn On Fountain!"
    mc "…"
    mc "Nothing happened."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Your command lacked authority."
    mc "Authority?"
    lucille "You have to think that you are the fountain’s superior."
    lucille "Remember that you are the future demon king."
    lucille "The very rules of this world shall bend to your will."
    nr "She’s right, I have authority in this world. I was summoned to be the demon king."
    nr "I will be the demon king…"
    nr "No… I AM the demon king!"
    mc "Turn On Fountain!"
    with flashbulb
    # Whoosh
    show Lucille Happy
    with Dissolve(0.5)
    lucille "You did it!"
    mc "I did it…"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "Let’s not get ahead of ourselves though."
    lucille "You’ve only done it once, try it again."
    mc "Right."
    mc "Turn off Fountain!"
    # Whoosh
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Looks like you're starting to get the concept."
    mc "Cool! Can I try it on other things?"
    show Lucille Pose
    with Dissolve(0.5)
    lucille "Go ahead, try it on that tree, think of a different command."
    mc "Hmmmm…"
    mc "I know."
    mc "Leaves Scatter!"
    # Whoosh
    mc "Blow Wind!"
    # Whoosh
    scene BG_Garden_Day_2
    show Lucille Smug
    with Dissolve(0.5)
    lucille "Very nice, looks like you have talent for it after all."
    # nr "This is amazing, I’ve never felt so powerful before."

    menu:
        "This is amazing, I’ve never felt so powerful before."
        "I was actually an amazing person after all.":
            $ demonWorld_Choice3 = 0
        "It’s thanks to Lucille for helping me grow.":
            $ demonWorld_Choice3 = 1

    if demonWorld_Choice3 == 0:
        mc "I always knew I was someone special."
        lucille "Don’t celebrate yet we’re just getting started."
        mc "Right."

    if demonWorld_Choice3 == 1:
        mc "Thank you Lucille."
        show Lucille Smile
        with Dissolve(0.5)
        lucille "Don’t thank me yet we’re just getting started."
        mc "Right."

    nr "We kept on training royal magic for the following days."
    scene BG_Garden_Night_2
    with Dissolve(0.5)
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "Milady, You two should take a break."
    "Demon Maid" "I suggest stopping for today, he’s already low on mana."
    hide Demon
    with Dissolve(0.5)
    show Lucille Normal
    with Dissolve(0.5)
    lucille "I suppose we have been using magic a lot these past few days."
    mc "I feel fine, let’s keep going for a while longer..."
    # Fall
    nr "What? I can’t stand anymore…"
    show Lucille Shocked
    with Dissolve(0.5)
    lucille "[playerName]!"
    # Fade black
    # Bedroom
    scene BG_Castle_Bedroom
    show Lucille Normal
    with Dissolve(0.5)
    lucille "..."
    mc "Lucille?... What happened to me?"
    lucille "You used up your mana."
    mc "My mana? Oh right my magical energy."
    mc "I remember reading about that."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "You should rest for now."
    mc "Yeah, okay… I guess I used a bit too much royal magic."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "...."
    lucille "So… How is it? Using royal magic?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "You’ve pretty much already grasped its power by now."
    mc "Well…  I dunno how to describe it exactly."
    mc "One thing is for sure... It feels powerful."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "It feels like being on top of the world right."
    lucille "But there is no such place."
    lucille "We can only bend the rules, we don’t change them."
    mc "Don’t worry about it…"
    # Fade black
    # Sleep Tone Music

    if (demonWorld_Choice1 + demonWorld_Choice2 + demonWorld_Choice3) == 3:
        jump demonWorld_Good
    elif (demonWorld_Choice1 + demonWorld_Choice2 + demonWorld_Choice3) == 2:
        jump demonWorld_Normal
    else:
        jump demonWorld_Bad

    return

label demonWorld_Good:
    # Hallway
    scene BG_Castle_Hall_Day
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "Good morning master."
    mc "Oh, good morning."
    mc "Have you seen Lucille? I haven’t seen her since breakfast."
    "Demon Maid" "She’s in an emergency meeting with some of the demon leaders."
    "Demon Maid" "It should be over any minute now."
    mc "Emergency meeting? I hope it’s nothing too serious."
    "Demon Maid" "I'm sure she’ll be fine. You worry too much, master."
    mc "Have you been calling me master?"
    "Demon Maid" "Yes, I’ve heard that you already mastered your royal magic."
    "Demon Maid" "You’re basically the demon king now, therefore my master."
    mc "Well… I wouldn’t say mastered. But I admit, I have gotten quite good at it."
    "Demon Maid" "By the way, how have things been progressing between you and milady?"
    mc "Huh? Well… we have been getting along pretty well lately."
    "Demon Maid" "Really? How far have you two gone?"
    mc "H-How far? We’re not really like that yet."
    mc "I could use some advice actually."
    mc "Our relationship’s been feeling too professional recently."
    "Demon Maid" "Advice? Well… If you want to get closer to milady, just talk about the things she likes."
    mc "The things she likes..."
    show Lucille Smile at left
    show Demon Maid at right
    lucille "Hey, There you are [playerName]."
    "Demon Maid" "Hello, Milady."
    mc "Oh, Lucille."
    show Lucille Normal at left
    lucille "Oh, Did I interrupt? Were you two talking about something?"
    mc "Nah we were just chatting about y'know… demon stuff."
    "Demon Maid" "…"
    show Lucille Happy
    lucille "Nevermind that, come with me. I have some good news to discuss with you."
    mc "That sounds promising.."
    # Library
    scene BG_Library
    mc "What’s this about Lucille?"
    show Lucille Smile
    lucille "I had just gotten back from a meeting with some of the top demon officials."
    lucille "I got them to agree to officially acknowledge you as part of the royal family."
    mc "Part of the royal family?"
    mc "Wait,  Does that mean that you and I..."
    show Lucille Embarassed
    lucille "...Yes, It would seem that way."
    nr "It’s kinda like we’re officially getting engaged."
    show Lucille Smug
    lucille "You are going to hold a lot more responsibility from now on."
    show Lucille Smile
    lucille "Being part of the royal family means you shall finally hold the title of demon king."
    mc "That’s right, I’m gonna become the demon king."
    nr "Demon king… Can I really handle such a title?"
    show Lucille Smile
    lucille "Don’t worry, I’m sure you’ll do fine."
    mc "I didn't even say anything."
    show Lucille Smug
    lucille "You didn’t have to, I can tell exactly what’s on your mind."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "You are my demon king after all."
    mc "Lucille...."
    lucille "..."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Don’t look at me like that, It’s embarrassing."
    mc "Oh yeah, sorry bout’ that."
    show Lucille Normal 2
    with Dissolve(0.5)
    nr "She looked so beautiful just now… There’s no doubt about it, I really like Lucille."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Oh right, I should mention that there's going to be a coronation ceremony."
    lucille "You will be officially recognized as the demon king at the throne room in front of the kingdom’s residents."
    mc "I hope they won’t turn out to hate me or something."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "There may be some opposition at first, but I’m sure you’ll gain their trust eventually."
    lucille "Here’s some reference. You better prepare for the coronation ceremony right away."
    mc "After everything we’ve been through… I’m actually gonna be crowned the demon king."
    mc "It’s all thanks to you Lucille."
    show Lucille Smug
    with Dissolve(0.5)
    lucille "Yeah, you should be grateful."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "But really, it was because you followed your goal."
    mc "Speaking of goals... "
    mc "How's that novel you've been writing."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "My novel..."
    mc "Did you finish it yet?"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "About that… It’s not really near completion yet."
    mc "Need some ideas? I can help."
    lucille "No need."
    show Lucille Happy
    with Dissolve(0.5)
    lucille "I have a feeling I’ll be coming up with new ideas soon."
    mc "Oh.. What makes you say that?"
    lucille "Let’s just say I thought up a really good story to write."
    show Lucille Smile
    with Dissolve(0.5)
    mc "I’ll look forward to it then."
    mc "I know you’ll write a good story."
    lucille "It might be a really dumb story though."
    mc "I don’t care, I’ll still buy a hundred copies."
    mc "It’s the novel made by you after all."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Don’t say stuff like that."
    lucille "You’ll get my hopes up…"
    mc "Haha..."
    # Fade black
    # Throne room
    scene BG_Throne_Room
    # Whisper whisper
    mc "Woah, there are a lot more people than I thought there would be."
    mc "I’m getting kinda nervous about this."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "C’mon all you have to do is sit on the throne."
    show Lucille Smug
    with Dissolve(0.5)
    lucille "That’s literally the easiest coronation ever."
    show Lucille Smile
    with Dissolve(0.5)
    mc "You’re right.. I can do this."
    mc "I've been through a lot after all."
    # Grand music
    hide Lucille
    with Dissolve(0.5)
    nr "I slowly make my way to the throne trying my best not to look stupid."
    mc "… "
    mc "Demon Maid?"
    # Serious music
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "…"
    hide Demon
    show Lucille Mad
    with Dissolve(0.5)
    lucille "Hey, you’re in the way."
    # Pulls sword
    show Demon Maid
    with Dissolve(0.5)
    hide Lucille
    "Demon Maid" "Sorry milady, but I can’t let you go through with this ceremony."
    "Demon Maid" "I’ve actually been assigned here by your father to protect the throne from your silly romance endeavors."
    show Lucille Normal 2
    with Dissolve(0.5)
    hide Demon
    lucille "What!? How could you..."
    hide Lucille
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "You are blinded by your affection milady, You were seriously going to give the title of demon king to this pathetic human."
    "Demon Maid" "I can’t allow someone like him to be the demon king."
    mc "You were so nice, but this was how you thought about me…"
    show Demon Maid Sword at center
    with Dissolve(0.5)
    "Demon Maid" "Sorry, but you’ll have to die now."
    "Demon Maid" "You have no place here, just look around you, no one even cares if I slay you."
    mc "…"
    # Whisper whisper
    nr "She’s right… They're all just watching.."
    nr "They’re judging my worth as demon king."
    nr "I’ll show them!"
    play sound 'sounds/PowerUp9.mp3'
    mc "Lower your weapon!"
    # Whoosh
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "…"
    show Demon Maid Sword
    with Dissolve(0.5)
    "Demon Maid" "Ahahaha! What the hell are you doing?"
    lucille "That sword is... "
    "Demon Maid" "This is a magical resistance sword."
    "Demon Maid" "Not even milady can dominate me with royal magic while I’m holding this."
    nr "Dammit, Am I really gonna die again here."
    show Lucille Normal 2 at left
    with Dissolve(0.5)
    show Demon Maid Sword at right
    with Dissolve(0.5)
    lucille "Don’t give up!"
    lucille "I believe in you. Even If the whole world doesn’t believe in you, I will!"
    show Lucille Pose at left
    with Dissolve(0.5)
    lucille "Don’t forget who you are!!"
    nr "Lucille… "
    hide Lucille
    show Demon Maid Sword at center
    with Dissolve(0.5)
    nr "She’s right, I am…"
    mc "I am the demon king!!"
    mc "Lucille's Demon King!!!"
    # Zwish
    # Screen shake
    "Demon Maid" "What the!? Such power!"
    mc "I will be the demon king and no one is gonna get in my way!"
    show Lucille Smile
    with Dissolve(0.5)
    hide Demon
    lucille "Magnificent.. As one would expect from my soulmate."
    hide Lucille
    show Demon Maid Sword
    with Dissolve(0.5)
    "Demon Maid" "You!!"
    # Sword break
    "Demon Maid" "Wha!?"
    play sound 'sounds/PowerUp9.mp3'
    mc "Acknowledge me as demon king!!"
    # Whooooosh
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "Yes your majesty!"
    "Demon Maid" "All hail the demon king [playerName]."
    mc "I did it…"
    "Crowd" "All hail the demon king [playerName]"
    mc "What!? Did I target them too?"
    hide Demon
    show Lucille Happy
    with Dissolve(0.5)
    lucille "No, everyone just acknowledges you now."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Who wouldn't after that grand display of demon power."
    mc "My power?"
    show Lucille Happy
    with Dissolve(0.5)
    lucille "Congratulations, You truly are the demon king now."
    mc "Demon king…"
    mc "No… that’s not what’s important."
    show Lucille Normal
    with Dissolve(0.5)
    lucille "What do you mean?"
    lucille "It’s what you have always wanted."
    mc "I've realized now, all I really wanted was to be by your side."
    show Lucille Embarassed
    with Dissolve(0.5)
    lucille "Eh? ...Really?"
    mc "Lucille…"
    lucille "What is it?"
    mc "Will you accept me as your king?"
    show Lucille Smile
    with Dissolve(0.5)
    lucille "...Only if you accept me as your queen."
    # Clap Clap
    nr "I’ve finally found a place where I belong."
    nr "Lucille will accept me no matter what."
    nr "I’ll do my best in order to be worthy of her."
    mc "I'm glad you were the one who summoned me."
    show Lucille Smile
    with Dissolve(0.5)
    lucille "I’m also glad you were the one I summoned."
    lucille "You really are my destined one."
    lucille "From now on we shall always be together."
    nr "I truly am happy to have come to this world."


    return

label demonWorld_Normal:
    # Hallway
    scene BG_Castle_Hall_Day
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "Good morning master."
    mc "Oh, good morning."
    mc "Have you seen Lucille? I haven’t seen her since breakfast."
    "Demon Maid" "She’s in an emergency meeting with some of the demon leaders."
    "Demon Maid" "It should be over any minute now."
    mc "Emergency meeting? I hope it’s nothing too serious."
    "Demon Maid" "I'm sure she’ll be fine. You worry too much, master."
    mc "Have you been calling me master?"
    "Demon Maid" "Yes, I’ve heard that you already mastered your royal magic."
    "Demon Maid" "You’re basically the demon king now, therefore my master."
    mc "Well… I wouldn’t say mastered. But I admit, I have gotten quite good at it."
    "Demon Maid" "By the way, how have things been progressing between you and milady?"
    mc "Huh? Well… we have been getting along pretty well lately."
    "Demon Maid" "Really? How far have you two gone?"
    mc "H-How far? We’re not really like that yet."
    mc "We have too much important stuff to do."
    "Demon Maid" "...It all depends on what you consider important."
    hide Demon
    show Lucille Smile
    with Dissolve(0.5)
    lucille "Hey, There you are [playerName]."
    "Demon Maid" "Hello, Milady."
    mc "Oh, Lucille."
    show Lucille Normal
    lucille "Oh, Did I interrupt? Were you two talking about something?"
    mc "Nah we were just chatting about y'know… demon stuff."
    "Demon Maid" "…"
    show Lucille Smug
    lucille "Nevermind that, come with me. I have some good news to discuss with you."
    mc "That sounds promising.."
    # Library
    scene BG_Library
    mc "What’s this about Lucille?"
    show Lucille Happy
    lucille "I had just gotten back from a meeting with some of the top demon officials."
    lucille "I got them to agree to officially acknowledge you as part of the royal family."
    mc "Wait,  Does that mean…."
    show Lucille HappyBlush
    lucille "That’s right, we’re getting marrie--"
    mc "I’m finally gonna become the demon king!"
    show Lucille MadBlush
    with Dissolve(0.5)
    lucille "…"
    mc "...What? Did I say something wrong?"
    show Lucille Normal 2
    lucille "It’s nothing you’re absolutely right."
    mc "Why do you suddenly look mad?"
    lucille "I’m not mad!"
    mc "Okay.. So I’m the demon king now? Just like that?"
    show Lucille Normal
    lucille "Well.. Not yet actually."
    lucille "We still have to do an event to officially acknowledge you as the new demon king."
    mc "Oh.. You mean like a coronation?"
    lucille "Yes, exactly. It would be a perfect event to introduce the new king to the demon public."
    mc "I hope they won’t turn out to hate me or something."
    show Lucille Smile
    lucille "There may be some opposition at first, but I’m sure you’ll gain their trust eventually."
    lucille "Here’s some reference. You better prepare for the coronation ceremony right away."
    nr "After everything I’ve been through… I’m actually gonna be crowned the demon king."
    nr "This is gonna be the best day of my life."
    # Fade black
    # Throne room
    scene BG_Throne_Room
    # Whisper whisper
    mc "Woah, there are a lot more people than I thought there would be."
    mc "I’m getting kinda nervous about this."
    show Lucille Normal 2
    lucille "C’mon all you have to do is sit on the throne."
    lucille "That’s literally the easiest coronation ever."
    mc "You’re right.. I can do this."
    mc "I've been through a lot after all."
    # Grand music
    hide Lucille
    nr "I slowly make my way to the throne trying my best not to look stupid."
    mc "… "
    mc "Demon Maid?"
    # Serious music
    show Demon Maid
    with Dissolve(0.5)
    "Demon Maid" "…"
    lucille "Hey, you’re in the way."
    # Pulls sword
    "Demon Maid" "Sorry milady, but I can’t let you go through with this ceremony."
    "Demon Maid" "I’ve actually been assigned here by your father to protect the throne from your silly romance ambitions."
    lucille "What!? How could you..."
    "Demon Maid" "You are blinded by your affection milady, You were seriously going to give the title of demon king to this pathetic human."
    "Demon Maid" "I can’t allow someone like him to be the demon king."
    mc "You were so nice, but this was how you thought about me…"
    show Demon Maid Sword
    with Dissolve(0.5)
    "Demon Maid" "Sorry, but you’ll have to die now."
    "Demon Maid" "You have no place here, just look around you, no one even cares if I slay you."
    mc "…"
    # Whisper whisper
    nr "She’s right… They're all just watching.."
    nr "They’re judging my worth as demon king."
    nr "I’ll show them!"
    play sound 'sounds/PowerUp9.mp3'
    with flashbulb
    mc "Lower your weapon!"
    # Whoosh
    "Demon Maid" "…"
    show Demon Maid
    "Demon Maid" "Ahahaha! What the hell are you doing?"
    lucille "It’s useless… "
    show Demon Maid Sword
    with Dissolve(0.5)
    "Demon Maid" "This is a magical resistance sword."
    "Demon Maid" "Not even milady can dominate me with royal magic while I’m holding this."
    nr "Dammit, Am I really gonna die again here."
    "Demon Maid" "Goodbye master…."
    # Slash
    show Lucille Sad
    with Dissolve(0.5)
    hide Demon
    lucille "Nooo!!!"
    # Splat
    mc "Eh?"
    nr "Lucille protected me with her body…"
    mc "LUCILLE!!!!!"
    hide Lucille
    show Demon Maid 2
    with Dissolve(0.5)
    "Demon Maid" "What have I done…"
    hide Demon
    show Lucille Sad
    lucille "[playerName]... You are…"
    lucille "...my demon king."
    # Fall
    hide Lucille
    nr "She’s gone…"
    nr "She was the one person who believed in me the most."
    show Demon Maid 2
    "Demon Maid" "…"
    mc "She died because of you!"
    mc "And because of all you cowards just watching there!"
    mc "I’ll never forgive all of you!!!"
    # Zwish
    # Screen shake
    play sound 'sounds/PowerUp9.mp3'
    with flashbulb
    "Demon Maid" "What is this power?"
    # Sword break
    with flashbulb
    play sound 'sounds/PowerUp9.mp3'
    mc "All of you should just die!!!!"
    # Whooooosh
    # Fade red
    nr "That was the tale of how the demon queen Lucille died… "
    nr "And how the most cruel demon king ever known was born…"

    return

label demonWorld_Bad:
    # Dining Room
    scene BG_Dining_Room
    lucille "I have to say… You mastered royal magic quite quickly."
    mc "It wasn’t much."
    mc "I’m destined to rule after all."
    show Lucille Normal 2
    lucille "There’s a lot more to being demon king than being a ruler you know."
    mc "I know.."
    nr "These past few days I’ve gained an even greater understanding of royal magic."
    nr "But sometimes it feels like my mind wanders through fog."
    mc "Royal magic’s power is really limitless isn’t it?"
    show Lucille Normal
    lucille "Yes, it’s power is way above anything else."
    lucille "That’s why we have to set our own limits"
    lucille "Remind ourselves that we are only mortal."
    mc "Why would you want to be mortal though…"
    mc "My life ended before without even being anything special."
    mc "But here, I can be the powerful demon king…"
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Is being the demon king the only special thing to you in this world?"
    mc "Is there anything else special this world has given me?"
    show Lucille Normal
    with Dissolve(0.5)
    lucille "..."
    show Demon Maid
    "Demon Maid" "Dinner is served."
    show Lucille Normal 2
    with Dissolve(0.5)
    lucille "Forget it…"
    # Leave
    hide Lucille
    "Demon Maid" "Ah! Milady, where are you going?"
    nr "What’s she moping about…"
    nr "Is she hiding something from me?"
    show Demon Maid
    "Demon Maid" "Did you two fight or something?"
    mc "Hmmmm.."
    nr "I wonder If my royal magic is strong enough to be used on people."
    mc "Hey you!"
    "Demon Maid" "Hm?"
    mc "Kneel!"
    # Whoosh
    "Demon Maid" "Yes."
    # Sprite drag down
    mc "Ho! How amusing."
    "Demon Maid" "Wha!? Did you just use royal magic one me?"
    mc "Say.. do you know If you Lucille is hiding any secrets from me?"
    "Demon Maid" "Why are you suddenly asking me that? I can’t tell you that."
    mc "Tell me!"
    "Demon Maid" "Yes."
    "Demon Maid" "Milady told to hide from you the fact  that she only summoned you to meet her fated soulmate."
    mc "Fated soulmate? Me?"
    "Demon Maid" "Yes, She discovered your destiny to be her lover using prediction royal magic and then summoned you here."
    mc "Ahahaha! Seriously!?"
    mc "Is this supposed to be some silly little romance novel."
    mc "Still… I am grateful, I can become demon king thanks to her."
    "Demon Maid" "Eh!? How could you make me do that?"
    "Demon Maid" "That was really rude, you know."
    mc "Shut up!"
    # Whoosh
    "Demon Maid" "…"
    # Bedroom
    scene BG_Castle_Bedroom
    show Lucille Normal
    lucille "Hey…"
    lucille "Sorry for my attitude earlier."
    lucille "It was uncalled for, but you really shouldn't be acting so arrogant."
    mc "No problem, I’m over it."
    lucille "…"
    nr "Oh Lucille… acting so tough again."
    nr "Deep down you're just some girl obsessed with love stories."
    lucille "I’ve talked with some of the demon officials earlier today."
    lucille "They’ve agreed to hold your ceremony to become the official demon king."
    mc "Oh, That’s nice."
    mc "I was thinking it was time for me to ascend to the throne."
    lucille "I cancelled the agreement however, It is still far too soon for you."
    mc "What!?"
    lucille "I fear you may be consumed by  the dark side of royal magic."
    nr "What a wasted perfect opportunity. I could’ve had all the power I needed."
    nr "You are clearly a burden to me now Lucille."
    mc "C’mon Lucille, I’m all ready to be demon king."
    mc "My royal magic is top notch."
    show Lucille Pose
    lucille "Being a king requires more than just powerful magic."
    show Lucille Normal
    lucille "You just aren't ready yet, I feel something is wrong with the way you are now."
    nr "Look like I’ll have to take some desperate measures."
    mc "Believe me, I can do this…"
    mc "Trust me!"
    # Whoosh
    lucille "…"
    lucille "Yes, you're absolutely right."
    lucille "I’ll have them prepare your coronation ceremony right away."
    mc "Thank you Lucille…"
    nr "Oh Lucille, Even someone like you is powerless against me now."
    nr "This world shall be mine for the taking."
    lucille "..."
    # Sleep Tone Music
    # Hallway
    scene BG_Castle_Hall_Day
    mc "Today’s finally the big day huh?"
    show Demon Maid
    "Demon Maid" "Right this way please."
    nr "At last my time to rule has come."
    # Doors open sound
    # White light
    # Throne Room
    scene BG_Throne_Room
    show Lucille Normal
    lucille "…"
    mc "Huh?"
    lucille "That’s enough, you can leave now demon maid."
    show Demon Maid
    "Demon Maid" "Yes, milady…"
    # Door sound
    mc "This place is totally empty."
    mc "What kind of coronation is this? Where are all my future subjects?"
    lucille "It’s just you and me here [playerName]..."
    mc "Oh I get it!"
    mc "It didn’t work on you did it?"
    show Lucille Normal 2
    lucille "I am the demon queen after all, you can't dominate me."
    lucille "You're not powerful enough."
    mc "Okay, you got me…"
    mc "What are gonna do now? Why call me over here?"
    mc "Are you going to kill me?"
    show Lucille Normal
    lucille "No, this wasn’t how it was supposed to turn out."
    lucille "This isn’t you."
    lucille "The royal magic, it’s corrupting your mind."
    mc "Corrupted? No, It’s more like…"
    mc "...The power of royal magic has opened my eyes."
    lucille "How could you give in…"
    lucille "You promised me!"
    lucille "You promised me that you would always be yourself no matter what."
    mc "This is myself Lucille...."
    lucille "No…"
    show Lucille Pose
    lucille "Return to your senses! "
    # Whoosh
    nr "I feel her magic penetrate my very being."
    nr "But I’ve dealt with her royal magic before."
    nr "This won’t work on me!!"
    # Whoosh
    mc "…"
    mc "Ahahaha! So this was how you resisted my royal magic!"
    lucille "Dammit."
    mc "Obey Me!"
    # Whoosh
    lucille "Don’t!! "
    # Slash
    # Red flash
    mc "Eh?"
    nr "I’m bleeding…"
    show Demon Maid Sword
    "Demon Maid" "…"
    "Demon Maid" "Sorry milady, I couldn't leave you alone with this scum."
    show Lucille Shocked
    lucille "[playerName]!!!"
    # Red tint
    nr "Lucille… even after all that, you would still care for me…"
    nr "I’m such a fool… I should have cared for you as well…"
    lucille "Nooooo!!!!"

    return





































































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
