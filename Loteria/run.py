# Importa o arquivo "mail.py"
import mail


print("************ LOTERIA ************")

#cel: Determina quantas células deverá ter o sorteio
cel = int(raw_input("Digite o número de células do sorteio: "))

print('\nEm seguida, digite seu E-Mail e Senha\n')

#chama a função testando
mail.testando(cel)


    

