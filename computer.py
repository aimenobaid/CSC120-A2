class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor: str, ram: int, storage: int, os: str, year_made: int, price: float):
        """Initialize a computer given all the attributes."""
        self.description = description
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.os = os
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def update_price(self, new_price: float):
        """Update the price of the computer."""
        self.price = new_price

    def update_os(self, new_os: str):
        """Update the operating system of the computer."""
        self.os = new_os

    def __str__(self) -> str:
        """Return a string representation of the computer."""
        return (f"{self.description} ({self.year_made})\n"
                f"Processor: {self.processor}, RAM: {self.ram}GB, Storage: {self.storage}GB\n"
                f"OS: {self.os}, Price: ${self.price:.2f}")
