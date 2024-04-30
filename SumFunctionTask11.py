def Jam(a,b,c):
    if b=='+':
        return a+c
def tarh(a,b,c):
    if b=='-':
        return a-c
def taqsim(a,b,c):
    if b=='/' or b=="//":
        return a//c
def zarb(a,b,c):
    if b=='*':
        return a*c
def mod(a,b,c):
    if b=='%':
        return a%c

a=int(input())
b=input()
c=int(input())
print(Jam(a,b,c))
print(tarh(a,b,c))
print(taqsim(a,b,c))
print(zarb(a,b,c))
print(mod(a,b,c))

#Nashud)))