#smtplib: Módulo responsavel por login e envio de e-mails.
import smtplib
#info_pessoal: arquivo "info_pessoal.py" responsável por ler csv com nome e e-mail.
import info_pessoal as info
#iteracao: arquivo "iteracao.py", esse arquivo contem a função de criacao da sequencia da loteria.
import iteracao as seq

#funcao "testando", recebe parametro cel
# Função faz uma verificação referente ao email informadondo se o mesmo é valido.
def testando(cel):
    endmail = raw_input("E-Mail: ")# Recebe o email do usuario para teste .
    pswd = raw_input("Password: ")#recebe a senha do usuario para teste.
    if 'gmail' in endmail: # Caso o email seja "gmail", a configuração é substituida.
            server = smtplib.SMTP('smtp.gmail.com:587')
            
    elif 'outlook' in endmail or 'hotmail' in endmail:# Caso o email seja "outlook" ou "hotmail", a configuração é substituida.
            server = smtplib.SMTP('smtp.live.com:587')
            
    else:# Caso o e-mail esteja incorreto, chama função novamente.
        print("\nE-Mail ou senha incorretos. Tente novamente\n")
        testando(cel)
    try:#realiza o login do email para teste
        server.starttls()
        server.login(endmail,pswd)
        
        print("FUNCIONANDO")# informa ao usuario que o email e senha estão corretos.
        send_mail(endmail,pswd,cel)#chama a função send_mail, passando os parametros de email, senha e numero de celulas.
        return
        #caso a autenticação do email de erro, ele chama a função novamente, e fecha o server, para poder logar de novo.
    except smtplib.SMTPAuthenticationError:
        print("\nE-Mail ou senha incorretos. Tente novamente\n")
        testando(cel)
        server.quit()


# Função para envio de e-mail.
def send_mail(endmail,pswd,cel):
    print(endmail,pswd)
# Lista de 1 á 60, total de números utilizado pela loteria.
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37          ,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
#Contador de mensagens enviadas
    c = 0
# ***   Variaveis   ***
    email_end = info.email()
    number = seq.itera(lista,cel)
    nome = info.nome()
# Verifica o dominio do email, configurando para determinadas opções, dependendo do que foi digitado.
    if 'gmail' in endmail:
            server = smtplib.SMTP('smtp.gmail.com:587')
            
    elif 'outlook' in endmail or 'hotmail' in endmail:
            server = smtplib.SMTP('smtp.live.com:587')

# Após passar pela verificação, loga no e-mail informado.        
    print("Enviando E-Mail")
    server.starttls()
    server.login(endmail,pswd)
# Entra no laço.
    while True:
        num1 = next(number)# Cria uma variavel com a sequencia de números
        nome1 = next(nome)#  Cria uma variavel com a sequencia de nomes

        if lista[-cel:] == num1:# Caso a proxima sequencia seja igual ao ultimo valor da lista...
            print("O numero de sequencias da loteria chegou ao fim")
            break# ... Finalize o programa.
            return
            
    # Tratamento de erro.
        try:
        #cria uma variavel com o corpo da mensagem
            message = ('Bom Dia {}.\nEssa sequencia lhe trara sorte para o proximo jogo {}'.format(nome1,num1))
            print("Numero {} enviado para {}\n".format(num1,nome1))
            server.sendmail(endmail, next(email_end),message)#envio de email(remetente, destinatario, mensagem)
            c = c + 1 # contador de mensagens enviadas
        # Caso haja queda na conexão de email, informe quantas requisições foram realizada, realize o login novamente    
        except smtplib.SMTPServerDisconnected:
            print("Erro de conexao SMTPServerDisconnected")
            print('Foram realizados {} requisicoes'.format(c))
            server.starttls()
            server.ehlo()
            server.login(endmail,pswd)            

    #Ao sair do while informa quantidade de requisições, fecha o email, termina o programa
    print('Foram realizado {} requisicoes'.format(c))
    server.quit()
    return
    
            

    
    
