import os
from psaw import PushshiftAPI
import time
import datetime
import json
import time
import pprint

# Convert to epoch
def timeConvert(date):
	return time.mktime(datetime.datetime.strptime(date, '%Y-%m-%d').timetuple())
# Convert from epoch to Y-M-D
def timeInverter(epoch):
	return time.strftime('%Y-%m-%d', time.localtime(epoch))


# List of epoch times for iteration
start = []
timeTuples = []
for i in ["%.2d" % i for i in range(3,13)]:
	start.append('2015-'+i+'-01')
for idx, date in enumerate(start[:-1]):
	timeTuples.append((timeConvert(date),timeConvert(start[idx+1])))
timeTuples.append((timeConvert('2015-12-01'),timeConvert('2015-12-31')))


start = []
for i in ["%.2d" % i for i in range(1,13)]:
	start.append('2016-'+i+'-01')
for idx, date in enumerate(start[:-1]):
	timeTuples.append((timeConvert(date),timeConvert(start[idx+1])))
timeTuples.append((timeConvert('2016-12-01'),timeConvert('2016-12-31')))



# Fetch using psaw
def fetch(sub, af, be):
	api = PushshiftAPI()
	gen =  api.search_submissions(subreddit=sub,
							   #limit=10,
							   after=af,
							   before=be,
							   #,filter=['body','created_utc']
							   )
	return list(gen)



topArticles = []
currDate = 1425164400
for i in range(671):

	day = fetch('politics', str(currDate),str(currDate+24*60*60))
	day.sort(key=lambda x: x.num_comments)
	topArticles.append(day[-10:])
	print('done with '+str(len(topArticles)))
	currDate = currDate+24*60*60
	

	
# Save to file
start = time.time()		
print('Saving to file...')
with open('articles.json', 'w') as outfile:
		json.dump(topArticles, outfile)
		end = time.time()
print('...Done in '+str(end - start))



#pretty_dict_str = pprint.pformat(day[0])
#pprint.pprint(pretty_dict_str)

