import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# Import Aer, el simulador

def create_cut_circuit():   
    q_reg = QuantumRegister(7,'q')
    c_reg = ClassicalRegister(3,'c')
    circuit = QuantumCircuit(q_reg,c_reg)
    circuit.reset(q_reg[0])
    circuit.reset(q_reg[1])
    circuit.reset(q_reg[2])
    circuit.reset(q_reg[3])
    circuit.reset(q_reg[4])
    circuit.reset(q_reg[5])
    circuit.reset(q_reg[6])

    circuit.barrier(q_reg)
#codificamos un 3 para el primer sumando
    circuit.x(q_reg[0])
    circuit.x(q_reg[1])
#codificamos un 3 para el primer sumando
    circuit.x(q_reg[2])
    circuit.x(q_reg[3])
    
    circuit.barrier(q_reg)
    
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
    circuit.swap(q_reg[4],q_reg[6])
    
    circuit.measure(q_reg[6],c_reg[2])
    circuit.measure(q_reg[5],c_reg[1])
    circuit.measure(q_reg[4],c_reg[0])

    circuit.draw()
    # Usamos Aer's qasm_simulator
    backend_sim = AerSimulator()
    circuit = transpile(circuit, backend_sim)

# Ejecutamos el circuito en el qasm simulator.
# Ponemos 1000 ejecuciones
#job_sim = backend_sim.run(transpile(circuit, backend_sim), shots=1000)

# Cogemos los resultados de la ejecución
    result_sim = backend_sim.run(circuit, shots=10, memory=True).result()

# Contamos los resultados
    counts = result_sim.get_counts(circuit)
    print(counts)
    #return circuit

create_cut_circuit()