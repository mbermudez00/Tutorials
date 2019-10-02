
#x = "ejemplo"
kilometer = [39.2, 36.5, 37.3, 37.8]
try:
    #x = "Caballo" if x=="ejemplol" else x  
    #feet = [3280.8399*x for x in kilometer] 
    feet = map(lambda x: float(3280.8399)*x, kilometer)
    print(list(feet))
except:
    print("esto paso el try")


# num = input("ingresa el numero maximo menor a 200: ") 
# try:
#     num = int(num)
#     print(2)
#     for i in range(3,(num+1)):
#         if i%2==1: print(i)
# except ValueError:
#     print("only number allowed!")

