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


# Consoles
- 2nd Gen Consoles
    - Atari 2600 TIA (1977)
- 3rd Gen Consoles
    - Sega 1000 (1983)
    - NES (1986)
- 4th Gen Consoles
    - SNES (1991)
- 5th Gen Consoles
    - PS-1 (1995)
- Universal Audio Architecture
    - References
        1. https://support.microsoft.com/en-us/topic/universal-audio-architecture-uaa-high-definition-audio-class-driver-available-for-windows-server-2003-windows-xp-and-window-2000-09fd84f2-b47b-909f-5659-4caf819395b9

        2. https://en.wikipedia.org/wiki/Universal_Audio_Architecture

        3. https://en.wikipedia.org/wiki/Technical_features_new_to_Windows_Vista#Audio_stack_architecture