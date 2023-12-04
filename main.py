from datetime import datetime
import os

def add_log(fileName, method):
    entryDate = (datetime.now()).strftime("%m/%d/%Y")
    logDeets =  input('Log entry: \n')
    entry = f'{entryDate} \n{logDeets}'
    with open(fileName, method) as recipie:
        recipie.write(entry)

def readLog(fileName):
    with open (fileName, 'r') as fileReader:
        print()
        print(fileName)
        print(fileReader.read())

def placeHodler():
    print('ERROR: THAT ONE \'S STILL COOKING')

#NOTE: MAIN FUNCTION
def main():
    keep_going = 'y'   
    while keep_going == 'y':
    
        print('''
            Welcome to cookingLog!
            Please select one of the following:

            1) Review Existing Recipie Log
            2) Add Note To Existing Recipie
            3) Add New Recipie

            ''')
        
        #Menu selection 
        selection = int(input('Selection: ')) 
        

        if selection in range(1, 4):
            fileName = f"{input('Enter recipie name: ')}.txt"
            if selection == 1:
                try:
                    readLog(fileName)
                except:
                    wantAddEntry = input('This file was not found. Would you like to add a new entry for this recipie (y/n)?').casefold()
                    if wantAddEntry == 'y':
                        add_log(fileName, 'w')

            elif selection == 2:
                try:
                    add_log(fileName, 'a')
                except:
                    print('File not found')
            elif selection == 3:
                if os.path.exists(fileName):
                    print('Ope! This recipie already has an entry. Please try again.')
                else:
                    add_log(fileName, 'w')
        else:
            print('ERROR: INVALID SELECTION \n')
        

        keep_going = input('Would you like to coninue using cookingLog? (y/n)').casefold()
    
    print('''
        Thank you for using cookingLog.
        END
          ''')
    
if __name__ == '__main__':
    main()