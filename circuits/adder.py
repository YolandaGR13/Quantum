import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from math import gcd
from numpy.random import randint
import pandas as pd
import importlib.util
from fractions import Fraction

def create_cut_circuit():   
    adder = QuantumCircuit()
    input_qr = QuantumRegister(4,'input')
    adder.add_register(input_qr)
    adder.ccx(input_qr[0], input_qr[1], input_qr[3])
    adder.cx(input_qr[0], input_qr[1])
    adder.ccx(input_qr[1], input_qr[2], input_qr[3])
    adder.cx(input_qr[1], input_qr[2])
    adder.cx(input_qr[0], input_qr[1])
    return adder

