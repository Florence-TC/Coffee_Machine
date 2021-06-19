class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.user_input = None

    def remaining(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money''')

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        user_choice = input()
        if user_choice == "1":
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
            elif self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
        elif user_choice == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
            elif self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.coffee < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
        elif user_choice == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
            elif self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.coffee < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
        elif user_choice == "back":
            pass

    def fill(self):
        print('Write how many ml of water you want to add:')
        self.water += int(input())
        print('Write how many ml of milk you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans you want to add:')
        self.coffee += int(input())
        print('Write how many disposable coffee cups you want to add:')
        self.cups += int(input())

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            user_input = input()
            if user_input == 'buy':
                self.buy()
            elif user_input == 'fill':
                self.fill()
            elif user_input == 'take':
                self.take()
            elif user_input == 'remaining':
                self.remaining()
            elif user_input == 'exit':
                break


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.action()
