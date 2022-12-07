# -*- coding: utf-8 -*-
"""
# Jordan Norwood
# 12/6/2022
# CTS-285 M5PROj
"""

class PizzaPrices:
    def __init__(self):
        
        pass
    
    def checkPrice(self, price, userAnswer):
        correctAnswer = price.fuse()
        Correct = (correctAnswer == userAnswer)
        return Correct
    
class PizzOrder:
    def __init__(self):
        self.prices = [] 
        self.priceIndex = 0 
        
    def addPrice(self, price):
       
        self.prices.append(price)
        
    def getPrices(self):
        
        
        if len(self.prices) == 0:
            return None
        price = self.prices[self.comboIndex]
        self.priceIndex += 1
        if self.priceIndex >= len(self.combos):
            self.priceIndex = 0
        return price
    
    def getAllPricess(self): 
        
        return self.prices
        
class Price:
    def __init__(self, order1, combine, order2, totalOrder):
        self.order1 = order1
        self.combine = combine
        self.order2 = order2
        self.totalOrder = totalOrder
        
    def __str__(self):
        """ 
        >>> Price = Price(4, "+", 10, 14)
        >>> str(myPrice)
        '4 + 10 = 14'
        >>> anotherPrice = Price(5, "+", 5, 25)
        >>> str(anotherPrice)
        '5 * 5 = 25'
        """
        priceString = str(self.order1) + " " + self.combine + " " + \
            str(self.order2) + " = " + str(self.totalOrder)
        return priceString
    
    def combinePrices(self):
        
        priceString = str(self.order1) + " " + self.combine + " " + \
            str(self.order2) + " = " "?"
        return priceString
        
    def fuse(self):
        """
        >>> myPrice = Price(4, "+", 10, 14)
        >>> myPrice.fuse()
        14
        >>> anotherPrice = Price(5, "*", 5, 25)
        >>> anotherPrice.fuse()
        25
        """
        order1 = self.order1
        combine = self.combine
        order2 = self.order2
        if (combine == "+"):
            totalOrder = order1 + order2
        if (combine == "*"):
            totalOrder = order1 * order2
        if (combine == "-"):
            totalOrder = order1 - order2
        if (combine == "/"):
            totalOrder = order1 // order2
        
        return totalOrder
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()