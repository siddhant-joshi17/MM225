import numpy as np
import matplotlib.pyplot as plt

# Data from the table
I_mA = np.array([0, 1, 2, 4, 6, 10, 15])         # current in mA
V_diode = np.array([0, 2.96, 3.09, 3.35, 3.60, 4.09, 4.67])   # volts
R = np.array([10410, 7780, 7460, 3190, 2780, 2190, 1850])     # ohms

# Convert current to Amps
I_A = I_mA * 1e-3  

# LED Power (Watts)
P = V_diode * I_A  

# Take logs (base 10 for plotting)
logP = np.log10(P[1:])   # skip first (0 W) to avoid log(0)
logR = np.log10(R[1:])

# Plot
plt.figure(figsize=(6,5))
plt.plot(logP, logR, 'o-', color='b', label="Log-Log data")
plt.xlabel("log10(Power) [log(W)]")
plt.ylabel("log10(Resistance) [log(Ω)]")
plt.title("Log-Log Plot: LDR Resistance vs LED Power")
plt.grid(True, which="both", ls="--", lw=0.7)
plt.legend()
plt.show()
