# Importa o arquivo "mail.py"
import mail


print("************ LOTERIA ************")

#cel: Determina quantas c�lulas dever� ter o sorteio
cel = int(raw_input("Digite o n�mero de c�lulas do sorteio: "))

print('\nEm seguida, digite seu E-Mail e Senha\n')

#chama a fun��o testando
mail.testando(cel)


    

