label dad_summoned:
    define dad_c = Character("Refi\'s Dad")

    dad_c "I HEARD YOU BEAT MY SON AT MARIO KART."
    dad_c "AND MADE A PACT WITH HIM ON IT."
    dad_c "I GUESS YOU REALLY WANTED TO DRIVE A POINT HOME"

    refi "Stop dad, you are embarassing me!"

    dad_c "WELL SON, WHAT IS ALL THIS, I WAS JUST MOWING THE LAWN!"

    refi "Dad, my friend needs help with his math test."
    refi "I made a pact him and now i have to help him. Can you help us?"

    dad_c "YES, BUT ONLY IF YOU SOLVE MY EVIL CHALLENGES!"

    you "I will try my best!"

    dad_c "YOU WONT CHEAT WILL YOU?"

    you "NO! I WOULD NEVER CHEAT!"

    dad_c "ARE YOU CERTAIN? MY CHALLENGES ARE VILLANOUSLY DIFFICULT!"

    you "NEVER EVER! I BELIEVE IN THE POWER OF DOING IT MYSELF! IT WOULD BREAK MY HEART TO CHEAT!"

    narrator "You would never cheat in these challenges!"
    
    dad_c "SO BE IT. DO MY CHALLENGES!"

    dad_c "CHALLENGE 1: DO 20 PUSHUPS!"

    dad_c "CHALLENGE 2: EDUCATE YOURSELF ON THE AXIOM OF CHOICE!"

    dad_c "CHALLENGE 3: DRINK A GLASS OF WATER AND EAT A FRUIT (BUY ONE IF YOU DON'T HAVE ONE)!"

    dad_c "CHALLENGE 4: GET EIGHT HOURS OF SLEEP!"

    dad_c "CHALLENGE 5: CALL SOMEONE YOU HOLD DEAR!"

    dad_c "CHALLENGE 6: DO THE LAUNDRY!"

    dad_c "CHALLENGE 7: COUNT THE GRAINS IN A BAG OF RICE!"

    dad_c "CHALLENGE 8: TAKE A YEAR LONG BREAK TO RESET YOUR MENTAL ATTITUDE!"

    dad_c "CHALLENGE 9: JOIN YOUR LOCAL SATANIC CULT (FOUND ONE IF THERE IS NONE)!"

    dad_c "CHALLENGE 10: READ A BOOK, AT LEAST 500 PAGES!"

    dad_c "CHALLENGE 11: TAKE PART IN A GAME JAM!"

    dad_c "CHALLENGE 12: FIND THE LOVE OF YOUR LIFE!"

    dad_c "CHALLENGE 13: LISTEN TO MUSIC BY PETER MAFFAY!"

    dad_c "CHALLENGE 14: GO TO THE PARK, TAKE A WALK!"

    dad_c "CHALLENGE 15: PLAN A VACATION!"

    dad_c "CHALLENGE 16: ASSEMBLE AN IKEA SHELF!"

    dad_c "CHALLENGE 17: DO SOME SELF REFLECTION!"

    dad_c "CHALLENGE 18: EDUCATE YOURSELF ON THE GAME ROCKS 'N' DIAMONDS!"

    dad_c "CHALLENGE 19: GET A DEGREE, IF YOU HAVE ONE, GET ANOTHER!"

    dad_c "CHALLENGE 20: LEARN AN INSTRUMENT!"

    dad_c "THESE WERE MY CHALLENGES!"

    dad_c "HOPE YOU LIKED THEM."

    dad_c "YOU DIDN'T CHEAT ON ANY DID YOU?"

    dad_c "HOW MANY DID YOU REALLY DO?"

    menu:
        "More than 14":
            dad_c "WELL DONE! I, LUCIFER, WILL GLADLY HELP YOU WITH YOUR MATH TEST."
            dad_c "I MUST SAY THOUGH, THAT I AM ONLY MEDIOCRE AT IT!"
            $ final_score += 1
        "More than 9":
            dad_c "HMPH, YOU MADE AN EFFORT AND ACKNNOWLEDGE THAT."
            dad_c "HAVE SOME OF THE MATERIALS I PREPARED BACK THEN FOR MY SONS!"    
        "Less than 10":
            dad_c "SON, I AM DISSAPOINTED!"
            dad_c "YOU REALLY SHOULD TRY TO LIVE A BETTER LIFE!"
            $ final_score -= 1



