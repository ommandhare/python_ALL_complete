

def getValues(eq1,eq2):
    lst1=[]
    eqM1=[]

    for ex in eq1:
        if ex.isdigit():
            ex = int(ex)
            # print(ex, type(ex))
            lst1.append(ex)
        else:
            lst1.append(ex)

    for ex in range(len(eq1)):
        if lst1[ex - 1] == "-":
            # print(lst1[ex])
            lst1[ex] = 0 - lst1[ex]
            # print(lst1[ex], type(lst1[ex]))
            eqM1.append(lst1[ex])
        else:
            eqM1.append(lst1[ex])

    # print(eqM1)

    lst2 = []
    eqM2 = []
    for ex in eq2:
        if ex.isdigit():
            ex = int(ex)
            # print(ex, type(ex))
            lst2.append(ex)
        else:
            lst2.append(ex)

    for ex in range(len(eq2)):
        if lst2[ex - 1] == "-":
            # print(lst1[ex])
            lst2[ex] = 0 - lst2[ex]
            # print(lst1[ex], type(lst1[ex]))
            eqM2.append(lst2[ex])
        else:
            eqM2.append(lst2[ex])

    # print(eqM2)
    return eqM1,eqM2


def getMatrices(equation1,equation2):
    A = []
    X = []
    B = []


    for ex in equation1:
        if type(ex) is int:
          if ex==equation1[-1]:
            B.append(ex)
          else:
            A.append(ex)
        elif ex=="x":
            X.append(ex)
        elif ex=="y":
            X.append(ex)



    for ex in equation2:
        if type(ex) is int:
           if ex==equation2[-1]:
            B.append(ex)
           else:
            A.append(ex)

    return A,B,X

def getDeterminant(a:list):
    f1 = a[0] * a[3]
    f2 = a[2] * a[1]
    D = f1 - f2
    return D


def getInverse(a:list):
        inMatrix = []
        a[3], a[0] = a[0], a[3]
        inMatrix.append(a[0])
        if a[1] > 0:
            a[1] = -a[1]
        else:
            a[1] = abs(a[1])

        inMatrix.append(a[1])
        if a[2] > 0:
            a[2] = -a[2]
        else:
            a[2] = abs(a[2])
        inMatrix.append(a[2])
        inMatrix.append(a[3])
        return inMatrix




def main():
    # eq1=input("enter the first equation::::")
    eq1 = "4x-3y=2"
    # eq2=input("enter the second equation::::")
    eq2 = "8x+5y=1"


    first,second=getValues(eq1,eq2)
    print("value matrix:::")
    # print(first,second)

    A,B,X=getMatrices(first,second)
    print("First equation matrices:::")
    print(A)
    print(B)
    print(X)

    print("#################################")
    print("NOW MULTIPLY X BY B")
    print(f"{A}={X}*{B}")

    print("######################################")
    print("PUTTING INVERSE EQUATION BECAUSE WE HAVE TO FIND X VALUES:::")
    print(f"{A}^-1*{B}")


    print("###################################")
    print("DETEMINANT :::::")
    Determinant=getDeterminant(A)
    print(f" |A|={Determinant}")


    print("###################################")
    print("INVERSE MATRIX")
    inMatrix=getInverse(A)
    print(inMatrix)



if __name__ == "__main__":
    main()


