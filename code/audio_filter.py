import os
import numpy as np
import librosa
import noisereduce as nr
import soundfile as sf
from pydub import AudioSegment

def load_audio(file_path, sr=16000):
    """Load audio and convert to mono with a target sample rate"""
    audio, _ = librosa.load(file_path, sr=sr, mono=True)
    return audio, sr

def reduce_noise(audio, sr):
    """Reduce background noise using noisereduce"""
    reduced_noise = nr.reduce_noise(y=audio, sr=sr)
    return reduced_noise

def apply_gain(audio, gain_db=10):
    """Apply gain in decibels to amplify the voice"""
    # Convert numpy to AudioSegment
    temp_path = "temp.wav"
    sf.write(temp_path, audio, 16000)
    audio_seg = AudioSegment.from_wav(temp_path)
    louder_audio = audio_seg + gain_db
    louder_audio.export(temp_path, format="wav")
    # Load back as numpy array
    clean_audio, _ = librosa.load(temp_path, sr=16000)
    os.remove(temp_path)
    return clean_audio

def save_audio(audio, sr, output_path):
    """Save the processed audio"""
    sf.write(output_path, audio, sr)

def process_audio(input_path, output_path, gain_db=10):
    print(f"Processing: {input_path}")
    audio, sr = load_audio(input_path)
    print("Reducing noise...")
    noise_reduced = reduce_noise(audio, sr)
    print(f"Applying {gain_db}dB gain to voice...")
    voice_amplified = apply_gain(noise_reduced, gain_db)
    print("Saving output...")
    save_audio(voice_amplified, sr, output_path)
    print(f"Done! Cleaned audio saved at: {output_path}")

if __name__ == "__main__":
    import argparse

    # parser = argparse.ArgumentParser(description="Clean and enhance voice in audio files.")
    # parser.add_argument("input", help="Input audio file path (wav or mp3)")
    # parser.add_argument("output", help="Output audio file path (wav)")
    # parser.add_argument("--gain", type=int, default=10, help="Gain in dB to apply to voice")

    # args = parser.parse_args()

    # process_audio(args.input, args.output, args.gain)


    INPUT_FILE = r'C:\Users\91930\Documents\Sound Recordings\user1.mp3'
    OUTPUT_FILE = r'C:\Users\91930\Documents\Sound Recordings\output.mp3'
    GAIN = 15
    process_audio(INPUT_FILE, OUTPUT_FILE, GAIN)