module dividebyN (
    input [4:0] audf,
    input clk,
    output reg d_clk
);
    reg [4:0] delayVal;

    initial begin
        d_clk = 0;
        delayVal = 0;
    end

    always @(posedge clk) begin
        if (delayVal == 0) begin
            delayVal = audf;
            d_clk = ~d_clk;
        end else begin
            delayVal -= 1;
        end
    end
endmodule
