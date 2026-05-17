#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Sequence Calculator v1.2.0
(https://github.com/myhead-no-hair/ict-to-maths-dse/blob/main/sequence_cal.py)
Author: My Head No Hair (https://github.com/myhead-no-hair)
Free for any educational use, while it is important to fulfil the academic integrity. 

Functions:
1. Arithmetic Sequence
Input: A th Term of sequence, Number of A th Term of sequence, B th Term of sequence, Number of B th Term of sequence
Output: Common Difference of this Arithmetic Sequence, First Term of this Arithmetic Sequence
Input: Find_Term
Output: Number of Find_Term th term

2. Fibonacci Sequence
Input: A th Term of sequence, Number of A th Term of sequence, B th Term of sequence, Number of B th Term of sequence, Find_Term
Output: Number of Find_Term th term

3. Adding-Dots Sequence
Input: Given Term of sequence (Initial Term:0), Number of Given Term of sequence, Integeral part of n of adding dots, Constant part of adding dots
Output: Initial Term of this Sequence # if (Given Term of sequence != 0)
Input: Find_Term
Output: Number of Find_Term th term

4. Geometry Sequence
Input: A th Term of sequence, Number of A th Term of sequence, B th Term of sequence, Number of B th Term of sequence
Output: Common Ratio of this Geometry Sequence, First Term of this Geometry Sequence
Input: Find_Term
Output: Number of Find_Term th term

This Program has no data type validation.
'''

import math
from fractions import Fraction

def fibonacci_seq(Term):# Refer to calculator program(https://webcal.freetzi.com/casio.fx-50FH/fibonacci.htm) with modifications
    try:
        a = (1 + (5)**(1/2))/2 # golden ratio
        return math.trunc(((5)**(-1/2))
                        *(a**(Term) - (1-a)**(Term)))
    except:
        print("Error occurred.")
        return 0

def produce_fraction_str(number):
    try:
        if number.is_integer():
            return str(number)
        else:
            return str(Fraction(number).limit_denominator().numerator)+"/"+str(Fraction(number).limit_denominator().denominator)
    except:
        print("Error occurred.")
        return 0

while True:
    print("="*48)
    print("="*12,"Sequence Calculator v1.1","="*12)
    Mode = input("Type of Sequence(A = Arithmetic Sequence, F = Fibonacci Sequence, D = Adding-Dots Sequence, G = Geometry Sequence):")

    if (Mode in ["A","Arithmetic Sequence"]):# (Mode in ["A","Arithmetic Sequence"]) has a similar meaning as (Mode == "A" or Mode == "Arithmetic Sequence"), but it is not appreciate to be used in HKDSE.
        # General term of Arithmetic Sequence
        print("="*8,"Arithmetic Sequence","="*8)
        while True:
            Term_of_Na = int(input("A th Term of sequence:"))
            Na = float(input("Number of A th Term of sequence:"))
            Term_of_Nb = int(input("B th Term of sequence:"))
            Nb = float(input("Number of B th Term of sequence:"))
            if Term_of_Na == Term_of_Nb:
                print("Terms of sequence cannot be the same. Please Re-enter.")
                continue
            elif Na == Nb:
                print("Numbers of Term of sequence cannot be the same. Please Re-enter.")
                continue
            else:
                break
        Common_Difference = (Na - Nb)/(Term_of_Na - Term_of_Nb)
        NOne = Na - (Common_Difference * (Term_of_Na-1))
        print("Common Difference of this Arithmetic Sequence:",produce_fraction_str(Common_Difference))
        print("First Term of this Arithmetic Sequence:",produce_fraction_str(NOne))
        Find_Term = int(input("Input Finding Term:"))
        Result = NOne + (Common_Difference * (Find_Term-1))
        print("Number of "+str(Find_Term)+" th term:",produce_fraction_str(Result))
        
    elif (Mode in ["F","Fibonacci Sequence"]):
        # Fibonacci Sequence
        print("="*8,"Fibonacci Sequence","="*8)
        while True:
            Term_of_Na = int(input("A th Term of sequence:"))
            Na = float(input("Number of A th Term of sequence:"))
            Term_of_Nb = int(input("B th Term of sequence:"))
            Nb = float(input("Number of B th Term of sequence:"))
            if Term_of_Na == Term_of_Nb:
                print("Terms of sequence cannot be the same. Please Re-enter.")
                continue
            elif Na == Nb:
                print("Numbers of Term of sequence cannot be the same. Please Re-enter.")
                continue
            else:
                break
        Fa1 = fibonacci_seq(Term_of_Na - 2)
        Fa2 = fibonacci_seq(Term_of_Na - 1)
        Fb1 = fibonacci_seq(Term_of_Nb - 2)
        Fb2 = fibonacci_seq(Term_of_Nb - 1)
        # Refer to calculator program(https://webcal.freetzi.com/casio.fx-50FH/simultaneous1.htm) with modifications
        NOne = ((Nb*Fa1) - (Na*Fb2)) / ((Fb1*Fa2) - (Fa1*Fb2)) # Number of T1 (very dangerous variable name)
        NTwo = ((Na)-(Fa1*NOne))/(Fa2) # Number of T2
        Find_Term = int(input("Input Finding Term:"))
        if Find_Term == 1:
            Result = NOne
        elif Find_Term == 2:
            Result = NTwo
        else:
            Result = fibonacci_seq(Find_Term - 2) * NOne + fibonacci_seq(Find_Term - 1) * NTwo
            # T(n+2) = fibonacci_seq(n-2)*NOne + fibonacci_seq(n-1)*NTwo
        print("Number of "+str(Find_Term)+" th term:",produce_fraction_str(Result))
        
    elif (Mode in ["D","Adding-Dots Sequence"]):
        # Adding-Dots Sequence
        print("="*8,"Adding-Dots Sequence","="*8)
        Term_of_Na = input("Given Term of sequence (Initial Term:0) :")
        Term_of_Na = int(Term_of_Na) if Term_of_Na else 0 # This syntax is not appreciate to be used in HKDSE.
        Na = float(input("Number of Given Term of sequence:"))
        Integeral_n = int(input("Integeral part of n of adding dots:"))
        Constant = int(input("Constant part of adding dots:"))
        if Term_of_Na == 0:
            NZero = Na
        else:
            NZero = Na - Term_of_Na*(Integeral_n*(1+Term_of_Na)/2 + Constant)
            print("Initial Term of this Sequence:",produce_fraction_str(NZero))
        Find_Term = int(input("Input Finding Term:"))
        Result = NZero + Find_Term*(Integeral_n*(1+Find_Term)/2 + Constant)
        print("Number of "+str(Find_Term)+" th term:",produce_fraction_str(Result))
           
        # if Term_of_Na < Find_Term:
        #     for n in range(Term_of_Na,Find_Term):
        #         Result += ((Integeral_n*n) + Constant)
        # elif Term_of_Na > Find_Term:
        #     for n in range(Term_of_Na-1,Find_Term+1,-1):
        #         Result -= ((Integeral_n*n) + Constant)
        
        
    elif (Mode in ["G","Geometry Sequence"]):
        # General term of Geometry Sequence
        print("="*8,"Geometry Sequence","="*8)
        while True:
            Term_of_Na = int(input("A th Term of sequence:"))
            Na = float(input("Number of A th Term of sequence:"))
            Term_of_Nb = int(input("B th Term of sequence:"))
            Nb = float(input("Number of B th Term of sequence:"))
            if Term_of_Na == Term_of_Nb:
                print("Terms of sequence cannot be the same. Please Re-enter.")
                continue
            elif Na == Nb:
                print("Numbers of Term of sequence cannot be the same. Please Re-enter.")
                continue
            else:
                break
        Expo_Na = Term_of_Na - 1
        Expo_of_Common_Ratio = (Expo_Na - (Term_of_Nb - 1))# can be negative
        Common_Ratio = (Na / Nb)**(1/Expo_of_Common_Ratio)
        NOne = Na*(Common_Ratio ** (-Expo_Na))
        if Expo_of_Common_Ratio//2 == 0:          
            print("Common Ratio of this Geometry Sequence:",produce_fraction_str(Common_Ratio),"or",produce_fraction_str(Common_Ratio*-1))
            if Expo_Na//2 == 0:# both even exponents
                print("First Term of this Geometry Sequence:",produce_fraction_str(NOne))
            else:# both odd exponents
                print("First Term of this Geometry Sequence respect to the two Common Ratio:",produce_fraction_str(NOne),"or",produce_fraction_str(NOne*-1))
        else:
            print("Common Ratio of this Geometry Sequence:",produce_fraction_str(Common_Ratio))
            print("First Term of this Geometry Sequence:",produce_fraction_str(NOne))
        Find_Term = int(input("Input Finding Term:"))
        Result = NOne*(Common_Ratio ** (Find_Term-1))
        print("Number of "+str(Find_Term)+" th term:",produce_fraction_str(Result))
    
    else:
        print("Invalid Type of Sequence.")
    
    print("="*24)            
    command = input("Quit? (Input \"Q\" to Quit):")
    if command in ["Q","q","Quit","quit"]:
        print("Program Ended.")
        print("="*48)
        break
       
