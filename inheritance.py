class User():
    def sign_in(self,email):
        self._email = email

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power,email):
        User.__init__(self,email)
        # super().__init__(self,email)
        self._name = name
        self._power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self._num_arrows}')


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('robin', 500)

print(wizard1.attack())
print(archer1.attack())

print(isinstance(wizard1, Wizard))

# Polymorphism

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)
