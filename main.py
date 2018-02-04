
from spy_details import spy_salutation,spy_name,spy_age,spy_rating
print ("Welcome to spychat!! let's get started")

def spychat(spy_salutation,spy_name,spy_age,spy_rating):#func creation
    menu_choice=raw_input("Do you want to continue as default user?Y N")
    if menu_choice.upper()=='Y':
        print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f" % (spy_salutation, spy_name, spy_age, spy_rating))
    elif menu_choice.upper()=='N':
        print "Let's create a new user"#creation of new user
        user1_name=raw_input("What is your name?")
        user1_age=input("Enter your age")
        if user1_age>12 and user1_age<50:
            print"You are of appropriate age."#for new user's age
            user1_rating=input("Tell us your rating")
            if spy_rating==10.0:
                print("You seem to be very intelligent")
            elif spy_rating>=8.0:
                print("You seem to be a good spy")
            elif spy_rating>=5:
                print("You seem to be more than average spy")
            elif spy_rating<5 and spy_rating>=4:
                print("You seem to be an average spy")
            elif spy_rating==3:
                print("You seem to be below average spy")
            else:
                print("You really need to improve")

            print  ("Your details are:\n Name= %s Age:%d Rating:%.3f"% (user1_name,user1_age,user1_rating))
        else:
            print ("We are sorry but you are retired now")#for new user
    else:
        print "Please choose a valid menu choice"

ask_user=raw_input("Are you a current user? Y  N")
if ask_user.upper() == 'Y':
    print("We already have your details as you are a current user. ")
    spychat(spy_salutation,spy_name,spy_age,spy_rating) #func called


elif ask_user.upper()=='N':

    spy_name=raw_input("what is your name?")#asking for details
    if len(spy_name)>=4:
        print("Hi! "+spy_name)
        spy_salutation=raw_input("Fill your salutation:mr ms dr er")
        spy_salutation=spy_salutation.upper()
        spy_age=0
        spy_age=input("How old are you?")
        if spy_age>12 and spy_age<50:
            print "You are of appropriate age"

            spy_rating=0.0
            spy_rating=input("Tell me your rating")
            if spy_rating==10.0:
                print("You seem to be very intelligent")
            elif spy_rating>=8.0:
                print("You seem to be a good spy")
            elif spy_rating>=5:
                print("You seem to be more than average spy")
            elif spy_rating<5 and spy_rating>=4:
                print("You seem to be an average spy")
            elif spy_rating==3:
                print("You seem to be below average spy")
            else:
                print("You really need to improve")
            print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f"% (spy_salutation,spy_name,spy_age,spy_rating))#final print of details
        else:
            print("You are retired now as your age is invalid")
    else:
        print("Plz enter the name of atleast 4 alphabets ")
else:
    print ("You have made an invalid entry.")#current user invalid option