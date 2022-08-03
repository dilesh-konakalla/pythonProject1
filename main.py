# class TrainTicket:
#     print("\n\nTicket Booking System\n")
#
#     def Ticket (self):
#                 people = int(input("\nEnter no. of Tickets : "))
#                 name_l = []
#                 age_l = []
#                 sex_l = []
#                 for p in range(people):
#
#                     name = str(input("\nName : "))
#                     name_l.append(name)
#                     age = int(input("\nAge  : "))
#                     age_l.append(age)
#                     sex = str(input("\nMale or Female : "))
#                     sex_l.append(sex)
#
#                 restart = str(input("\nDid you forgot someone? y/n: "))
#                 if restart in ('y', 'YES', 'yes', 'Yes'):
#                     restart = 'Y'
#                 else:
#                     x = 0
#                     print("\nTotal Ticket : ", people)
#                     for p in range(1, people + 1):
#                         print("Ticket : ", p)
#                         print("Name : ", name_l[x])
#                         print("Age  : ", age_l[x])
#                         print("Sex : ", sex_l[x])
#                         print("price", 700)
#
#                         x = x + 1
#
#
# class Showing(TrainTicket):
#
#     def show(self):
#      print("Thanks for booking")
#
# o = Showing();
# o.Ticket()
# o.show()
# print(" booking successfull")






























import re
txt = "use of python in machine learning"
x= re.search("use.*learning$",txt)
if(x):
    print(" yes ")
else:
    print("no ")
y=re.findall("in",txt)
print(y)
searchObj = re.search("\s",txt)
print(" the white spaced character is locatesd ")