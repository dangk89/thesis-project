import json
import os

dataSet = []
n = 0
for file in os.listdir('data/'):
	with open('data/'+file) as f:
		data = json.load(f)
	print(data[0])

"""	
	for i in range(10):
		dataSet.append(data[i])
		print('done')
		n+=1
		print(i)
"""
print(len(dataSet))