import subprocess
import re

def write_opcode_input(file_path, opcode_val):
    with open(file_path, 'w') as file:
        file.write(f"{opcode_val:020b}\n")

def run_verilog_simulation():
    # Run the Verilog simulator (assuming Icarus Verilog here)
    subprocess.run(["iverilog", "-o", "testbench.vvp", "audioCircuitTB.sv", "audioCircuit.sv", "dividebyN.sv", "noise_tone_generator.sv"])
    subprocess.run(["vvp", "testbench.vvp"])

def replace_opcode_sequence(file_path, new_sequence):
    # Ensure the new_sequence is a valid 20-bit binary string
    if not re.fullmatch(r'[01]{20}', new_sequence):
        raise ValueError("New sequence must be a 20-bit binary string")

    # Read the Verilog code from the file
    with open(file_path, 'r') as file:
        code = file.read()

    # Define the pattern to match the line containing the binary sequence assignment
    pattern = r'opcode_mem\[0\] = 20\'b[01]{20};'

    # Define the replacement string with the new binary sequence
    replacement = f'opcode_mem[0] = 20\'b{new_sequence};'

    # Replace the old sequence with the new one
    modified_code = re.sub(pattern, replacement, code)

    # Write the modified code back to the same file
    with open(file_path, 'w') as file:
        file.write(modified_code)

def main():
    # Generate opcode input
    audio_freq = 0b00001  #  5-bit audio frequency
    audio_ctrl = 0b1000  #  4-bit audio control
    audio_vol = 0b1101  #  4-bit audio volume
    address = 0b110011  #  7-bit address

    # Format the fields into binary strings with leading zeros
    audio_freq_str = f"{audio_freq:05b}"
    audio_ctrl_str = f"{audio_ctrl:04b}"
    audio_vol_str = f"{audio_vol:04b}"
    address_str = f"{address:07b}"
    
    opcode_value = f"{audio_freq_str}{audio_ctrl_str}{audio_vol_str}{address_str}"

    file_path = 'audioCircuitTB.sv'  # Your input and output Verilog file
    new_sequence = str(opcode_value)  # Replace with your new 20-bit binary sequence
    print(new_sequence)

    replace_opcode_sequence(file_path, new_sequence)

    # Run Verilog simulation
    run_verilog_simulation()

if __name__ == "__main__":
    main()