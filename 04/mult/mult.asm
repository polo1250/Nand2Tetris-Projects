// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// The idea is to add R0(n) to itself R1(m) times, and store the result in R2 (sum) 

	//Initial Setup
	// set i = 0
	@i
	M=0

	// set m = R0
	@R0
	D=M
	@m
	M=D

	// set n = R1
	@R1
	D=M
	@n
	M=D

	// set sum = 0
	@sum
	M=0

     (LOOP)
	//Check if (i==n) goto END
	@i
	D=M
	@n
	D=D-M
	@TERM
	D;JEQ 

	//Add m to sum
	@m
	D=M
	@sum
	M=M+D
	
	//i++
	@i
	M=M+1

	@LOOP
	0;JMP

	//Store the value of sum in R2
     (TERM)
	@sum
	D=M
	@R2
	M=D
	@END
	0;JMP
	



     (END)
	@END
	0;JMP
