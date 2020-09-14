#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:12:45 2020

@author: raphaelbruni
"""


# A program that prints a school

def draw_school():
    print('-------------------------------------')
    for x in range(0,8):
        print('- -                               - -')
        if x == 1:
            print('- -   –––––      /\       –––     - -\n'
                  '- -   |         /  \     |        - -\n'
                  '- -   |        /––––\    |        - -\n'
                  '- -   |       /      \    –––     - -\n' 
                  '- -   |      /        \      |    - -\n'
                  '- -   |     /          \     |    - -\n'
                  '- -   –––––               –––     - -')
        
        if x == 5:
            print('- -            -------            - -')
        if x == 6:
            print('- -            |   o |            - -')
        if x == 7:
            print('- -            |     |            - -')
    print('-------------------------------------')
    for x in range (0, 8):
        print('               |     |               ')
        
        #if x == 2:
           # print ('               ------                 ')
            
    
   
        

        
