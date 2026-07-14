import matplotlib.pyplot as plt

# Dummy data for Left Plot (Accuracy over 5 epochs)
epochs = [1, 2, 3, 4, 5]
accuracy = [0.55, 0.72, 0.83, 0.89, 0.94]

# Dummy data for Right Plot (FPS of 3 setups)
hardware = ['CPU', 'GPU', 'Edge TPU']
fps = [15, 120, 90]

# Create a figure with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

# Left plot: Line plot
ax1.plot(epochs, accuracy, marker='o', color='teal', linewidth=2)
ax1.set_title('Training Accuracy over Epochs')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Accuracy')
ax1.set_xticks(epochs)
ax1.grid(True, linestyle='--', alpha=0.6)

# Right plot: Bar chart
ax2.bar(hardware, fps, color=['#e74c3c', '#2ecc71', '#3498db'], width=0.5)
ax2.set_title('Inference Speed')
ax2.set_xlabel('Hardware Setup')
ax2.set_ylabel('Frames Per Second (FPS)')
ax2.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
