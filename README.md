# Common Password Dectetor
Hello this is a project that I've worked on because I'm board! Anyway the purpose is to detect the security of an inputted password
checking for common patterns and common passwords.
## Warning
This is just a passion project and I would highly reccomend using an actual Common Password Detector in an real environment, or use another project ontop of this.
# Requirements
`Python 3.12` [Link](https://www.python.org/downloads/release/python-3120/)
# Quick Start
`1:` **Install the package:**
`[Insert Here]` 
`2.` **Import the library into your script:**
```
import commonpasswords
```
`3.` **Use the Detect function:**
```
import commonpasswords
commonpasswords.detect("[password]", True/False)
```
# Detect Function
The function "dectect" detects if the inputted password is common or unsecure
```
commonpasswords.detect([The password your trying to detect], [True/False Returns the reasons that is reduced points in a table])
Output: [Points, [Reasons]]
```

# Configure
The configure function allows you to customize the library more! Running this function before the detect function isn't required.
*If data isn't entered here is will just resort to its default with no harm*
```
{
"startingpoints": Int

"commonlayout": {
  "enabled": bool, # (Enabled?)
  "pointsremove": Int, # (How many points to remove if the check fails)
  "pointsadd": Int, # (How many points to add if the check passes)
  "reason": Str, # (If the check fails what is the reason it failed)
}

}
```

