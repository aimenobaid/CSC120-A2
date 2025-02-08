# main.py for the object-oriented code
from oo_resale_shop import ResaleShop
from computer import Computer

def main():
    """to demonstrate the functionality of the ResaleShop."""
    # create the resale shop
    shop: ResaleShop = ResaleShop()
    
    # create computers and add them to the inventory
    comp1: Computer = Computer("Gaming Laptop", "Intel i7", 16, 512, "Windows 10", 2020, 1000.0)
    comp2: Computer = Computer("Workstation", "AMD Ryzen 9", 32, 1024, "Ubuntu 22.04", 2019, 1500.0)
    comp3: Computer = Computer("Macbook Pro", "M2", 16, 1024, "macOS 14 Sequoia", 2023, 1000)
    
    # print the little banner cuz its cute
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    shop.buy(comp1)  # Buying computers for the shop
    shop.buy(comp2)  
    shop.buy(comp3)
    
    print("Initial Inventory:")
    print("-" * 21)
    shop.print_inventory()  # print current inventory
    

    # refurbish the first computer (upgrading OS)
    shop.refurbish(comp1, "Windows 11")
    shop.refurbish(comp3, "macOS 15 Sequoia")
    
    print("-" * 21)
    print("After Refurbishment:")
    print("-" * 21)
    shop.print_inventory()
    
    # sell the second computer
    shop.sell(comp2)
    print("-" * 21)
    print("After Selling:")
    print("-" * 21)
    shop.print_inventory()

if __name__ == "__main__":
    main()
