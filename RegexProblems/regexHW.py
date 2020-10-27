import sys, re
probNum = int(sys.argv[1])
solutions = ["/^(0|100|101)$/", "/^[01]+$/", "/0$/", "/\w*[aeiou]\w*[aeiou]\w*/i", "/^1[01]*0$/", "/^1[01]*110[01]*$/", "/^.{2,4}$/","/^[0-9]{3} *-? *[0-9]{2} *-? *[0-9]{4}$/", "/^.*?d/im", "/^11*0[10]*1$/"]
problems = {x+31:sol for x, sol in enumerate(solutions)}

print(problems[probNum])
