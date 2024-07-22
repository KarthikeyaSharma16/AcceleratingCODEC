`timescale 1us/1ps

module audioCircuitTB;
    reg [19:0] opcode_mem [0:0]; // Memory array with one element
    reg [19:0] opcode;
    reg clk;
    wire [8:0] shiftReg;

    audioCircuit uut (.clk(clk), .opcode(opcode), .shiftReg(shiftReg));

    initial begin
        clk = 0;
    end

    always #16.67 clk = ~clk;

    initial begin
        $readmemh("opcode.txt", opcode_mem);
        opcode = opcode_mem[0];
        #100;
        $display("At time %0t, shift register value: %b", $time, shiftReg);
        $finish();
    end
endmodule