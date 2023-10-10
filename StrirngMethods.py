# name=input("Name: ").upper()
# address=input("Street Address: ").upper()
# phone=input("Phone Number: ").upper()
# myNameIs="My name is: "
# myAddress="and I live at "
# myPhone="My phone number "
# print((myNameIs + name + myAddress+address + myPhone +phone).title())




firstSentence= "hello, my name is Baha. "
name=firstSentence.split('is')
upperName=name[1]
uppername2=name[0]
print(upperName)
print(uppername2)
secondSentence="i was boen in California, but now I live in Chicago. "
thirdSentence="i have also lived in Spain, Turkey, and Dubai. "
fourthSetece="my wife is form turkey. "
fifthsemtence="i have two sons: one is 12, and the other 18."

print(uppername2.capitalize()+upperName.capitalize()+secondSentence.capitalize()+thirdSentence.capitalize()+fourthSetece.capitalize()+fifthsemtence.capitalize())
x=True