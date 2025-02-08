from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory: list = [Computer]

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def buy(self, computer: Computer):
        """Add a computer to the inventory."""
        # 1. call Computer(...) constructor
        # to create Computer instance
        # 2. inventory.append(...) to add the
        # new computer instance to the inventory
        self.inventory.append(computer)

    def sell(self, computer: Computer) -> bool:
        """Remove a computer from inventory if it exists and return True if successful."""
        if computer in self.inventory:
            self.inventory.remove(computer)
            return True
        return False
    
    def refurbish(self, computer: Computer, new_os: str = None) -> bool:
        """Refurbish a computer by updating its price and optionally updating its OS."""
        if computer in self.inventory:
            if computer.year_made < 2018:
                computer.update_price(250)  # Set a lower price for older computers
            else:
                computer.update_price(500)  # Higher price for newer computers
            if new_os:
                computer.update_os(new_os)
            return True
        return False

    def print_inventory(self):
        """Print the current inventory of the resale shop."""
        if not self.inventory:
            print("No inventory available.")
        else:
            for computer in self.inventory:
                print(computer)

