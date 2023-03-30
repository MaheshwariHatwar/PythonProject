class BasePasswordManager:
    def __init__(self,old_password):
        self.old_password = old_password
        
        
    def get_password(self):
        
        print(self.old_password[-1])
        
        
    def is_correct(self, password):
        if password == self.old_password[-1] :
            print(True)
        else:
             print(False)

class PasswordManager(BasePasswordManager):

    def __init__(self,old_password):
        BasePasswordManager.__init__(self,old_password)
    
    def get_level(self):
        if self.old_password[-1].isalpha() or self.old_password[-1].isdigit():
            print('Level-0')
        elif self.old_password[-1].isalnum():
            print('Level-1')
        else:
            print('Level-2')
    
    def set_password(self):
    
        if self.old_password[-1].isalpha() or self.old_password[-1].isdigit():
            print("password is not strong")
            y=1
        elif self.old_password[-1].isalnum():
            y=2
        else:
            y=3
    
        while(True):
            k=input('\nPlease input a Strong Password:')
            if k.isalpha() or k.isdigit():
                z=1
            elif k.isalnum():
                z=2
            else:
                z=3
                if len(k)>=6 and z==3:
                    break
                elif len(k)>=6 and z>y:
                    break
                else:
                    print('\nPassword Not Set!Required a password of higher level than you previous password.')
                    print('\nNew Password Set!')
        self.old_password.append(k)
    
x = ['Alpha123', 'Betabeta', '123456']
    
current = PasswordManager(x)
    
current.get_password()
a=input('Please type in your password to verify:')
current.is_correct(a)
current.get_level()
current.set_password()
current.get_password()
