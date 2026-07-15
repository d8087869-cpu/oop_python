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

#4
class UserProfile:
    def __init__(self,username):
        self.__username = username
        self.__followers = 0
    @property
    def followers(self):
        return self.__followers
    def follow(self):
        self.__followers = self.__followers + 1 
    def unfollow(self):
        if self.__followers > 0:
            self.__followers = self.__followers -1 
profile = UserProfile('charlie')
profile.follow()
profile.follow()
profile.follow()
profile.unfollow()
print(profile.follow)

#5
class UserProfile:
    def __init__(self,username,bio):
        self.username = username
        self._bio=bio
    @property
    def bio(self):
        return self._bio
class VerifiedUser(UserProfile):
    def __init__(self, username, bio,badge):
        super().__init__(username, bio)
        self.badge =badge 
    def full_description(self):
        print(f'{self.username} [{self.badge}]: {self.bio}')
user = VerifiedUser('celeb','singer and songwriter' , 'V')
user.full_description()

#6 
class UserProfile:
    def __init__(self,username,age):
        self.username = username
        self.__age = age 
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if new_age >= 13 and new_age <= 120:
            self.__age =new_age
        else:
            print('Invaled age.')
p = UserProfile('david', 26)
p.age = 10
p.age = 200
p.age = 25
print(p.age)

#7
class UserAccount:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    def check_password(self,attempt):
        if attempt == self.__password:
            return True
        else:
            return False
    def change_password(self,old,new):
        if old == self.__password:
            self.__password=new 
            print('password changed.')
        else: 
            print('incorrect old password')
account = UserAccount('admin' , 'secret')
print(account.check_password('worng'))
account.change_password('secret','new123')
print(account.check_password('new123'))

#8
class Post:
    def __init__(self,auther,contry):
        self.auther = auther
        self.contry = contry
        self.__likes = 0 
        self.__like_by = []
    @property 
    def likes(self):
        return self.__likes
    def like(self, username):
        if username not in self.__like_by:
            self.__like_by.append(username)
            self.__likes = self.__likes +1
    def unlike(self,username):
        if username in self.__like_by:
            self.__like_by.remove(username)
            self.__likes = self.__likes -1 
    def status(self):
        print(f'post by {self.auther}: {self.likes} likes')
post = Post('alice', 'hello world')
post.like('charlie')
post.like('david')
post.unlike('bob')
post.like('gabi')
post.status()

# 9  
class UserProfile:
    def __init__(self,username):
        self.username = username
        self.__is_public = True
        self.__show_email= False
        self.__show_age = False
    @property
    def is_public(self):
        return self.__is_public
    @is_public.setter
    def is_public(self,value):
        if isinstance(value, bool):
            self.__is_public= value
        else:
             print("is_public must be True or False.")

    @property
    def show_email(self):
        return self.__show_email
    @show_email.setter
    def show_email(self, value):
        if isinstance(value, bool):
            self.__show_email = value
        else:
            print("show_email must be True or False.")

    @property
    def show_age(self):
        return self.__show_age
    @show_age.setter
    def show_age(self, value):
        if isinstance(value, bool):
            self.__show_age = value
        else:
            print("show_age must be True or False.")

    def privacy_summary(self):
        print(f"is_public: {self.__is_public} | show_email: {self.__show_email} | show_age: {self.__show_age}")

profile = UserProfile('david')
profile.show_email =True
profile.is_public = 'yes'
profile.privacy_summary()

#10 
class UserAccount:
    def __init__(self,username,email,password,age):
        self.__username = username
        self.__email=email
        self.__password=password
        self.__age = age
        self._login_count = 0
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_username):
        if len(new_username) >= 3:
            self.__username = new_username
        else:
            print('username too short')
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new_email):
        if '@' in new_email:
            self.__email =new_email
        else:
            print('invalid email')
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if new_age>= 13 and new_age <=120:
            self.__age=new_age
        else:
            print('invalid age')
    
    def password(self,old,new):
        if old == self.__password:
            self.__password = new 
            print('password change')
        else:
            print('incorrect old password')
    def login(self,password):
        if password == self.__password:
            self._login_count = self._login_count +1 
            print('welcome')
        else:
            print('login failed')

    def account_summary(self):
        print(f'username {self.__username} | email: {self.__email} | age: {self.__age} | logins: {self._login_count}')
account= UserAccount('user1' , 'u@mail.com', 'pass123', 20)
account.login('worng1')
account.login('worng2')
account.login('pass123')
account.email = "newuser1@mail.com"
account.age = 25
account.account_summary()