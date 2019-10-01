import re

def validatePwd(pwds):
    pwdList = pwds.split(',')
    validated = []
    for i in pwdList:
        if len(i) >= 6 and len(i) <=12\
           and re.search('[a-z]',i)\
           and re.search('[A-Z]',i)\
           and re.search('[0-9]',i)\
           and re.search('[$#@]',i):
            validated = validated + [i]
        else:
            print("else")
    return validated

pwdStr = input("Please insert list of passwords (separated by comma)\n")
print(validatePwd(pwdStr))