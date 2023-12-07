"""
Final Project: Text-based Adventure Game
===========================
Course:   CS 5001
Student:  Peihao Li
SEMESTER: Fall 2023
"""


import time


def setup_time_limit():
    """Sets up a 10-minute time limit for the game."""
    global start_time, time_limit
    start_time = time.time()
    time_limit = 600


def check_time_limit_exceeded():
    """Checks if the time limit for the game is exceeded."""
    return time.time() - start_time > time_limit


def intro():
    """Displays the introductory text for the game."""
    print("Welcome to the Detective Conan Adventure Game!")
    print("In this game, you will take on the role of Shinichi Kudo, a brilliant high school detective.")
    print("Note: This is a detective puzzle game where you have to find the murderer in 10 minutes.")
    input("Press Enter to start your adventure...")
    print("\nYou're in Tokyo, Japan. As a renowned detective, you solve mysteries with your keen observation and deduction skills.")
    print("But everything changes when a day at the amusement park leads to an unexpected turn of events...")
    input("Press Enter to continue...")


def main_characters():
    """Displays the main characters of the game."""
    print("\nMain Characters:")
    print("1. Shinichi Kudo/Conan Edogawa: A high school detective.")
    print("2. Ran Mouri: Your childhood friend and skilled in karate.")
    print("3. Kogoro Mouri: Ran's father and a private detective, often clueless about cases.")
    print("4. Three Kids: A group of elementary school students.")
    print("5. The Black Organization: A mysterious and dangerous group.")
    input("Press Enter to begin your investigation...")


def amusement_park():
    """Displays a description of the park."""
    print("\nYou and Ran, your very good friend, have a special day planned.")
    print("You've promised Ran to accompany her to the famous Dorobija Amusement Park.")
    print("Today, you've arrived at the bustling, colorful park, filled with the sounds of laughter and excitement.")
    input("Press Enter to continue...")


def roller_coaster_choice():
    """Allow the player to choose whether or not to track the three children."""
    print("\nYou and Ran are about to enter the roller coaster queue.")
    print("Suddenly, you notice three kids sneaking through a small hole next to the entrance, leading to the middle of the roller coaster tunnel.")
    
    print("1. Track three kids.")
    print("2. Continue to line up with Ran.")
    while True:
        choice = input("What do you choose to do? (Type 1 or 2) ")
        if choice == "1":
            track_kids()
            break
        elif choice == "2":
            meet_hitomi()
            break
        else:
            print("\nInvalid choice. Please type 1 or 2.")


def track_kids():
    """Track down three children and collect clues."""
    print("\nYou decide to track down the three children...")
    print("After a brief conversation, you learn they snuck in because they couldn't afford the tickets but wanted to ride the roller coaster.")
    print("Understanding their situation, you return to the entrance to meet Ran.")
    add_clue("Clue 1", "Three kids enter a roller coaster tunnel.")
    meet_hitomi()


def meet_hitomi():
    """Show new characters."""
    print("\nWhile lining up with Ran, you meet a girl named Hitomi and her friends.")
    handshake_with_hitomi()


def handshake_with_hitomi():
    """Communicate with Hitomi."""
    print("\nYou shake hands with Hitomi and introduce yourselves.")
    guess_occupation()


def guess_occupation():
    """Guess Hitomi's occupation."""
    while True:
        print("\nYou notice that Hitomi was wearing a pearl necklace and she's hands are very strong and have calloused palms.")
        choice = input("Guess Hitomi's occupation: 1. Waitress 2. Gymnast 3. Physical Education Teacher: ")
        if choice == "2":
            print("\nYou deduce that Hitomi is likely a gymnast.")
            add_clue("Clue 2", "Hitomi is a gymnast.")
            break
        elif choice in ["1", "3"]:
            print("\nThat doesn't seem right. Let's think again.")
        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.")

clues = {}


def add_clue(clue_number, clue_description):
    """Adding clues."""
    global clues
    clues[clue_number] = clue_description


def show_clues():
    """Displays the clues that have been collected."""
    if not clues:
        print("\nNo clues collected yet.")
    else:
        print("\nClues Collected:")
        for clue_number, clue_description in clues.items():
            print(f"{clue_number}: {clue_description}")


def roller_coaster_seating():
    """Ride the roller coaster."""
    print("\nYou and Ran meet a couple, Kishida and Aiko, who also know Hitomi.")
    print("You notice that Hitomi and her friend are sitting in the first row, while your and Ran's seats are in the second row, and Kishida and Aiko's seats are in the third row.")
    choice = input("1. Switch places with Hitomi. 2. Go straight to the roller coaster and sit in the second row: ")

    if choice == "1":
        print("\nHitomi mentions that she and her friend also want to sit in the first row, so you and Ran don't switch seats.")
    elif choice == "2":
        print("\nYou decide to go straight to the roller coaster and sit in your assigned seats in the second row.")
    else:
        print("\nInvalid choice. Please type 1 or 2.")
        roller_coaster_seating()
    if handle_input():
        return


def roller_coaster_incident():
    """The man in black enters."""
    print("\nAs everyone is getting seated, two men dressed in black rush past, shouting 'Get out of the way!' and make their way to the last row.")
    print("One of them is carrying a silver-colored box. You and Ran take note of this unusual behavior.")

    print("\nAll the passengers, including you and Ran, are now seated, waiting for the roller coaster to start.")
    input("Press Enter as the roller coaster begins its journey...")
    if handle_input():
        return


seating_chart = {
    "1A": "Hitomi",
    "1B": "Hitomi's friend",
    "2A": "Shinichi (You)",
    "2B": "Ran",
    "3A": "Kishida",
    "3B": "Aiko",
    "4A": "Man in black 1",
    "4B": "Man in black 2"
}


def show_seating_chart():
    """Display the seating chart."""
    print("\nRoller Coaster Seating Chart:")
    for seat, occupant in seating_chart.items():
        print(f"{seat}: {occupant}")


def roller_coaster_tunnel():
    """The roller coaster enters the tunnel."""
    print("\nAs the roller coaster plunges into a dark tunnel, you feel a drop of water on your face.")
    print("Thinking it's just dew from the cave, you don't pay it much mind.")
    print("Suddenly, three children shout as they pick up a pearl that had fallen in the tunnel.")
    add_clue("Clue 3", "Falling Pearl")
    input("Press Enter as the roller coaster exits the tunnel...")
    print("\nTo everyone's horror, as the roller coaster emerges from the tunnel, you discover that Mr. Kishida's head has been cut off.")
    if handle_input():
        return


def post_roller_coaster_incident():
    """After the murder."""
    print("\nThe police arrive, and everyone is escorted back to the entrance of the roller coaster.")
    post_incident_conversations()


def talk_to_three_kids():
    """Talking to three kids."""
    print("\nYou talk to the three kids.")
    print("They say, 'We picked up a few pearls that flew down in the roller coaster tunnel.'")
    add_clue("Clue 4", "Pearls found by kids in the tunnel.")


def talk_to_man_in_black():
    """Talking to man in black."""
    print("\nYou approach the men in black.")
    print("They say, 'It was just an unusual accident, we're not murderers, and we have urgent business that requires us to leave immediately.'")


def talk_to_aiko():
    """Talking to Aiko."""
    print("\nYou try to talk to Aiko.")
    print("Aiko has been crying and can't speak.")


def talk_to_hitomi():
    """Talking to Hitomi."""
    print("\nYou talk to Hitomi and her friends.")
    print("They say, 'We were sitting in the first row of the roller coaster and we don't know what happened in the tunnel'.")


def post_incident_conversations():
    """Allow the player to choose who to talk to."""
    while True:
        print("\nWho do you want to talk to?")
        print("1. The three kids")
        print("2. The man in black")
        print("3. Aiko")
        print("4. Hitomi and her friends")
        print("5. Done talking")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            talk_to_three_kids()
        elif choice == "2":
            talk_to_man_in_black()
        elif choice == "3":
            talk_to_aiko()
        elif choice == "4":
            talk_to_hitomi()
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please choose a number between 1 and 5.")

        if handle_input():
            continue


def discover_new_clues():
    """Gather new clues."""
    print("\nAfter your conversations, the police make two crucial discoveries:")
    print("1. A knife with blood stains is found in Aiko's handbag.")
    print("2. A treble hook attached to a thin wire is found in the roller coaster tunnel.")

    add_clue("Clue 4", "Knife with blood in Aiko's handbag")
    add_clue("Clue 5", "Treble Hook with thin wire in tunnel")

    print("\nThese clues are now added to your clue library.")
    input("Press Enter to continue the investigation...")


def final_judgment():
    """Choose the killer."""
    print("\nIt's time to pass judgment on the killer. Who do you think it is?")
    print("1. The man in black")
    print("2. Aiko")
    print("3. Hitomi")
    print("4. Hitomi's friend")
    choice = input("Make your choice (1-4): ")

    if choice == "1":
        print("The men in black were nervous and in a hurry to leave, but there's no actual evidence against them. You have let the real murderer go. Game over.")
        return False
    elif choice == "2":
        print("Despite the bloody knife in Aiko's handbag, there's no sufficient motive or evidence she could commit the murder. You have let the real murderer go. Game over.")
        return False
    elif choice == "3":
        print("Congratulations, your judgment is correct. The real murderer is Hitomi.")
        input("Press Enter to view the reasoning process.")
        reasoning_process()
        return True
    elif choice == "4":
        print("Hitomi's friend, being in seat 1B, couldn't have committed the murder without being detected. You have let the real murderer get away. Game over.")
        return False
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
        return final_judgment()    


def reasoning_process():
    """Show the reasoning process."""
    print("\nReasoning Process:")
    print("Hitomi used her handbag to pad her back before she got on the roller coaster, which ensured that the safety bar wouldn't lock up. After the safety bar was lowered, she had enough room to get out. The moment the roller coaster enters the tunnel, Hitomi climbs up and puts the thin wire rope with the hook around Kishida's neck. The hook was then thrown out at random so that it would hook onto the tracks of the roller coaster, and with the coaster's rapid speed, Kishida's head was cut off almost instantly. Since Hitomi was a gymnast, she had enough strength and flexibility to support her in doing so.")
    print("Due to the sudden movement of one's eyes from the outdoors into the dark tunnel, those around them were unable to see what was happening, and the loud noise of the roller coaster prevented bystanders from realizing that Hitomi was committing the crime. As for the motive, Hitomi and Kishida were lovers during their college days, and then Kishida broke up with Hitomi because of Aiko, which made Hitomi want to kill Kishida. As for the water droplets on your face, they are Hitomi's tears that she shed when she killed him.")
    input("Press Enter to conclude the game...")


def final_episode():
    """Tracking the Man in Black."""
    print("\nAs you conclude the case, you notice the two men in black leaving in a hurry.")
    print("1. Follow the men in black and see what they are going to do.")
    print("2. Continue the tour with Ran.")
    choice = input("What do you choose to do? (Type 1 or 2) ")

    if choice == "1":
        follow_men_in_black()
    elif choice == "2":
        continue_with_ran()
    else:
        print("\nInvalid choice. Please type 1 or 2.")
        final_episode()


def follow_men_in_black():
    """The results of tracking the man in black."""
    print("\nYou decide to follow the men in black. As you tail them, one of them suddenly turns, hiding in the shadows. Before you realize it, he knocks you out and gives you a pill. You feel hot and pass out...")
    print("The story will continue... stay tuned.")
    input("Press Enter to conclude the game...")


def continue_with_ran():
    """Continue touring the park."""
    print("\nChoosing not to dwell on the men in black, you continue your tour of the amusement park with Ran, enjoying the rest of your day.")
    print("The ending is: Game over.")
    input("Press Enter to conclude the game...")


def handle_input():
    """Allows players to view clues and seating charts."""
    while True:
        user_input = input("\nEnter a command ('clue', 'seat'), or press Enter to continue: ")
        if user_input.lower() == "clue":
            show_clues()
        elif user_input.lower() == "seat":
            show_seating_chart()
        elif user_input == "":
            return True
        else:
            print("\nInvalid command. Type 'clue', 'seat', or press Enter to continue.")  


def start_game():
    """Starts the Detective Conan Adventure Game."""
    setup_time_limit()
    intro()
    main_characters()
    amusement_park()
    roller_coaster_choice()
    roller_coaster_seating()
    roller_coaster_incident()
    roller_coaster_tunnel()
    post_roller_coaster_incident()
    post_incident_conversations()
    discover_new_clues()

    if final_judgment():
        final_episode()

    if check_time_limit_exceeded():
        print("Time's up! Game over.")
    else:
        print("Thank you for playing the Detective Conan Adventure Game!")


if __name__ == "__main__":
    start_game()
