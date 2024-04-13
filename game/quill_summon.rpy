label the_quill_summoned:

    define qs_states = [False] * 10
    define counter = 0
    define ghost_1 = Character("Ghost 1")
    define ghost_2 = Character("Ghost 2")
    define ghost_3 = Character("Ghost 3")
    define ghost_4 = Character("Ghost 4")
    define ghost_5 = Character("Ghost 5")

refi "What do you want to ask them?"

label quill_select:
    menu:

        "What is 1+1?" if not qs_states[0]:
            $qs_states[0] = True
            ghost_1 "2"
            ghost_2 "10"
            ghost_3 "2"
            ghost_4 "That is beneath me."
            ghost_5 "2"

        "Are you good at math?" if not qs_states[1]:
            $qs_states[1] = True
            ghost_1 "Yes"
            ghost_2 "Yes"
            ghost_3 "I am okay."
            ghost_4 "I am the best!"
            ghost_5 "Yes"  

        "Are you a liar?" if not qs_states[2]:
            $qs_states[2] = True
            ghost_1 "No"
            ghost_2 "No"
            ghost_3 "No"
            ghost_4 "I have never lied in my life"
            ghost_5 "No"

        "What is your favorite math fact?" if not qs_states[3]:
            $qs_states[3] = True
            ghost_1 "Axiom Of Choice"
            ghost_2 "Bankmayer conjecture"
            ghost_3 "I dont know."
            ghost_4 "I usually only cite myself."
            ghost_5 "The gaussian sum formula"

        "Do you think you are a good teacher?" if not qs_states[4]:
            $qs_states[4] = True
            ghost_1 "I try to be."
            ghost_2 "The best out there"
            ghost_3 "Yes"
            ghost_4 "Obviously the best."
            ghost_5 "I think I would be okay."

        "Are you a ghost?" if not qs_states[5]:
            $qs_states[5] = True
            ghost_1 "Yes"
            ghost_2 "I am an abberation."
            ghost_3 "I live on through my work."
            ghost_4 "Yes I died a glorious death."
            ghost_5 "Yes."

        "How old were you when you died?" if not qs_states[6]:
            $qs_states[6] = True
            ghost_1 "56"
            ghost_2 "78"
            ghost_3 "80, though my work lives on."
            ghost_4 "36. The best die young."
            ghost_5 "19"

        "How did you die?" if not qs_states[7]:
            $qs_states[7] = True
            ghost_1 "Heart attack."
            ghost_2 "Stabbed by a compass."
            ghost_3 "Drug overdose"
            ghost_4 "An even greater drug overdose."
            ghost_5 "Too much coffee."

        "What was your profession?" if not qs_states[8]:
            $qs_states[8] = True
            ghost_1 "Teacher"
            ghost_2 "Teacher"
            ghost_3 "Teacher was my day job."
            ghost_4 "Being awesome"
            ghost_5 "Almost Teacher"

        "What is your favorite Ice cream?" if not qs_states[9]:
            $qs_states[9] = True
            ghost_1 "Pistacchio"
            ghost_2 "Vanilla"
            ghost_3 "Strawberry Cheese Cake"
            ghost_4 "Macadamia chocolate with white truffle oil."
            ghost_5 "Deez Nutz!"
        
    $counter += 1
    if counter < 5:
        refi "What do you want to ask next?"
        jump quill_select
    refi "Alright, which do you think is the math teacher ghost?"

    menu:
        "Ghost 1":
            ghost_1 "Thank you for choosing me. Of course, as a former math teacher, I will help you with your math problems." 
            $ final_score += 1
        "Ghost 2":
            ghost_2 "You've been FOOOOOOOOOOOOOLED!!!!!!! Good Luck on your math test, IDIOT!"
            $ final_score -= 1 
        "Ghost 3": 
            ghost_3 "Math really isn't my thing, but I think, I can help you."
            ghost_3 "By the way, I am a famous musician, maybe you have heard of me."
            you "What is you name?"
            ghost_3 "It's Peter."
        "Ghost 4":
            ghost_4 "Of course you chose me. Everybody knows I am the best. I will be the best teacher you have ever had."
            $ final_score -= 1
        "Ghost 5": 
            ghost_5 "I was only a teacher in training, but maybe I can help you."