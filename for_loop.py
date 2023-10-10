# #loops
# my_list=[1,2,2,3,3,3]
# print(my_list.index(2))

# students=["Bob", "Rob","Elli", "Nate"]
# for student in students:
#  #student_names= student
#  print(student)


# countries=["Spain","UAE","Turkey","Peru","Guatemala","Mexico","Algeria"]
# last_index=countries[-1]
# for each_country in countries:
#      print(each_country)



# sentence="Thank God it's Friday!"
# count=0
# for each_index in sentence:
#     count+= 1
# print(count)

    #use end ='' in print statement to beatify the output

# user_input=input("enter the letter: ")
# bears="The Chicago Bears Finally won last night"
# count=0
# for char in bears:
#     if user_input == char:
#         count+=1
# if count > 0
#     print(f"The letter'{user_input}\' appears '{count}\' times")
# else:
#     print("Entered letter does not appear in the string")
animal_list=["koala","cat","fox","panda","chipmank","sloth","penguin","dolphin"]
user_input=input("Enter animal name: ")
if user_input in animal_list:
    print(f"{user_input} is member of the lsit")
else:
    print("Not matching")