from collections import Counter
import random

#TODO: Improvement — display options as a numbered list and allow users
# to input number as vote instead of typing in option


print("""

welcome to
:::::::::  :::::::::   ::::::::   ::::::::  :::    :::  ::::::::  :::
:+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:   :+:  :+:    :+: :+
+:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+  +:+   +:+
+#++:++#+  +#++:++#:  +#+    +:+ +#+    +:+ +#++:++    +#++:++#++
+#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+  +#+          +#+
#+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#   #+#  #+#    #+#
#########  ###    ###  ########   ########  ###    ###  ########



:::     :::  ::::::::  ::::::::::: ::::::::::: ::::    :::  ::::::::
:+:     :+: :+:    :+:     :+:         :+:     :+:+:   :+: :+:    :+:
+:+     +:+ +:+    +:+     +:+         +:+     :+:+:+  +:+ +:+
+#+     +:+ +#+    +:+     +#+         +#+     +#+ +:+ +#+ :#:
 +#+   +#+  +#+    +#+     +#+         +#+     +#+  +#+#+# +#+   +#+#
  #+#+#+#   #+#    #+#     #+#         #+#     #+#   #+#+# #+#    #+#
    ###      ########      ###     ########### ###    ####  ########



    -----  Everyone contribute an idea. -----
""")


while True:
    ideas = input('How many people have ideas? \n')
    if (ideas.isdigit()):
        break
    else:
        print("\nNumber please!\n")
        continue

number_of_ideas = int(ideas)
options = {}
players = {}

for i in range (number_of_ideas):
    player = input(f"\nPlayer {i + 1}, please enter your name: \n")
    opinion = input(f"\nAlright {player}, what's your plan: \n")
    print("\n"*30)
    options[opinion] = 0
    players[player] = 0

# lets players decide between voting or random decision
def decisions():
    dec = input("""

    'vote' or 'randomize'?
    """)
    if dec.lower() == 'vote':
        return voting_process()
    elif dec.lower() == 'randomize':
        return comp_decide()
    else:
        print("That's not a option nitwit.")
        return decisions()

# computer chooses a random option as winner
def comp_decide():
    computer_options = list(options.items())
    computer_decision = random.choice(computer_options)
    print(f"""
    The computer has chosen {computer_decision[0]}!
    """)

# shows each player the available options before voting
def print_options(options):
    print('\nOptions:')
    for option in options.keys():
        print(f"""
        - {option}
        """)

# players have 5 chances to enter valid voting option
def voting_process():
    print("""

    ********************************************************************************
                       |        o                          |        o
    .    ,    ,---.    |---     .    ,---.    ,---.        |---     .    ,-.-.    ,---.
     \  /     |   |    |        |    |   |    |   |        |        |    | | |    |---'
      `'      `---'    `---     `    `   '    `---|        `---'    `    ` ' '    `---
                                                __|
    ********************************************************************************
    """)

    for player in players.keys():
        print_options(options)
        tries = 0
        while tries < 5:
            pick = input(f"""
                What's your pick {player}?

                """)
            if pick in options.keys():
                options[pick] += 1
                print("\n"*20)
                break
            else:
                tries += 1
                print(f"\nInvalid input. You have {5 - tries} tries remaining ")


    # calculates winner from dict values
    # auto tie breaker is not a bug, it's a feature
    top_contestant_info = Counter(options).most_common(1)
    winner, top_votes = top_contestant_info[0]
    print(f"""\n-----------------------------

        {winner} won with {top_votes}!

-----------------------------
    """)

decisions()
