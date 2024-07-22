import numpy as np
import sounddevice as sd

def binary_to_int(binary_str):
    return int(binary_str, 2)

# Generate a waveform based on the DAC value
def generate_audio_signal(dac_value, sample_rate=44100, duration=2.0):
    # DAC value ranges from 0 to 511 for 9-bit data
    if not (0 <= dac_value <= 511):
        raise ValueError("DAC value must be between 0 and 511")

    # Create a time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Create a waveform based on the DAC value
    # Convert DAC value to a waveform amplitude
    amplitude = dac_value / 511.0 * 0.5  # Scale to range [0, 0.5] to avoid clipping
    frequency = 440  # Example frequency (A4 pitch), you can adjust this

    # Generate the waveform
    waveform = amplitude * np.sin(2 * np.pi * frequency * t)

    return waveform

# Function to play audio
def play_audio(waveform, sample_rate=44100):
    sd.play(waveform, samplerate=sample_rate)
    sd.wait()  # Wait until the sound has finished playing

if __name__ == "__main__":
    # Example 9-bit binary value
    binary_value = '101011010'  # Example 9-bit binary value

    # Convert binary to DAC value
    dac_value = binary_to_int(binary_value)

    # Generate and play audio signal
    audio_signal = generate_audio_signal(dac_value)
    play_audio(audio_signal)
