# fruit_manager.py

class FruitManager:
    def __init__(self):
        self.fruit_stock = {}

    def add_fruit(self, name, quantity):
        if name in self.fruit_stock:
            self.fruit_stock[name] += quantity
        else:
            self.fruit_stock[name] = quantity

    def view_fruit_stock(self):
        print("Fruit Stock:")
        for fruit, quantity in self.fruit_stock.items():
            print(f"{fruit}: {quantity} units")

    def update_fruit_stock(self, name, new_quantity):
        if name in self.fruit_stock:
            self.fruit_stock[name] = new_quantity
            print(f"{name} stock updated to {new_quantity} units")
        else:
            print(f"{name} is not in the stock.")


# customer.py

class Customer:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add Fruit to Stock")
            print("2. View Fruit Stock")
            print("3. Update Fruit Stock")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter fruit name: ")
                quantity = int(input("Enter quantity: "))
                self.manager.add_fruit(name, quantity)
                print(f"{quantity} {name} added to the stock.")

            elif choice == '2':
                self.manager.view_fruit_stock()

            elif choice == '3':
                name = input("Enter fruit name: ")
                new_quantity = int(input("Enter new quantity: "))
                self.manager.update_fruit_stock(name, new_quantity)

            elif choice == '4':
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = FruitManager()
    customer = Customer(manager)
    customer.run()
