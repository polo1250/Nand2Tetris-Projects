    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @0
    D=A
    @LCL
    A=M
    D=D+A
    @addr
    M=D
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @addr
    A=M
    M=D
  (LOOP_START)
    @0
    D=A
    @ARG
    A=M
    D=D+A
    @addr
    M=D
    @addr
    A=M
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @0
    D=A
    @LCL
    A=M
    D=D+A
    @addr
    M=D
    @addr
    A=M
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @SP
    M=M-1
    @SP
    A=M
    D=D+M
    M=D
    @SP
    M=M+1
    @0
    D=A
    @LCL
    A=M
    D=D+A
    @addr
    M=D
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @addr
    A=M
    M=D
    @0
    D=A
    @ARG
    A=M
    D=D+A
    @addr
    M=D
    @addr
    A=M
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @1
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @SP
    M=M-1
    @SP
    A=M
    D=M-D
    M=D
    @SP
    M=M+1
    @0
    D=A
    @ARG
    A=M
    D=D+A
    @addr
    M=D
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @addr
    A=M
    M=D
    @0
    D=A
    @ARG
    A=M
    D=D+A
    @addr
    M=D
    @addr
    A=M
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @LOOP_START
    D;JNE
    @0
    D=A
    @LCL
    A=M
    D=D+A
    @addr
    M=D
    @addr
    A=M
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
