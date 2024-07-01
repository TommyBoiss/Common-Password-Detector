import re
commonlayouts = [r'^[a-z]+${3}', r'^[0-9a-z,./*\-+]+${3}']
# abcdefghijklmnopqrstuvwxyz 1234567890qwertyuiopasdfghjklzxcvbnm,./*-+

def detect(password:str, reason:bool = False):
    reasons = []
    points = 5
    passwordlower = password.lower()
    # CHECKING FOR COMMON LAYOUTS
    for i in commonlayouts:
        test_set = set(i.lower())
        if re.match(i, passwordlower):
            if reason == True:
                reasons.append("Contains common combination")
            points -= 1
        else: 
            print("added1")
            points += 1

    # CHECKING FOR COMMON WORDS
    with open('src\commonpasswords\commonwords.txt', 'r') as file:
        alreadysetcommonwords = False
        for line in file:
            print(line)
            if alreadysetcommonwords == False:
                if line in password:
                    print(alreadysetcommonwords)
                    if reason == True:
                        reasons.append("Contains common words")
                    points -= 1
                    alreadysetcommonwords = True
                else: 
                    points += 1
                    alreadysetcommonwords = True
            else:break


    return points
    
