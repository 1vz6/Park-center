print('Bem vindo ao kalash-park')

hight = float(input('Qual sua altura?: '))

if hight >= 1.20:
    print('Você pode brinca na montanha russa')
    age = int(input('Qual sua idade? '))
    if age < 18:
        custo = 5
        print('Seu ingresso vai custar R$5.00')
    elif age <= 18:
        custo = 12
        print('Seu ingresso vai custar R$12.00')
    else:
        custo = 24
        print('Seu ingresso vai custar R$24.00')

    photo = input('Você gostaria de tirar uma foto de recordação? Sim(s) Não(n) ')
    if photo == 's':
        custo += 3

    print(f'Seus custo vai custar R${custo}')
else:
    print('Você não pode brinca na montanha russa')

