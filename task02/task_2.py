"""
Task_2 Version 0.4

Everything is working as it must be
"""

import json

def genderSort(username, names):
    name = names['name']
    surname = names['last_name']

    if not (username == 'null' or 
            name == None or 
            surname == None):
        with open('m_names.txt') as mal_names:
            for line in mal_names:
                var = [line, line[:5]]
                if (username.find(var[0]) > -1 or 
                    username.find(var[1]) > -1 or
                    name.find(var[0]) > -1 or 
                    name.find(var[1]) > -1):
                    return 'male'
                
        with open('f_names.txt') as fem_names:
            for line in fem_names:
                var = [line, line[:5]]
                if (username.find(var[0]) > -1 or 
                    username.find(var[1]) > -1 or
                    name.find(var[0]) > -1 or 
                    name.find(var[1]) > -1):
                    return 'female'

        
    
    return '----'
    

def main():
    with open('users.json') as f_in:
        userDict = json.load(f_in)

    male,female = [], []
    for d in userDict:
        gender = genderSort(d, userDict[d])
        userDict[d]['gender'] = gender
        if gender == 'male':
            male.append(d)
        elif gender == 'female':
            female.append(d)

    with open("male.txt", "w") as f:
        for m in male:
            f.write(m +"\n")
    
    with open("female.txt", "w") as f:
        for fm in female:
            f.write(fm +"\n")
            
     

if __name__ == '__main__':
    main()