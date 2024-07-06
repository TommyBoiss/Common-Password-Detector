import commonpasswords
commonpasswords.configure({ "startingpoints": 10,
"commonlayout": {
  "enabled": True,
  "pointsremove": 5,
  "pointsadd": 2,
  "reason": "testing"
},
"commonwords": {
  "enabled": True,
  "pointsremove": 5,
  "pointsadd": 2,
  "reason": "test"
}

})
def question():
    print(commonpasswords.detect(input("Password\n"), True))
    question()
question()

