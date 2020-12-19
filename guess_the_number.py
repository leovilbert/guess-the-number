from random import randint

computer = randint(1, 10)

print('Pensei em número de 1 a 10. \nVocê deve chutar até acertar! Vamos lá!!')

while True:    
    user = input('Sua escolha: ')

    if user.isnumeric() != True:
        print('Ei, digite um número!')
        continue
    else:
        user = int(user)
        if user > 10:
            print('Chute um número ENTRE 0 e 10.')
            
        if user > computer:
            print('Chutou muito alto, tente um número menor.')
            continue
        
        if user < computer:
            print('Chutou muito baixo, tente um número maior.')
            continue
        
        if user == computer: 
            print('Parabéns! Você acertou!')
            break
