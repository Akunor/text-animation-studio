import time
import sys
from colorama import Fore, Back, Style, init
from letters import combine_letters

# Initialize colorama for Windows compatibility
init(autoreset=True)

test_frames = [
    ((Fore.YELLOW + combine_letters("Hi!", spacing=1)), 2),
    
    ((Fore.GREEN + combine_letters("My name is Akunor.", spacing=1)), 2),
    
    ((Fore.MAGENTA + combine_letters("I am a member...", spacing=1)), 1),

    ((Fore.MAGENTA + combine_letters("of GitHub!", spacing=1)), 2),
]

def clear():
    # ANSI clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def display_frame(frame):
    clear()
    # Write the frame content without print() to avoid extra newlines
    sys.stdout.write(frame[0])
    sys.stdout.flush()

def play_animation(frames):
    try:
        while True:
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            
            for frame in frames:
                display_frame(frame)
                if frame[1] > 0:
                    time.sleep(frame[1])
                else:
                    time.sleep(1)
                
    except KeyboardInterrupt:
        clear()
        sys.stdout.write(Fore.GREEN + "Bye!" + Style.RESET_ALL + "\n")
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    play_animation(test_frames)