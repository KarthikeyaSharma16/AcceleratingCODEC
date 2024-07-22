import subprocess

def write_opcode_input(file_path, opcode_val):
    with open(file_path, 'w') as file:
        file.write(f"{opcode_val:020b}\n")

def run_verilog_simulation():
    # Run the Verilog simulator (assuming Icarus Verilog here)
    subprocess.run(["iverilog", "-o", "testbench.vvp", "audioCircuitTB.sv", "audioCircuit.sv", "dividebyN.sv", "noise_tone_generator.sv"])
    subprocess.run(["vvp", "testbench.vvp"])

def main():
    # Generate opcode input
    audio_freq = 0b00101  #  5-bit audio frequency
    audio_ctrl = 0b1000  #  4-bit audio control
    audio_vol = 0b1101  #  4-bit audio volume
    address = 0b110011  #  7-bit address
    opcode_value = (audio_freq << 15) | (audio_ctrl << 11) | (audio_vol << 7) | address
    
    write_opcode_input("opcode.txt", opcode_value)
    
    # Run Verilog simulation
    run_verilog_simulation()

if __name__ == "__main__":
    main()