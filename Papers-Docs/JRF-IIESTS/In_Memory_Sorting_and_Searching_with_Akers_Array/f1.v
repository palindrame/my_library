module f1(
    input x,
    input y,
    input z,
    output f
);

    // implements: z'x + zy
    assign f = ( ~z & x ) | ( z & y );

endmodule
