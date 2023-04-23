# """
# OOP
# object
# class
# """

# # we use the pascal naming convention

# class Brawlers:


#     #Constructor
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

    
#     # class methods
#     def run(self):
#         print('🏃🏽‍♂️')

#     def attack(self):
#         print('🤺')

#     def heal(self):
#         print('🚑')

#     def die(self):
#         life = False

#         return life
        


# poco = Brawlers('Poco', 'Play Guitar')
# poco.attack()
# poco.run()
# poco.heal()
# print('------------------')
# shelly = Brawlers('Shelly', 'Ultra shotgun')
# shelly.run()
# print('------------------')
# el_primo = Brawlers('El primo', 'Jump')
# el_primo.heal()
# print('------------------')
# # colt = Brawlers()
# # print(colt.die())





class User:

    basket = []

    def __init__(self, name, username, gender, email, number):
        self.name = name
        self.username = username
        self.gender = gender
        self.email = email

        self.number = number





    def get_detail(self):

        return f'Name: {self.name} \nUsername: {self.username} \nEmail: {self.email} \nNumber: {self.number} \n{self.gender}'
    

    def add_to_basket(self):
        product = input('Type a product: ')

        self.basket.append(product)

        print(f'{product} has been added.')



class Customer(User):
    pass



class Seller(User):
    pass

cust = Customer("zxcursed", "dotafag", "", "@gmail.com", "8 800 555 355")

seller = Seller("Lenin", "USSR top", "Male", "imCommunist@gmail.com", "8 927 475 33 05")


print(cust.username)
print(seller.email)