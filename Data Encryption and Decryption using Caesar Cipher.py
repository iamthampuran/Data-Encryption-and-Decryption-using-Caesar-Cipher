plain_text = input("Enter the plain text: ")
key = int(input("Enter the key value: "))
ctext = ""
for i in plain_text:
  if i.isalpha() and i.isupper():
    i = chr((ord(i)+key-65)%26 + 65)
    ctext = ctext + i
  elif i.isalpha() and i.islower():
    i = chr((ord(i)+key-97)%26 + 97)
    ctext = ctext + i
    
  else:
    ctext = ctext + i
print("For the plain text",plain_text,"\nCipher Text = ",ctext)

ptext = ""
key2 = 0

for key2 in range(0,27):
  ptext = ""
  for i in ctext:
    if i.isalpha() and i.isupper():
      i = chr((ord(i) - key2 - 65)%26 + 65)
      ptext = ptext + i
    elif i.isalpha() and i.islower():
      i = chr((ord(i) - key2 - 97)%26 + 97)
      ptext = ptext + i
    else:
      ptext = ptext + i
  print('For the key ', key2,' the plain text is: ',ptext)    

