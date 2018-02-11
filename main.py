from spy_details import spy_salutation,spy_name,spy_age,spy_rating
print ("Welcome to spychat!! let's get started")

STATUS_MSG_LIST=['On Mission','JAMES BOND','SHERLOCK HOLMES','DETECTING','Spychat only']#creation of list containing status
FRIEND_NAME=[]
FRIEND_AGE=[]
FRIEND_RATING=[]
FRIEND_ONLINE=[]

def add_status(current_status_msg):#func creation for adding status
    if current_status_msg == None:
        print ("You don\'t have any status right now")
    else:
        print "Your current status is"+" "+current_status_msg

    user_status_choice=raw_input("Do you want to select from older status?Y N")
    if user_status_choice.upper() =='Y':

        sr_no=1
        for all_status in STATUS_MSG_LIST:
            print str(sr_no)+"."+ all_status
            sr_no=sr_no+1
        choose_status = input("From the given choices,which one do you want to put now?")
        put_status=STATUS_MSG_LIST(choose_status-1)


    elif user_status_choice.upper() =='N':
        put_status=raw_input("Create a new status :")
        STATUS_MSG_LIST.append(put_status)
    else:
        print "Invalid choice "
    return put_status #return the status to be put


def add_friend():#func creation for adding frnd
    frnd_name=raw_input("What is your name?")#asking for details n appending them
    frnd_salutation=raw_input("What should I call you? mr ms dr er")
    frnd_salutation=frnd_salutation.upper()
    frnd_name=frnd_salutation+"."+frnd_name
    frnd_age=input("What is you age?")
    frnd_rating=input("Tell me your rating")
    frnd_online=True

    if len(frnd_name)>2 and 50>=frnd_age>=12 and frnd_rating>=spy_rating:
        FRIEND_NAME.append(frnd_name)
        FRIEND_AGE.append(frnd_age)
        FRIEND_RATING.append(frnd_rating)
        FRIEND_ONLINE.append(True)
    else:
        print"The details entered do not meet the requirement to be your friend"

    return len(FRIEND_NAME)



def spychat(spy_salutation,spy_name,spy_age,spy_rating):#func creation
    current_status_msg = None

    menu_choice_defaultuser = raw_input("Do you want to continue as default user?Y N")  # menuchoice creation for dfault user
    if menu_choice_defaultuser.upper()=='Y':
        print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f" % (spy_salutation, spy_name, spy_age, spy_rating))

    elif menu_choice_defaultuser.upper()=='N':
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

    show_menu = True #menucoice creation for features
    while show_menu:
        menu_choice_for_features = input(
            "Which feature do you want to explore?\n 1.Add a status update\n 2.Add a friend\n 3.Send a secret message\n 4.Read a secret message\n 5.Read chats from a user\n 6.Close application\n")
        if menu_choice_for_features == 1:
            updated_status_msg = add_status(current_status_msg)#addstatus func call
            print "YOUR STATUS:" + updated_status_msg
        elif menu_choice_for_features == 2:
            updated_frnds=add_friend()#addfriend func call
            print "The no of friends are"+" "+str(updated_frnds)
        elif menu_choice_for_features == 3:
            print "3"
        elif menu_choice_for_features == 4:
            print "4"
        elif menu_choice_for_features == 5:
            print "5"
        elif menu_choice_for_features == 6:
            show_menu = False
        else:
            print "Invalid choice for features"

ask_user=raw_input("Are you a current user? Y  N")#asking for default user or new one
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
            spychat(spy_salutation, spy_name, spy_age, spy_rating)
        else:
            print("You are retired now as your age is invalid")
    else:
        print("Plz enter the name of atleast 4 alphabets ")
else:
    print ("You have made an invalid entry.")#current user invalid option