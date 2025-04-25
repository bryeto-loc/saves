#Para homens: 66 + (13,8 x peso em kg) + (5 x altura em cm) – (6,8 x idade em anos)
#TMB = 655 + (9,6 x peso em kg) + (1,8 x altura em cm) - (4,7 x idade em anos) para mulheres.
#para mulheres: 655 + (9,6 x peso em kg) + (1,8 x altura em cm) – (4,7 x idade em anos)
sex = str(input("qual seu genero: "))
peso = int(input("peso: "))
old = int(input("idade: "))
altura = int(input("altura em cm: "))
if sex == "homem":
    TMB = 66 + (13.8 * peso) + (5 * altura) - (4,7 * old)
    print('sua TMB é de' ,TMB)
elif sex == "mulher":
    TMB = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * old)
    print('sua TMB é de' ,TMB)
else:
    print('insira um sexo valido')
print('para calcular seu get escolha o nivel de atividade')
esc = int(input('escolha entre\n[ 1 ] SEDENTÁRIO \n[ 2 ] LEVEMENTE ATIVO \n[ 3 ] MODERADAMENTE ATIVO \n[ 4 ] MUITO ATIVO\n [ 5 ] EXTREMAMENTE ATIVO: \n'))
if esc == 1:
    GET = TMB * 1.2
    print('Seu GET (Gasto Energetico Total) é de {}' .format(GET))
elif esc == 2:
    GET = TMB * 1.375
    print('Seu GET (Gasto Energetico Total) é de {}' .format(GET))
elif esc == 3:
    GET = TMB * 1.55
    print('Seu GET (Gasto Energetico Total) é de {}' .format(GET))
elif esc == 4:
    GET = TMB * 1.725
    print('Seu GET (Gasto Energetico Total) é de {}' .format(GET))
elif esc == 5:
    GET = TMB * 1.9
    print('Seu GET (Gasto Energetico Total) é de {}' .format(GET))
else:
    exit

#OBJETIVO
print('tendo seu GET em mãos. Escolha seu objetivo')
obj = int(input('escolha entre\n[ 1 ] GANHO DE MASSA \n[ 2 ] EMAGRECIMENTO \n[ 3 ] MANTER PESO: \n'))
if obj == 1:
    GETF = GET + 500
    print('De acordo com sua escolha sua meta calórica diária é de' ,GETF)
elif obj == 2:
    GETF = GET - 500
    print('De acordo com sua escolha sua meta calórica diária é de' ,GETF)
elif obj == 3:
    GETF = GET 
    print('De acordo com sua escolha sua meta calórica diária é de' ,GETF)
else:
    print('Insira uma opção válida')
    exit

#macros 
protein = (GETF * 0.30) / 4
carbo = (GETF * 0.50) / 4
fat = (GETF * 0.25) / 9
print('Sua necessidade calórica é de {:.2}. Seus macros são de \nPROTEINA {:.2} \nCARBOIDRATOS {:.2} \nGORDURA {:.2}' .format(GETF, protein, carbo, fat))


