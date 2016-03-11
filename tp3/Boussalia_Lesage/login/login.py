import re

class AlreadyUsedError(Exception):
    pass

class ToLongLoginError(Exception):
    pass

class NoMinASCIIError(Exception):
    pass

class NeedAdminDecisionForLoginError(Exception):
    pass

class LoginCreator:
    def __init__(self, dataAccess):
        self.dataSystem= dataAccess

    def calculate_new_login(self, name, first_name,secondTry=False):
        if secondTry:
            return name[0:7]+first_name[0]
        return name[0:8]
        

    def create_login(self, name,first_name,login):
        if len(login)>8:
            raise ToLongLoginError()
        if re.match(r"^[a-z]{1,}$", login) ==None:
            raise NoMinASCIIError()
        if self.dataSystem.exist(login):
            raise AlreadyUsedError()
        return self.dataSystem.createUser(login, name, first_name);

    def create_login_auto(self, name, first_name,secondTry=False):
        try:
            login= self.calculate_new_login(name, first_name, secondTry)
            return self.create_login(name, first_name, login)
        except AlreadyUsedError :
            if (secondTry):
                raise NeedAdminDecisionForLoginError()
            return  self.create_login_auto(name, first_name,True)
        except NoMinASCIIError :
            raise  NoMinASCIIError()

#class User:
#    def __init__(self, login, name, first_name):
#        self.login= login
#        self.name=name
#        self.first_name=first_name
