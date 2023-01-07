# Question 17

# Your friend will complete this function
def play_once(human_plays_first):
    """
        Must play one round of the game. If the parameter
        is True, the human gets to play first, else the
        computer gets to play first. When the round ends,
        the return value of the function is one of
        -1 (human wins), 0 (game drawn),
        1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random    # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} ".format(human_plays_first, result))
    return result


# (b)
comp_sc = 0
human_sc = 0

# (c)
is_human_player = True
player = input("Will the human play first? ")
if player == "No":
    is_human_player = False
        
# (d)
rounds = 1

# (a)
while True:
    # The below 6 lines are part of (c)
    if is_human_player:
        winner = play_once(is_human_player)
        print("It's your turn.")
        is_human_player = False
    else:
        winner = play_once(is_human_player)
        print("It's my turn.")
        is_human_player = True
    
    if winner == -1:
        human_sc += 1
        print("You win!")
    elif winner == 1:
        comp_sc += 1
        print("I win!")
    else:
        print("Game drawn!")
    
    print("I score " + str(comp_sc) + " and you score " + str(human_sc) + ".")
    # The line below is part of (d)
    print("You have won " + str(int((human_sc/rounds) * 100)) + "% of the match.")

    play_again = input("Do you want to play again? ")
    
    if play_again == "Goodbye":
        break
    else:
        rounds += 1