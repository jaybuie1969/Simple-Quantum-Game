"""
This fle is a simple procedural Python program for a probability test
It takes a single gate and then applies a Hadamard - T - Hadamard gate sequence to it, producing a state of:
    (1/sqrt(2))[cos^2(pi / 8)|0> sin^2(pi / 8) * exp(-i * pi / 4)|1>]
This provides approximately 1 in 6.8 chance that when measured, any given qubit will resolve to a one instead of a zero
"""

# Import IBM's Quantum Information Systems Kit (qiskit) package in order to construct and run the quantum circuit
import qiskit

# Set the registers used in each quantum circuit
rQuantum = qiskit.QuantumRegister(1)
rClassical = qiskit.ClassicalRegister(1)

# Each run of this circuit will only be a single shot
shots = 1

# Initialize the quantum circuit for this run
# The qubit at this point is in the state [|0>] with vector
cQuantum = qiskit.QuantumCircuit(rQuantum, rClassical)

# Apply the first Hadamard gate to the qubit in the quantum register
# The qubit at this point is in the superposition state (1/sqrt(2))[|0> |1>]
cQuantum.h(rQuantum)

# Apply the T gate to the qubit in the quantum register
# The qubit at this point is in the superposition state (1/sqrt(2))[|0> exp(i * pi  4)|1>]
cQuantum.t(rQuantum)

# Apply the second Hadamard gate to the qubit in the quantum register
# The qubit at this point is in the superposition state (1/sqrt(2))[|0> exp(i * pi  4)|1>]
cQuantum.h(rQuantum)

# Measure the qubit in the quantum register and place the result in the classical register
# The qubit at this point is in the final desired superposition state (1/sqrt(2))[cos^2(pi / 8)|0> sin^2(pi / 8) * exp(-i * pi / 4)|1>]
cQuantum.measure(rQuantum, rClassical)

# Initialize the object that will hold the results of running the quantum circuit
result = None

# Create a job, excute it and get the result
# By default, this quantum circuit runs on a loacal, simulated quantum computer
# If you would rather submit the circuit to a real IBM quantum processor, comment out this code, un-comment the code below, and provide an API Key.
print("Running on local simulated quantum processor")
job = qiskit.execute(cQuantum, backend=qiskit.Aer.get_backend("qasm_simulator"), shots=shots)
result = job.result()
"""
"""

"""
# Set the API token to use for submitting the circuit(s) and enable the connection to the API
apiToken = "GET YOUR IBM Q EXPERIENCE API TOKEN AT https://quantumexperience.ng.bluemix.net/qx/"
qiskit.IBMQ.enable_account(apiToken)

# (Re-)initialize the result object to None and retrieve the list of back-end quantum processors currently available from IBM
result = None
backends = qiskit.IBMQ.backends()

iTo = len(backends)
if (iTo > 0):
    # At least one quantum processor is available, start with the first one, and submit the job to it; iterate through the list of available
    # processors until one is able to accept the job

    i = 0
    while ((i < iTo) and (result == None)):
        # This loop is not yet at the end of the list, and no result has yet been retrieved from a quantum processor, attempt to submit the circuit to 
        # the processor at the current position in the list

        if (str(backends[i]).lower().find("simulator") == -1):
            # This processor is a real one and not a simulator, attempt to submit the quantum circuit to it
            print("Submitting to IBM quantum processor {0}".format(str(backends[i])))

            try:
                # The job submission is enclosed within a try/except block so that it will not throw an error if the job could not be submitted or retrieved
                job = qiskit.execute(cQuantum, backend=backends[i], shots=shots)
                result = job.result()
            except:
                # The job submission or retrieval threw an error, swallow it and simply move to the next back-end processor in the list
                pass

        # Incremenent the back-end list counter before attemptint to iterate through this loop again
        i = i + 1
"""

if (result != None):
    # The quantum circuit was run successfully, display the results and let the player know whether or not they won

    # Get the first (should be the only) key from the dictionary object of counts that were returned from the test run
    finalState = list(result.get_counts(cQuantum).keys())
    print("Game Result: {0}\n{1}".format(finalState[0], "You Win! :)" if (finalState[0] == "1") else "You Lose! :("))

else:
    # The quantum circuit was not run, there was no IBM quantum processor available to take the job
    print("ERROR - No Quantum Processors Available!  The Game Could Not Be Played.")
