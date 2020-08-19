from save_data import cur_cache

# i will improve it later

def convert_cur(a1,c1 = 'inr',c2 = 'inr'):
    a1 = float(''.join(str(a1).split(',')))
    a2 = str(a1*float(cur_cache(c1))/float(cur_cache(c2)))
    intg,d = a2.split('.')
    #lst = list(intg)[:-3]
    #a = [lst[i*2]+lst[i*2+1]+',' for i in range(len(lst)//2)]+[intg[-3:]]
    #print(intg,d)
    
    return(intg+'.'+d[:2])
    
    #return(intg+'.'+d[:2])
    

