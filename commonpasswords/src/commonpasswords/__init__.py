import re
commonlayouts = ["abc", "qwerty", "efg", "123", "456"]
consecutiveletterspattern = r'([a-zA-Z0-9])\1\1'
# abcdefghijklmnopqrstuvwxyz 1234567890qwertyuiopasdfghjklzxcvbnm,./*-+

def detect(password:str, reason:bool = False):
    reasons = []
    points = 5
    passwordlower = password.lower().strip()
    # CHECKING FOR COMMON LAYOUTS
    alreadysetpatternsreasons = False
    alreadysetpatternsadd = False
    for i in commonlayouts:
            if re.match(i, passwordlower):
                if reason == True and alreadysetpatternsreasons == False:
                    reasons.append("Contains common combination")
                    alreadysetpatternsreasons = True
                points -= 1
                alreadysetpatterns = True
            else: 
                if alreadysetpatternsadd == False:
                    points += 1
                    alreadysetpatternsadd = True
            

    # CHECKING FOR COMMON WORDS
    with open('src/commonpasswords/commonwords.txt', 'r') as file:
        alreadysetcommonwordsadd = False
        alreadysetcommonwordsreasons = False
        for line in file:
                if line.strip() in passwordlower:
                    if reason == True and alreadysetcommonwordsreasons == False:
                        reasons.append("Contains common words")
                        alreadysetcommonwordsreasons = True
                    points -= 1
                else: 
                    if alreadysetcommonwordsadd == False:
                        points += 1
                        alreadysetcommonwordsadd = True

    match = re.search(consecutiveletterspattern, passwordlower)
    if match:
        if reason == True:
            reasons.append("Repetitive letters")
        points -= 1
        alreadysetcommonwords = True
        
    else: 
        points += 1
        alreadysetcommonwords = True


    if reason == True:
        return [points, reasons]
    else:
        return points
    
