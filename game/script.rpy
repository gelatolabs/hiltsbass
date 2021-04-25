label start:
    scene bg black
    "Welcome to Hell!\nLevel B1: Limbo"
    "You got run over by a truck hauling $300,000 of stolen/smuggled MVidiot RTA6900 graphics cards. You find yourself in purgatory facing the Clerk of Learning and Information for Perpetual Pergatorial Imprisonment."
    clippi "NEXT!"

    scene bg limbo with dissolve
    show mc normal at right
    show clippi normal at left
    "Wha..."
    "*Where the hell am I?*"
    "*Why does it look like I'm in the backrooms?*"
    clippi "It looks like you're going to hell! Would you like help?"
    "...?"
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
    clippi "You're in purgatory, for now at least."
    clippi "We gotta figure out if you're fit to go meet the big man in the sky or not."
    mc "And how do we figure that out?"
    clippi "Well, we're just gonna wait around until you do something that's either heaven-worthy or hell-worthy."
    mc "Okay..."

    label toShitOrNotToShit: # that is the question
        menu:
            "Well, do something!"
            "Take a shit on his desk":
                "Well, don't mind if I do..."
            "Don't take a shit on his desk":
                clippi "Come on now, I haven't got all day!"
                jump toShitOrNotToShit

    show clippi angry at left
    clippi "WTF!!"
    clippi "Obscene! Indecent! Lewd!"
    clippi "Straight to hell! Do not pass go! Do not collect $200!"
    clippi "In fact, there is a special place in hell for weird perverts like you: level B2! Into the hellevator with you!"

    "An underling escorts you into the hellevator and down to level B2..."

    scene bg black with dissolve
    #play sound elevatorOpen
    "Level B2: Lust"
    #play sound elevatorDing
    "The hellelevator door slowly slides open to reveal a woman at the desk of a sex shop. She is currently on the phone (in which the receiver is the shape of a banana). You overhear his conversation."
    scene bg lust with dissolve
    show mc lust at right
    show lust normal at left

    lust "We're all out of the XXL model, this pandemic has seen a surge in the urge if you know what I mean!"  
    "She slams the phone down and greets you in a sultry voice."
    lust "What can I do for you honey? Is it getting hot in here or is it just me? I have some really interesting new content that looks like it might just fit you well!"  
    "She presents a stack of 4 different magazines on the desk infront of you." #These could be used to depict the 4 choices as well (content of the magazines)
    lust "Choose your poison, you nasty little freak!"  
    "You slowly spread them out and get an unsettling feeling when you realize the pages are sticky. You carefully inspect the covers: (\"Fun with Buns\", \"Deep 'n' Cheep\", \"Blowin' for Owin\", and \"Smokey or Chokey BBQ\"). How shall you proceed?"

    menu:
        "Steal the magazines and run back into the hellelevator.": #lose
            "The hellevator doors slam shut and you hear a voice: \"Hell is no place for common thieves!\""
        "Bring the magazines to the restroom and take care of bidnazz.": #lose
            "After relieving some tension you return the somewhat moister magazines to the desk and head back to the hellevator."
        "Donate the magazines to a box labelled charity.": #lose
            "The charity box glows with a pale yellow light. It engulfs you and pulls you back into the hellevator."
        "Lick the magazines to further investigate the source of the stickiness.": #win
            "It appears as though the stickiness is of human origin. You lick your lips and decide there is nothing more to be said or done here and proceed back to the hellevator."

    scene bg black with dissolve
    #play sound elevatorOpen
    "Level B3: Gluttony"
    #play sound elevatorDing
    "A faint ding indicates you have arrived at the next level. As the door opens you are overwhelmed by an extremely unpleasant odor and thick fog."
    scene bg gluttony with dissolve
    show mc gluttony at right
    show gluttony normal at left

    mc "coughs and chokes"
    gluttony "A'hoy there matey, hope you worked up an appetite!"
    "The voice startles you and as the fog clears it reveals the source: a human body with a pig's head, donning a pirate hat and an eye patch at a hot dog stand." #insert picture of scene
    mc "I'm absolutely famished, what's on the menu?"
    gluttony "Arrrr well we've got quite the variety land lubber, let me show you what we've got!"
    "The pirate pig winks and uses his peg leg to point at the menu behind him and awaits your response."

    menu:
        "Bloody goat cheesecake: Handcrafted with only the finest sacrifical animal milk. Topped off with the finely ground kidney stones of traitors. 5,000 calories per serving. ": #lose
            "As you sink your teeth into the cheesecake you feel a crunch as the kidney stone fragments do their work and you pass out." 
        "Huawei'n pizza: Experience a taste of the orient, all ingredients and information from authentic sources (8 slices). 1,000 calories per slice.": #lose
            "After downing the whole pizza you feel like you have somehow been violated and head back to the hellevator."
        "Juicy vegan bites: Meat of the highest quality, consisting solely of murderers who are vegan. 500 calories pers serving, gluten free.": #win
            "It doesn't taste quite right but somehow you feel healthier and your digestive tract springs into action. With renewed energy you sprint to the hellevator."
        "Spring rolls: No ingredients are listed but strangely enough there is a music note.": #lose
            pass # rickroll

    scene bg black with dissolve
    "Level B4: Greed"
    "The hellevator descends to the next level and instead of a ding you hear the cha-ching of a cash register as the door opens."
    "You feel a chill down your spine as you glance at what sits before you behind a card table."
    scene bg greed with dissolve
    show mc greed at right
    show greed normal at left

    "The grim reaper himself stares at you and feels like it is directly through your soul. His eyes are burning red orbs of light."
    #play sound evilLaugh
    greed "Hey [pname], good to see you again buddy! It's been a hot minute! *evil laugh*"
    greed "I've been playing with myself all night, care to join me? I'll deal you 4 cards, choose one to seal your fate!"

    menu:
        "Jack: The Jack reminds you of a time you scalped video cards during a pandemic and had a good laugh about it.": #win
            "After selecting the Jack card an unholy cackling pierces your ears and you flaunt an evil smile on your way back to the hellevator, feeling a sense of accomplishment." 
        "Queen: The Queen brings back memories of your various adulterous escapades in VR.": #lose
            "Upon choosing the Queen you realize the error of your ways and understand that things are only going up from here."
        "King: The King elicits a time of great prosperity when you achieved great wealth from being the king of shoplifting prophylactics.": #lose
            "The extra small size was your biggest seller. Who knew such small things could lead to big profits? The hellevator doors await your return for ascension"
        "Ace: The Ace instantly refreshes your memories of purchasing nails at the hardware store for nefarious purposes.": #lose
            "If only they had seen it coming, maybe you wouldn't be in this mess! RIP"

    scene bg black with dissolve
    "Level B5: Wrath"
    scene bg wrath with dissolve

    scene bg black with dissolve
    "Level B6: Heresy"
    scene bg heresy with dissolve

    scene bg black with dissolve
    "Level B7: Violence"
    scene bg violence with dissolve

    scene bg black with dissolve
    "Level B8: Fraud"
    scene bg fraud with dissolve

    scene bg black with dissolve
    "Level B9: Treachery"
    scene bg treachery with dissolve

    # Ending A: Kill Satan

    scene bg black with dissolve
    "Heaven"
    scene bg heaven with dissolve

    # Ending B: Kill God

    return
