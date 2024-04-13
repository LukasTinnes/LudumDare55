# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define refi = Character("Refi")
define narrator = Character("")
define frank = False
define the_word = False
define nightmare_machine = False
define dad = False
define the_quill = False
define final_score = 0
define ghosts = Character("The quill ghosts")
define devs = Character("The developers")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    refi "Shit! I can NOT believe you beat me."

    you "You should have practiced more in Mario Kart!"

    refi "Shouldn't you be practicing for your math test?"

    you "Yes, I know! That's why I made this pact with you."

    refi "You summoned a demon and entered a pact with it, to help you with your math exam?"

    you "...Yes."

    refi "...righhht. Want me too steal the answer sheet?"

    you "NO! I WILL NOT CHEAT!"

    refi "Okay, calm down bro."

    you "I am sick and tired of getting bad grades. I want to pass on my own."

    refi "Hm... Usually, I would just go the easy route and just cheat. You know. As demons do."

    you "Apparently not in Mario Kart."

    refi "I would never! Even demons have standards. Maybe we can call up some of my buddies instead?"

    you "What are more demons going to accomplish?"

    refi "They could be good at math. Better than me at least."

    you "I guess..."

    refi "Alright. This is my contact list."

    narrator "Reficul hands you a demonic grimoire."

    refi "There are five beings in this grimoire, which could be helpful. Tell me which one you want to summon and I will tell you more about them."
   

label grimoire:

    menu:
        "Frank Bankmayer" if not frank:
            refi "Frank Bankmayer... Oh wait he is my dad's Tax Consultant. He certainly knows math. It's his job!"

            you "You can... just summon people?"

            refi "What about it?"

            refi "Do you want to summon him or not?"

            menu:
                "Yes":
                    refi "Okay, let's summon Frank Bankmayer."
                    $frank = True
                    call bankmayer_summoned from _call_bankmayer_summoned
                "No":
                    refi "Alright, let's check out the others first."
        "The Living Word" if not the_word:
            narrator "I am actually already here. Do you want to speak with me?"

            menu:
                "Yes":
                    narrator "Refi shows you a box."
                    refi "I found this box. It apparently needs a key!"
                    narrator "You see a black void, it contains a narrative hole. In it though is the key to the box."
                    narrator "You gather that you can bring offerings to the hole to shape a key to how you need it to be."
                    narrator "It seems, that different offerings have a different effects on the key in the hole."
                    narrator "You gather, that your key needs to be a creature with red fur, long claws, round eyes, long hair and a tail."
                    $the_word = True
                    call narrator_summoned from _call_narrator_summoned
                "No":
                    narrator "Fine then. I guess you don't want to play the game."
                    narrator "Well, I guess you actually LOST at Mario Kart."
                    you "Wait no that's not what I wanted at all."
                    narrator "Too bad, have fun with your F!"
                    return
        "The Nightmare Machine" if not nightmare_machine:
            refi "The Nightmare Machine, is an interesting friend of mine."
            refi "I love playing games with it, well, only one game really."
            refi "You can give it an input and it gives you a possible future."
            refi "Let's try focussing on success with it."
            you "Sure, maybe visualizing it could give me some confidence."
            refi "You want me to summon it then?"

            menu:
                "Yes":
                    refi "Alright, let me summon it."
                    call nightmare_summoned from _call_nightmare_summoned
                    $nightmare_machine = True
                "No":
                    refi "Alright, let's check out the others first."
        "Dad" if not dad:
            refi "I guess we can call my dad."
            refi "I don't even really know whether he is good at math."
            refi "Want me to call him anyways?"

            menu:
                "Yes":
                    refi "Alright, you wanted it..."
                    call dad_summoned from _call_dad_summoned
                    $dad = True
                "No":
                    refi "Alright, let's check out the others first."
        "The Quill" if not the_quill:
            refi "The quill is a magical item that allows ghosts to write with it. I remember that one ghost was a math teacher."

            refi "But there is a problem. Five ghosts are holding the quill and you do not know which one is holding the quill."

            refi "Ask them questions, to find out who the math teacher is. You can only ask 5 questions."

            refi "Do you want to summon the quill?"

            menu:
                "Yes":
                    $the_quill = True
                    call the_quill_summoned from _call_the_quill_summoned
                "No":
                    refi "Alright, let's check out the others first."
    
    if not(frank and the_word and the_quill and dad and nightmare_machine):
        jump grimoire
        
    # This ends the game.

    if final_score == 5:
        narrator "A few days later you have taken the math test and received your results. It is an A+."
        narrator "You have summoned all the people who have helped you again. Including me, the narrator."
        frank_character "Congratulations."
        narrator "The nightmare machine shows you visions of congratulations"
        dad_c "CONGRATULATIONS."
        ghosts "Congratulations."
        refi "Congratulations."
        narrator "You feel congratulated."
    elif -2 <= final_score < 0:
        narrator "A few days later you have taken the math test and received your results. It is a D but at least you passed."
        narrator "Nobody showed up to your afterparty. In Fact, I am leaving too now."
        narrator "At least you won at Mario Kart."
    elif 0 <= final_score <= 4:
        narrator "A few days later you have taken the math test and received your results. It is a B."
        narrator "It is not the best result possible, but we are all really proud of you."
        narrator "You really summoned your courage."
        refi "See, you could do it! You put in a good effort."
    else: 
        devs "Congratulations, you fucked up so bad, not even the narrator wanted to come back here. How the hell did you do that?"
        devs "You should really feel bad about yourself. By the way.... That math test."
        devs "You got an F. Every single question was false. You kind of insulted the teacher with your performance."

    return
