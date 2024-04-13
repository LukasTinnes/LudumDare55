label nightmare_summoned:
    define ghost_1 = Character("The Nightmare Machine")

    menu:
        "Knowledge":
            label nm_knowledge:
            menu:
                "Fact":
                    label nm_fact:
                    menu:
                        "Object":
                            jump nm_fail
                        "Property":
                            jump nm_fail
                "Belief":
                    label nm_belief:
                    menu:
                        "Ego":
                            label nm_ego:
                            menu:
                                "Naiveté":
                                    menu:
                                        "Knowledge":
                                            jump nm_knowledge
                                        "Pride":
                                            label nm_pride:
                                            menu:
                                                "Success":
                                                    jump nm_mid
                                                "Belief":
                                                    jump nm_belief
                                "Confidence":
                                    menu:
                                        "Feeling":
                                            jump nm_feeling
                                        "Work":
                                            label nm_work:
                                            menu:
                                                "Diligence":
                                                    menu:
                                                        "Success":
                                                            jump nm_mid
                                                        "Tiredness":
                                                            jump nm_tiredness
                                                "Time":
                                                    label nm_time:
                                                    menu:
                                                        "Change":
                                                            menu:
                                                                "Success":
                                                                    jump nm_mid
                                                                "Fact":
                                                                    jump nm_fact
                                                        "Clock":
                                                            menu:
                                                                "Machine":
                                                                    menu:
                                                                        "Human":
                                                                            menu:
                                                                                "Ego":
                                                                                    jump nm_ego
                                                                                "Energy":
                                                                                    jump nm_energy
                                                                        "Dream":
                                                                            menu:
                                                                                "Experience":
                                                                                    jump nm_experience
                                                                                "Nightmare":
                                                                                    menu:
                                                                                        "Nightmare Machine":
                                                                                            jump nm_success
                                                                "Digit":
                                                                    menu:
                                                                        "Fact":
                                                                            jump nm_fact
                                                                        "Success":
                                                                            jump nm_mid
                        "Object":
                            jump nm_fail
        "Feeling":
            label nm_feeling:
            menu:
                "Personality":
                    label nm_personality:
                    menu: 
                        "Ego":
                            jump nm_ego
                        "Nurture":
                            menu:
                                "Love":
                                    menu:
                                        "Praise":
                                            menu:
                                                "Pride":
                                                    jump nm_pride
                                                "Success":
                                                    jump nm_mid
                                        "Reward":
                                            menu:
                                                "Pride":
                                                    jump nm_pride
                                                "Success":
                                                    jump nm_mid
                                "Hate":
                                    menu:
                                        "Insult":
                                            menu:
                                                "Experience":
                                                    jump nm_experience
                                                "Ego":
                                                    jump nm_ego
                                        "Pubishment":
                                            jump nm_fail
                "Experience":
                    label nm_experience:
                    menu:
                        "Valence":
                            menu:
                                "Ego":
                                    jump nm_ego
                                "Personality":
                                    jump nm_personality
                        "Arousal":
                            menu:
                                "Energy":
                                    label nm_energy:
                                    menu:
                                        "Work":
                                            jump nm_work
                                        "Time":
                                            jump nm_time
                                "Tiredness":
                                    label nm_tiredness:
                                    menu:
                                        "Sloth":
                                            jump label_nm_fail
                                        "Depression":
                                            jump label_nm_fail

    label nm_success:
        refi "You somehow uncovered the Nightmare Machine in all its recursive beauty! I didn't even know this was possible. You are a genius!!"
        $ final_score += 1
        jump nm_out
        

    label nm_mid:
        refi "You did it! This should help you gain some confidence right?"
        you "I guess so."
        jump nm_out

    label nm_fail:
        refi "Well... sorry about that. Maybe we should leave the Nightmare machine alone for the day..."
        $ final_score -= 1
        jump nm_out 

    label nm_out: 