import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

def create_cut_circuit():   
    qreg_q = QuantumRegister(3, 'q')
    circuit = QuantumCircuit(qreg_q)

    circuit.x(qreg_q[0])
    circuit.barrier()
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.x(qreg_q[1])
    circuit.cx(qreg_q[1], qreg_q[2])
    circuit.x(qreg_q[1])
    circuit.barrier()
    return circuit