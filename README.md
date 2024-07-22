# AcceleratingCODEC

Instructions for simulation
- Click on the following hyperlink to download iVerilog https://bleyer.org/icarus/
- Download the latest version available.
- Once downloaded, open command prompt and type `iverilog` to verify the installation.
- `cd` into `Atari2600_TIA` folder, and run `python3 instructions.py` on the command prompt. If you need to set any register values, you can do that by editing the following fields in the `instructions.py` script :
    1. audio_freq
    2. audio_ctrl
    3. audio_vol
- The resultant output bit stream appearing in the command prompt can be plugged into `play_audio.py` script to play the resultant audio.