import platform
import subprocess
import sys

def install_ffmpeg():
    system = platform.system()

    if system == "Windows":
        print("Installing ffmpeg on Windows...")
        subprocess.run(["pip", "install", "ffmpeg-python"])  
        print("ffmpeg installation completed.")
    elif system == "Darwin": 
        print("Installing ffmpeg on macOS...")
        subprocess.run(["brew", "install", "ffmpeg"])  
        print("ffmpeg installation completed.")
    elif system == "Linux":
        print("Installing ffmpeg on Linux...")
        subprocess.run(["apt-get", "install", "-y", "ffmpeg"])  
        print("ffmpeg installation completed.")
    else:
        print("Unsupported operating system.")
        sys.exit(1)

install_ffmpeg()
