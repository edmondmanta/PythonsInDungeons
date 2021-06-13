import os
import winsound
import Player
import Story

intro = Story.Chapter()
intro.intro_msg()

sound = 'Main_Menu.wav'
winsound.PlaySound(sound,winsound.SND_ASYNC)

print('Would you like to start the adventure?')
user_answer = input('Yes or No -> ')
if user_answer.upper() == 'YES':
    print('OK')
    os.system('cls')
    answer = input('''What class would you like to be? Press a number to select a class 
1 - Warrior - strong, agile, packs a punch
2 - Mage - slick caster, turns enemies to dust 
    ''')
    if answer == '1':
        player_name = input("""You have chosen to be a mighty warrior
What is the character's name ? -> """)
        player = Player.Warrior(player_name)
        print("Entering a dangerous world.....be prepared")
        input('Press ENTER key to continue')
        os.system("cls")
        sound = 'Exploring.wav'
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        choice1 = Story.Chapter()
        choice1.first_path()
        path_option = input("Choose a path: ")
    elif answer == '2':
        player_name = input("""You have chosen to be a clever wizard
What is the character's name ? -> """)
        player = Player.Wizard(player_name)
        print("Entering a dangerous world.....be prepared")
        os.system('cls')
        sound = 'Exploring.wav'
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        choice1 = Story.Chapter()
        choice1.first_path()
        path_option = input("Choose a path: ")



    else:
        print('Choose a valid option')

else:
    print('Thank you, good bye')


