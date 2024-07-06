import importlib.resources
import re
commonlayouts = ["qwerty", "qazwsxedcrfvtgbyhnujmik,ol.p;/"]
consecutiveletterspattern = r'([a-zA-Z0-9])\1\1'
digitpattern = r"[0-9]"
letterspattern = r"[a-zA-Z]"
specialpattern = r'[!@#$%^&*()-+{}:"?/><,.;:]'
datepattern = r'*\b(?:19|20)\d{2}(?!\d)*'


# abcdefghijklmnopqrstuvwxyz 1234567890qwertyuiopasdfghjklzxcvbnm,./*-+

def detect(password:str, reason:bool = False, configuration:dict = {}):
    reasons = []
    points = 0
    passwordlower = password.lower().strip()
    commonwordsdatabase = importlib.resources.files(__package__) / "commonwords.txt"

    commonlayoutenabled = True
    commonlayoutpointsremove = 1
    commonlayoutpointsadd = 0
    commonlayoutreason = "Contains common combination"
    commonlayoutminimin = 3

    commonwordsenabled = True
    commonwordspointsremove = 1
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

    charactertypesenabled = True
    charactertypesremove = 1
    charactertypesadd = 0
    charactertypesrequirement = 1
    charactertypesreason = "Only "+ str(charactertypesrequirement) +" type of Character"

    dateenabled = True
    dateremove = 1
    dateadd = 0
    datereason = "Possibily contains a date"
    
    points = configuration.get("startingpoints", 0)
    commonwordsdatabase = configuration.get("commonwordsdatabase", importlib.resources.files(__package__) / "commonwords.txt")
    
    commonlayoutfolder = configuration.get("commonlayout")
    if commonlayoutfolder != None: 
        commonlayoutenabled = commonlayoutfolder.get("enabled", True)
        commonlayoutpointsremove = commonlayoutfolder.get("pointsremove", 1)
        commonlayoutpointsadd = commonlayoutfolder.get("pointsadd", 0)
        commonlayoutreason = commonlayoutfolder.get("reason", "Contains common combination")
        commonlayoutreason = commonlayoutfolder.get("minimin", 3)

    commonwordsfolder = configuration.get("commonwords")
    if commonwordsfolder != None: 
        commonwordsenabled = commonwordsfolder.get("enabled", True)
        commonwordspointsremove = commonwordsfolder.get("pointsremove", 1)
        commonwordspointsadd = commonwordsfolder.get("pointsadd", 0)
        commonwordsreason = commonwordsfolder.get("reason", "Contains common words")

    consecutivelettersfolder = configuration.get("consecutiveletters")
    if consecutivelettersfolder != None: 
        consecutivelettersenabled = consecutivelettersfolder.get("enabled", True)
        consecutiveletterspointsremove = consecutivelettersfolder.get("pointsremove", 1)
        consecutiveletterspointsadd = consecutivelettersfolder.get("pointsadd", 0)
        consecutivelettersreason = consecutivelettersfolder.get("reason", "Contains Repetitive letters")
        
    lengthfolder = configuration.get("length")
    if consecutivelettersfolder != None: 
        lengthenabled = lengthfolder.get("enabled", True)
        lengthrequirement = lengthfolder.get("requirement", 8)
        lengthpointsremove = lengthfolder.get("pointsremove", 1)
        lengthpointsadd = lengthfolder.get("pointsadd", 0)
        lengthreason = lengthfolder.get("reason", "Password is lower than " + str(lengthrequirement) + " characters")

    charactertypesfolder = configuration.get("charactertypes")
    if consecutivelettersfolder != None: 
        charactertypesenabled = charactertypesfolder.get("enabled", True)
        charactertypesrequirement = charactertypesfolder.get("requirement", 8)
        charactertypespointsremove = charactertypesfolder.get("pointsremove", 1)
        charactertypespointsadd = charactertypesfolder.get("pointsadd", 0)
        charactertypesreason = charactertypesfolder.get("reason", "Only "+ str(charactertypesrequirement) +" type of Character")

        datefolder = configuration.get("date")
    if consecutivelettersfolder != None: 
        dateenabled = datefolder.get("enabled", True)
        datepointsremove = datefolder.get("pointsremove", 1)
        datepointsadd = datefolder.get("pointsadd", 0)
        datereason = datefolder.get("reason", "Only "+ str(charactertypesrequirement) +" type of Character")


    # CHECKING FOR COMMON LAYOUTS
    if commonlayoutenabled == True:
        alreadysetpatternsreasons = False
        alreadysetpatternsadd = False
        for icommon in commonlayouts:
          
          for i in range(len(icommon) - 2):
            substr = icommon[i:i+commonlayoutminimin-1]

            if substr in passwordlower:
             if alreadysetpatternsreasons == False:
                if reason == True:
                    reasons.append(commonlayoutreason)

                points -= commonlayoutpointsremove
                alreadysetpatternsreasons = True
                

            else:
                    if alreadysetpatternsadd == False:
                        points += commonlayoutpointsadd
                        alreadysetpatternsadd = True

        
            

    # CHECKING FOR COMMON WORDS
    if commonwordsenabled == True:
     with open(commonwordsdatabase, 'r') as file:
        alreadysetcommonwordsreasons = False
        alreadysetcommonwordsadd = False
        for line in file:
                if line in passwordlower:

                    if reason == True and alreadysetcommonwordsreasons == False:
                        reasons.append(commonwordsreason)
                        alreadysetcommonwordsreasons = True
                    points -= commonwordspointsremove
                    break
                else:
                    if alreadysetcommonwordsadd == False:
                        points += commonwordspointsadd
                        alreadysetcommonwordsadd = True



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

# Detects for more than a certain amount of text catagories
    if charactertypesenabled == True:
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

    if dateenabled == True:
     if re.search(datepattern, password):
        points -= dateremove
        if reason == True:
            reasons.append(datereason)
     else: 
        points += dateadd
        
    

         
    

    if reason == True:
        return [points, reasons]
    else:
        return points
    
