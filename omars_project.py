import numpy as np

class VendingMachine():
    def __str__(self) -> str:
        return """This is a vending machine. 
                it can take up to 3 Quarters, 3 Dimes, and 1 Nickel.
                prices are set uniform for the whole VendingMachine class"""
        
    def __init__(self):
        #these values represents bits for each coin
        self.Q1 = False
        self.Q2 = False
        self.D1 = False
        self.D2 = False
        self.N = False
        # I use these two variables as messengers between two methods.
        self.var1 = False 
        self.var2 = False
        # this is the storage for overall input sum
        self.summary = 0
    
    prices = {'Pop-tarts':.95, 'M&Ms': .85, 'Chips': .60, 'Gum': .25}
    
    
    
    # Describing methods
    def addCoin(self):
        if not self.var1:
            self.var1 = True
        elif not self.var2 and self.var1:
            self.var1 = False
            self.var2 = True
        else:
            print('Are you trying to purchase a Tesla or something?')

    def addQuarter(self):
        self.var1, self.var2 = self.Q1, self.Q2
        self.addCoin()
        self.Q1, self.Q2 = self.var1, self.var2

    def addDime(self):
        self.var1, self.var2 = self.D1, self.D2
        self.addCoin()
        self.D1, self.D2 = self.var1, self.var2

    def addNickel(self):
        if not self.N:
            self.N = True
        else:
            print("Why so many nickels? Do you think I am a hobo or something?")
    
    def sumTotal(self):
        total = np.array([self.Q2, self.Q1])
        total = np.where(total == False, 0, 1).astype('str')
        sm = ''.join(total)
        quarters = int(sm, 2) *.25
        total = np.array([self.D2, self.D1])
        total = np.where(total == False, 0, 1).astype('str')
        sm = ''.join(total)
        dimes = int(sm, 2) *.10
        final_sum = quarters + dimes
        final_sum = final_sum + .5 if self.N else final_sum
        self.summary = final_sum

    def availItems(self):
        self.sumTotal()
        print("Here's the list of what you can buy for that:")
        for k, v in VendingMachine.prices.items():
            if v <= self.summary:
                print(k)
        
        if min(VendingMachine.prices.values()) > self.summary:
            print('Nothing, you are too broke')

    def reset(self):
        self.Q1 = self.Q2 = self.D1 = self.D2 = self.N = False
        self.summary = 0




if __name__ == '__main__':
    print("Press Q for quarters, D for dimes, N for a nickel, R to reset, and X to exit >>>")
    #Instantiating vending machine
    vendor = VendingMachine()
    
    while True:
        input_key = input()
        if input_key.lower() == 'x':
            # exit key
            print('aborted')
            break
        
        if input_key.lower() == 'd':
            vendor.addDime()
        
        if input_key.lower() == 'q':
            vendor.addQuarter()

        if input_key.lower() == 'n':
            vendor.addNickel()
        
        if input_key.lower() == 'r':
            vendor.reset()
        
        # gets the list of items that can be purchased with the current sum: 
        vendor.availItems()

