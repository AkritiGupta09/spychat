from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime

print ("Welcome to spychat!! let's get started")

NEW_USER_DEATAILS=[]
STATUS_MSG_LIST=['On Mission','JAMES BOND','SHERLOCK HOLMES','DETECTING','Spychat only']#creation of list containing status
FRIEND_DETAILS=[{'name':'shefali','age':21,'rating':5.6,'online':True,'chats':[]},{'name':'shivani','age':22,'rating':4.5,'online':True,'chats':[]}]



def select_a_frnd():#func creation to select a frnd
    sr_no=1
    for frnd in FRIEND_DETAILS:
        print str(sr_no)+"."+frnd['name']
        sr_no=sr_no+1

    choose_frnd=input("Choose a friend:")
    actual_frnd=FRIEND_DETAILS[choose_frnd-1]
    #print "The message will be sent to" + actual_frnd####error

    return actual_frnd

def send_a_msg():#func created to send a msg
    chosen_frnd_to_send=select_a_frnd()
    original_img=raw_input("Write a name of the image with which you to encode the image:")
    secret_msg=raw_input("Write the message which you want to encrypt:")
    output_path="OUTPUT.jpeg"
    Steganography.encode(original_img,output_path,secret_msg)

    user_chat={'message':secret_msg,'time_of_msg':datetime.now(),'sender_you':True}#dic creation for timestamp
    print "MESSAGE IS ENCRYPTED!"

    FRIEND_DETAILS[chosen_frnd_to_send]['chats'].append(user_chat)

def read_a_msg():#funccreated to send a msg
    chosen_frnd_to_read=select_a_frnd()
    output_img_name=raw_input("Select the image from which data is to be decoded:")
    decrypted_text=Steganography.decode(output_img_name)

    user_chat = {'message': output_img_name, 'time_of_msg': datetime.now(), 'sender_you': False}  # dic creation for timestamp
    FRIEND_DETAILS[chosen_frnd_to_read]['chats'].append(user_chat)

    print 'Your decoded message is:' + decrypted_text


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

    frnd = {'salutation': '', 'name': '', 'age': 0, 'rating': 0.0, 'online': 'True'}  # dictionary creation

    frnd['name']=raw_input("What is your name?")#asking for details n appending them
    frnd['salutation']=raw_input("What should I call you? mr ms dr er")
    frnd['salutation']=frnd['salutation'].upper()
    frnd['name']=frnd['salutation']+"."+frnd['name']
    frnd['age']=input("What is you age?")
    frnd['rating']=input("Tell me your rating")
    frnd['online']=True

    if len(frnd['name'])>2 and 50>=frnd['age']>=12 and frnd['rating']>=spy['rating']:
        FRIEND_DETAILS.append(frnd)

    else:
        print"The details entered do not meet the requirement to be your friend"

    return len(FRIEND_DETAILS)



def spychat(spy_salutation,spy_name,spy_age,spy_rating):#func creation
    current_status_msg = None

    menu_choice_defaultuser = raw_input("Do you want to continue as default user?Y N")  # menuchoice creation for dfault user
    if menu_choice_defaultuser.upper()=='Y':
        print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f" % (spy_salutation,spy_name,spy_age,spy_rating))

    elif menu_choice_defaultuser.upper()=='N':
        print "Let's create a new user"#creation of new user

        new_user={'username':'','userage':0,'userrating':0.0}#dic for newuser

        new_user['username']=raw_input("What is your name?")
        new_user['userage']=input("Enter your age")
        if new_user['userage']>12 and new_user['userage']<50:
            print"You are of appropriate age."#for new user's age
            new_user['userrating']=input("Tell us your rating")
            if new_user['userrating']==10.0:
                print("You seem to be very intelligent")
            elif new_user['userrating']>=8.0:
                print("You seem to be a good spy")
            elif new_user['userrating']>=5:
                print("You seem to be more than average spy")
            elif new_user['userrating']<5 and new_user['userrating']>=4:
                print("You seem to be an average spy")
            elif new_user['userrating']==3:
                print("You seem to be below average spy")
            else:
                print("You really need to improve")

            print  ("Your details are:\n Name= %s Age:%d Rating:%.3f"% (new_user['username'],new_user['userage'],new_user['userrating']))
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
    spychat(spy['salutation'],spy['name'],spy['age'],spy['rating']) #func called


elif ask_user.upper()=='N':

    spy = {'salutation': '', 'name': '', 'age': 0, 'rating': 0.0}  # dictionary creation

    spy['name']=raw_input("what is your name?")#asking for details
    if len(spy['name'])>=4:
        print("Hi! "+spy['name'])

        spy['salutation']=raw_input("Fill your salutation:mr ms dr er")
        spy['salutation']=spy['salutation'].upper()

        spy['age']=input("How old are you?")
        if spy['age']>12 and spy['age']<50:
            print "You are of appropriate age"

            spy['rating']=input("Tell me your rating")
            if spy['rating']==10.0:
                print("You seem to be very intelligent")
            elif spy['rating']>=8.0:
                print("You seem to be a good spy")
            elif spy['rating']>=5:
                print("You seem to be more than average spy")
            elif spy['rating']<5 and spy['rating']>=4:
                print("You seem to be an average spy")
            elif spy['rating']==3:
                print("You seem to be below average spy")
            else:
                print("You really need to improve")
            print("Your details are:\n Name= %s.%s Age:%d Rating:%.3f"% (spy['salutation'],spy['name'],spy['age'],spy['rating']))#final print of details
            spychat(spy['salutation'], spy['name'], spy['age'], spy['rating'])#func call
        else:
            print("You are retired now as your age is invalid")
    else:
        print("Plz enter the name of atleast 4 alphabets ")
else:
    print ("You have made an invalid entry.")#current user invalid option