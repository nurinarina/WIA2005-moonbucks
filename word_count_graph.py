# Plotting the Word Count vs Country Graph
# Using matplotlib function
import numpy as np
import matplotlib.pyplot as plt

N = 5  # no of bars

negative = (133, 154, 545, 191, 450)  # total no of negative words respective to the country's sequence
positive = (183, 211, 233, 268, 395)  # total no of positive words respective to the country's sequence
ind = np.arange(N)
width = 0.35

fig = plt.subplots(figsize=(10, 7))
p1 = plt.bar(ind, negative, width)
p2 = plt.bar(ind, positive, width,
             bottom=negative)

plt.ylabel('Word count')  # y-axis
plt.title('Positive and Negative Word Count for Each Country')  # graph's title
plt.xticks(ind, ('South Korea', 'Japan', 'Great Britain', 'China', 'Canada'))  # x-axis
plt.yticks(np.arange(0, 910, 50))
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))  # legends

plt.show()

