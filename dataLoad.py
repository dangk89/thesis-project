import json
import os

def counter():
	count = 0
	for file in os.listdir('data/'):
		with open('data/'+file) as f:
			data = json.load(f)
		count += len(data)
		print(file+'\n'+str(len(data))+'\n')
	print('total comments: '+str(count))

counter()
