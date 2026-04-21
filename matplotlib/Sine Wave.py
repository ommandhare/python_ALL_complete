import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
amplitude = 1.0
frequency = 1.0
phase = 0.0

# Create the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)

# Generate initial sine wave
x = np.linspace(0, 10, 1000)
y = amplitude * np.sin(frequency * x + phase)
line, = ax.plot(x, y, lw=2)
ax.set_title("Interactive Sine Wave")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Define slider positions
ax_amp = plt.axes([0.1, 0.25, 0.8, 0.03])
ax_freq = plt.axes([0.1, 0.20, 0.8, 0.03])
ax_phase = plt.axes([0.1, 0.15, 0.8, 0.03])

# Create sliders
slider_amp = Slider(ax_amp, 'Amplitude', 0.1, 5.0, valinit=amplitude)
slider_freq = Slider(ax_freq, 'Frequency', 0.1, 5.0, valinit=frequency)
slider_phase = Slider(ax_phase, 'Phase', 0.0, 2*np.pi, valinit=phase)

# Update function
def update(val):
    amp = slider_amp.val
    freq = slider_freq.val
    ph = slider_phase.val
    line.set_ydata(amp * np.sin(freq * x + ph))
    fig.canvas.draw_idle()

# Connect sliders to update function
slider_amp.on_changed(update)
slider_freq.on_changed(update)
slider_phase.on_changed(update)

plt.show()