import json
from time import sleep
from termcolor import colored

def inputed():
    print()
    timeprint('Please, type the path to your json file: ')
    path = input()
    if path.split('.')[-1] != 'json':
        timeprint('The type of your file is not json!')
        return inputed()
    else:
        source_json = open(path, encoding="utf-8")
        data = json.load(source_json)
        return data


def navigate(data):
    if isinstance(data, dict) == True:
        
        categories = data.keys()
        for cat in categories:
            timeprint('')
            timeprint(cat)
        category = input('Please, choose a category and enter it: ')
        while True:
            if category in categories:
                return navigate(data[category])
            else:
                category = input('There is no such category. Please, enter the right one: ')
    elif isinstance(data, list) == True:
    
        timeprint('Choose the element of the list from 0 to '+str(len(data)-1)+': ')
        
        for i in range(len(data)-1):
            print(str(i)+' --- '+str(data[i]))
        indx = input('Index of the element: ')
        while True:

            if indx in [str(item) for item in range(len(data)-1)] :
                return navigate(data[int(indx)])
            else:

                indx = input('Please type the correct index: ')
    else:
        timeprint(data)
        timeprint('Thank you for using this program!')
        return ''

def timeprint(line: str):
    '''
    This function prints the text in looong time
    '''
    for char in line:
        print(char, end='', flush=True)
        sleep(0.03)
    print()


if __name__ == "__main__":
    print(navigate(inputed()))
