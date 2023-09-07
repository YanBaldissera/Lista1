""" Neste exercício, iniciamos criando a função de menu, que utiliza uma tupla para definir os campos obrigatórios e apresenta opções para 
cadastrar usuários, imprimir usuários e sair. Em seguida, inicializamos um dicionário para armazenar o banco de usuários e criamos uma 
função que recebe os campos obrigatórios como parâmetros.

Posteriormente, foi desenvolvido a função para imprimir os usuários, utilizando *args e **kwargs para receber o ID do usuário e os 
outros campos. Na opção 1, a função percorre os IDs e campos dos usuários, realizando a impressão. Já na opção 2, solicita ao usuário 
os nomes a serem pesquisados e utiliza a função get para obter o valor da chave "nome".

Na opção 3, utilizamos a função filter para filtrar os campos desejados conforme a solicitação do usuário. Na opção 4, seguimos um método 
semelhante ao da opção 3, mas antes pedimos ao usuário os nomes a serem pesquisados e, em seguida, os campos de pesquisa."""

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
        
    id_usuario = f"usuário_{len(banco_usuarios) + 1}"
    banco_usuarios[id_usuario] = usuario
    print("Usuário cadastrado com sucesso!!!")
    
    
def imprimirUsuarios(*args, **kwargs):
    """Vai imprimir os valores desejados por pesquisa do usuário"""
    menu = int(input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nDigite a opção: "))
    
    if menu == 1:
        for idUsuario, infoUsuario in banco_usuarios.items():
            print(f"Usuário ID: {idUsuario}")
            print(infoUsuario)
            
    elif menu == 2:
        nomeDosCampos = input("Digite os nomes dos campos separados por vírgula: ").split(",")
        for idUsuario, infoUsuario in banco_usuarios.items():
            if infoUsuario.get('nome') in nomeDosCampos:
                print(f"Usuário ID: {idUsuario}")
                print(infoUsuario)
                
    elif menu == 3:
        valoresDosCampos = []
    
        while True:
            campoDeBusca = input("Digite o campo de busca ou 'sair' para encerrar: ")
            if campoDeBusca.lower() == 'sair':
                break
        
            valorDoCampo = input(f"Digite o valor do campo {campoDeBusca}: ")
            valoresDosCampos.append((campoDeBusca, valorDoCampo))
        
        def filtro(usuario):
            """Retorna True se o usuário atender aos critérios, caso contrário, False."""
            return all(usuario.get(campo) == valor for campo, valor in valoresDosCampos)

        usuariosFiltrados = filter(
            filtro, banco_usuarios.values()
        )
    
        for infoUsuario in usuariosFiltrados:
            for idUsuario, info in banco_usuarios.items():
                if info == infoUsuario:
                    print(f"Usuário ID: {idUsuario}")
                    print(infoUsuario)
                    
    elif menu == 4:
        nomes = input("Digite os nomes separados por vírgula: ").split(",")
        campos = {}
    
        while True:
            campoDeBusca = input("Digite o campo de busca ou 'sair' para encerrar: ")
            if campoDeBusca.lower() == 'sair':
                break
            
            valorDoCampo = input(f"Digite o valor do campo {campoDeBusca}: ")
            campos[campoDeBusca] = valorDoCampo
        
        def filtro(usuario):
            """Retorna uma lista dos usuários que atendem aos critérios de filtro."""
            return usuario.get('nome') in nomes and all(usuario.get(campo) == valor for campo, valor in campos.items())

        usuariosFiltrados = filter(filtro, banco_usuarios.values())
    
        for infoUsuario in usuariosFiltrados:
            for idUsuario, info in banco_usuarios.items():
                if info == infoUsuario:
                    print(f"Usuário ID: {idUsuario}")
                    print(infoUsuario)
    
    else:
        print("Opção inválida!")
    
    
#Inicializando uma tupla para receber os valores obrigatorios
def menu():
    """função main do projeto serve para iniciar e rodar o código"""
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
            
            
menu()
    
    
        
        
    
    