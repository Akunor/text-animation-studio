# Terminal ASCII Animation Studio

A Python toolkit for creating beautiful terminal-based ASCII art animations, perfect for intro videos, presentations, or creative terminal displays.

## Features

- **ASCII Letter Templates**: Pre-built uppercase, lowercase, numbers, and punctuation characters
- **Easy Animation System**: Simple frame-based animation with customizable timing
- **Color Support**: Full colorama integration for colorful terminal displays
- **Smart Letter Combining**: Automatically combines letters with proper alignment and spacing
- **Audio Support**: Optional audio playback synchronized with animations
- **Cross-platform**: Works on Windows, macOS, and Linux terminals

## What It Does

This toolkit allows you to create simple, smooth ASCII text animations directly in your terminal.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Akunor/text-animation-studio
cd animation-intro-video
```

### 2. Install Dependencies

```bash
pip install colorama
```

For audio support:
- **Windows**: WAV files work automatically using built-in `winsound` (no installation needed!)
- **MP3 support** (optional, cross-platform): 
  ```bash
  pip install pydub
  ```
  Note: pydub requires ffmpeg for MP3 support. Install ffmpeg separately.

### 3. Create Your Animation Script

Create a new Python file (e.g., `my_animation.py`) and set it up:

```python
from colorama import Fore, Style, init
from letters import combine_letters
from display import play_animation

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Define your frames
# Each frame is a tuple: (content, duration_in_seconds)
my_frames = [
    ((Fore.CYAN + combine_letters("Hello!", spacing=1)), 2),
    ((Fore.GREEN + combine_letters("My name is", spacing=1)), 2),
    ((Fore.YELLOW + combine_letters("Akunor.", spacing=1)), 3),
    ((Fore.MAGENTA + combine_letters("Welcome!", spacing=1)), 2),
]

if __name__ == "__main__":
    play_animation(my_frames)
```

### 4. Run Your Script

```bash
python my_animation.py
```

Press `Ctrl+C` to stop the animation.

## Usage Details

### Creating Frames

Each frame is a tuple containing:
1. **Content**: The ASCII art text (can include colorama colors)
2. **Duration**: How long to display the frame in seconds

```python
((Fore.CYAN + combine_letters("Text here", spacing=1)), 2)
```

### Using `combine_letters()`

The `combine_letters()` function converts text into ASCII art:

```python
combine_letters("Hello", spacing=1)  # spacing is the number of spaces between letters
```

**Supported Characters:**
- Uppercase letters: A-Z
- Lowercase letters: a-z
- Numbers: 0-9
- Punctuation: `! ? . , ' : ; - _` and space

### Adding Colors

Use colorama's `Fore` for text colors:

```python
from colorama import Fore, Style

Fore.CYAN    # Cyan text
Fore.GREEN   # Green text
Fore.YELLOW  # Yellow text
Fore.MAGENTA # Magenta text
Fore.BLUE    # Blue text
Fore.RED     # Red text
Fore.WHITE   # White text

Style.BRIGHT # Make text bright/bold
```

### Example: Full Animation

```python
from colorama import Fore, Style, init
from letters import combine_letters
from display import play_animation

init(autoreset=True)

frames = [
    # Frame 1: Greeting
    ((Fore.CYAN + combine_letters("Hi!", spacing=1)), 1.5),
    
    # Frame 2: Introduction
    ((Fore.GREEN + combine_letters("I'm Sam", spacing=1)), 2),
    
    # Frame 3: More info
    ((Fore.YELLOW + combine_letters("A student", spacing=1)), 2),
    
    # Frame 4: Final message
    ((Fore.MAGENTA + Style.BRIGHT + combine_letters("Thanks!", spacing=1)), 2),
]

if __name__ == "__main__":
    play_animation(frames)
```

### Adding Audio to Your Animation

You can add background audio to your animation for a more immersive experience:

```python
from colorama import Fore, Style, init
from letters import combine_letters
from display import play_animation

init(autoreset=True)

frames = [
    ((Fore.CYAN + combine_letters("Hi!", spacing=1)), 2),
    ((Fore.GREEN + combine_letters("My name is Sam", spacing=1)), 2),
    ((Fore.YELLOW + combine_letters("Welcome!", spacing=1)), 2),
]

if __name__ == "__main__":
    # Add audio file path (supports mp3, wav, ogg)
    audio_file = "path/to/your/audio.mp3"  # Set to None to disable audio
    play_animation(frames, audio_file=audio_file, loop=True)
```

**Audio Features:**
- **Windows**: Built-in support for WAV files (no installation needed!)
- **MP3 support**: Install pydub for MP3 playback (requires ffmpeg)
- Audio loops automatically with the animation (can be disabled)
- Gracefully handles missing audio files or unsupported formats
- Audio stops when animation is interrupted (Ctrl+C)

**Note**: On Windows, convert MP3 files to WAV format for easiest setup (no additional packages needed). You can use online converters or tools like Audacity.

**Syncing Frames to Audio:**

To calculate equal frame timings based on audio duration:

```python
from display import calculate_frame_timings_from_audio

# Calculate duration per frame for equal distribution
audio_file = "your_audio.mp3"
num_frames = 5
frame_duration = calculate_frame_timings_from_audio(audio_file, num_frames)

if frame_duration:
    print(f"Each frame should be {frame_duration:.2f} seconds")
    # Use this duration for all frames to sync with audio
```

## File Structure

```
animation-intro-video/
├── letters.py      # Letter templates and combine_letters() function
├── display.py      # Animation display functions (play_animation)
└── README.md       # This file
```

## Tips

- **Line Length**: Be aware that if any one frame is too long for your terminal display it will break, so avoid putting long lines on a single frame.
- **Spacing**: Adjust the `spacing` parameter in `combine_letters()` to control letter spacing (default is 1)
- **Timing**: Experiment with frame durations to find the right pacing for your animation
- **Colors**: Mix and match colors for visual appeal
- **Screen Recording**: Use screen recording software to capture your animations for videos

## Requirements

- Python 3.6+
- colorama (install with `pip install colorama`)
- **Audio (Windows)**: Built-in `winsound` supports WAV files - no installation needed!
- **Audio (MP3 support)**: pydub (optional - install with `pip install pydub`, requires ffmpeg)

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork, modify, and create your own animations! If you create something cool, consider sharing it.

---

**Enjoy creating your terminal animations!**

