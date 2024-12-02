class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} ({self.ano_publicacao}) por {self.autor} - {status}"


class Usuario:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)

    def __str__(self):
        return f"{self.nome} (Matrícula: {self.matricula}) - Livros emprestados: {len(self.livros_emprestados)}"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, titulo, autor, ano_publicacao):
        livro = Livro(titulo, autor, ano_publicacao)
        self.livros.append(livro)

    def cadastrar_usuario(self, nome, idade, matricula):
        usuario = Usuario(nome, idade, matricula)
        self.usuarios.append(usuario)

    def emprestar_livro(self, matricula, titulo):
        usuario = next((u for u in self.usuarios if u.matricula == matricula), None)
        livro = next((l for l in self.livros if l.titulo == titulo), None)
        if usuario and livro:
            if usuario.emprestar_livro(livro):
                print(f"Livro '{titulo}' emprestado para {usuario.nome}.")
            else:
                print(f"Livro '{titulo}' não está disponível.")
        else:
            print("Usuário ou livro não encontrado.")

    def devolver_livro(self, matricula, titulo):
        usuario = next((u for u in self.usuarios if u.matricula == matricula), None)
        livro = next((l for l in self.livros if l.titulo == titulo), None)
        if usuario and livro:
            usuario.devolver_livro(livro)
            print(f"Livro '{titulo}' devolvido por {usuario.nome}.")
        else:
            print("Usuário ou livro não encontrado.")

    def listar_livros_disponiveis(self):
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        print("\nLivros disponíveis:")
        for livro in disponiveis:
            print(livro)

    def listar_usuarios_com_livros(self):
        usuarios_com_livros = [usuario for usuario in self.usuarios if usuario.livros_emprestados]
        print("\nUsuários com livros emprestados:")
        for usuario in usuarios_com_livros:
            print(usuario)


biblioteca = Biblioteca()

# Cadastro de livros
biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
biblioteca.cadastrar_livro("1984", "George Orwell", 1949)
biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)

# Cadastro de usuários
biblioteca.cadastrar_usuario("João Silva", 25, "1234")
biblioteca.cadastrar_usuario("Maria Oliveira", 30, "5678")

# Operações
biblioteca.emprestar_livro("1234", "1984")
biblioteca.emprestar_livro("5678", "O Senhor dos Anéis")
biblioteca.devolver_livro("1234", "1984")

# Relatórios
biblioteca.listar_livros_disponiveis()
biblioteca.listar_usuarios_com_livros()
