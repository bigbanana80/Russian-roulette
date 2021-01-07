import random

print('*****Russian roulette*****')
flag = True
gun = 3
#number of players input and making sure its a number between 1 to 6
no_of_players = 0
try:
    no_of_players =int(input('Number of players?(number from 2 to 6)'))  
except ValueError:
    print("you can't pass a string as a number")
while no_of_players < 0 or no_of_players > 6:
        no_of_players = int(input("Invalid number pls try again: "))
#making a list of players
players = []
while no_of_players != 0:
    players.append(no_of_players)
    no_of_players = no_of_players - 1
players.sort()
#print(players)
#some essential variables
gun_spin = 0
gun_shot = 0
#the game code
while flag :
    while flag:
            try:             
                if len(players)>=1:
                    if len(players)>=1:
                        gun_spin = random.choices(players, k = 1) 
                    print(f'player number {gun_spin} has been selected!') 
                    gun_spin_int = gun_spin.pop()
                    gun_shot = random.randint(1,6)
                    print('Spinned the meg.')
                    if gun_shot == 3:
                        print(f'player number {gun_spin_int} has been killed!')
                        players.remove(gun_spin_int)
                        if len(players) == 1:
                            if len(players)>=1:
                                winner  = players.pop()
                                print(f'player number {winner}  is  the winner!!!')
                            else:
                                print('GameOver')
                        else:
                            print(f'{len(players)} number of players are still alive')
                    break  
                else:
                    print("GameOver")
                    flag = False
                    break                    
            except ValueError:
                print('invalid value.')
#basically i needed 2 loops to make the game work, by changing flag to false and break statments 
# i controlled the loop ,  i can easily add user input and GUI to complete the game but its unnecessary    
     
    
        