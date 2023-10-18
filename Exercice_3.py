M=int(input("Entrer le nombre 1:"))
N=int(input("Entrer le nombre 2:"))
s=0
for i in range(2,N):
   
    if N%i==0:
        s+=i
z=0        
for j in range(2,M):
    
    if M%j==0:
        z+=j
if z==N and s==M:
    print(M,"est",N,"sont des amis")
else :
    print(M,"et",N,"ne sont pas amis")