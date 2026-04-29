# ProcessDesign_Task4_edu

• Overview 
This project implements a single‑cycle Boolean processor capable of executing a small instruction set:
- AND
- OR
- NOT (via ALU inversion flag)

Processor computes the Boolean expression:
    Y = A·B + C'·D

This is achieved by executing the following program:
    and t4, t0, t1    ; t4 = A & B
    andn t6, t2, t3    ; t6 = (~C) & D
    or  t0, t4, t6    ; t0 = t4 | t6

• File Structure
Task4Processor/
 instruction.py 
 register_file.py 
 alu.py 
 data_memory.py 
 control_unit.py 
 datapath.py 
 simulate.py 

• How to run
1. Install Python 3.8+  
2. Open a terminal inside the project folder  
3. Run:
   python simulate.py

• Example Usage
The processor accepts four Boolean inputs:
- A → t0  
- B → t1  
- C → t2  
- D → t3  

The inverted value of C (handled by the ALU inversion flag when executing ANDN) is preloaded into t5.


• Output Includes 
- Instruction executed  
- ALU operation  
- Register values  
- Intermediate results  
- Final output Y  

