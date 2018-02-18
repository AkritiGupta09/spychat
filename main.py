from spy_details import spy,FRIEND_DETAILS
from spy_details import Spy,Chatmsgs,Newuser,Friend
from steganography.steganography import Steganography
from datetime import datetime
import time
import csv


print ("Welcome to spychat!! let's get started")

STATUS_MSG_LIST=['On Mission','JAMES BOND','SHERLOCK HOLMES','DETECTING','Spychat only']#creation of list containing status

def load_friends():
    with open('friends1.csv','rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            if row:
                name=row[0]
                salutation=row[1]
                age=row[2]
                rating=[3]
                spy=Spy(name,salutation,age,rating)
                FRIEND_DETAILS.append(spy)
load_friends()

def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[1:]:
            if row:
                secret_msg=row[0]
                time=row[1]
                sender_you=row[2]
                print "Chats are:"+secret_msg+" "+time+" "+sender_you
load_chats()

def select_a_frnd():#func creation to select a frnd
    sr_no=1
    for frnd in FRIEND_DETAILS:
        print str(sr_no)+"."+frnd.name
        sr_no=sr_no+1

    choose_frnd=input("Choose a friend:")
    actual_frnd=choose_frnd-1

    return actual_frnd

def send_a_msg():#func created to send a msg
    chosen_frnd_to_send=select_a_frnd()
    print "The msg will be sent to:" +" " +FRIEND_DETAILS[chosen_frnd_to_send].name
    original_img=raw_input("Write a name of the image with which you to encode the image:")
    secret_msg=raw_input("Write the message which you want to encrypt:")
    output_path="OUTPUT.jpeg"
    Steganography.encode(original_img,output_path,secret_msg)
    time=datetime.now()
    sender_you=True

    user_chat=Chatmsgs(secret_msg,time,sender_you)#objct creation
    print "MESSAGE IS ENCRYPTED!"+"at"+time.strftime("%a ,%d %m %Y, %H:%M")
    FRIEND_DETAILS[chosen_frnd_to_send].chats.append(user_chat)

    with open('chats.csv', 'a') as chats_data:#save to csv
        writer = csv.writer(chats_data)
        writer.writerow([FRIEND_DETAILS[chosen_frnd_to_send],secret_msg,time])


def read_a_msg():#funccreated to send a msg
    chosen_frnd_to_read=select_a_frnd()
    print "You are reading from "+" "+ FRIEND_DETAILS[chosen_frnd_to_read].name
    output_img_name=raw_input("Select the image from which data is to be decoded:")
    decrypted_text=Steganography.decode(output_img_name)
    time=datetime.now()
    sender_you=False
    user_chat=Chatmsgs(decrypted_text,time,sender_you)#objctcreation
    print 'Your decoded message is:' + decrypted_text
    FRIEND_DETAILS[chosen_frnd_to_read].chats.append(user_chat)


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
        put_status=STATUS_MSG_LIST[choose_status-1]


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
    frnd_name=frnd_salutation+"."+" "+frnd_name
    frnd_age=input("What is you age?")
    frnd_rating=input("Tell me your rating")
    frnd_online=True

    if len(frnd_name)>2 and 50>=frnd_age>=12 and frnd_rating>=spy.rating:

        frnd = Friend(frnd_salutation,frnd_name,frnd_age,frnd_rating,frnd_online)  # object creation
        FRIEND_DETAILS.append(frnd)

        with open('friends1.csv', 'a') as friends_data:
            writer=csv.writer(friends_data)
            writer.writerow([frnd.name,frnd.age,frnd.rating,frnd.online])
    else:
        print"The details entered do not meet the requirement to be your friend"

    return len(FRIEND_DETAILS)



def spychat(spy_salutation,spy_name,spy_age,spy_rating):#func creation
    current_status_msg = None

    menu_choice_defaultuser = raw_input("Do you want to continue as default user?Y N")  # menuchoice creation for dfault user
    if menu_choice_defaultuser.upper()=='Y':
        print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f" % (spy.salutation,spy.name,spy.age,spy.rating))

    elif menu_choice_defaultuser.upper()=='N':
        print "Let's create a new user"#creation of new user

        new_user=Newuser('',0,0.0)#object created for class Newuser

        new_user.newuser_name=raw_input("What is your name?")

        new_user.newuser_age=input("Enter your age")
        if new_user.newuser_age>12 and new_user.newuser_age<50:
            print"You are of appropriate age."#for new user's age

            new_user.newuser_rating=input("Tell us your rating")
            if new_user.newuser_rating==10.0:
                print("You seem to be very intelligent")
            elif new_user.newuser_rating>=8.0:
                print("You seem to be a good spy")
            elif new_user.newuser_rating>=5:
                print("You seem to be more than average spy")
            elif new_user.newuser_rating<5 and new_user.newuser_rating>=4:
                print("You seem to be an average spy")
            elif new_user.newuser_rating==3:
                print("You seem to be below average spy")
            else:
                print("You really need to improve")

            print  ("Your details are:\n Name= %s Age:%d Rating:%.3f"% (new_user.newuser_name,new_user.newuser_age,new_user.newuser_rating))
        else:
            print ("We are sorry but you are retired now")#for new user

    else:
        print "Please choose a valid menu choice"

    show_menu = True #menucoice creation for features
    while show_menu:
        menu_choice_for_features = input("Which feature do you want to explore?\n 1.Add a status update\n 2.Add a friend\n 3.Send a secret message\n 4.Read a secret message\n 5.Read chats from a user\n 6.Close application\n")
        if menu_choice_for_features == 1:
            updated_status_msg = add_status(current_status_msg)#addstatus func call
            print "YOUR STATUS:" + updated_status_msg
        elif menu_choice_for_features == 2:
            updated_frnds=add_friend()#addfriend func call
            print "The no of friends are"+" "+str(updated_frnds)
        elif menu_choice_for_features == 3:
            send_a_msg()
        elif menu_choice_for_features == 4:
            read_a_msg()
        elif menu_choice_for_features == 5:
            print "5"
        elif menu_choice_for_features == 6:
            show_menu = False
        else:
            print "Invalid choice for features"

ask_user=raw_input("Are you a current user? Y  N")#asking for default user or new one
if ask_user.upper() == 'Y':
    print("We already have your details as you are a current user. ")
    spychat(spy.salutation,spy.name,spy.age,spy.rating) #func called


elif ask_user.upper()=='N':

    spy=Spy('','',0,0.0)#object creation named spy for Spy class

    spy.name=raw_input("what is your name?")#asking for details
    if len(spy.name)>=4:
        print("Hi! "+spy.name)

        spy.salutation=raw_input("Fill your salutation:mr ms dr er")
        spy.salutation=spy.salutation.upper()

        spy.online=True
        spy.age=input("How old are you?")
        if spy.age>12 and spy.age<50:
            print "You are of appropriate age"

            spy.rating=input("Tell me your rating")
            if spy.rating==10.0:
                print("You seem to be very intelligent")
            elif spy.rating>=8.0:
                print("You seem to be a good spy")
            elif spy.rating>=5:
                print("You seem to be more than average spy")
            elif spy.rating<5 and spy.rating>=4:
                print("You seem to be an average spy")
            elif spy.rating==3:
                print("You seem to be below average spy")
            else:
                print("You really need to improve")
            print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f"% (spy.salutation,spy.name,spy.age,spy.rating))#final print of details
            spychat(spy.salutation, spy.name, spy.age, spy.rating)#func call
        else:
            print("You are retired now as your age is invalid")
    else:
        print("Plz enter the name of atleast 4 alphabets ")
else:
    print ("You have made an invalid entry.")#current user invalid option