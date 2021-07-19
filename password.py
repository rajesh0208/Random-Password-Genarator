import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(97,122))
specialcharacter=chr(random.randint(33,47))
number=chr(random.randint(48,57))
specialcharacter1=chr(random.randint(58,64))
password = uppercaseLetter1 + uppercaseLetter2+number+specialcharacter+specialcharacter1
password = shuffle(password)


print(password)
