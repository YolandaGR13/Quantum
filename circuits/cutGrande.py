import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

def create_cut_circuit():   
    q_reg = QuantumRegister(7,'q')
    circuit = QuantumCircuit(q_reg)
    #la inicializacion de los registros debe hacerse fuera del circuito
    #circuit.reset(q_reg[1])
    #circuit.reset(q_reg[2])
    #circuit.reset(q_reg[3])
    #circuit.reset(q_reg[4])
    #circuit.reset(q_reg[5])
    #circuit.reset(q_reg[6])
    #circuit.reset(q_reg[0])

    circuit.swap(q_reg[0], q_reg[4])
    circuit.swap(q_reg[2], q_reg[5])
    circuit.barrier(q_reg)
    circuit.swap(q_reg[0], q_reg[1])
    circuit.swap(q_reg[1], q_reg[3])
    circuit.barrier(q_reg)

#first 2 qbit adder starts
    circuit.ccx(q_reg[0],q_reg[1],q_reg[3])
    circuit.cx(q_reg[0],q_reg[1])
    circuit.ccx(q_reg[1],q_reg[2], q_reg[3])
    circuit.cx(q_reg[1], q_reg[2])
    circuit.cx(q_reg[0],q_reg[1])
#first 2 qbit finish

    circuit.barrier(q_reg)
    circuit.swap(q_reg[4],q_reg[5])
    circuit.swap(q_reg[3],q_reg[5])

#second 2 qbit adder starts
    circuit.ccx(q_reg[3],q_reg[4],q_reg[6])
    circuit.cx(q_reg[3],q_reg[4])
    circuit.ccx(q_reg[4],q_reg[5], q_reg[6])
    circuit.cx(q_reg[4], q_reg[5])
    circuit.cx(q_reg[3],q_reg[4])
#first 2 qbit finish

    circuit.barrier(q_reg)
    circuit.swap(q_reg[2],q_reg[6])
    circuit.swap(q_reg[2],q_reg[4])
    circuit.swap(q_reg[0],q_reg[3])
    circuit.swap(q_reg[1],q_reg[3])
    circuit.barrier(q_reg)
    #quitamos este swap para que sea little endian 
    #circuit.swap(q_reg[4],q_reg[6])
    

    return circuit