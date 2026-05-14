import math

string_length = float(input("Length of the string: ")) # unit:meter
have_speed = bool(int(input("Have wave speed? (1:Yes,0:No) : ")))

if have_speed:
    wave_speed = float(input("Wave speed: "))
else:
    tension = float(input("Tension of the string: ")) # unit:Newton
    mass = float(input("Mass of the string: ")) # unit:kilogram
    wave_speed = math.sqrt(tension*string_length/mass)
    # string_length/mass = tension/(wave_speed^(2))
    print("Wave speed (round off to 3 sig. fig. if need): ",round(wave_speed,3))

term_harmonic = int(input("The term of harmonic: "))
one_fixed_end = bool(int(input("Only One Fixed end? (1:Yes,0:No) :")))

if not(one_fixed_end):
    wave_length = string_length*2 /term_harmonic
    # string_length = wave_length * term_harmonic /2
else:
    wave_length = string_length*4 /(term_harmonic*2-1)
    # string_length = wave_length * (term_harmonic*2-1) /4

frequency = wave_speed/ wave_length # unit:Hz or 1/second
# wave_speed = frequency*wave_length 

print("Wavelength of this harmonic: ",round(wave_length,3))
print("Frequency of this harmonic: ",round(frequency,3))
