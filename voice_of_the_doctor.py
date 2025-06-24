from gtts import gTTS
from pydub import AudioSegment
import platform
import subprocess
import os

def text_to_speech_with_gtts(input_text, output_filepath="final.mp3"):
    from gtts import gTTS
    from pydub import AudioSegment
    import platform
    import subprocess

    # Generate mp3 using gTTS
    tts = gTTS(text=input_text, lang='en', slow=False)
    tts.save(output_filepath)

    # Optional: Convert and play
    try:
        sound = AudioSegment.from_mp3(output_filepath)
        wav_path = "final.wav"
        sound.export(wav_path, format="wav")

        os_name = platform.system()
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
    except Exception as e:
        print(f"Error in conversion or playback: {e}")

    return output_filepath
