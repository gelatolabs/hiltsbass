label start:
    scene bg black
    $ pname = "You"
    "Welcome to Hell!\nLevel B1: Limbo"
    "You got hit by a truck. You find yourself in Limbo, facing the Clerk of Learning and Information for Perpetual Purgatorial Imprisonment (CLIPPI)."
    clippi "NEXT!"

    scene bg limbo with dissolve
    show mc normal at right
    show clippi normal at left
    mc "Wha..."
    mc "*Where the hell am I?*"
    clippi "It looks like you're going to Hell! Would you like help?"
    mc "Huh?"
    show clippi bored at left
    clippi "C'mon dude, my shift's supposed to end in five minutes, and I gotta get home to watch Desperate Housewives."

    python:
        pname = renpy.input("So hurry it up and tell me your name.").strip()

    clippi "Alright [pname], looks like you got creamed by a truck."
    mc "Wha..."
    clippi "*sigh* Isn't it obvious?"
    clippi "YOU ARE DEAD."
    mc "Whaaaaaaaaaaaaaaaaaaa-"
    clippi "WILL YOU STOP THAT?"
    clippi "*sigh*"
    clippi "You're in Limbo, for now at least."
    clippi "We gotta figure out if you're fit to go meet the big man in the sky or not."
    mc "And how do we figure that out?"
    clippi "Well, we're just gonna wait around until you do something that's either Heaven-worthy or Hell-worthy."
    mc "Okay..."

    label toShitOrNotToShit: # that is the question
        menu:
            "Well, do something!"
            "Take a shit on his desk":
                pass
            "Don't take a shit on his desk":
                clippi "Come on now, I haven't got all day!"
                jump toShitOrNotToShit

    "Well, don't mind if I do..."
    show clippi angry at left
    clippi "WTF!!"
    clippi "Obscene! Indecent! Lewd!"
    clippi "Straight to Hell! Do not pass go! Do not collect $200!"
    clippi "In fact, there is a special place in Hell for weird perverts like you: Level B2! Into the Hellevator with you!"

    "An underling escorts you into the Hellevator..."
    underling "Psst... want to get out of here?"
    underling "You look pretty strong... I bet you could take Satan."
    underling "Just keep sinning and make your way deeper and deeper down into the depths of Hell."
    underling "Satan usually hangs out down in B9. Go fuck him up and you should be able to escape."
    underling "Take this map. It'll help guide you."
    $ have_map = True

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide clippi
    scene bg black
    with dissolve
    play sound elevatorOpen
    play sound fire loop
    "Level B2: Lust"
    "The Hellevator is under attack!"

    $ difficulty = 1
    call elevator

    play sound elevatorDing
    "You always knew your Guitar Hero skills would save your life one day."
    "The Hellelevator door slowly slides open to reveal a woman at the desk of a sex shop. She is currently on the phone (in which the receiver is the shape of a banana). You overhear her conversation."
    scene bg lust
    show mc lust at right
    show lust normal at left
    with dissolve

    lust "We're all out of the XXL model, this pandemic has seen a surge in the urge if you know what I mean!"
    "She slams the phone down and greets you in a sultry voice."
    lust "What can I do for you honey? Is it getting hot in here or is it just me? I have some really interesting new content that looks like it might just fit you well!"
    "She presents a stack of 4 different magazines on the desk infront of you." #These could be used to depict the 4 choices as well (content of the magazines)
    lust "Choose your poison, you nasty little freak!"
    "You slowly spread them out and get an unsettling feeling when you realize the pages are sticky. You carefully inspect the covers: (\"Fun with Buns\", \"Deep 'n' Cheep\", \"Blowin' for Owin\", and \"Smokey or Chokey BBQ\"). How shall you proceed?"

    show mc lust at menuRight
    show lust normal at menuLeft
    with ease
    menu:
        "Choose \"Fun with Buns\" to satisfy your appetite & beyond.": #win
            show mc lust at right
            show lust normal at left
            with ease
            "You grab the \"Fun with Buns\" magazine and head to the restroom to relieve yourself of some pressure.  Along the way you grab 3 bags of cheeseter's hawt fries."
        "Choose \"Deep 'n' cheep\" to get more bang for your buck.": #lose
            show mc lust at right
            show lust normal at left
            with ease
            "This magazine is half price but it should still get the job done.  That's what she said!"
        "Choose \"Smokey or Chokey\" because gag reflexes are foreign to you.": #lose
            show mc lust at right
            show lust normal at left
            with ease
            "Oh yeah, the cover on this one is hot as hell and will really pump you up!"
        "Choose \"Blowin' for Owin\".": #lose
            show mc lust at right
            show lust normal at left
            with ease
            "Debt is not something that is easily erased.  Where there's a will there's a way, anything to avoid that edicktion notice!"

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide lust
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B3: Gluttony"
    "The Hellevator is under attack!"

    $ difficulty = 2
    call elevator

    play sound elevatorDing
    "A faint ding indicates you have arrived at the next level. As the door opens you are overwhelmed by an extremely unpleasant odor and thick fog."
    scene bg gluttony
    show mc gluttony at right
    show gluttony normal at left
    with dissolve

    mc "*coughs and chokes*"
    gluttony "A'hoy there matey, hope you worked up an appetite!"
    "The voice startles you and as the fog clears it reveals the source: a human body with a pig's head, donning a pirate hat and an eye patch at a hot dog stand." #insert picture of scene
    mc "I'm absolutely famished, what's on the menu?"
    gluttony "Arrrr well we've got quite the variety land lubber, let me show you what we've got!"
    "The pirate pig winks and uses his peg leg to point at the menu behind him and awaits your response."

    show mc gluttony at menuRight
    show gluttony normal at menuLeft
    with ease
    menu:
        "Bloody goat cheesecake: Handcrafted with only the finest sacrifical animal milk. Topped off with the finely ground kidney stones of traitors. 5,000 calories per serving. ": #lose
            show mc gluttony at right
            show gluttony normal at left
            with ease
            "As you sink your teeth into the cheesecake you feel a crunch as the kidney stone fragments do their work and you pass out."
        "Huawei'n pizza:  Experience a taste of the orient, all ingredients and information sourced from international origins. (8 slices).  1,000 calories per slice.": #lose
            show mc gluttony at right
            show gluttony normal at left
            with ease
            "After downing the whole pizza you feel like you have somehow violated someone's personal data and go back to the hellevator."
        "Scalper scallops:  Special of the day, all you can scalp!!": #win
            show mc gluttony at right
            show gluttony normal at left
            with ease
            "A fond memory of the riches you earned scalping video cards during a pandemic makes you feel warm and juicy inside."
        "Spring rolls: No ingredients are listed but strangely enough there is a music note.": #lose
            #play sound rickroll
            show mc gluttony at right
            show gluttony normal at left
            with ease

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide gluttony
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B4: Greed"
    "The Hellevator is under attack!"

    $ difficulty = 3
    call elevator

    #play sound kaching
    "The Hellevator descends to the next level and instead of a ding you hear the cha-ching of a cash register as the door opens."
    "You feel a chill down your spine as you glance at what sits before you behind a card table."
    scene bg greed
    show mc greed at right
    show greed normal at left
    with dissolve

    "The grim reaper himself stares at you and feels like it is directly through your soul. His eyes are burning red orbs of light."
    #play sound evilLaugh
    greed "Hey [pname], good to see you again buddy! It's been a hot minute! *evil laugh*"
    greed "I've been playing with myself all night, care to join me? I'll deal you 4 cards, choose one to seal your fate!"

    show mc greed at menuRight
    show greed normal at menuLeft
    with ease
    menu:
        "Catapult:  The first card has an image of a catapult launching a poor traitorous soul into the fiery jaws of a massive hellhound.": #lose
            show mc greed at right
            show greed normal at left
            with ease
            "After selecting the catapault the image comes to life and you witness the poor soul's demise. Maybe they should be more loyal next time!"
        "Shield:  The next card showcases a shield being held by a knight protecting villagers from a dragon's fiery breath.": #lose
            show mc greed at right
            show greed normal at left
            with ease
            "Upon choosing the shield, a sense of goodness warms your heart.  You feel more virtuous and believe you have done something right."
        "Gold:  The third card has a pot of gold with a leprechaun menacingly staring at it in obsession.": #lose
            show mc greed at right
            show greed normal at left
            with ease
            "The gold card is hot to the touch and smells of greed. Haven't you been greedy enough for one day?"
        "Sword:  The last card shows a blood-soaked sword wielded by a massive ogre, seemingly in a state of bloodlust.": #lose
            show mc greed at right
            show greed normal at left
            with ease
            "As you touch the sword it melts in your hand to form a pool of blood. Rage envelops you and in the blink of an eye you decapitate the grim reaper with his own scythe."
            "He immediately reassembles and chuckles."
            greed "Third time this week!"

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide greed
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B5: Wrath"
    "The Hellevator is under attack!"

    $ difficulty = 4
    call elevator

    play sound elevatorDing
    scene bg wrath
    show mc wrath at right
    show wrath normal at left
    with dissolve

    "After a rapid descent the elevator starts to shake and then comes to an abrupt stop. The doors struggle to open and you step into a maze of thick vines, with the feeling that you are being watched."
    wrath "WHO DOST DISTURBETH ME??!"
    "Two purple ovals spring open and you realize that the grape vine is speaking to you."
    mc "It's me, uhhh [pname]."
    wrath "[pname], what a lovely name! You had me worried that it might be the big boss."
    mc "I used to be a boss where I come from."
    wrath "Uhh yeah, you sure look like one alright! I hope you don't mind but I have some work for you, I don't get out much these days so here's a few quests for you to mull over. Choose whichever one you fancy!"

    show mc wrath at menuRight
    show wrath normal at menuLeft
    with ease
    menu:
        "Quest 1:  Grapes needs to assert his juice & dominance in the field. Go drown out the other vines by overwatering them.": #win
            show mc wrath at right
            show wrath normal at left
            with ease
            "You locate a garden hose and irrigate the hell out of the other vines until they die. Have things gotten better or worse?"
        "Quest 2:  A pesky squirrel has been chewing on grape nuts. Make him a memory.": #lose
            show mc wrath at right
            show wrath normal at left
            with ease
            "Armed with a hacksaw and steel toe boots, you march to the vantage point but upon looking into the innocent creature's little eyes, you decide to spare him." #lose
        "Quest 3:  Grapes' main squeeze has been spotted juicing other fruits in the neighbourhood. Go clean that up.": #lose
            show mc wrath at right
            show wrath normal at left
            with ease
            "You systematically expire the apple, orange, and kiwi. That's the last juice they will be squirting. Fruit salad anyone?"
        "Quest 4:  The vending machine is out of order so Grapes needs you to pick him up a Kit Kat.  Hopefully he won't notice you only eat yours widthwise.": #lose
            show mc wrath at right
            show wrath normal at left
            with ease
            "You hand Grapes his Kit Kat and bite into yours while in the landscape orientation.  Grapes is visibly disturbed and belts out."
            wrath "In all my ears in this vine I have never witnessed such heresy, feel my wrath!!"

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide wrath
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B6: Heresy"
    "The Hellevator is under attack!"

    $ difficulty = 5
    call elevator

    play sound elevatorDing
    scene bg heresy
    show mc normal at right
    show heresy normal at left
    with dissolve

    "The Hellevator speeds down to the next level. You take a deep breath as the doors slowly spread open. You do a double-take as what stands before you is a life-size chocolate wrapped in an aluminum foil shell. The thin strip of paper sticking out of it's head wiggles as it begins to speak."
    heresy "Hey there sweet cheeks, I'm Hereshey Kiss. You've come to the right place!"
    mc "I have?"
    heresy "Of course, you look like a non-believer!"
    mc "I do?"
    heresy "*Giggles* It's written all over your face! I have a challenge for you, let's see if you are at my level!"
    mc "Sure thing, why not?"
    heresy "Pick one of the following actions that you think would melt me in your mouth and not in your hand."

    show mc normal at menuRight
    show heresy normal at menuLeft
    with ease
    menu:
        "Action 1:  Perform candy-bar genocide.": #win
            show mc normal at right
            show heresy normal at left
            with ease
            "You open a bag of mini snickers and proceed to smash them with a hammer until there is nothing left but a mess of wrappers and goo. Hereshey kiss looks on in horror and quickly rolls away!"
        "Action 2: Give Hereshey Kiss a kiss.": #lose
            show mc normal at right
            show heresy normal at left
            with ease
            "You lean in and give hersehey a peck on the wrapper. She blushes and returns the favour. Could this be the start of something special?"
        "Action 3: Woo her with some sweet talk": #lose
            show mc normal at right
            show heresy normal at left
            with ease
            "You lean in closer to Hereshey to whisper in her ear"
            mc "You know what my favourite drink is? Hot chocolate!"
            "Game over!"
        "Action 4: Play her a tune using only your body parts.": #lose
            show mc normal at right
            show heresy normal at left
            with ease
            "Needless to say, it didn't go well..."

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide heresy
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B7: Violence"
    "The Hellevator is under attack!"

    $ difficulty = 6
    call elevator

    play sound elevatorDing
    scene bg violence
    show mc violence at right
    show violence normal at left
    with dissolve

    "The sound of drumming grows louder and louder as the hellevator descends. You hear what sounds like a war cry and can only imagine what awaits you on the other side of the door.  As it opens you see a group of ancient warriors donning battle gear gathered around a fire.  The largest one turns and approaches you."
    violence "Speak now or I will split you in two."
    mc "Uhhh yes sir, your wish is my command."
    violence "That's more like it, what is your K/D ratio?"
    mc "I'd rather not say."
    violence "Actions speak louder than words anyway, let's see what you're really made of!"
    "The War Lord lays down a map infront of you with four cities."
    violence "Ok grunt, which one should we attack?"

    menu:
        "Los Santos: The city of angels is not what it used to be. It's time to burn it to the ground and put the citizens back in misery!": #lose
            "You mark Los Santos on the map and the War Lord shakes his head in disagreement."
            violence "We'll need more weapons for that job!"
        "Liberty City: It somehow reminds you of New Yawk. Word on the street is that crime has increased exponentially as of late.": #lose
            "Upon selecting Liberty City you realize you have made a mistake.  The War Lord grows impatient and snarls."
            violence "Haven't you ever invaded anywhere before? Those cowards are not worth our time."
        "San Andreas: A beautiful coastal settlement that is flourishing. Silicon is used here in abundance to enhance enjoyment.": #lose
            "After choosing San Andreas the War Lord realizes you have no clue what you are doing and swings his sword, splitting you in two. Now he has 99 problems but you ain't one."
        "Vice City: It has turned into a wretched collection of souls consumed by deception. Tax evasion is at an all-time high.": #win
            "You point to Vice City and the War Lord cracks an evil smile."
            violence "Yes, we shall strike at dawn and rain hell down upon this fradulent scum!"

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide violence
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B8: Fraud"
    "The Hellevator is under attack!"

    $ difficulty = 7
    call elevator

    play sound elevatorDing
    scene bg fraud
    show mc fraud at right
    show fraud normal at left
    with dissolve

    "After a short drop and a sudden stop, the hellevator doors squeak open to reveal a somewhat familiar face. Behind a desk sits a sleightly bent out of shape paper clip wearing a rastacap."
    fraud "Hey mon, how are you doing? Welcome to dee next level right?"
    mc "Hell yeah!"
    fraud "I be Trippi, you may have met my cousin CLIPPI up in Limbo."
    mc "Yes, it was a pleasure. I left something from my behind for him."
    fraud "How kind and thoughtful! You have made great progress, hopefully you're up for your final test!"
    mc "Hit me with your best shot!"
    fraud "Alright [pname], let's see how low you can really go! I'm afraid our lead software engineer recently met his demise. Help us get out of this jam!"
    "Trippi dusts off a box labelled 1995, removes some floppy dicks and places them infront of you."

    menu:
         "MyScrewSoft WinBlows 95: There's a sticky (literally) note indicating that the key has been lost.  You must crack it to perform a reinstall.": #lose
            "You grab the stack of 13 floppy disks and 72 hours later crack the code.  Unfortunately Ludum dare 48 is over by then and you fail miserably."
         "WinRawr v.1.54 Beta: release 04-22-95: It all fits on one disk but are you really so treacherous to perform such a treacherous task as robbing the poor honest developers of a license fee?": #win
             "Knowing well that a special place in hell is reserved for such perfidy, you easily patch and crack the beloved software and Trippi is happily browsing archives of questionable content."
         "Adoobie PhotoSlop 3.0: Trippi is frustrated that he can't edit his cat pictures anymore.  Help him out by restoring this ability.": #lose
            "The software reminds me of you a more \"civilized\" era when licenses were perpetual instead of monthly fees.  Your good deed does not go unnoticed."
         "BROOM 3D: A timeless classic, the witch on the cover looks as though she has slain many beings from the depths of hell.  It looks like it has been very well used.": #lose
            "Upon inserting the diskette in your drive an all-too familiar clunking sound notifies you instantly that this disk is toast.  Better luck next time!"

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide fraud
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Level B9: Treachery"
    "The Hellevator is under attack!"

    $ difficulty = 8
    call elevator

    play sound elevatorDing
    scene bg treachery
    show mc normal at right
    show satan normal at bigLeft
    with dissolve

    # Ending A: Kill Satan

    $ renpy.take_screenshot()
    $ renpy.save("autosave")
    hide mc
    hide satan
    scene bg black
    with dissolve
    play sound elevatorOpen
    "Heaven"
    "The Hellevator is under attack!"

    $ difficulty = 9
    call elevator

    play sound elevatorDing
    scene bg heaven
    show mc normal at right
    show god normal at bigLeft
    with dissolve

    # Ending B: Kill God

    return

label gameOver:
    scene bg black
    "Looks like you're not quite cut out for Hell. Up to Heaven with you! GAME OVER"
    $ renpy.load("autosave")
