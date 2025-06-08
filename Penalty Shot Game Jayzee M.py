from sys import exit
import random

class interfaces:
    @staticmethod
    def main_menu():
        while True:
            print("--- Hockey Penalty Shot Game by Jayzee Monserate ---")
            print("-> Type 'Z' to start the game. ")
            print("-> Type 'X' to quit the game. \n")
            prompt = input("Enter 'Z' or 'X' here: ").upper()
            if prompt == "Z":
                game_code()
            elif prompt == "X":
                exit()
            else:
                print ("Please type either 'Z' or 'X'!")
    
    @staticmethod
    def display_score(round_num, user_points, bot_points):

        print(f"After Round {round_num}:")
        print(f" +{'-'*9}+{'-'*9}+{'-'*9}+")
        print(f" |{'':^9}|{'Points':^9}|{'Shot %':^9}|")
        print(f" +{'-'*9}+{'-'*9}+{'-'*9}+")
        print(f" |{'You':^9}|{user_points:^9}|{(user_points/round_num)*100:^9.2f}|") 
        print(f" +{'-'*9}+{'-'*9}+{'-'*9}+")
        print(f" |{'Bot':^9}|{bot_points:^9}|{(bot_points/round_num)*100:^9.2f}|")
        print(f" +{'-'*9}+{'-'*9}+{'-'*9}+")
    

    @staticmethod
    def num_between():
        print("Please choose a whole number between 1 to 5!")

    @staticmethod
    def shot_visual(save, shot):
        holes = ['1', '2', '3', '4', '5']
        
        if isinstance(save, int):
            save = [save]

        if shot in save:
            holes[shot - 1] = '#'
        else: # if shot was successful
            holes[shot - 1] = 'X'

        print(f"\n +{'-'*11}+")
        print(f" |  {holes[2]}     {holes[0]}  |")
        print(f" |           |")
        print(f" | {holes[3]}   {holes[4]}   {holes[1]} |")
        print(f" +{'-'*11}+ \n")

class phase:
    @staticmethod
    def attack():
        while True:
            try:
                user_shot = int(input("Enter which hole you are going to shoot at: "))
                if user_shot in range(1, 6):
                    print(f"You shot at the {user_shot} hole.")
                    bot_cover = random.random()

                    if bot_cover < 0.05: # 5% to cover one hole
                        bot_save = [random.randint(1, 5)]
                        print(f"The bot covered the {bot_save[0]} hole.")
                    elif bot_cover < 0.7: # 65% to cover two holes
                        while True:
                            bot_save = random.sample(range(1, 6), 2)
                            bot_save.sort()
                            if bot_save != [1, 3]:
                                break
                        print(f"The bot covered the {bot_save[0]} and {bot_save[1]} holes.")
                    elif bot_cover < 0.85: # 15% to cover all lower holes (3, 4, and 5)
                        bot_save = [2, 4, 5]
                        print("The bot performed the butterfly cover!")
                        print("All the lower parts of the net were covered.")
                    else: # 15% to cover three random holes other than the 2-4-5 combination
                        while True:
                            bot_save = random.sample(range(0, 6), 3)
                            bot_save.sort()
                            if bot_save != [2, 4, 5]: # avoids the butterfly cover combination
                                break
                        print(f"The bot covered the {bot_save[0]}, {bot_save[1]}, and {bot_save[2]} holes.")

                    if user_shot in bot_save:
                        print("-+- The shot was saved by the bot. -+-")
                    else:
                        print("-+- YOU SCORE!!! -+-")
                    interfaces.shot_visual(bot_save, user_shot)
                    return 1 if user_shot not in bot_save else 0
                elif user_shot == 0:
                    print ("Returning to Main Menu... \n")
                    interfaces.main_menu()
                else:
                    interfaces.num_between()
            except ValueError:
                interfaces.num_between()
    
    
    @staticmethod
    def defend():
        while True:
            try:
                save_area = []
                user_cover = random.random()
                user_save_1 = int(input("Enter which hole you are going to cover: "))
                if user_save_1 in range(0,6):
                    save_area.append(user_save_1)
                    if user_cover < 0.6: # 60% chance to cover a second hole 
                        print("You can cover another hole due to luck!")
                        while True:
                            user_save_2 = int(input("Enter the other hole that you are going to cover: "))
                            if user_save_1 != user_save_2 and user_save_2 in range(1,6):
                                save_area.append(user_save_2)
                                save_area.sort()
                                break
                            else:
                                print(f"Please choose a number between 1 to 5 (that is not {user_save_1})!")

                        print(f"You chose the {save_area[0]} and {save_area[1]} holes to cover.")
                    elif 0 in save_area:
                        print ("Returning to Main Menu... \n")
                        interfaces.main_menu()
                    else:
                        print(f"You chose the {user_save_1} hole to cover.")
                    bot_shot = random.randint(1, 5)
                    print(f"The bot shot at the {bot_shot} hole.")
                    
                    if bot_shot in save_area:
                        print("-+- THE SHOT WAS SAVED BY YOU!!! -+-")
                    else:
                        print("-+- The bot scores. -+-")
                    interfaces.shot_visual(save_area, bot_shot)
                    return 0 if bot_shot in save_area else 1
                else: 
                    interfaces.num_between()
            except ValueError:
                interfaces.num_between()
    
def game_code():
    user_points = 0
    bot_points = 0
    round_n = 0
    print ("\n To go back to the Main Menu at anytime, type '0'. \n")
    while True:
        user_points += phase.attack()
        bot_points += phase.defend()
        round_n += 1
        interfaces.display_score(round_n, user_points, bot_points)

          
while True:
    try:
        interfaces.main_menu()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        