"""
This  is a treasure hunt game
"""
print("""
   ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ---- \
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~    ~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
      """)

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

path = input("""
        You are standing at the entrance.
        There are two paths in front of you.
        Which path do you choose? ("left" or "right")""").lower()

if path == "left":
    print("You have chosen the path to the island.\nYour treasure adventure continues!")
    path = input("""
                You are the bank to go to the island.
                There are choices to take you across the river to the island.
                Which is your choice to cross the river? ("boat" or "swim")
            """).lower()
elif path == "right":
    print("You feel of the cliff!\nGame Over")
    exit()
else:
    print("Game Over! You chose a wrong path.")
    exit()

if path == swim:
    print("You reached the island by swimming")
    path = input("""
                You are on the island.
                There are three caves to choose from. One has the treasure
                 Which cave do you choose? ("cave1" or "cave2" or "cave3") 
                 """).lower()
elif path == boat:
    print("The boat has pirates the stole, because they also want the treasure")
    break
else:
    print("Game Over! You chose a wrong option.")
    exit()

if path == "cave1":
    print("You found the treasure, You won the game!\nGame Winner")
elif path == "cave2" or path == "cave3":
    print("The wrong you choose has beasts in side.\nGame Over!")
    exit()
else:
    print("Game Over! You chose a wrong option.")
    exit()
