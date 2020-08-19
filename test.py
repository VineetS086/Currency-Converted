from main import convert_cur
flag = True
print('Enter the currency code when asked about Currency...(eg - INR for Indian Rupees, AUD for Australian Dollar)')
while flag:
    a = input('Amount: ')
    b = input('Currency_1 :')
    c = input('Currency_2: ')  
    print(convert_cur(a,b,c))
    if input('Enter \'quit\' to exit program') == 'quit':
        flag = False
