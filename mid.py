import platform
# name="Jonny"
# address='1212 Rodman St'
# phone='312 312 3223'
# print("My name is "+name+","+ " My home adress is: " +address,"and phone nmber is: "+ phone)

# num=input("Enter number: ")
# x=float(num)
# num2=input("Enter number: ")
# y=float(num2)
# sum=x+y
# print(sum)
# side1=input("Enter the long: ")
# length=float(side1)
# side2=input("Enter second width: ")
# width=float(side2)
# square=length*width

# print(square)

# triplequotes='''\nThis is the final desition to let you "GO", we are trully sorry for inconvinience'''
# print(triplequotes)

# tripleQuotesNextLine='''Geek
# Bored
# Strong'''
# print(tripleQuotesNextLine)
# set1=set()
# print("initial blank Set: ")
# print(set1)


# creatingMizSet=set([1,2,3,'Greece',4,'Portugal', 'German'])
# print(creatingMizSet)
# print(creatingMizSet[3])


# km=input("Enter number: ")
# x =float(km)
# mils=x*1.6
# mile_str=str(mils)
# meters=(int(x*1000))**2
# print("\n"+str(x))
# print ("Entered km: "+ km +" Equals to: "+ str(meters)+ " square meters")


# def km_to_miles(kilometers):
#     miles = float(kilometers *0.621371)
#     return miles



# distance_km=input("Enter distance in kilometers: ")
# converted_km=(float(distance_km))*km_to_miles
# print("\n This is distance in miles: "+ str(converted_km))





# number =int(input("First entrey: "))
# # convert_to_interger=int(number)
# # print(number)
# number_two= int(input('Second second number entry: '))
# #conversion_two=(((number_two))/number_two)**2
# conversion_two=number/number_two
# remainder_number= number%number_two
# print("This should be something: "+str(conversion_two)+ "\nThis is remaider: " + str(remainder_number))




#Get the length of the string
test_str="How long us this string?"
str_length= len(test_str)

print("test_str is: " + str(str_length) + " characters longs")
print(f"test_str is {str_length} characters longs")


txt="Rainy day is Florida"
text="Rainy\tday\tis\tFlorida"
txt2="Sometime We Get Hurricane"
upper_case=txt.upper()
lower_case=txt2.lower()
capitolize_str=lower_case.capitalize()
swap_case_in_string= capitolize_str.swapcase()
title_string=txt.title()
expand_tabs=text.expandtabs()
print("\n"+ upper_case,"\n" + lower_case, "\n"+ capitolize_str,"\n"+ swap_case_in_string,"\n"+ title_string,"\n" +expand_tabs)
print(txt.find("Florida"))


sentence= "I hope the Bears don't lose again tomorrow!"
replaced_version=sentence.replace("don't","start").replace("lose", "winning")
#replaced_two=replaced_version.replace("lose", "winning")
print(replaced_version)


name=input("Name: ")
address=input("Street Address: ")
phone=input("Phone Number: ")
print("\nMy name is "+name+ " and I live at "+address+ ". My phone number is "+phone)