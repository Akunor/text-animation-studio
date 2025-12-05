from colorama import Fore, Back, Style, init
from letters import combine_letters
from display import play_animation

# Initialize colorama for Windows compatibility
init(autoreset=True)

thank_you_frames = [
    ((Fore.BLUE + combine_letters("THANK YOU!", spacing=1)), 1.5),
    ((Fore.MAGENTA + combine_letters("FOR WATCHING!", spacing=1)), 1.5),
]

if __name__ == "__main__":    
    play_animation(thank_you_frames, loop=True)