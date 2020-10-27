import sys, re
probNum = int(sys.argv[1])
solutions = []
solutions.append("/^0$|^100$|^101$/") #31
solutions.append("/^[01]+$/") #32
solutions.append("/0$/") #33
solutions.append("/\w*[aeiou]\w*[aeiou]\w*/i") #34 
solutions.append("/^0$|^1[01]*0$/") #35
solutions.append("/^[01]*110[01]*$/") #36
solutions.append("/^.{2,4}$/") #37
solutions.append("/^[0-9]{3} *-? *[0-9]{2} *-? *[0-9]{4}$/") #38
solutions.append("/^.*?d/im") #39
solutions.append("/^11*0[10]*1$|^00*1[10]*0$/") #40
solutions.append(r"/\b[pck]\w*/i") #41
solutions.append("/^.(..)*$/s") #42
solutions.append("/^(0([01][01])*|1[01]([01][01])*)$/") #43
solutions.append("/^0*(10+)*$/") #44 
solutions.append("/^[.XO]{64}$/i") #45
solutions.append("/^[XO]*[.][XO]*$/i") #46
solutions.append("/(^XX*O+[.]|[.]O+X*X$)/i|^[.]|[.]$/") #47
solutions.append("/^([bc]+a?[bc]*|[bc]*a[bc]*)$/") #48
solutions.append("/^([bc]+(a[bc]*a)*[bc]*|[bc]*(a[bc]*a)+[bc]*)$/") #49
solutions.append("/[02]*(1[02]*1)*[02]*/") #50
solutions.append(r"/(.)\1{9}/s") #51
solutions.append(r"/(\w)\w*\1/i") #52
solutions.append(r"/(\w)+\1\w*/") #53
solutions.append(r"/(\w)+\w*\1\w*/") #54
solutions.append(r"/^(0|1)[10]*\1$/") #55
problems = {x+31:sol for x, sol in enumerate(solutions)}
print(problems[probNum])
