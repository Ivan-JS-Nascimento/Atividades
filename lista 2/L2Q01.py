print('Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?')
n = int(input())
qtd_trocas=0
for i in range(n):
    nome_participante=input()
    palavra_falada=input()
    if i==0:
        palavra_inicial=palavra_falada
        palavra_atual=palavra_falada
    else:
        if palavra_falada!=palavra_atual:
            qtd_trocas += 1
            print(f'Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…')
            if qtd_trocas==1:
                erro_n1=nome_participante
                erro_p1=palavra_falada
            elif qtd_trocas==2:
                erro_n2=nome_participante
            palavra_atual=palavra_falada
        if qtd_trocas==5:
            print(f'Caramba, que confusão! A palavra {palavra_inicial} já tá toda embaralhada e virou {palavra_falada}!')
if palavra_falada==palavra_inicial and qtd_trocas==0:
    print(f'Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_inicial}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.')
elif palavra_falada==palavra_inicial:
    print(f'Parece que ocorreram {qtd_trocas} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_inicial} conseguiu chegar no fim do telefone sem fio.')
else:
    if qtd_trocas==1:
        print(f'Poxa, foi por pouco, só quem errou foi {erro_n1} que disse {erro_p1} ao invés de {palavra_inicial}…')
    elif qtd_trocas==2:
        print(f'Se não fosse pelos erros de {erro_n1} e {erro_n2} a palavra {palavra_inicial} poderia ter chegado até o fim, talvez eles devessem tentar de novo.')
    else:
        print(f'É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_inicial} acabou virando {palavra_falada}. No total, ocorreram {qtd_trocas} trocas.')