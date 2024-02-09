#Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, B+ if 70 or above and so on... 
#print failed if the score is below 50, if score > 100 print invalid

r1=int(input("enter physics score :"))
r2=int(input("enter maths score :"))
r3=int(input("enter science score :"))
r4=int(input("enter chemistry score :"))
r5=int(input("enter bio score :"))

R=r1+r2+r3+r4+r5

if (R>100):
    print ("Invalid")
if (R>=90 and R<=100):
    print("A+ grade")
elif (R>=80 and R<90):
    print("A grade")
elif (R>=70 and R<80):
    print("B+ grade")
elif (R>=60 and R<70):
    print("B grade")
elif (R>=50 and R<60):
    print("C grade")
elif (R<50):
    print("FAIL")