def funksjon(svar1,svar2):
    svar1 = input("True/False: ")
    svar2 = input("True/False: ")

    if svar1 == True and svar2 == True :
        return 1
    elif svar1 == False or svar2 == False :
        return 0
    else :
        return None
