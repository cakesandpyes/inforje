n=int(input())
a=n
zn=0
br=0
brzn=0
prosjek=0
znbroj=0
while(n>0):
    zn=n%10
    n=n//10
    znbroj+=zn
    brzn+=1
prosjek=znbroj/brzn
while(a>0):
    zn=a%10
    a=a//10
    if(zn<prosjek):
        br+=1
print("Ima", br,"ispod prosjeka")
