# ⭐ Homework (Most Important)

# Create a program for students' marks.

# marks = np.array([85, 76, 91, 68, 95])

# Print:

# Total Marks
# Average Marks
# Highest Marks
# Lowest Marks
# Standard Deviation

import numpy as np
marks = np.array([85, 76, 91, 68, 95])

# Total Marks
total_marks=np.sum(marks)
print(total_marks)

# Average Marks
print(total_marks/5)

# Highest Marks
print(np.max(marks))

# Lowest Marks
print(np.min(marks))

# Standard Deviation
print(np.std(marks))