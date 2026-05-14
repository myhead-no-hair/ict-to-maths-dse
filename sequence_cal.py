import math
from fractions import Fraction

def fibonacci_seq(Term):
    a = (1/2)*(1 + (5)**(1/2))
    return math.trunc(((1/5)**(1/2))
                      *(a**(Term) - (-a)**(-Term)))
    
def produce_fraction_str(number):
    if number.is_integer():
        return str(number)
    else:
        return str(Fraction(number).limit_denominator().numerator)+"/"+str(Fraction(number).limit_denominator().denominator)

while True:
    Mode = input("Type of sequence(A = Arithmetic Sequence, F = Fibonacci Sequence, D = Adding-Dots Sequence, G = Geometry Sequence):")

    if Mode == "A":
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
        print("Integer of "+str(Find_Term)+" th term:",produce_fraction_str(Result))
        
    elif Mode == "F":
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
        Find_Term = int(input("Input Finding Term:"))
        Fa1 = fibonacci_seq(Term_of_Na - 2)
        Fa2 = fibonacci_seq(Term_of_Na - 1)
        Fb1 = fibonacci_seq(Term_of_Nb - 2)
        Fb2 = fibonacci_seq(Term_of_Nb - 1)
        NOne = ((Nb*Fa1) - (Na*Fb2)) / ((Fb1*Fa2) - (Fa1*Fb2))
        NTwo = ((Na)-(Fa1*NOne))/(Fa2)
        if Find_Term == 1:
            Result = NOne
        elif Find_Term == 2:
            Result = NTwo
        else:
            Result = fibonacci_seq(Find_Term - 2) * NOne + fibonacci_seq(Find_Term - 1) * NTwo
        print("Integer of "+str(Find_Term)+" th term:",str(int(Result)))
        
    elif Mode == "D":
        # Adding-Dots Sequence
        print("="*8,"Adding-Dots Sequence","="*8)
        Term_of_Na = int(input("A th Term of sequence:"))
        Na = float(input("Number of A th Term of sequence:"))
        Integeral_n = int(input("Integeral part of n of adding dots:"))
        Constant = int(input("Constant part of adding dots:"))
        Find_Term = int(input("Input Finding Term:"))
        Result = Na
        if Term_of_Na < Find_Term:
            for n in range(Term_of_Na,Find_Term):
                Result += ((Integeral_n*n) + Constant)
        elif Term_of_Na > Find_Term:
            for n in range(Term_of_Na-1,Find_Term+1,-1):
                Result -= ((Integeral_n*n) + Constant)
        print("Integer of "+str(Find_Term)+" th term is :",str(int(Result)))    
        
    elif Mode == "G":
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
        # Expo_Nb = Term_of_Nb - 1
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
                
    command = input("Quit? (Input \"Q\" to Quit):")
    if command == "Q":
        break
       
