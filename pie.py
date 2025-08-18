import matplotlib.pyplot as plt

# Data from the table
frequency = [1, 10, 50, 100, 140, 180, 200, 500, 1000]
voltage = [0.7, 4.1, 3.7, 3.36, 2.95, 2.62, 2.45, 1.24, 0.64]

# Plot
plt.figure(figsize=(8,5))
plt.plot(frequency, voltage, marker='o', linestyle='-', color='b', label='Voltage vs Frequency')

# Labels and title
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs Frequency")
plt.grid(True)
plt.legend()

# Optional: Log scale for frequency if needed
# plt.xscale("log")

plt.show()
