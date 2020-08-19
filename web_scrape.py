from bs4 import BeautifulSoup
import requests
import re
import personal

# Take amount(a1,nd),currency_1(c1,op),currency_2(c2,op)
#returns amount2(a2).str()

def Cur_convert(a1,c1 = 'inr' ,c2 = 'inr'):
    
    if c1.lower()==c2.lower():
        return a1
    try:
        
        a1 = ''.join(str(a1).split(','))
        url = 'https://www.google.co.in/search?safe=strict&sxsrf=ALeKk00UTTc_ZOphsxXDPTHX3wvDSV7imA%3A1596867430073&ei=ZkMuX4btA8nyrAHwx664Bg&q='+str(a1)+'+'+c1+'+to+'+c2+''         
        # Personal
        agent = personal.user_agent()
        # Personal
        headers = {'User-Agent':agent}
        x = requests.get(url,headers = headers)
        soup = BeautifulSoup(x.content, 'html.parser')
        tags = str(soup('span'))
        amount = re.findall('"DFlfde SwHCTb" \w*-\w*="2" \w*-\w*="(\S+)">',tags)[0]
        return amount
    except:
        return'Invalid Inputs'
        
        

