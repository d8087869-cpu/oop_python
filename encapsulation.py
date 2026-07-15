#1 
class UserProfile:
    def __init__(self,username):
        self.__username = username
    
    @property
    def username(self):
        return self.__username
profile = UserProfile('alice99')
print(profile.username)
#print(profile.__username)
#2
class UserProfile:
    def __init__(self,username,email):
        self.__username =username
        self.__email = email
    
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
profile = UserProfile("bob", "bob@mail.com")
print(profile.username)
print(profile.email)

#3
class UserProfile:
    def __init__(self,username):
        self.__username = username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_username):
        if len(new_username) >=3:
            self.__username = new_username
        else:
            print('username too short')
p = UserProfile('alice')
p.username = "ab"
p.username = "alexis"
print(p.username)