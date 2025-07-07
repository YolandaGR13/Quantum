from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi

qubits = 4
outputQubits = 4
shots = 1024
	
circuits = [QuantumCircuit(qubits, qubits),]
ALGORITHM = "Grover"
	  
ONE = [0, 1]
ZERO = [1, 0]

expected = [(0, 0.0625),(1, 0.0625),(2, 0.0625),(3, 0.0625),(4, 0.0625),(5, 0.0625),(6, 0.0625),(7, 0.0625),(8, 0.0625),(9, 0.0625),(10, 0.0625),
(11, 0.0625),(12, 0.0625),(13, 0.0625),(14, 0.0625),(15, 0.0625),]

TEMPLATE = 'common.solo_circuit.splitting.template.txt'
ORIGINAL_QUBITS = 4
SPLIT = False
def oracle_0() :	 # Looks for 0
	U = QuantumCircuit(4)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	return U
def oracle_1() :	 # Looks for 1
	U = QuantumCircuit(4)
	U.x(0)
	U.x(1)
	U.x(2)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(1)
	U.x(2)
	return U
def oracle_2() :	 # Looks for 2
	U = QuantumCircuit(4)
	U.x(0)
	U.x(1)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(1)
	U.x(3)
	return U
def oracle_3() :	 # Looks for 3
	U = QuantumCircuit(4)
	U.x(0)
	U.x(1)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(1)
	return U
def oracle_4() :	 # Looks for 4
	U = QuantumCircuit(4)
	U.x(0)
	U.x(2)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(2)
	U.x(3)
	return U
def oracle_5() :	 # Looks for 5
	U = QuantumCircuit(4)
	U.x(0)
	U.x(2)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(2)
	return U
def oracle_6() :	 # Looks for 6
	U = QuantumCircuit(4)
	U.x(0)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(3)
	return U
def oracle_7() :	 # Looks for 7
	U = QuantumCircuit(4)
	U.x(0)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	return U
def oracle_8() :	 # Looks for 8
	U = QuantumCircuit(4)
	U.x(1)
	U.x(2)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(1)
	U.x(2)
	U.x(3)
	return U
def oracle_9() :	 # Looks for 9
	U = QuantumCircuit(4)
	U.x(1)
	U.x(2)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(1)
	U.x(2)
	return U
def oracle_10() :	 # Looks for 10
	U = QuantumCircuit(4)
	U.x(1)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(1)
	U.x(3)
	return U
def oracle_11() :	 # Looks for 11
	U = QuantumCircuit(4)
	U.x(1)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(1)
	return U
def oracle_12() :	 # Looks for 12
	U = QuantumCircuit(4)
	U.x(2)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(2)
	U.x(3)
	return U
def oracle_13() :	 # Looks for 13
	U = QuantumCircuit(4)
	U.x(2)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(2)
	return U
def oracle_14() :	 # Looks for 14
	U = QuantumCircuit(4)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(3)
	return U
def oracle_15() :	 # Looks for 15
	U = QuantumCircuit(4)
	U.mcp(pi, [0, 1, 2], 3)
	return U
def diffuser() :
	U = QuantumCircuit(4)
	U.h(0)
	U.h(1)
	U.h(2)
	U.h(3)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.mcp(pi, [0, 1, 2], 3)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.h(0)
	U.h(1)
	U.h(2)
	U.h(3)
	return U


for i in range(0, len(circuits)) :
	for j in range (0, qubits) :
		circuits[i].h(j)

for i in range (0, 0) :
	circuits[0].append(oracle_0(), [0,1,2,3])
	circuits[0].append(oracle_1(), [0,1,2,3])
	circuits[0].append(oracle_2(), [0,1,2,3])
	circuits[0].append(oracle_3(), [0,1,2,3])
	circuits[0].append(oracle_4(), [0,1,2,3])
	circuits[0].append(oracle_5(), [0,1,2,3])
	circuits[0].append(oracle_6(), [0,1,2,3])
	circuits[0].append(oracle_7(), [0,1,2,3])
	circuits[0].append(oracle_8(), [0,1,2,3])
	circuits[0].append(oracle_9(), [0,1,2,3])
	circuits[0].append(oracle_10(), [0,1,2,3])
	circuits[0].append(oracle_11(), [0,1,2,3])
	circuits[0].append(oracle_12(), [0,1,2,3])
	circuits[0].append(oracle_13(), [0,1,2,3])
	circuits[0].append(oracle_14(), [0,1,2,3])
	circuits[0].append(oracle_15(), [0,1,2,3])
	circuits[0].append(diffuser(), [0,1,2,3])


startQubit = qubits-outputQubits
for i in range(0, len(circuits)) :
	for j in range(startQubit, qubits) :
		circuits[i].measure(j, qubits-j-1)

#expanded = circuits[0].decompose(reps=2)   # Esto es para pintar el circuit. A mayor reps, más detalla.
#print(expanded)
