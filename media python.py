

P1=input("digite uma nota:");
P2=input("digite uma nota:");

m=float(P1)+float(P2);
m=m/2;
print(m);
if(m>=6):
    print("aprovado");           #tem que ter indentar para funcionar código

elif(m<6 and m>4):
    print("em ifa");

else:
    print("reprovado");
