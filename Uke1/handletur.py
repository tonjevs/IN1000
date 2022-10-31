Brød = 20
Melk = 15
Ost = 40
Youghurt = 12

sum = 0

print("Hei! Velkommen til IFI-butikken. ")
inp = input("Hvor mange brød vil du ha? ")
sum+= int(inp)*Brød

inp = input("Hvor mange melker vil du ha? ")
sum+= int(inp)*Melk

inp = input("Hvor mange oster vil du ha? ")
sum+= int(inp)*Ost

inp = input("Hvor mange youghurt vil du ha? ")
sum+= int(inp)*Youghurt

print("Du skal betale" , sum , "kr")
