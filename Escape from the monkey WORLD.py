# # MAIN GAME SECTIONS START # #
import random
import time

def section4_3():
    print(" ")
    print("You take the flaregun")
    time.sleep(1)
    print("You fire the flare high into the sky.")
    time.sleep(1)
    print("A Few minutes later you hear the dull rumbling of an engine.")
    time.sleep(1)
    print("A Helicopter slowly comes into view! You're saved!")
    time.sleep(2)
    print(".....")
    time.sleep(1)
    print("As you look up at your saviour a horrible realisation hits you.")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print("THE MISCHIEVOUS MONKEY FROM THE AIRPLANE?!")
    time.sleep(1)
    print("Panic sets in, but before you can react the helicopter falls out of the sky onto the boat.")
    time.sleep(1)
    print("You are killed instantly.")
    time.sleep(1)
    print("Congratu...lations? ")
    gameover()
    # # ALMOST A WINNER WINNER CHICKEN DINNER

def section4_2():
    print("Flare [1]")
    print("Sail [2]")
    answer = input("")
    if answer == "1":
        section4_3()

    elif answer == "2":
        time.sleep(1)
        print("The soothing sound of an engine roaring to life fills your ears.")
        time.sleep(1)
        print("You sail off into the sunset. But you will never forget Monkey World.")
        time.sleep(1)
        print(" ")
        print("CONGRATULATIONS! YOU SURVIVED!")
        print("You're the best :)")
        # # WINNER WINNER CHICKEN DINNER

def section4_1():
    print("You spy a boat parked in the water ahead of you. Freedom awaits!")
    print(" ")
    time.sleep(1)
    print("You climb aboard.")
    print(" ")
    time.sleep(1)
    print("You spot a flaregun in the cabin.")
    time.sleep(1)
    print("You also notice a key in the ignition and give it a twist.")
    time.sleep(1)
    print("Do you attempt to sail away? Or do you fire the flare and wait for help?")
    section4_2()

def monkey_finish():
    print("After asserting your dominance over the monkeys, you have a tough choice to make.")
    print("Do you stay and be Monkey God forever [1]")
    print("Or follow the seagull noise? [2]")
    answer = input(" ")
    if answer == "1":
        time.sleep(1.5)
        monkeywin()
    elif answer == "2":
        time.sleep(1.5)
        print("You follow the soothing sound of seagulls and find a lovely beach.")
        print(" ")
        section4_1()
    else:
        print("Comon is not that hard just choose one, try again!")
        print(" ")
        monkey_finish()

def gorillafight():
    print("Do you accept?")
    print("Yes? [1]")
    print("No? [2]")
    answer2 = input("")
    if answer2 == "1":
        print(" ")
        print("You accept the gorillas challenge.")
        time.sleep(1.5)
        print("The gorilla charges at you but slips on a nearby banana peel! Convenient!")
        time.sleep(1.5)
        print("The gorilla flies full speed into a tree and dies instantly.")
        time.sleep(1.5)
        print("The monkeys all break out into applause driven by admiration and fear.")
        time.sleep(1.5)
        monkey_finish()
    elif answer2 == "2":
        print("The gorilla attacks anyway and kills you instantly in one powerful blow.")
        time.sleep(1.5)
        gameover()
    else:
        gorillafight()


def section4():
    print("How do you decide to move forward?")
    print("Follow the voices [1]? ")
    print("Follow the seagulls [2]? ")
    answer = input(" ")
    if answer == "1":
        time.sleep(1.5)
        print("You follow the voices and found a group of monkeys having a chat...")
        time.sleep(1.5)
        print("As you approach you hear snippets of conversation.")
        time.sleep(1.5)
        print("Confused but curious you continue to approach.")
        time.sleep(1.5)
        print("The monkeys all turn in unison to look at you. Oh no!")
        time.sleep(1.5)
        print("Before you have time to react the monkeys have formed a ring around you!")
        time.sleep(1.5)
        print("Out of nowhere a gorilla enters the circle and appears to be challenging you to a duel.")
        time.sleep(1.5)
        print(" ")
        gorillafight()

    elif answer == "2":
        time.sleep(1.5)
        print("You follow the soothing sound of seagulls and find a lovely beach.")
        print(" ")
        section4_1()
    else:
        print("There is only two choices, try again!")
        print(" ")
        section4()


def riddle_2_lose():
    print("You not smarter than a monkey, try again!")
    print(" ")
    time.sleep(1.5)
    riddle_2()

def riddle_2_win():
    print ("You win!")
    print ("The journal reveals the next path is on the right")
    print(" ")
    print("You leave the cabin and head left. Further along at the next fork you take a right.")
    time.sleep(1.5)
    print("As you are walking you hear faint voices in one direction, and seagulls squawking in the other.")
    print(" ")
    time.sleep(1.5)
    section4()
    
def riddle_2():
    print("Jay goes into a room where there are 3 primates Monkey A, Monkey B and Monkey C.")
    time.sleep(1)
    print("Monkey A is trying to walk like a human.")
    time.sleep(1)
    print("Monkey B is trying to hold a pen against the paper.")
    time.sleep(1)
    print("Monkey C is trying to build blocks.")
    time.sleep(1.5)
    print(" ")
    riddle_2_choice()

def riddle_2_choice():
    answer = input("Who is the smartest primate in the room?: ").lower()
    if answer == "jay":
        time.sleep(1.5)
        riddle_2_win()
    else:
        time.sleep(1.5)
        riddle_2_lose()

def riddle_lose():
    print("You not smarter than a monkey, try again")
    print(" ")
    time.sleep(1.5)
    riddle_1()

def riddle_win():
    print ("You win!")
    time.sleep(1.5)
    print ("The journal reveals the next path is on the left")
    time.sleep(1.5)
    print(" ")
    print("Next question...")
    print(" ")
    riddle_2()

def riddle_choice():
    answer = input("Make your choice [1/2/3/4]: ")
    if answer == "4" or answer == "Four".lower():
        time.sleep(1.5)
        riddle_win()
    else:
        riddle_lose()

def riddle_1():
    print("If five monkeys can eat five bananas in five minutes. How many minutes would it take for four monkeys to eat four bananas?")
    print(" ")
    time.sleep(1)
    print("1: Four")
    time.sleep(1)
    print("2: Sixteen")
    time.sleep(1)
    print("3: Twenty Five")
    time.sleep(1)
    print("4: Five")
    print(" ")
    time.sleep(1)
    riddle_choice()

def section3():
    print("Do you eat the delicious berries? Or take a peek at the withered Journal? ")
    print("Delicious berries? [1]")
    print("Withered journal? [2]")
    table_choice = input("")
    if table_choice == "1":
        print("You picked and ate the berries...")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("Oh no! they were poisonous!")
        print("You died :(")
        gameover()
    elif table_choice == "2":
        print(" ")
        print("You take a flick through the journal.")
        time.sleep(1.5)
        print("It seems to have been written by an explorer in the past.")
        time.sleep(1.5)
        print("Turning the pages you find a few riddles.")
        time.sleep(1.5)
        print("The journal explains that completing the riddles will unlock the path forward.")
        print(" ")
        time.sleep(1.5)
        riddle_1()
    else: 
        print(f"Wrong choice {name}, try again")
        section3()

def section2_2():
    print("You head inside the cabin stepping over monkey skulls and peeled bananas.")
    time.sleep(1.5)
    print("In the center of the room is a large table with some delicious looking berries and a withered journal on top.")
    print(" ")
    time.sleep(1.5)
    section3()

def section2_1():
    print(" ")
    print("As you head back toward the secret tunnel, you see the monkeys playing which almost makes you forget the locked cabin.")
    time.sleep(1.5)
    print("A Monkey takes your hand and leads you back toward the cabin. Is this the same one from earlier?")
    time.sleep(1.5)
    print("The monkey taps at the keypad which is hilarious. To your surprise you hear the door unlock.")
    time.sleep(1.5)
    section2_2()

def code_end():
    print("[1] Attempt to kick down the door.")
    print("[2] Head back towards the monkeys.")
    answer = input("[1]/[2]?: ")
    if answer == "1":
        time.sleep(1)
        print(" ")
        print("You attempt to kick down the door and obviously fail having just survived a plane crash. Calm down Rambo.")
        time.sleep(1)
        print("Feeling a little deflated, you decide to head back toward the monkeys.")
        section2_1()
    elif answer == "2":
        print("Annoyed by the locked door, you decide to go back and watch the monkeys to make yourself feel better.")
        section2_1()
    else:
        code_end()

def code_fail():
    time.sleep(1)
    print("TOO MANY ATTEMPTS.")
    time.sleep(1)
    print("PLEASE TRY AGAIN LATER.")
    time.sleep(1)
    print(" ")
    print("What will you do now?")
    print(" ")
    code_end()

def code_success():
    print("The keypad beeps and to your surprise you hear the lock snap open. A little shocked at your genius you step through the now open door..")
    section2_2()

def codelock3():
    time.sleep(1)
    print("1 ATTEMPTS REMAINING.")
    time.sleep(1)
    pword = input("Please enter your password: ")
    print(" ")
    if pword == shackword:
        code_success()
    else:
        time.sleep(1)
        print("INVALID PASSWORD. TRY AGAIN.")
        code_fail()
    
def codelock2():
    time.sleep(1)
    print("2 ATTEMPTS REMAINING.")
    time.sleep(1)
    pword = input("Please enter your password: ")
    print(" ")
    if pword == shackword:
        code_success()
    else:
        time.sleep(1)
        print("INVALID PASSWORD. TRY AGAIN.")
        codelock3()

def codelock1():
    print("3 ATTEMPTS REMAINING.")
    time.sleep(1)
    pword = input("Please enter your password: ")
    print(" ")
    if pword == shackword:
        code_success()
    else:
        time.sleep(1)
        print("INVALID PASSWORD. TRY AGAIN.")
        codelock2()
    
def codelock_start():
    global shackword
    shackword = "banana"
    print("You try to open the door but it is locked.")
    time.sleep(1.5)
    print("Below a thin screen you see a small keyboard resembling a Nokia phone from the 1990s.")
    time.sleep(1.5)
    print("You take a look at the screen. There seems to be a space for a 6 character password.")
    print(" ")
    time.sleep(1.5)
    codelock1()

def rps_success():
    print("YOU WON!!! The monkey holds your hand and takes you to what looks like a secret passage tunnel <3 ")
    print(" ")
    time.sleep(1.5)
    print("Seeing the light on the other side of the tunnel, you find a cabin!")
    time.sleep(1.5)
    codelock_start()

def rps_game():
    if user_choice == Monkey_choice:
        print(f"Both players selected {user_choice}. Its a tie, Try again!")
        time.sleep(1.5)
        user_input()
    elif user_choice == "rock":
        if Monkey_choice == "scissors":
            print(f"Rock smashes scissors! {name} win!")
            rps_success()
        else:
            print(f"Paper covers rock! {name} lose. Try again!")
            time.sleep(1.5)
            user_input()
    elif user_choice == "paper":
        if Monkey_choice == "rock":
            print(f"Paper covers rock! {name} win!")
            rps_success()
        else:
            print(f"Scissors cuts paper! {name} lose. Try again!")
            time.sleep(1.5)
            user_input()
    elif user_choice == "scissors":
        if Monkey_choice == "paper":
            print(f"Scissors cuts paper! {name} win!")
            rps_success()
        else:
            print(f"Rock smashes scissors! {name} lose. Try again!")
            time.sleep(1.5)
            user_input()

def user_input():
    global user_choice
    global Monkey_choice 
    possible_choices = ["rock", "paper", "scissors"]
    Monkey_choice = random.choice(possible_choices)
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        print(f"\n{name} chose {user_choice}, Monkey chose {Monkey_choice}.\n")
        time.sleep(1.5)
        rps_game()
    else: 
        print(f"Wrong choice {name}, try again")
        user_input()



def section2():
    print("Walking down the path you spot a mischievous monkey. The monkey tackles you to the ground and says... rock, paper, scissors?")
    time.sleep(1.5)
    print("Thinking what the f**k is happening, you don't seem to have a choice lol")
    print(" ")
    user_input()

def section1_3():
    print(" ")
    print("You chose the cliff thinking you'll get a better view of the area. What a waste of steps because all you see is some dodgy rocks you'll have to climb down into the abyss")
    answer = input("Do you dare to climb down or turn back? [TURN/CLIMB]: ").lower()
    if answer == "climb":
        print("You should've known, first step down and rolly polly you go. SPLAT! ")
        gameover()
    elif answer == "turn":
        print("Thought there were no chickens in the jungle, you turn back to the original path.")
        section1_2()
    else:
        section1_3()

def section1_2():
    print(" ")
    print("Down in the deep dark forest you go.")
    time.sleep(1.5)
    print("You seem to be going round in circles. ")
    time.sleep(1.5)
    print("Oh no, the direction you've gone looks to be a dead end. A big fat rock is blocking the way")
    time.sleep(1.5)
    print("Rather than using your energy to tackle this rock, you take a different direction....")
    print(" ")
    time.sleep(1.5)
    section2()

def section1_1():
    print(" ")
    print("Lost out your mind and shocked of your only survival. You have a decision to make... Either turn LEFT into the deep dark jungle or turn RIGHT to what look like some cliffs")
    time.sleep(1.5)
    answer = input("[LEFT] or [RIGHT]?: ").lower()
    if answer == "left":
        section1_2()
    elif answer == "right":
        section1_3()
    else:
        section1_1()

def section1():
    print(" ")
    print(f"{name} the {player_char} you are enjoying a relaxing plane ride as you are on vacation.")
    time.sleep(2)
    print("BANG!!!!!...")
    time.sleep(2)
    print("All of a sudden you hear a hudge explosion the engine and the engine starts to fail.")
    time.sleep(2)
    print("The plane slowly starts to descend, you hear people screaming for there life")
    time.sleep(2)
    print("SMOKE!!")
    time.sleep(1)
    print("SCMREAAING!!!")
    time.sleep(1)
    print("FIREEEE!!!")
    time.sleep(2)
    print("The plane is rapidly coming down, you think back.....")
    time.sleep(2)
    print("Did that mischievous looking monkey have somthing to do with it..??")
    time.sleep(2)
    print(" _                        ")
    print("| |                        ")
    print("| |__   __ _ _ __   __ _   ")
    print("| '_ \ / _` | '_ \ / _` |   ")
    print("| |_) | (_| | | | | (_| |    ")
    print("|_.__/ \__,_|_| |_|\__, |   ")
    print("                    __/ |  ")
    print("                   |___/  ")
    time.sleep(3)
    print("You have Crashed!! and quickly come to realize you are the only survivor")
    time.sleep(2)
    print("You make it your mission to escape this island!")
    time.sleep(2)
    section1_1()
# # MAIN GAME SECTIONS END # #
# # GAME OVER SECTION START # #
def gameover():
    print("GAME OVER")
    time.sleep(1.5)
    answer = input("Try again? [Y/N]: ").lower()
    if answer == "y" or answer == "yes":
        intro()
    elif answer =="n" or answer =="no":
        exit()
    else:
        gameover()

def monkeywin():
    print("       __          ")
    print("  w  c(..)o   (      ")
    print("   \__(-)    __)    ")
    print("       /\   (       ")
    print("      /(_)___)     ")
    print("     w /|           ")
    print("      | \  ")
    print("      m  m  ")
    print("")
    print("CONGRATULATIONS. You did not escape but you did become the monkey god!")
    # # THIS IS A WINNING PATH

    gameover()
# # GAME OVER SECTION END # #

# # INTRO AND NAME ENTRY SECTIONS START # #
def intro4():
    global player_char
    player_char = input("Make your choice [1/2/3/4]: ")
    if player_char == "1":
        player_char = "Big Strong Lumberjack"
        time.sleep(1.5)
        section1()
    elif player_char == "2":
        player_char = "Docile Businessman"
        time.sleep(1.5)
        section1()
    elif player_char == "3":
        player_char = "Ninja"
        time.sleep(1.5)
        section1()
    elif player_char =="4":
        time.sleep(1.5)
        monkeywin()
    else:
        intro4()

def intro3():
    print(" ")
    print("Select a character type")
    time.sleep(1)
    print("1: Big Strong Lumberjack")
    time.sleep(1)
    print("2: Docile Businessman")
    time.sleep(1)
    print("3: Ninja")
    time.sleep(1)
    print("4: Monkey God")
    time.sleep(1)
    print(" ")
    intro4()
    
def intro2_2():
    print(" ")
    answer = input(f"{name}? What a strange name, are you sure thats correct? [Y/N]: ").lower()
    if answer == "y" or answer =="yes":
        time.sleep(1.5)
        intro3()
    elif answer =="n" or answer =="no":
        time.sleep(1.5)
        intro2()
    else:
        intro2_2()
def intro2():
    global name
    print(" ")
    name = input("Please enter your name: ").capitalize()
    time.sleep(1.5)
    intro2_2()

def intro1():
    print(" ")
    answer = input("Do you wish to begin? [Y/N]: ").lower()
    if answer == "y" or answer =="yes":
        time.sleep(1.5)
        intro2()
    elif answer =="n" or answer =="no" :
        time.sleep(1.5)
        print("Your loss, have a nice day!")
    else:
        intro1()

def intro():
    print("Escape from the monkey world!")
    time.sleep(1.5)
    intro1()
# # INTRO AND NAME ENTRY SECTIONS END # #

intro() # # GAME START