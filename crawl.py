import os
from psaw import PushshiftAPI
import time
import datetime
import json
import time


# List of candidates
candidates = [
				['hillary','clinton'],
				['bernie','sanders'],
				['donald','trump'],
				['ted','cruz']
				]

# List of subreddits
subs = ['politics']


# Convert to epoch
def timeConvert(date):
	return time.mktime(datetime.datetime.strptime(date, '%Y-%m-%d').timetuple())
# Convert from epoch to Y-M-D
def timeInverter(epoch):
	return time.strftime('%Y-%m-%d', time.localtime(epoch))

# List of epoch times for iteration
start = []
timeTuples = []
for i in ["%.2d" % i for i in range(1,13)]:
	start.append('2016-'+i+'-01')
for idx, date in enumerate(start[:-1]):
	timeTuples.append((timeConvert(date),timeConvert(start[idx+1])))
timeTuples.append((timeConvert('2016-12-01'),timeConvert('2016-12-31')))


# Time formatting
after = time.mktime(datetime.datetime.strptime(after, '%Y-%m-%d').timetuple())
after = int(after)
readable_after = time.strftime('%d %b %Y %I:%M %p', time.localtime(after))
before = time.mktime(datetime.datetime.strptime(before, '%Y-%m-%d').timetuple())
before = int(before) + 86399
readable_before = time.strftime('%d %b %Y %I:%M %p', time.localtime(before))
#print('Searching for posts between ' + readable_after + ' and ' + readable_before + '.')
currentDate = before



# Fetch using psaw
def fetch(k,sub, af, be):
	api = PushshiftAPI()
	gen =  api.search_comments(q=k, 
							   subreddit=sub,
							   #limit=size,
							   after=af,
							   before=be
							   #,filter=['body','created_utc']
							   )
	return list(gen)


# Use fetch for all candidates
def fetch_all():
	for sub in subs:
		for candidate in candidates:
			for tup in timeTuples:
				filename = 'data/'+candidate[1]+'_'+sub+'_'+timeInverter(tup[0])+'_'+timeInverter(tup[1])+'.json'
				print('searching for '+filename)						
				if filename[5:] in os.listdir('data/'):
					print(filename+' already present \n')
				else:

					start = time.time()
					print('First...')
					first = [e.d_ for e in fetch(candidate[0], sub, int(tup[0]), int(tup[1]))]
					end = time.time()
					print('...Done in '+str(end - start))


					start = time.time()
					print('Second...')
					second = [e.d_ for e in fetch(candidate[1], sub, int(tup[0]), int(tup[1]))]
					end = time.time()
					print('...Done in '+str(end - start))

					start = time.time()
					print('Comments...')
					#comments = [i for n, i in enumerate(first+second) if i not in (first+second)[n + 1:]]
					comments = [dict(t) for t in {tuple(d.items()) for d in (first+second)}]
					end = time.time()
					print('...Done in '+str(end - start))

					print(len(comments))
					
					start = time.time()		
					print('Saving to file...')
					with open(filename, 'w') as outfile:
						json.dump(comments, outfile)
					end = time.time()
					print('...Done in '+str(end - start))

			# Fetch with first and second query, and merge
			#filename = 'data/'+candidate[0]+candidate[1]+'_'+after+'_to_'+before+'_size_'+str(size)+'.json'



fetch_all()

#print(len(first))
#print(len(second))
#print(len(comments))
