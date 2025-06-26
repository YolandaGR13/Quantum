
from qiskit_ibm_runtime.fake_provider import FakeAlgiers, FakeAlmadenV2
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library.standard_gates import *
from qiskit.visualization import plot_histogram
from qiskit.quantum_info.operators import Operator
from math import pi
import numpy 
from qiskit.visualization import plot_state_city 
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import MCMT

#numpy.set_printoptions(threshold=sys.maxsize)
def create_cut_circuit():   
	qreg = QuantumRegister(4, 'q') 
	circuit = QuantumCircuit(qreg)
	
	ZERO = [1, 0]
	#Input qubits initialization:
	circuit.initialize(ZERO, 0)
	circuit.initialize(ZERO, 1)
	circuit.initialize(ZERO, 2)
	#Output qubits MUST BE set to 0
	circuit.initialize(ZERO, 3)
	#HADAMARD GATES#
	print("aqui llego")
 
	circuit.h(0)
	circuit.h(1)
	circuit.h(2)


	circuit.x(0)
	circuit.x(1)
	circuit.mcx([0, 1, 2], 3)
	circuit.x(0)
	circuit.x(1)

	circuit.barrier()
	circuit.x(0)
	circuit.x(2)
	circuit.mcx([0, 1, 2], 3)
	circuit.x(0)
	circuit.x(2)

	circuit.barrier()
	circuit.x(1)
	circuit.x(2)
	circuit.mcx([0, 1, 2], 3)
	circuit.x(1)
	circuit.x(2)
	print("aqui llego")
 
	circuit.barrier()
	circuit.mcx([0, 1, 2], 3)

	circuit.barrier()
       
	
	return circuit
   
