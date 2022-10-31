def lesInnMatFil():
    matretter = []
    fil = open("mat.txt" , "r")

    for linje in fil:
        info = linje.split(",")
            matretter.append(info[0])
    return matretter

def velgMatretter():
    matretter = lesInnMatFil("matretter.txt")
    valgt_mat = []

    for i in range(n):
        valgt_mat.append(random.choice(matretter))

    return valgt_mat
