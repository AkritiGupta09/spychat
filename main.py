
from spy_details import spy_salutation,spy_name,spy_age,spy_rating
print ("Welcome to spychat!! let's get started")

def spychat(spy_salutation,spy_name,spy_age,spy_rating):
    print spy_salutation,spy_name,spy_age,spy_rating

#user=raw_input("Do you want to continue as a default user?Y N")
#if user.upper()=='Y':

ask_user=raw_input("Are you a current user? Y  N")
if ask_user.upper() == 'Y':
    print("We already have your details. ")
    spychat(spy_salutation,spy_name,spy_age,spy_rating) #func called


elif ask_user.upper()=='N':

    spy_name=raw_input("what is your name?")
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
            print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f"% (spy_salutation,spy_name,spy_age,spy_rating))
        else:
            print("You are retired now")
    else:
        print("Plz enter the name of atleast 4 alphabets ")
else:
    print ("you have made an invalid entry")