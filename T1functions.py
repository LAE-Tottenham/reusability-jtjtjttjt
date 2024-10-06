import math

def firstHyp():   # get the length and width of the first triangle from the user and find hyp
    validOpp=False
    validAdj=False
    while validOpp==False:
        opp1 = float(input("Enter your first triangle's opposite side length: "))
        if opp1>0:
            validOpp=True
    while validAdj==False:
        adj1 = float(input("Enter your first triangle's adjacent side length: "))
        if adj1>0:
            validAdj=True
    hyp1 = math.sqrt(opp1**2 + adj1**2)
    return hyp1

def secondHyp():  # get the length and width of the second triangle from the user and find hyp
    validOpp=False
    validAdj=False
    while validOpp==False:
        opp2 = float(input("Enter your second triangle's opposite side length: "))
        if opp2>0:
            validOpp=True
    while validAdj==False:
        adj2 = float(input("Enter your second triangle's adjacent side length: "))
        if adj2>0:
            validAdj=True
    hyp2 = math.sqrt(opp2**2 + adj2**2)
    return hyp2

def triangle(h1,h2):   # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    opp3 = h1
    adj3 = h2
    hyp3 = math.sqrt(opp3**2 + adj3**2)
    return hyp3

def soh(): 
    unknown=input("are you looking for opp, hyp or angle? ")
    if unknown=="opp":
        a=float(input("enter angle "))
        a2=math.radians(a)
        h=float(input("enter hyp "))
        ans= (math.sin(a2))*h
    elif unknown=="hyp":
        a=float(input("enter angle "))
        a2=math.radians(a)
        o=float(input("enter opp "))
        ans= o/(math.sin(a2))
    elif unknown=="angle":
        o=float(input("enter opp "))
        h=float(input("enter hyp "))
        x=o/h
        ans1= math.asin((x))
        ans= math.degrees(ans1)
    else:
        ("enter a valid unknown")
    return ans
    
def cah():
    unknown=input("are you looking for adj, hyp or angle? ")
    if unknown=="adj":
        a=float(input("enter angle "))
        a2=math.radians(a)
        h=float(input("enter hyp "))
        ans= (math.cos(a2))*h
    elif unknown=="hyp":
        a=float(input("enter angle "))
        a2=math.radians(a)
        adj=float(input("enter adj "))
        ans= adj/(math.cos(a2))
    elif unknown=="angle":
        adj=float(input("enter adj "))
        h=float(input("enter hyp "))
        x=adj/h
        ans1= math.acos((x))
        ans= math.degrees(ans1)
    else:
        ("enter a valid unknown")
    return ans

def toa():
    unknown=input("are you looking for opp, adj or angle? ")
    if unknown=="opp":
        a=float(input("enter angle "))
        a2=math.radians(a)
        adj=float(input("enter adj "))
        ans= (math.tan(a2))*adj
    elif unknown=="adj":
        a=float(input("enter angle "))
        a2=math.radians(a)
        o=float(input("enter opp "))
        ans= o/(math.tan(a2))
    elif unknown=="angle":
        o=float(input("enter opp "))
        adj=float(input("enter adj "))
        x=o/adj
        ans1= math.atan((x))
        ans= math.degrees(ans1)
    else:
        ("enter a valid unknown ")
    return ans

def cosineRule():
    b=float(input("enter b "))
    c=float(input("enter c "))
    A=float(input("enter angle A "))
    ADeg=math.radians(A)
    aSqr= (b**2 + c**2) - (2*b*c*(math.cos(ADeg)))
    a=math.sqrt(aSqr)
    return a

def sineRule():
    unknown=input("are you looking for side or angle? ")
    if unknown=="angle":
        a=float(input("enter side a "))
        A=float(input("enter angle A "))
        b=float(input("enter side b "))
        ADeg=math.radians(A)
        sinAns=((math.sin(ADeg))/a)*b
        ans1=math.asin(sinAns)
        ans=math.degrees(ans1)
    elif unknown=="side":
        a=float(input("enter side a "))
        A=float(input("enter angle A "))
        B=float(input("enter angle B "))
        ADeg=math.radians(A)
        BDeg=math.radians(B)
        sinAns=(a/(math.sin(ADeg)))*(math.sin(BDeg))
    return ans