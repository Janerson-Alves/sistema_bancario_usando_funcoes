import time


def menu(): #Define a função menu
    while True: #Inicia um loop infinito para exibir o menu até que uma opção válida seja selecionada.
        #Exibe o menu de opções para o usuário.
        print("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar Usuário
        [5] Criar conta bancaria
        [6] Sair
        """)
        opcao = input("=> ") #Solicita a escolha do usuário.
        if opcao.lower() in ['1', '2', '3', '4', '5', '6']: #Verifica se a opção selecionada é válida(se esta dentro da lista que passamos)
            return opcao.lower() #Retorna a opção selecionada pelo usuário, convertida para minúsculas e para o loop.
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.") #Se a opção não for inválida, exibe uma mensagem de erro e continua o loop.


def deposito(saldo, valor, extrato): #Define a função Depositar
    saldo += valor  # Adiciona o valor ao saldo
    extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra a transação no extrato (adiciona o registro)
    return saldo, extrato  # Retorna o saldo atualizado e o extrato

def sacar(saldo, valor, extrato, limite, numero_saque, limite_saque): #Define a função e passa os argumentos
    if valor > saldo: #Verifica se o valor do saque e maior que o saldo
        print('Erro na Operação! Você não possui saldo suficiente para o saque!')
    elif valor > limite: #Verifica se o valor do saque e maior que o limite da conta
        print('Erro na Operação! O Valor do saque excede o limite') 
    elif numero_saque > limite_saque: #Verifica se o numero_saque e maior que o linite_saque(3)
        print('Erro na Operação! Numero máximo de saques excedido')
    elif valor <= 0: #Verifica se o valor do saque e menor igual a zero
        print('Erro na Operação! Valor digitado e invalido!')
    else: # Se todas as verificações forem falsas
        saldo -= valor # Retira o valor(saque) do saldo
        extrato += f'Saque: R$ {valor:.2f}\n' #Registra a transação no extrato (adiciona o registro)
        numero_saque += 1 #Acrescenta +1 em cada saque realizado!
    return saldo, extrato #Retonar 2 argumentos saque, extrato

def extrato(saldo, *, extrato):#Criando a função extrato
    if extrato: #Verifica se há algo na variavel extrato
        print('#################### Extrato ####################')
        print(extrato) #Mostra na tela tudo que tem na variavel extrato
    else: # se afirmação acima for falsa
        print('\nNão foram realizadas movimentações') 
    
    print(f'\nSaldo: R$ {saldo:.2f}') #Mostra o saldo da conta
    print('######################################################')
    

def criar_usuario(lista_usuarios): #Cria a função criar_usuario e passa o argumento lista_usuarios
    # Pede para o usuário digitar os dados que esta sendo pedido(nome, data_nascimento, cpf, endereço)
    nome = input('Digite o seu nome: ')
    data_nascimento = input('Digite a data de nascimento no formato DD/MM/AAAA: ') 
    cpf = input('Digite o seu CPF no formato XXX.XXX.XXX-XX: ') 
    endereco = input('Digite o seu endereço (logradouro, numero - Bairro - Cidade/UF): ')
    
    #Verifica se o CPF já esta cadastrado:
    for usuario in lista_usuarios: #Iterá sobre cada dado da lista
        if usuario['cpf'] == cpf: #Verifica se o cpf digitado esta na lista
            print('Ja existe um usuário cadastrado com esse CPF') 
            return #Retorna para o cadastro
        
    #Criando um dicionario com as informações do usuario
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    #Adicionando os dados do dicionario a lista
    lista_usuarios.append(novo_usuario)
    
    #Mensagem de usuário cadastrado com sucesso
    print('Usuário cadastrado com sucesso!!!!')
    
def conta_corrente(lista_contas, lista_usuarios): 
    # Solicitar CPF do usuário para vincular à conta
    cpf = input("Digite o CPF do usuário para o qual deseja criar a conta: ")
    
    # Verificar se o usuário com CPF fornecido existe na lista de usuários
    usuario_encontrado = None 
    for usuario in lista_usuarios: 
        if usuario['cpf'] == cpf: 
            usuario_encontrado = usuario 
            break 
    
    # Se nenhum usuário foi encontrado com o CPF fornecido, exibir mensagem e sair da função
    if usuario_encontrado is None:
        print('Não foi encontrado nenhum usuário com o CPF fornecido.')
        return
    
    # Criar o número da conta (sequencial) a partir de 1
    numero_conta = len(lista_contas) + 1
    
    # Criar um dicionário com as informações da conta corrente
    nova_conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado 
    }
    
    # Adicionar as informações do dicionário da conta na lista_contas
    lista_contas.append(nova_conta)
    
    # Mensagem de conta bancária criada com sucesso
    print('Conta corrente criada com sucesso!!')
    print(f'Número da conta: {numero_conta}')
    print(f'Titular da conta: {usuario_encontrado["nome"]}')
    

#lista para armazenar usuários e contas
lista_usuarios = []
lista_contas = []

#Controle do número de saques
numero_saque = 0
limite_saque = 3

# Lista para armazenar usuários e contas
lista_usuarios = []  # Inicializa uma lista vazia para armazenar os dados dos usuários
lista_contas = []  # Inicializa uma lista vazia para armazenar os dados das contas

# Variáveis de controle para o número máximo de saques
numero_saque = 0  # Inicializa a variável que conta o número de saques como zero
limite_saque = 3  # Define o limite máximo de saques como 3

saldo = 0  # Inicializa o saldo da conta como zero
extrato_conta = ''  # Inicializa o extrato da conta como uma string vazia

# Loop principal que exibe o menu e processa as opções escolhidas pelo usuário
while True:
    opcao = menu()  # Chama a função menu() para exibir o menu e obter a opção escolhida pelo usuário
    
    # Verifica a opção selecionada e executa a função correspondente
    if opcao == '1':
        valor_deposito = float(input('Digite o valor do deposito: R$ '))
        saldo, extrato_conta = deposito(saldo, valor_deposito, extrato_conta) # Chama a função para realizar o depósito (passa os 3 parametros porém substituindo o parametro valor pelo valor_deposito)
        
    elif opcao == '2': 
        valor_saque = float(input('Digite o valor do saque: R$ '))
        saldo, extrato_conta = sacar(saldo=saldo, valor=valor_saque, extrato=extrato_conta, limite=1000, numero_saque=numero_saque, limite_saque=limite_saque)  # Chama a função para realizar o saque
        
    elif opcao == '3':
        extrato(saldo, extrato=extrato_conta) # Chama a função para exibir o extrato da conta
        
    elif opcao == '4':
        criar_usuario(lista_usuarios) # Chama a função para criar um novo usuário
        
    elif opcao == '5':
        conta_corrente(lista_contas, lista_usuarios) # Chama a função para criar uma nova conta corrente
        
    elif opcao == '6':
        print('Saindo...')
        time.sleep(2)
        break
    
        
