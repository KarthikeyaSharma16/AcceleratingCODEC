module audioCircuit (
    input [19:0] opcode,
    input clk,
    output [8:0] shiftReg
);
    wire d_clk;

    // Instantiate internal modules
    dividebyN d (
        .audf(opcode[19:15]),  // Match port name
        .clk(clk),
        .d_clk(d_clk)
    );

    noise_tone_generator n (
        .clk(d_clk),
        .audc(opcode[14:11]),  // Match port name
        .shift_reg(shiftReg)  // Match port name
    );

endmodule
