#This calculates the probability of getting the right door when chosing one at random and an extra one is opened. 
#We predict that changing door will increase your chances of wining. 
from __future__ import division
import random


def play_game(num_doors, door_change_option):
    car_location = random.randint(0, num_doors - 1)
    player_choice = random.randint(0, num_doors - 1)
    opened_door = random.randint(0, num_doors - 1)
    while opened_door == player_choice or opened_door == car_location:
        opened_door = random.randint(0, num_doors - 1)
    if door_change_option == 1:
        player_choice_changed = random.randint(0, num_doors - 1)
        while player_choice_changed == player_choice or player_choice_changed == opened_door:
            player_choice_changed = random.randint(0, num_doors - 1)
        return player_choice_changed == car_location
    else:
        return player_choice == car_location
        
        
        
def play_lots (times_played, num_doors, door_change_option):
    sum = 0
    for num in range(times_played):
        sum += play_game(num_doors, door_change_option)
    if door_change_option == 1: 
        return "With door change we get " + str((sum/times_played)*100) + "% right"
    else: 
        return "Without door change we get " + str((sum/times_played)*100) + "% right"
        


print play_lots(100000, 3, 1)
print play_lots(100000, 3, 0)
        
