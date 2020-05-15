"""
File: nimm.py
-------------------------
The game where players alternate taking 1 or 2 stones until there are zero left.
"""



def nimm():

    pile = 20
    player_num = 0
    while pile > 0:
        if player_num == 1:
            player_num = 2
        else:
            player_num = 1
        print("There are " + str(pile) + " stones left")
        answer = int(input("Player " + str(player_num) + " would you like to remove 1 or 2 stones? "))
        while answer > 2 or answer < 1:
            answer = int(input("Please enter 1 or 2: "))
        print("")
        pile -= answer

    if player_num == 1:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

def main():
    nimm()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
