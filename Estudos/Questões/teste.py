x=float(input('Digite a primeira nota:'))
y=float(input('Digite a segunda nota:'))
z=float(input('Digite a terceira nota:'))
m=(x+y+z)/3
if (m>=7 and m<=10):
    print('Aluno aprovado com média',m)
elif (m>=4 and m<=6.9):
    print('Aluno vai fazer prova final, nota',m)
elif m<3.9:
    print('Aluno reprovado com média',m)
else:
    print('Inválido')