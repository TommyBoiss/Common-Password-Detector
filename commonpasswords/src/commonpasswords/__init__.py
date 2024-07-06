import re
commonlayouts = ["qwerty", "qazwsxedcrfvtgbyhnujmik,ol.p;/"]
consecutiveletterspattern = r'([a-zA-Z0-9])\1\1'
digitpattern = r"[0-9]"
letterspattern = r"[a-zA-Z]"
specialpattern = r'[!@#$%^&*()-+{}:"?/><,.;:]'
datepattern = r'\b(?:19|20)\d{2}(?!\d)'


# abcdefghijklmnopqrstuvwxyz 1234567890qwertyuiopasdfghjklzxcvbnm,./*-+
class main:
 def __init__(self):
    self.startingnumber = 0

    self.commonlayoutenabled = True
    self.commonlayoutpointsremove = 1
    self.commonlayoutpointsadd = 0
    self.commonlayoutreason = "Contains common combination"
    self.commonlayoutminimin = 3

    self.commonwordsenabled = True
    self.commonwordspointsremove = 1
    self.commonwordspointsadd = 0
    self.commonwordsreason = "Contains common words"

    self.consecutivelettersenabled = True
    self.consecutivelettersremove = 1
    self.consecutivelettersadd = 0
    self.consecutivelettersreason = "Contains Repetitive letters"

    self.lengthenabled = True
    self.lengthrequirement = 8
    self.lengthremove = 1
    self.lengthadd = 0
    self.lengthreason = "Password is lower than " + str(self.lengthrequirement) + " characters"

    self.charactertypesenabled = True
    self.charactertypesremove = 1
    self.charactertypesadd = 0
    self.charactertypesrequirement = 1
    self.charactertypesreason = "Only "+ str(self.charactertypesrequirement) +" type of Character"

    self.dateenabled = True
    self.dateremove = 1
    self.dateadd = 0
    self.datereason = "Possibily contains a date"

 def _configure(self, configuration:dict):
    self.startingnumber = configuration.get("startingpoints", 0)

    commonlayoutfolder = configuration.get("commonlayout")

    if commonlayoutfolder != None: 
        self.commonlayoutenabled = commonlayoutfolder.get("enabled", True)
        self.commonlayoutpointsremove = commonlayoutfolder.get("pointsremove", 1)
        self.commonlayoutpointsadd = commonlayoutfolder.get("pointsadd", 0)
        self.commonlayoutreason = commonlayoutfolder.get("reason", "Contains common combination")
        self.commonlayoutreason = commonlayoutfolder.get("minimin", 3)

    commonwordsfolder = configuration.get("commonwords")
    if commonwordsfolder != None: 
        self.commonwordsenabled = commonwordsfolder.get("enabled", True)
        self.commonwordspointsremove = commonwordsfolder.get("pointsremove", 1)
        self.commonwordspointsadd = commonwordsfolder.get("pointsadd", 0)
        self.commonwordsreason = commonwordsfolder.get("reason", "Contains common words")

    consecutivelettersfolder = configuration.get("consecutiveletters")
    if consecutivelettersfolder != None: 
        self.consecutivelettersenabled = consecutivelettersfolder.get("enabled", True)
        self.consecutiveletterspointsremove = consecutivelettersfolder.get("pointsremove", 1)
        self.consecutiveletterspointsadd = consecutivelettersfolder.get("pointsadd", 0)
        self.consecutivelettersreason = consecutivelettersfolder.get("reason", "Contains Repetitive letters")
        
    lengthfolder = configuration.get("length")
    if consecutivelettersfolder != None: 
        self.lengthenabled = lengthfolder.get("enabled", True)
        self.lengthrequirement = lengthfolder.get("requirement", 8)
        self.lengthpointsremove = lengthfolder.get("pointsremove", 1)
        self.lengthpointsadd = lengthfolder.get("pointsadd", 0)
        self.lengthreason = lengthfolder.get("reason", "Password is lower than " + str(self.lengthrequirement) + " characters")

    charactertypesfolder = configuration.get("charactertypes")
    if consecutivelettersfolder != None: 
        self.charactertypesenabled = charactertypesfolder.get("enabled", True)
        self.charactertypesrequirement = charactertypesfolder.get("requirement", 8)
        self.charactertypespointsremove = charactertypesfolder.get("pointsremove", 1)
        self.charactertypespointsadd = charactertypesfolder.get("pointsadd", 0)
        self.charactertypesreason = charactertypesfolder.get("reason", "Only "+ str(self.charactertypesrequirement) +" type of Character")

        datefolder = configuration.get("date")
    if consecutivelettersfolder != None: 
        self.dateenabled = datefolder.get("enabled", True)
        self.datepointsremove = datefolder.get("pointsremove", 1)
        self.datepointsadd = datefolder.get("pointsadd", 0)
        self.datereason = datefolder.get("reason", "Only "+ str(self.charactertypesrequirement) +" type of Character")





    # Finish off the code /: Have fun don't stay up lates


 def _detect(self, password:str, reason:bool = False):
    reasons = []
    points = self.startingnumber
    passwordlower = password.lower().strip()

    # CHECKING FOR COMMON LAYOUTS
    if self.commonlayoutenabled == True:
        alreadysetpatternsreasons = False
        alreadysetpatternsadd = False
        for icommon in commonlayouts:
          
          for i in range(len(icommon) - 2):
            substr = icommon[i:i+self.commonlayoutminimin-1]

            if substr in passwordlower:
             if alreadysetpatternsreasons == False:
                if reason == True:
                    reasons.append(self.commonlayoutreason)

                points -= self.commonlayoutpointsremove
                alreadysetpatternsreasons = True
                print("remove")
                

            else:
                    if alreadysetpatternsadd == False:
                        points += self.commonlayoutpointsadd
                        alreadysetpatternsadd = True
                        print("addlayout")
        
            

    # CHECKING FOR COMMON WORDS
    if self.commonwordsenabled == True:
     with open('src/commonpasswords/commonwords.txt', 'r') as file:
        alreadysetcommonwordsreasons = False
        alreadysetcommonwordsadd = False
        for line in file:
                if line.strip() in passwordlower:
                    if reason == True and alreadysetcommonwordsreasons == False:
                        reasons.append(self.commonwordsreason)
                        alreadysetcommonwordsreasons = True
                    points -= self.commonwordspointsremove
                    break
                elif alreadysetcommonwordsadd == False:
                    points += self.commonwordspointsadd
                    alreadysetcommonwordsadd = True
                    print("addwords")



# Checking for consecutive letters
    if self.consecutivelettersenabled == True:
        match = re.search(consecutiveletterspattern, passwordlower)
        if match:
            if reason == True:
                reasons.append(self.consecutivelettersreason)
            points -= self.consecutivelettersremove
        else:
            points += self.consecutivelettersadd
        
# Check if less than 8 characters
    if self.lengthenabled == True:
        if len(password) < self.lengthrequirement:
            points -= self.lengthremove
            if reason == True:
                reasons.append(self.lengthreason)
        else:
            points += self.lengthadd

# Detects for more than a certain amount of text catagories
    if self.charactertypesenabled == True:
        CatagoryaCount = 0
        if re.search(letterspattern, passwordlower):
            CatagoryaCount += 1
        if re.search(digitpattern, passwordlower):
            CatagoryaCount += 1
        if re.search(specialpattern, passwordlower):
            CatagoryaCount += 1
        if CatagoryaCount == self.charactertypesrequirement:
            points -= self.charactertypesremove
            if reason == True:
                reasons.append(self.charactertypesreason)
        else:
            points += self.charactertypesadd

    if self.dateenabled == True:
     if re.search(datepattern, password):
        points -= self.dateremove
        if reason == True:
            reasons.append(self.datereason)
     else: 
        points += self.dateadd
        
    

         
    

    if reason == True:
        return [points, reasons]
    else:
        return points
    
mainclass = main()
def configure(configuration:dict):
    return mainclass._configure(configuration)
def detect(password:str, reason:bool = False):
    return mainclass._detect(password, reason)
    
