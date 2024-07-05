import re
commonlayouts = ["qwerty"]
consecutiveletterspattern = r'([a-zA-Z0-9])\1\1'
digitpattern = r"[0-9]"
letterspattern = r"[a-zA-Z]"
specialpattern = r'[!@#$%^&*()-+{}:"?/><,.;:]'
datepattern = r'[\d{4}]'


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
    self.datereason = "Only "+ str(self.charactertypesrequirement) +" type of Character"

 def _configure(self, configuration:dict):
    self.startingnumber = configuration.get("startingpoints", 0)

    commonlayoutfolder = configuration.get("commonlayout")

    if commonlayoutfolder != None: 
        self.commonlayoutenabled = commonlayoutfolder.get("enabled", True)
        self.commonlayoutpointsremove = commonlayoutfolder.get("pointsremove", 1)
        self.commonlayoutpointsadd = commonlayoutfolder.get("pointsadd", 0)
        self.commonlayoutreason = commonlayoutfolder.get("reason", "Contains common combination")

    commonwordsfolder = configuration.get("commonwords")
    if commonwordsfolder != None: 
        self.commonwordsenabled = commonwordsfolder.get("enabled", True)
        self.commonwordspointsremove = commonwordsfolder.get("pointsremove", 1)
        self.commonwordspointsadd = commonwordsfolder.get("pointsadd", 0)
        self.commonwordsreason = commonwordsfolder.get("reason", "Contains common words")

    # Finish off the code /: Have fun don't stay up lates


 def _detect(self, password:str, reason:bool = False):
    reasons = []
    points = self.startingnumber
    passwordlower = password.lower().strip()

    # CHECKING FOR COMMON LAYOUTS
    if self.commonlayoutenabled == True:
        alreadysetpatternsreasons = False
        for icommon in commonlayouts:
          
          for i in range(len(icommon) - 2):
            substr = icommon[i:i+3]

            if substr in passwordlower:
             if alreadysetpatternsreasons == False:
                if reason == True:
                    reasons.append(self.commonlayoutreason)

                points -= self.commonlayoutpointsremove
                alreadysetpatternsreasons = True
                print("remove")
                

            else:
                    points += self.commonlayoutpointsadd
        
            

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
                    alreadysetcommonwordsadd = True
                    break
        if alreadysetcommonwordsadd == True:
            points += self.commonwordspointsadd



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

    if re.search(datepattern, password):
        points -= 1
        if reason == True:
            reasons.append("Possibily contains a date")
        
    

         
    

    if reason == True:
        return [points, reasons]
    else:
        return points
    
mainclass = main()
def configure(configuration:dict):
    return mainclass._configure(configuration)
def detect(password:str, reason:bool = False):
    return mainclass._detect(password, reason)
    
