from datetime import datetime

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.online=True
        self.chats=[]
        self.current_status_msg=None

spy=Spy("akriti","ms",22,0.1)

friend_one=Spy("shefali",'ms',20,3.4)
friend_two=Spy("shivani",'ms',22,3.2)
friend_three=Spy("arshia",'ms',25,5.4)

FRIEND_DETAILS=[friend_one,friend_two,friend_three]


class Newuser:
    def __init__(self,newuser_name,newuser_age,newuser_rating):
        self.newuser_name=newuser_name
        self.newuser_age=newuser_age
        self.newuser_rating=newuser_rating

class Friend:
    def __init__(self,salutation,name,age,rating,online):
        self.salutation=salutation
        self.name=name
        self.age=age
        self.rating=rating
        self.online=online


class Chatmsgs:
    def __init__(self,secret_msg,time_of_msg,sender_you):
        self.secret_msg=secret_msg
        self.time_of_msg=time_of_msg
        self.sender_you=sender_you
