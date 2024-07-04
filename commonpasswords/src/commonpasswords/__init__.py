import re
import json
commonlayouts = ["abc", "qwerty", "efg", "123", "456"]
consecutiveletterspattern = r'([a-zA-Z0-9])\1\1'
digitpattern = r"[0-9]"
letterspattern = r"[a-zA-Z]"
specialpattern = r'[!@#$%^&*()-+{}:"?/><,.;:]'

startingnumber = 0

commonlayoutenabled = True
commonlayoutpointsremove = 1
commonlayoutpointsadd = 0
commonlayoutreason = "Contains common combination"

commonwordsenabled = True
commonwordpointsremove = 1
commonwordspointsadd = 0
commonwordsreason = "Contains common words"

consecutivelettersenabled = True
consecutivelettersremove = 1
consecutivelettersadd = 0
consecutivelettersreason = "Contains Repetitive letters"

lengthenabled = True
lengthrequirement = 8
lengthremove = 1
lengthadd = 0
lengthreason = "Password is lower than " + str(lengthrequirement) + " characters"

charactertypes = True
charactertypesremove = 1
charactertypesadd = 0
charactertypesrequirement = 1
charactertypesreason = "Only "+ str(charactertypesrequirement) +" type of Character"

# abcdefghijklmnopqrstuvwxyz 1234567890qwertyuiopasdfghjklzxcvbnm,./*-+

def configure(configuration:json):
    print(configuration)



def detect(password:str, reason:bool = False):
    reasons = []
    points = startingnumber
    passwordlower = password.lower().strip()

    # CHECKING FOR COMMON LAYOUTS
    if commonlayoutenabled == True:
        alreadysetpatternsreasons = False
        for i in commonlayouts:
            if re.match(i, passwordlower):
                if reason == True and alreadysetpatternsreasons == False:
                    reasons.append(commonlayoutreason)
                    alreadysetpatternsreasons = True
                points -= commonlayoutpointsremove
            else:
                    points += commonlayoutpointsadd
            

    # CHECKING FOR COMMON WORDS
    if commonwordsenabled == True:
     with open('src/commonpasswords/commonwords.txt', 'r') as file:
        alreadysetcommonwordsreasons = False
        alreadysetcommonwordsadd = False
        for line in file:
                if line.strip() in passwordlower:
                    if reason == True and alreadysetcommonwordsreasons == False:
                        reasons.append(commonwordsreason)
                        alreadysetcommonwordsreasons = True
                    points -= commonwordpointsremove
                    alreadysetcommonwordsadd = True
                    break
        if alreadysetcommonwordsadd == True:
            points += commonwordspointsadd



# Checking for consecutive letters
    if consecutivelettersenabled == True:
        match = re.search(consecutiveletterspattern, passwordlower)
        if match:
            if reason == True:
                reasons.append(consecutivelettersreason)
            points -= consecutivelettersremove
        else:
            points += consecutivelettersadd
        
# Check if less than 8 characters
    if lengthenabled == True:
        if len(password) < lengthrequirement:
            points -= lengthremove
            if reason == True:
                reasons.append(lengthreason)
        else:
            points += lengthadd


    if charactertypes == True:
        CatagoryaCount = 0
        if re.search(letterspattern, passwordlower):
            CatagoryaCount += 1
        if re.search(digitpattern, passwordlower):
            CatagoryaCount += 1
        if re.search(specialpattern, passwordlower):
            CatagoryaCount += 1
        if CatagoryaCount == charactertypesrequirement:
            points -= charactertypesremove
            if reason == True:
                reasons.append(charactertypesreason)
        else:
            points += charactertypesadd

         
    

    if reason == True:
        return [points, reasons]
    else:
        return points
    
    
