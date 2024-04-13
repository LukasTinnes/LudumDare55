label bankmayer_summoned:

    define frank_counter = 0
    define frank_character = Character("Frank")
    narrator "An angry looking, balding man in his fifties stands before you in his bathrobe."
    frank_character "What the hell is going on? I was just about to take a bath. UNBELIEVABLE! The youth of today. The water is still running!"
    frank_character "Do you have any idea who I am? I'm Doctor Bankmayer. The best consultant on this whole continent."
    frank_character "What do you have to say for yourselves?"

    menu:
        "I need help in math.":
            frank_character "Wh-WhaT? .... Huh? ... THE FUCK!?"
            $ frank_counter -=1
        "I'm sorry about summoning you out of the blue.":
            frank_character "Well, at least you are polite when disturbing people."
            $ frank_counter +=1
        "Refi could you turn off the bathwater?":
            frank_character "Wow... There you go. He summons me and he doesnt even talk to me. Rude!"
    
    frank_character "You could at least give me some clothes! You know how cold it is? I'm an old man, I could catch a cold."

    menu:
        "I still have some of my old halloween costumes":
            frank_character "Do you think I'm a god damn joke? Get me some real clothes."
            $ frank_counter -=1
        "I will give you some of mine":
            frank_character "These are way too small. I guess it's better than nothing."
        "I will get some of my father's real quick":
            frank_character "Not my style but at least it fits."
            $ frank_counter +=1
    
    frank_character "Why was I summoned now?"

    menu:
        "I need help in math":
            frank_character "Unbelievable, you could have at least said please! Or something really."
            $ frank_counter -=1
        "Sorry, I summoned you by accident. I asked for a man who is very good at math, because I need a teacher":
            frank_character "Well you are right about the math part. I am the greatest tax consultant around."
            $ frank_counter +=1
        "Sir, I have summoned you, because I need help in math please":
            frank_character "You should have called me instead, before disturbing me during my bath time."
    
    frank_character "Why should I even help you?"

    menu:
        "Well if the renowned Frank can't help me... NO ONE can help me.":
            frank_character "Oh if you say it like that, I guess I could help you out a bit."
            $ frank_counter +=1
        "What do you want for your services?":
            frank_character "A thousand euros in tuition. But you certainly can not afford that."
            $ frank_counter -=1
        "You certainly have kids yourself. You know how much help we need":
            frank_character "No. But I see that you need help."
    
    frank_character "But time is money. What am I getting for my time here?"

    menu:
        "How about 15€. That's about all I have.":
            frank_character "It's about all I get then."
            $ frank_counter -=1
        "I have this painting from art class":
            frank_character "You know. On my off time, I sometimes visit museums. This is an okay piece. Good job, I guess."
            frank_character "Maybe I can hang it up in my office."
        "A mug that says 'This is how a cool Tax Consultant looks like'":
            frank_character "Now THIS is good thinking. Sell the person you are negotiating with exactly what they need."
            $ frank_counter +=1
    
    if frank_counter < 0:
        frank_character "You know what... No I will not help you. You have been rude to me. You have ruined my bath. And you have ruined my night."
        frank_character "I will go home now to take my bath. Leave me alone!"
        $ final_score -= 1
    elif frank_counter > 0:
        frank_character "Alright alright, I guess I can help you with you math."
        $ final_score += 1
    else:
        frank_character "Ugh... I guess I can help. But I won't like it."

    
    
