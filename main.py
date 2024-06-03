import time
import itertools
import os
from colorama import Fore, Style, init
import pyfiglet
import webbrowser
import subprocess

# Initialize colorama
init()

# Define colors
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

# Create an infinite iterator for the colors
color_cycle = itertools.cycle(colors)

# Create large text using pyfiglet with color
large_text = pyfiglet.figlet_format("zh4bx", font="starwars")
logo_text = pyfiglet.figlet_format("zh4bx jacking tool", font="slant")

def clear_screen():
    # Clear command for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def redirect_to_telegram():
    print("Redirecting to the Telegram channel...")
    webbrowser.open("https://t.me/zhtricks")

def blink_text(large_text, logo_text, options, interval=0.5):
    try:
        # Redirect to Telegram channel at the start
        redirect_to_telegram()
        time.sleep(3)  # Pause for 3 seconds to allow redirection

        # Clear the screen
        clear_screen()
        
        # Print the large text for 5 seconds
        print(next(color_cycle) + large_text)
        time.sleep(5)
        
        # Clear the screen again
        clear_screen()

        # Print the logo text with rotating colors
        print(next(color_cycle) + logo_text)
        
        # Print the options in rotating colors with good size
        for option in options.split("\n"):
            print(next(color_cycle) + option + Style.RESET_ALL)
        
        while True:
            # Get user input for option selection
            selection = input(f"{Fore.RED}{Style.BRIGHT}Enter(1, 2, 3, 4): {Style.RESET_ALL}")
            
            # Perform actions based on user selection
            if selection == '1':
                print("Executing Instagram jacking without account")
                subprocess.run(["python", "without.py"])
                
            elif selection == '2':
                print("Executing Instagram jacking with account")
                subprocess.run(["python", "with.py"])
                
            elif selection == '3':
                print("https://email-checker.net/")
                # Open the website for email validation
                webbrowser.open("https://email-checker.net/")
            
            elif selection == '4':
                print("Running Instagram reset script...")
                # Execute the reset.py script
                subprocess.run(["python", "reset.py"])
                
            else:
                print("Invalid selection")

    except KeyboardInterrupt:
        # Handle the Ctrl+C to exit the loop
        clear_screen()
        print(f"{Style.RESET_ALL}Blinking stopped.")

# Define the options with color and good size
options_text = f"""
{Fore.RED}1. Instagram jacking without account
{Fore.GREEN}2. Instagram jacking with account
{Fore.BLUE}3. Email validator
{Fore.YELLOW}4. Instagram reset mail
"""

# Call the function with the desired large text, logo, options, and interval
blink_text(large_text, logo_text, options_text, interval=0.5)
      
