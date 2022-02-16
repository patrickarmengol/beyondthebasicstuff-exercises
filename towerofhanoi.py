'''
Tower of Hanoi game exercise for "Beyond the Basic Stuff with Python"
This was my go at writing the game without any help, just looking at the sample output.
Seems like we ended up with similar implementations. 
'''

import sys

NUM_DISKS = 5

def display_game(state):
    # vertical sections of rods; one more than ndisks for aesthetics
    for section in range(NUM_DISKS, -1, -1):
        # iterate through each rod; left to right, A to C
        for rod in state.keys(): # i could have done for rod in 'ABC', but this works in this version of python
            # check if stack of disks on current rod is tall enough to reach section (zero-indexed)
            if len(state[rod]) >= section + 1:
                disk = state[rod][section]
                num_ats = disk
                num_spaces = NUM_DISKS - num_ats
                print(f"{' ' * num_spaces}{'@' * num_ats}_{disk}{'@' * num_ats}{' ' * num_spaces}", end='') # is the max 9 then...
            else:
                print(f"{' ' * NUM_DISKS}||{' ' * NUM_DISKS}", end='') # this is a bit redundant; could probably do only 1 print
         # newline for each section
        print()
    # rod labels
    print(f"{' ' * NUM_DISKS} A{' ' * NUM_DISKS}{' ' * NUM_DISKS} B{' ' * NUM_DISKS}{' ' * NUM_DISKS} C")

def prompt_move():
    # loop until valid input
    while True:
        print('''
enter the letters of "from" and "to" rods, or QUIT
e.g. AB to move top disk from rod a to rod b
''')
        user_in = input('> ').upper()
        if user_in == 'QUIT':
            print('bye')
            sys.exit()
        elif user_in not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('invalid input')
            continue
        else:
            return user_in

def execute_move(state, move):
    source, destination = move

    # check if from rod is empty
    if not state[source]:
        raise Exception('"from" tower is empty')
    # check if source top disk is bigger than destination top
    elif state[destination] and state[source][-1] > state[destination][-1]:
        raise Exception(f'disk {state[source][-1]} cannot rest on top of disk {state[destination][-1]}')
    # all other moves are valid
    else:
        state[destination].append(state[source].pop()) # modifies in place; no need to return
        

def main():
    print('''
tower of hanoi

move the tower of disks, one at a time, to another tower
larger disks cannot rest on top of smaller disks
''')

    # initialize game dictionary; each entry represents a rod and its disks
    game_state = {
        'A': list(range(NUM_DISKS, 0, -1)),
        'B': [],
        'C': []
    }

    # show initial state to player
    display_game(game_state)

    # main game loop; exits at success
    while game_state['C'] != list(range(NUM_DISKS, 0, -1)):
        user_move = prompt_move()
        try:
            execute_move(game_state, user_move)
            display_game(game_state)
        except Exception as e:
            print(e)
            
    print('congrats, you win')
        


if __name__ == '__main__':
    main()