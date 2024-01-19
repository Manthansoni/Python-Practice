# Format of code
class NameOfClass():
    class_attribute = 'value'
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        #code
    
    @ 
    def cls_method(cls,param1, param2):
        #code

    @staticmethod
    def stc_method(param1,param2):
        #code

# actual code
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print('run')

    @classmethod
    def adding_things(cls,num1,num2):
        '''
            add
        '''
        return cls('Teddy',num1 + num2)

    @staticmethod
    def adding_things1(num1,num2):
        '''
        add
        '''
        return num1 * num2


player1 = PlayerCharacter('Manthan',21)

print(PlayerCharacter.adding_things(10,20))

print(player1.name)
