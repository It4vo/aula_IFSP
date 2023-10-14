i=0
ifa=0
apr=0
repr=0
while(i<4):
    nome=input("digite um nome:");
    P1=input("digite uma nota:");
    P2=input("digite uma nota:");
    m=float(P1)+float(P2);
    m=m/2;
    print(m);
    if(m>=6):
        print(nome,"foi aprovado");           #tem que ter indentar para funcionar código
        apr=apr+1
    elif(m<6 and m>4):
        print(nome,"está em ifa");
        ifa = ifa + 1
    else:
        print(nome,"foi reprovado");
        repr=repr+1
    i=i+1

print(apr,"alunos foram aprovados");
print(ifa,"alunos  estão em ifa");
print(apr,"alunos foram reprovados");
