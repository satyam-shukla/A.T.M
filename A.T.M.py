password=2345
balance = 1000000
insert = input('Enter your card : ')
print('''English-1
Hindi-2
 ''')
language = int(input('Enter your language : '))
if language == 1:
    print('English')
    pin = int(input('Enter your pin'))
    if password == pin:
        print('Welcome to our bank ! ')
        print('''Please choose your account type :
        1. Saving account
        2. Current account''')
        account = int(input("Enter type of account : "))
        if account == 1:
            print('Welcome to your saving account')
            print('Please type which type of transaction do you want : ')
            print('1. Withdraw Amount')
            print('2. Balance Enquriy')
            transactions = int(input('Enter the type of transactions : '))
            if transactions == 1:
                print('Enter Withdrawal Amount : ')
                amount = int(input('Withdrawal Amount'))
                if balance !=0 and balance >= amount:
                    print('Collect Your Amount Please :) ')
                    balance -= amount
                    print('''Do you want transction receipt ? 
                    1. yes
                    2. no''')
                    receipt = int(input())
                    if receipt == 1:
                        print('Your Current Balance is ',balance)
                        print("Take your receipt! Thanks for paperless transaction")
                    elif receipt == 2:
                        print('Thanks for paperless transaction')
                    else:
                        print('Please choose a correct number of valid transiction. ')
                else:
                    print('Insuffcient balance')   
            elif transactions == 2:
                print('''Do you want transction receipt ? 
                        1. yes
                        2. no''')
                receipt = int(input())
                if receipt == 1:
                    print('Take your receipt! Thanks for paperless transaction')
                    print('balance :',balance)
                #We print receipt on paper on that condition
                elif receipt == 2:
                    print('Thanks for paperless transaction')
                    print('Your balance is ',balance)
                else:
                    print('Please choose a valid number for receipt. ')
            else:
                priint('Please enter correct number for transaction type.')
        elif account == 2:
            print('Welcome to your current account')
            print('Please type which type of transaction do you want : ')
            print('1. Withdraw Amount')
            print('2. Balance Enquriy')
            transactions = int(input('Enter the type of transactions : '))
            if transactions == 1:
                print('Enter Withdrawal Amount : ')
                amount = int(input('Withdrawal Amount'))
                if balance !=0 and balance >= amount:
                    print('Collect Your Amount Please :) ')
                    balance -= amount
                    print('''Do you want transction receipt ? 
                    1. yes
                    2. no''')
                    receipt = int(input())
                    if receipt == 1:
                        print('Your Current Balance is ',balance)
                        print("Take your receipt! Thanks for paperless transaction")
                    elif receipt == 2:
                        print('Thanks for paperless transaction')
                    else:
                        print('Please choose a correct number of valid transiction. ')
                else:
                        print('Insuffcient balance')   
            elif transactions == 2:
                print('''Do you want transction receipt ? 
                        1. yes
                        2. no''')
                receipt = int(input())
                if receipt == 1:
                    print('Take your receipt! Thanks for paperless transaction')
                    print('balance :',balance)
#We print receipt on paper on that condition
                elif receipt == 2:
                        print('Thanks for paperless transaction')
                        print('Your balance is ',balance)
                else:
                        print('Please choose a valid number for receipt. ')
            else:
                priint('Please enter correct number for transaction type.')
            
        else:
                print('Please select correct account  type! ')        
    else:
        print('Enter correct password'