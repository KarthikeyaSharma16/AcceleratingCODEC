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
        $display("opcode_mem : %0b", opcode_mem[0]);
        opcode = opcode_mem[0];
        $display("Opcode : %0b", opcode);
        #500;
        $display("At time %0t, shift register value: %b", $time, shiftReg);
        $finish();
    end
endmodule