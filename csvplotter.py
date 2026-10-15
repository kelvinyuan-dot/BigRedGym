
import csv
import matplotlib.pyplot as plt

time = []
target = []
actual = []

with open("height_data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        time.append(float(row["time"]))
        target.append(float(row["target_height"]))
        actual.append(float(row["actual_height"]))

fig, ax = plt.subplots(figsize=(11, 5))

ax.step(time, target, where="post",
        label="Target Height", linestyle="--", linewidth=2)

ax.plot(time, actual,
        label="Actual Height", linewidth=1.5)

ax.set_xlabel("Time (s)")
ax.set_ylabel("Base Height (m)")
ax.set_title("Base Height Tracking")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("height_tracking.pdf")
print("Saved height_tracking.pdf")
