
class WizardPlayer:
    
    def __init__(self, name="anonym", age=0):
        self.name = name
        self.age = age

    def attack(self):
        return "utok 1. stupne"

    
class HeadWizard(WizardPlayer):

    def __init__(self, type, name, age):
        super().__init__(name, age)
        self.type = type

    def attack(self):
        return "utok 2. stupne"

    def avada_kedavra(self):
        return "Avada Kedavra"

# player1 = WizardPlayer("david", 35)

# print(player1.attack())

# print(" -------------------")
player2 = HeadWizard("good", "david", 35)
print(player2.type)
print(player2.name)
print(player2.age)


print(dir(player2))



# print(player2.age)
# print(player2.attack())
# print(player2.avada_kedavra())

# print("-----------")

# print(isinstance(player1, WizardPlayer))