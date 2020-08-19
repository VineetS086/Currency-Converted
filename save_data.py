import json
import time
from web_scrape import Cur_convert

#

def cur_cache(cur):
    #Loading Data
    cur = cur.lower()
    with open('Currency_Price_list.txt','r') as handle:
        file = json.loads(handle.read())
    
    #Search, retrieving, adding new
    if time.time()-file['time'] > 72000:
        print('Updating...\nPlease Weight')
        for i in file['data']:
            file['data'][i] = str(float(Cur_convert(1000,i,'inr'))/1000)
        file['time'] = time.time()
        file['noted_time'] = time.ctime()
    if cur not in file['data'].keys():
        print('Searching for new Currency')
        try:
            cur_ = str(float(Cur_convert(1000,cur,'inr'))/1000)
            print('Added new currency...')
            file['data'][cur] = cur_
        except:
            return('Invalid Currency')
        
    #Saving Data
    with open('Currency_Price_list.txt','w') as handle:
        handle.write(json.dumps(file, indent = 4))
    return file['data'][cur]

