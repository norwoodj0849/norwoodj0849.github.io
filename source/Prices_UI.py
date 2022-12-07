# -*- coding: utf-8 -*-
"""
# Jordan Norwood
# 12/6/2022
# CTS-285 M5PROj
"""

import Prices as pizza

class Prices_UI:
    def __init__ (self):
        self.pizza = pizza.PizzaPrices()
        self.number = pizza.PizzOrder()
        
    def showMenu(self):
        print ("1. Answer Checker")
        print ("2. Data Bank")
        print ("3. Exit")
        
    def menu(self):
        self.showMenu()
        choice = int(input("Choose: "))
        if choice == 1:
            self.doAnswerChecker()
        elif choice == 2:
            self.doDataBank()
        elif choice == 3:
            return False
        else: 
            print("Not available.")
        return True 
    
    def parsePrice(self, price):
       
        priceElements = price.split(" ")
        order1 = int(priceElements[0])
        combine = priceElements[1]
        order2 = int(priceElements[2])
        totalOrder = int(priceElements[4])
        price = pizza.Price(order1, combine, order2, totalOrder)
        return price
    
    def doAnswerChecker(self):
        print("Two Price Adding Example: 4 + 10 = 14")
        priceTyped = input("Total of Two Prices: ")
        price = self.parsePrice(priceTyped)
        print("Your two price  and the corrcet Total was: ", str(price))
        Correct = self.pizza.checkPrice(price, price.totalOrder)
        if Correct:
            print("Price of your Pizza has been created!")
        else:
            print("Sorry...it was not created.")
        
   
        
    def doDataBank(self):

        choice = -1
        while choice != 0:  
                
            print("Data Bank ")
            print("1. Make The Total Price of the Pizza")
            print("2. Add the Pizza's Price")
            print("3. List All of the Pizza's Prices")
            print("4. Exit")
            choice = int(input("Choose: "))
            
            if choice == 1:
                price = self.number.getPrices()
                if price == None:
                    print("No total prices in data bank.")
                    return False
                print("Next Price: (", self.number.priceIndex, ")")
                print(price.combinePrices())
                total = int(input()) 
                Correct = self.pizza.checkPrice(price, price.total)
                if Correct:
                    print("Your Price Of Pizza Has Been Created!")
                else:
                    print("Sorry...it was not created.")
            elif choice == 2:
                self.doAddPrices()
            elif choice == 3:
                self.listAllPrices()
            elif choice == 4:
                return False
                
    def doAddPrices(self):
        print("Two Price Example: 4 + 10 = 14")
        priceTyped = input("Total Price: ")
        price = self.parsePrice(priceTyped)
        self.number.addPrice(price)
        print("The price is added in.")
        
    def listAllPrices(self):
        
        allPrices = self.number.getAllPrices()
        print ("---- All data ----")
        if len(allPrices) == 0:
            print("No Prices in data bank.")
        else:
            for price in allPrices:
                print(price)
        print ("----------------------")