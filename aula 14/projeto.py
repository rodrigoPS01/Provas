contador_membro = 1
contador_livro = 1

class Livro:
    def __init__(self, titulo:str, autor:str, id:int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.stats = True

class Membro:
    def __init__(self, nome:str, n_membro:int) -> None:
        self.nome = nome
        self.n_membro = n_membro
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo = []
        self.registro_membros = []

    def add_livro(self):
        global contador_livro
        livro1 = Livro(titulo=str(input('nome do livro: ')).lower(), autor=str(input('Nome do autor: ')), id=contador_livro)
        self.catalogo.append(livro1)
        contador_livro += 1

    def add_membro(self):
        global contador_membro
        membro1 = Membro(nome=str(input('Qual o nome do membro: ')), n_membro=contador_membro)
        self.registro_membros.append(membro1)
        contador_membro +=1

    def emprestimo(self):
        id = int(input('Qual o seu ID de membro da biblioteca: '))
        for membro_atual in self.registro_membros:
            if id == membro_atual.n_membro:
                livro = str(input(f'{membro_atual.nome}, qual o nome do livro que você gostaria de pegar emprestado: ')).lower()
                for livro_atual in self.catalogo:
                    if livro == livro_atual.titulo:
                        if livro_atual.stats == True:
                            livro_atual.stats = False
                            membro_atual.livros_emprestados.append(livro)
                        else:
                            return 'Livro ja emprestado'
                    else:
                        return 'Livro invalido'
            else:
                return 'O ID que você digitou é invalido'        

    def devolucao(self):
        livro = str(input('Qual o nome do livro que você esta devolvendo: ')).lower()
        for i in self.catalogo:
            if livro == i.titulo:
                i.stats = True

    def filtro(self):
        escolha = str(input('Escreva o Título ou Autor ou ID do livro que gostaria de achar: '))
        for i in self.catalogo:
            if escolha == i.titulo or escolha == i.autor or int(escolha) == i.id:
                print(f'''
                Informações do Livro
                Título: {i.titulo}
                Autor: {i.autor}
                ID: {i.id}
                Disponibilidade para emprestimo: {i.stats}
                ''')
            else:
                print('Livro não encontrado')


biblioteca = Biblioteca()

while True:
    menu = int(input('''Menu de interação
1 - Adicionar livro
2 - Adicionar membro
3 - Emprestimo de livro
4 - Devolução de livro
5 - Pesquisar livro
0 - Sair
'''))

    match menu:
        case 1:
            print('Vamos Adicionar um livro')
            biblioteca.add_livro()
            print('Livro adiconado com sucesso')
        case 2:
            print('Vamos adicionar um membro')
            biblioteca.add_membro()
            print('Membro adicionado com sucesso')
        case 3:
            print('Vamos checar se você pode pegar um livro emprestado')
            print(biblioteca.emprestimo())
            print('Parabéns emprestimo realizado com sucesso')
        case 4:
            print('Vamos realizar a devolução de um livro')
            biblioteca.devolucao()
            print('Devolução realizada com sucesso')
        case 5:
            print('Pesquisar licros')
            biblioteca.filtro()
        case 0:
            break
        case _:
            print('Digite uma opção valida')
