import time
import sys
import threading
from colorama import Fore, Back, Style, init
from letters import combine_letters

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Audio support - use built-in winsound on Windows, or try other methods
AUDIO_AVAILABLE = False
audio_play_function = None

try:
    import winsound
    AUDIO_AVAILABLE = True
    audio_play_function = 'winsound'
except ImportError:
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        AUDIO_AVAILABLE = True
        audio_play_function = 'pydub'
    except ImportError:
        try:
            import sounddevice as sd
            import soundfile as sf
            AUDIO_AVAILABLE = True
            audio_play_function = 'sounddevice'
        except ImportError:
            AUDIO_AVAILABLE = False

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

def calculate_frame_timings_from_audio(audio_file, num_frames):
    if not AUDIO_AVAILABLE:
        print("Warning: Audio library not available. Cannot calculate audio duration.")
        return None
    
    try:
        # For WAV files, use wave module (built-in)
        if audio_file.lower().endswith('.wav'):
            import wave
            with wave.open(audio_file, 'r') as wav_file:
                frames = wav_file.getnframes()
                sample_rate = wav_file.getframerate()
                duration = frames / float(sample_rate)
                frame_duration = duration / num_frames
                return frame_duration
        
        # For MP3 files, try pydub
        elif audio_file.lower().endswith('.mp3'):
            try:
                from pydub import AudioSegment
                audio = AudioSegment.from_mp3(audio_file)
                duration = len(audio) / 1000.0  # pydub returns duration in milliseconds
                frame_duration = duration / num_frames
                return frame_duration
            except ImportError:
                print("Warning: pydub not installed. Cannot get MP3 duration.")
                print("Install with: pip install pydub")
                return None
        
        else:
            print(f"Warning: Unsupported audio format. Use WAV or MP3.")
            return None
            
    except Exception as e:
        print(f"Error calculating audio duration: {e}")
        return None

def play_audio_file(audio_file):
    """Play audio file using available method"""
    if audio_play_function == 'winsound':
        # winsound only supports WAV files
        if not audio_file.lower().endswith('.wav'):
            raise ValueError("winsound only supports WAV files. Please convert your audio to WAV format.")
        # Calculate duration first
        import wave
        with wave.open(audio_file, 'r') as wav_file:
            frames = wav_file.getnframes()
            sample_rate = wav_file.getframerate()
            duration = frames / float(sample_rate)
        # Play sound asynchronously and wait for duration
        winsound.PlaySound(audio_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(duration)
        # Stop the sound
        winsound.PlaySound(None, winsound.SND_PURGE)
    elif audio_play_function == 'pydub':
        from pydub import AudioSegment
        from pydub.playback import play
        if audio_file.lower().endswith('.mp3'):
            audio = AudioSegment.from_mp3(audio_file)
        elif audio_file.lower().endswith('.wav'):
            audio = AudioSegment.from_wav(audio_file)
        else:
            raise ValueError(f"Unsupported format. Use WAV or MP3.")
        play(audio)
    elif audio_play_function == 'sounddevice':
        data, samplerate = sf.read(audio_file)
        sd.play(data, samplerate)
        sd.wait()

def play_animation(frames, audio_file=None, loop=True):
    # Initialize and play audio if provided
    audio_thread = None
    audio_stop_event = None
    
    if audio_file and AUDIO_AVAILABLE:
        try:
            audio_stop_event = threading.Event()
            
            def play_audio_loop():
                """Play audio in a loop until stopped"""
                while not audio_stop_event.is_set():
                    try:
                        play_audio_file(audio_file)
                        # If we get here, audio finished. If looping, play again
                        if not loop:
                            break
                    except Exception as e:
                        if not audio_stop_event.is_set():
                            print(f"Audio playback error: {e}")
                        break
            
            audio_thread = threading.Thread(target=play_audio_loop, daemon=True)
            audio_thread.start()
            print(f"Playing audio: {audio_file}")
            time.sleep(0.3)  # Small delay to let audio start
        except Exception as e:
            print(f"Warning: Could not play audio file '{audio_file}': {e}")
            print("Continuing without audio...")
    elif audio_file and not AUDIO_AVAILABLE:
        print("Warning: No audio library available.")
        print("On Windows, WAV files work automatically with built-in winsound.")
        print("For MP3 support, install: pip install pydub")
        print("Continuing without audio...")
    
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
        if audio_stop_event:
            audio_stop_event.set()
        clear()
        sys.stdout.write(Fore.GREEN + "Bye!" + Style.RESET_ALL + "\n")
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    play_animation(test_frames)