import matplotlib.pyplot as plt
import numpy as np

python = (80, 50, 10, 90)
java = (30, 70, 5, 20)
networking = (50, 40, 15, 70)
machine_learning = (50, 60, 2, 50)

people = ['kara', 'calvin', 'victor', 'charles']

index = np.arange(4)
plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java")
plt.bar(index+0.4, networking, width=0.2, label="Networking")
plt.bar(index+0.6, machine_learning, width=0.2, label="Machine learning")

plt.title('IT SKILLS LEVELS')
plt.xlabel('person')
plt.xticks(index+0.2, people)
plt.legend(loc="upper left")
plt.ylim(0, 120)

plt.show()
