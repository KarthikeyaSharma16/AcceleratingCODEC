module noise_tone_generator (
    input clk,
    input [3:0] audc,
    output reg [8:0] shift_reg
);
    wire feedback;
    reg [15:0] enable;

    initial begin
        shift_reg = 9'b101011010; 
    end

    // 4x16 Decoder to determine feedback enable signals
    always @(*) begin
        enable = 16'b0;
        if (audc < 10)
            enable[audc] = 1'b1;
        else
            enable[audc] = 1'b0;
    end

    // Generate feedback signal
    assign feedback = ^(shift_reg & enable[8:0]);  

    always @(posedge clk) begin
        shift_reg <= {feedback, shift_reg[8:1]};
    end
endmodule
