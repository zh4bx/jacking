import time
import itertools
import os
from colorama import Fore, Style, init
import pyfiglet
import webbrowser
import subprocess
                                                           # Initialize colorama                                      init()

# Define colors                                            colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

# Create an infinite iterator for the colors
color_cycle = itertools.cycle(colors)

# Create large text using pyfiglet with color
large_text = pyfiglet.figlet_format("zh4bx", font="starwars")

def clear_screen():
    # Clear command for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def blink_text(text, options, interval=0.5):
    try:
        # Clear the screen
        clear_screen()

        # Print the large text for 5 seconds
        print(next(color_cycle) + text)
        time.sleep(5)

        # Clear the screen again
        clear_screen()

        # Print the options in rotating colors
        for option in options.split("\n"):
            print(next(color_cycle) + option)

        while True:
            # Get user input for option selection
            selection = input("enter (1, 2, 3, 4): ")

            # Perform actions based on user selection
            if selection == '1':
                print("Executing Instagram jacking without account")
                subprocess.run(["python", "without.py"])

            elif selection == '2':
                print("Executing Instagram jacking with account")
                subprocess.run(["python", "with.py"])

            elif selection == '3':
                print("Redirecting to email validator website...")
                # Open the website for email validation
                webbrowser.open("https://email-checker.net/")

            elif selection == '4':
                print("Running Instagram reset script...")
                # Execute the reset.py script
                subprocess.run(["python", "reset.py"])

            else:
                print("Invalid selection. Please enter 1, 2, 3, or 4.")

    except KeyboardInterrupt:
        # Handle the Ctrl+C to exit the loop
        clear_screen()
        print(f"{Style.RESET_ALL}Blinking stopped.")

# Define the options with color
options_text = f"{Fore.RED}1. Instagram jacking without pass\n{Fore.GREEN}2. Instagram jacking with pass\n{Fore.BLUE}3. Email validator\n{Fore.YELLOW}4. Instagram reset mail\n"

# Call the function with the desired large text, options, and interval
blink_text(large_text, options_text, interval=0.5)
