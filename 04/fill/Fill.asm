// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

	// Setup variables
	// Store the beginning address of the screen memory map in the addr variable
	@SCREEN
	D = A
	@addr 
	M = D

    
      (LOOP1)
	// Check the status of the keyboard keys
	// If keyboard value is zero go to loop, go to the loop to fill the screen
	// Else start again
	// Get KBD value in D
	@KBD
	D = M
	// If D == 0, goto loop3, else continue
	@PART1
	D;JEQ
	@PART2
	D;JNE
	
	      (PART1)
		// Initialize the variable i to 0
		@i
		M = 0

		// Initialize the variable n to the height in term of pixels of the screen
		@8192
		D = A
		@n
		M = D

	      (LOOP2)
		// If i == n, goto loop1
		@i
		D = M
		@n
		D = D - M
		@LOOP1
		D;JEQ
		
		// RAM[addr + i] = 0
		@addr
		D = M
		@i
		A = D + M
		M = 0

	
		// i++
		@i
		M = M + 1

		@LOOP2
		0;JMP

	
	      (PART2)
		// Initialize the variable i to 0
		@i
		M = 0

		// Initialize the variable n to the height in term of pixels of the screen
		@8192
		D = A
		@n
		M = D

	      (LOOP3)
		// If i == n, goto loop1
		@i
		D = M
		@n
		D = D - M
		@LOOP1
		D;JEQ
		
		// RAM[addr + i] = -1
		@addr
		D = M
		@i
		A = D + M
		M = -1

	
		// i++
		@i
		M = M + 1

		@LOOP3
		0;JMP
