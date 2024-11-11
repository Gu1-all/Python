# Atividade POO - Código
# Pedro Guilherme Pinheiro Alves

class Funcionario:
    def __init__(self, nome=str, cargo=str, salario=int):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario  

    def get_Salario(self):
        return self.__salario

    def aumentarSalario(self, aumento):
        if aumento > 0:
            self.__salario += aumento
        else:
            print("Aumento deve ser positivo.")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)
        self._bonus = bonus

    def get_salario(self):
        return super().get_Salario() + self._bonus


funcionario = Funcionario("João", "Colaborador", 2000)
print(f"{funcionario.nome} : \n Cargo - {funcionario.cargo} \n Salario - R$ {funcionario.get_Salario():.2f}")
funcionario.aumentarSalario(500)
print(f"Salário de {funcionario.nome} teve um aumento de R$500,00! Salario atual é de: R$ {funcionario.get_Salario():.2f}")

print("")

gerente = Gerente("Carlos", "Gerente", 5000, 2000)
print(f"{gerente.nome}: \n Cargo - {gerente.cargo} \n Salario - R$ {gerente.get_Salario():.2f}")
gerente.aumentarSalario(1000)
print(f"Salário de {gerente.nome} teve um aumento de R$1000,00! Salario atual + bonus é de: R$ {gerente.get_Salario():.2f}")


# Atividade POO - Questões
# Pedro Guilherme Pinheiro Alves

# Como a herança facilitou a criação da classe Gerente?
    # Devido a todos os atributos já terem sido pré-estabelecidos, não tive que reescrever
    # os mesmo atributos e parti direto para o código da classe, assim, facilitando
    # a criação do código.

# Como o encapsulamento protegeu o acesso direto ao salário?
    # Ao proteger o dado, evita-se a modificação do mesmo de forma maliciosa ou não intencional

# O que mudaria no código se o salário fosse acessível diretamente?
    # Qualquer um teria acesso a esse dado e poderia livremente mudar seu valor.
