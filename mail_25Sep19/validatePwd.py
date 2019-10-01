def validatePwd(pwds):
    pwdList = pwds.split(',')
    validated = []
    for i in pwdList:
        lower = False
        upper = False
        nr = False
        schar = False
        if len(i) >= 6 and len(i) <= 12:
            for j in i:
                if j.islower():
                    lower = True
                if j.isupper():
                    upper = True
                if j.isnumeric():
                    nr = True
                if j == '$' or j == '#' or j == '@':
                    schar = True
            if lower and upper and nr and schar:
                validated = validated + [i] 
    return validated

print("Please insert the list of passwords (separated by comma)")
pwdStr = input()
print(validatePwd(pwdStr))