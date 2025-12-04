import time
import sys
from colorama import Fore, Back, Style, init
from letters import combine_letters

# Initialize colorama for Windows compatibility
init(autoreset=True)

frames = [    
    # Frame 2: HI! in yellow (slightly different)
    [(Fore.YELLOW + combine_letters("Hi!", spacing=1)), 2],
    
    # Frame 3: My name is...
    [(Fore.GREEN + combine_letters("My name is Sam.", spacing=1)), 2],
    
    # Frame 5a: I am a...
    [(Fore.MAGENTA + combine_letters("I am a student...", spacing=1)), 1],

    # Frame 5b: student at...
    [(Fore.MAGENTA + combine_letters("at the university...", spacing=1)), 1],

    # Frame 5c: the
    [(Fore.MAGENTA + combine_letters("of Oxford!", spacing=1)), 2],
]

def clear():
    # ANSI clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def display_frame(frame):
    """Display a frame without adding extra newlines"""
    clear()
    # Write the frame content without print() to avoid extra newlines
    sys.stdout.write(frame[0])
    sys.stdout.flush()

try:
    while True:
        # Hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        
        for frame in frames:
            display_frame(frame)
            if frame[1] > 0:
                time.sleep(frame[1])  # frame delay (slightly longer for readability)
            else:
                time.sleep(1)
            
except KeyboardInterrupt:
    clear()
    sys.stdout.write(Fore.GREEN + "Bye!" + Style.RESET_ALL + "\n")
    # Show cursor again
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
