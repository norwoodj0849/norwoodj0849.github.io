# -*- coding: utf-8 -*-
"""
# Jordan Norwood
# 12/6/2022
# CTS-285 M2HW2
"""

import Prices_UI as ui
import Prices as pizza
import PizzOrder as number

def main():
    
    gui = ui.Prices_UI()
    
    keepGoing = True
    while keepGoing == True:
        keepGoing = gui.menu()
    print("Now You've got all the Prices fo the pizza.")
    
if __name__ == "__main__":
    main()
