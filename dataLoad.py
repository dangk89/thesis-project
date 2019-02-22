import json
import os

def counter():
	count = 0
	trump_c = 0
	hil_c = 0
	ted_c = 0
	bern_c = 0
	for file in os.listdir('data/'):
		with open('data/'+file) as f:
			data = json.load(f)
		if file[:2] == 'cl':
			hil_c += len(data)
		elif file[:2] == 'cr':
			ted_c += len(data)
		elif file[:2] == 'tr':
			trump_c += len(data)
		elif file[:2] == 'sa':
			bern_c += len(data)




		count += len(data)
		#print(file+'\n'+str(len(data))+'\n')

	print('trump: '+str(trump_c))
	print('hillary:'+str(hil_c))
	print('cruz: '+str(ted_c))
	print('bernie: '+str(bern_c))
	print('total comments: '+str(count))

counter()
