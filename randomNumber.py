from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, Measure  # import the operations we want to perform (Hadamard and measurement)

import projectq.setups.ibm #use ibm
from projectq.backends import IBMBackend

eng = MainEngine()  # create a default compiler (the back-end is a simulator)
# eng = MainEngine(IBMBackend())
qubit1 = eng.allocate_qubit()  # allocate 1 qubit
qubit2 = eng.allocate_qubit()
qubit3 = eng.allocate_qubit()
qubit4 = eng.allocate_qubit()
qubit5 = eng.allocate_qubit()

# for x in range(0,4):
H | qubit1  # apply a Hadamard gate
H | qubit2
H | qubit3
H | qubit4
H | qubit5

Measure | qubit1  # measure the qubit
Measure | qubit2
Measure | qubit3
Measure | qubit4
Measure | qubit5

eng.flush()  # flush all gates (and execute measurements)
q1 = int(qubit1)
q2 = int(qubit2)
q3 = int(qubit3)
q4 = int(qubit4)
q5 = int(qubit5)

output = 0

if q1 == 1:
	output += 1
if q2 == 1:
	output += 2
if q3 == 1:
	output += 4
if q4 == 1:
	output += 8
if q5 == 1:
	output += 16

print("Random number is {}".format(output))  # output measurement result
