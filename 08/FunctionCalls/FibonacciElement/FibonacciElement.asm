    @256
    D=A
    @SP
    M=D
    @Sys$RET1
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @0
    D=A+D
    @SP
    A=M
    D=A-D
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    @Sys.init
    0;JMP
  (Sys$RET1)
(Sys.init)
    @4
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @Sys.init$RET2
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @1
    D=A+D
    @SP
    A=M
    D=A-D
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    @Main.fibonacci
    0;JMP
  (Sys.init$RET2)
  (Sys.init$WHILE)
    @Sys.init$WHILE
    0;JMP
(Main.fibonacci)
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
    @2
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
    @Main.fibonacci$RIGHTLT1
    D;JLT
    @SP
    A=M
    M=0
    @Main.fibonacci$WHATEVERLT1
    0;JMP
  (Main.fibonacci$RIGHTLT1)
    @SP
    A=M
    M=-1
    @Main.fibonacci$WHATEVERLT1
    0;JMP
  (Main.fibonacci$WHATEVERLT1)
    @SP
    M=M+1
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @Main.fibonacci$IF_TRUE
    D;JNE
    @Main.fibonacci$IF_FALSE
    0;JMP
  (Main.fibonacci$IF_TRUE)
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
    @LCL
    D=M
    @R13
    M=D
    @R13
    D=M
    @5
    D=D-A
    A=D
    D=M
    @R14
    M=D
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @ARG
    A=M
    M=D
    @ARG
    D=M
    @SP
    M=D+1
    @R13
    D=M
    @1
    D=D-A
    A=D
    D=M
    @THAT
    M=D
    @R13
    D=M
    @2
    D=D-A
    A=D
    D=M
    @THIS
    M=D
    @R13
    D=M
    @3
    D=D-A
    A=D
    D=M
    @ARG
    M=D
    @R13
    D=M
    @4
    D=D-A
    A=D
    D=M
    @LCL
    M=D
    @R14
    A=M
    0;JMP
  (Main.fibonacci$IF_FALSE)
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
    @2
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
    @Main.fibonacci$RET3
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @1
    D=A+D
    @SP
    A=M
    D=A-D
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    @Main.fibonacci
    0;JMP
  (Main.fibonacci$RET3)
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
    @Main.fibonacci$RET4
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @1
    D=A+D
    @SP
    A=M
    D=A-D
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    @Main.fibonacci
    0;JMP
  (Main.fibonacci$RET4)
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
    @LCL
    D=M
    @R13
    M=D
    @R13
    D=M
    @5
    D=D-A
    A=D
    D=M
    @R14
    M=D
    @SP
    M=M-1
    @SP
    A=M
    D=M
    @ARG
    A=M
    M=D
    @ARG
    D=M
    @SP
    M=D+1
    @R13
    D=M
    @1
    D=D-A
    A=D
    D=M
    @THAT
    M=D
    @R13
    D=M
    @2
    D=D-A
    A=D
    D=M
    @THIS
    M=D
    @R13
    D=M
    @3
    D=D-A
    A=D
    D=M
    @ARG
    M=D
    @R13
    D=M
    @4
    D=D-A
    A=D
    D=M
    @LCL
    M=D
    @R14
    A=M
    0;JMP