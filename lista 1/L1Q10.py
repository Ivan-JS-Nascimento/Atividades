print('Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…')
print('Quantos dos amigos dele conseguirão ajudar dessa vez?')
quant_p = int(input())
n1=''
n2=''
n3=''
n4=''
lugar=''

if quant_p != 0:
    print('Hora da lista dos amigos da vez!')
    # sobre os nomes fornecidos
    n1=input()
    print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.' if n1=='Barney' else 'Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.' if n1=='Robin' else 'O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.' if n1=='Marshall' else 'Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.' if n1=='Lily' else f'{n1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
    if quant_p > 1:
        n2=input()
        print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.' if n2=='Barney' else 'Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.' if n2=='Robin' else 'O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.' if n2=='Marshall' else 'Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.' if n2=='Lily' else f'{n2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
    if quant_p > 2:
        n3=input()
        print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.' if n3=='Barney' else 'Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.' if n3=='Robin' else 'O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.' if n3=='Marshall' else 'Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.' if n3=='Lily' else f'{n3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
    if quant_p > 3:
        n4=input()
        print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.' if n4=='Barney' else 'Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.' if n4=='Robin' else 'O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.' if n4=='Marshall' else 'Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.' if n4=='Lily' else f'{n4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')

if quant_p != 0:
    lugar=input()

if lugar == 'MacLaren’s Pub' or quant_p==0:
    lugar='MacLaren’s Pub'
    quant_m_c=int(input())
# após receber todos os nomes
if quant_p==2:
    if (n1 == 'Marshall' or n1 == 'Lily') and (n2 == 'Marshall' or n2 == 'Lily'):
        print('Nada melhor que um casal para dar conselhos de relacionamento.')
    elif (n1 == 'Barney' or n1 == 'Marshall') and (n2 == 'Marshall' or n2 == 'Barney'):
        print('Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.')
elif quant_p==4:
    is_n1_core = (n1 == 'Barney' or n1 == 'Robin' or n1 == 'Marshall' or n1 == 'Lily')
    is_n2_core = (n2 == 'Barney' or n2 == 'Robin' or n2 == 'Marshall' or n2 == 'Lily')
    is_n3_core = (n3 == 'Barney' or n3 == 'Robin' or n3 == 'Marshall' or n3 == 'Lily')
    is_n4_core = (n4 == 'Barney' or n4 == 'Robin' or n4 == 'Marshall' or n4 == 'Lily')
    if is_n1_core and is_n2_core and is_n3_core and is_n4_core:
        print('O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.')

# saídas especiais relacionando nomes com local escolhido
if (n1 == 'Barney' or n2 == 'Barney' or n3 == 'Barney' or n4 == 'Barney') and lugar=='Arena de Laser Tag':
    print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
elif quant_p==1 and n1=='Robin' and lugar=='Carmichael’s':
    print('Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.')
elif quant_p!=0 and lugar=='MacLaren’s Pub':
    has_core_friend = (n1 == 'Barney' or n1 == 'Robin' or n1 == 'Marshall' or n1 == 'Lily' or
                       n2 == 'Barney' or n2 == 'Robin' or n2 == 'Marshall' or n2 == 'Lily' or
                       n3 == 'Barney' or n3 == 'Robin' or n3 == 'Marshall' or n3 == 'Lily' or
                       n4 == 'Barney' or n4 == 'Robin' or n4 == 'Marshall' or n4 == 'Lily')
    if has_core_friend:
        print('Não tem erro, né? Estar no MacLaren’s é como estar em casa.')
    else:
        print('Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.')

# relatório final
print('')
if quant_p==0:
    print(f'Relatório da situação de Ted:\nTed foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.\n- Quantidade de cervejas bebidas por Ted: {quant_m_c} cervejas.')
else:
    print('Relatório da situação de Ted:')
    if quant_p == 1:
        print(f'- Ted foi consolado por: {n1}.')
    elif quant_p == 2:
        print(f'- Ted foi consolado por: {n1} e {n2}.')
    elif quant_p == 3:
        print(f'- Ted foi consolado por: {n1}, {n2} e {n3}.')
    else:
        print(f'- Ted foi consolado por: {n1}, {n2}, {n3} e {n4}.')
    print(f'- O local de afogar as mágoas foi: {lugar}.')
    # Frases envolvendo a quantidade de pessoas
    if quant_p==1:
        print('- Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas.')
    elif quant_p==2:
        print('- Duas pessoas se compadeceram com a situação do pobre Ted.')
    elif quant_p==3:
        print('- Três pessoas! Ted conseguiu se divertir bastante.')
    else:
        is_n1_core = (n1 == 'Barney' or n1 == 'Robin' or n1 == 'Marshall' or n1 == 'Lily')
        is_n2_core = (n2 == 'Barney' or n2 == 'Robin' or n2 == 'Marshall' or n2 == 'Lily')
        is_n3_core = (n3 == 'Barney' or n3 == 'Robin' or n3 == 'Marshall' or n3 == 'Lily')
        is_n4_core = (n4 == 'Barney' or n4 == 'Robin' or n4 == 'Marshall' or n4 == 'Lily')
        if is_n1_core and is_n2_core and is_n3_core and is_n4_core:
            print('- O quinteto junto consegue resolver qualquer problema!')
        else:
            print('- Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre.')
    #----
    if lugar== 'MacLaren’s Pub':
        print(f'- Quantidade de cervejas bebidas pelo grupo: {quant_m_c*(quant_p+1)} cervejas.')
    print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')