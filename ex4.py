""" Nesse exercício a primeira função a ser criada foi o menu, aonde foi utilizada uma tupla para a criação dos campos obrigatorios e o menu.
A partir do menu você relaiza as chamadas das funções como a cadastrar usuários e imprimir o usuários e a saida.
Após isso foi criada a diciónario no inicio para receber o banco de usuários após foi criada um função que recebe por parametros 
os campos definidos como obrigatorios"""

banco_usuarios = {}

def cadastrarUsuario(camposObrigatorios):
    """ retorna um usuário para o dicionário banco_usuarios"""
    usuario = {}
    for campo in camposObrigatorios:
        usuario[campo] = input(f"Digite o valor para {campo}: ")
    while True:
        campoNovo = input("Caso seja necessário digite um campo adicional ou sair para encerrar: ")
        if campoNovo.lower() == 'sair':
            break
        usuario[campoNovo] = input(f"Digite o valor para {campoNovo}: ")
        
    id_usuario = print(f"usuário {len(banco_usuarios) + 1}")
    banco_usuarios[id_usuario] = usuario
    print("Usuário cadastrado com sucesso!!!")
    
    
    
    
    
    
#Inicializando uma tupla para receber os valores obrigatorios
def menu():
    camposObrigatorios = ()
    while True:
        novoCampo = input("Digite um campo obrigatório ou sair para encerrar: ")
        if novoCampo.lower() == 'sair':
            break
        camposObrigatorios += (novoCampo, )
    
    while True:
    
        print("1 - cadastrar usuário\n 2 - imprimir usuários \n 0 - encerrar.")
        menu = int(input(f"Entre com uma das opções: "))
    
        if menu == 1:
            cadastrarUsuario(camposObrigatorios)
        elif menu == 2:
            imprimirUsuarios()
        elif menu == 0:
            print("Encerrando o programa!!!")
            break
        else:
            print("Opção inválida")
    
    
        
        
    
    