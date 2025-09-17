Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())
quant_aulas = int(input())
quant_faltas = int(input())
media = float((Nota1+Nota2+Nota3)/3)
presenca = (100 * (quant_aulas-quant_faltas))/quant_aulas
print(f'Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.')
if media >= 8 and presenca >= 75:
    print('Chris está APROVADO por nota e por presença! 🎉')
    print('Pisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.')
if media >= 7 and media < 8 and presenca >= 75:
    print('Chris está APROVADO! ✅')
    print('Sacomé, né? Passou raspando, mas a pizza ainda ficou longe.')
if media >= 7 and presenca < 75:
    print('Chris ESTÁ REPROVADO por FALTA. ❌')
    print('Trágico! Não adianta só saber, tem que aparecer.')
if media < 7 and presenca >= 75:
    print('Chris ESTÁ REPROVADO por NOTA. ❌')
    print('Chris, já pro seu quarto ou eu vou te bater até você virar o avesso!')
if media < 7 and presenca < 75:
    print('Chris ESTÁ REPROVADO por NOTA e por FALTA. ❌')
    print('Chris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.')