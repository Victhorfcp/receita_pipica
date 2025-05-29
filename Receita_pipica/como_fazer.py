print("Hoje vamos aprender a fazer pipoca de chocolate branco com leite ninho.")
print()
print("Iremos precisar de: óleo, milho de pipoca, chocolate branco e leite ninho.")
print()

possui = input(f"Você possui todos os ingredientes? [S]im ou [N]ão: ")

possui = possui.lower()

if possui:
       
    if possui == "sim" or possui ==  "s":
        print("Ótimo, então vamos começar...")
    elif possui == "não" or possui == "n":
        print("Precisamos dos igredientes para começar. ")
        exit()
    else:
        print("Preciso da sua resposta para continuarmos. ")


    print()
    print("Primeiro despeje o óleo na panela")
    print("Depois de esquentar um pouco, jogue o milho.")
    print("Assim que a primeira pipoca estourar, coloque em fogo baixo e feche a tampa.")

    continuidade = input("Está conseguindo seguir o passo a passo? [S]im ou [N]ão:")
    continuidade = continuidade.lower()

    if continuidade == "sim" or continuidade == "s":
        print("Ótimo, vamos continuar...")
    elif continuidade == "não" or continuidade == "n":
        print("Sem problemas, volte e revise os passos com calma.")
    else:
        print("Preciso da sua resposta para continuarmos. ")
        exit()

    continuidade2 = input("Podemos continuar? [S]im ou [N]ão: ")
    continuidade2 = continuidade2.lower()

    if continuidade2 == "sim" or continuidade2 == "s":
        print("Ótimo, vamos continuar...")
    elif continuidade2 == "não" or continuidade2 == "n":
        print("Sem problemas, sugiro que recomeçe todos os passos.")
        exit()
    else:
        print("Preciso da sua resposta para continuarmos. ")
        exit()

    print("Agora aguardaremos todas as pipocas estourarem, enquanto isso colocamos o chocolate branco para derreter.")
    print("Pra isso, coloque o chocolate branco em um recipiente de vidro e leve ao microondas por volta de 30 segundos.")
    print("Após finalizar a pipoca, retire e coloque em outro recipiente.")
    print("Ao finalizar o chocolate branco, despeje ele sobre a pipoca enquanto mexe os dois.")
    print("Após finalizar esse processo, despeje o leite ninho sobre a pipoca e mexa novamente.")

    deu_certo = input("Deu certo? [S]im ou [N]ão: ")
    if deu_certo == "sim" or deu_certo == "s":
        print("Que bom, aproveite sua pipoca.")
    else:
        print("Sugiro que volte e recomeçe o processo")
    
else:
    print("Preciso da sua resposta para continuarmos. ")