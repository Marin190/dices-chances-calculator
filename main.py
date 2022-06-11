import random, sys, threading
import matplotlib.pyplot as plt
try: launch = int(input("How many roll > "))
except : print("invalid number"), sys.exit()
try: dices = int(input("How many dices > "))
except : print("invalid number"), sys.exit()
a = (dices * 6) - (dices - 1)
Fresult = {}
for i in range(a): Fresult[str(i + dices)] = 0
def main():
	global Fresult
	result = 0
	for i in range(dices):
		result = result + random.randint(1, 6)
	Fresult[str(result)] = Fresult[str(result)] + 1
threading.Thread(target=main)
for i in range(launch): threading.Thread(target=main).start()
left = []
height = []
tick_label = []
for i in range(a): left.append(i + dices)
for i in range(a): height.append(Fresult[str(i + dices)])
for i in range(a): tick_label.append(str(i + dices))
plt.bar(left, height, tick_label = tick_label, width = 0.5, color = ['red', 'green'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dices algo')
plt.show()
