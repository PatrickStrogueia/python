import abc

# ==============================================================================
# 1. ENCAPSULAMENTO (Encapsulation)
# ==============================================================================
# O encapsulamento protege os dados internos de um objeto de modificações
# diretas indesejadas, expondo apenas o que é necessário por meio de métodos ou propriedades.
# Em Python, usamos um underline (_) para indicar que um atributo é protegido,
# e dois underlines (__) para torná-lo privado (mecanismo de Name Mangling).

class ContaEstudante:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado. Não pode ser acessado diretamente fora da classe.
        self.__limite = 500.0         # Limite fixo privado.

    # Usamos o decorador @property para criar um "getter" (método de leitura)
    @property
    def saldo(self):
        """Retorna o saldo atual. Acesso controlado apenas para leitura."""
        return self.__saldo

    # Usamos o decorador @limite.setter para criar um "setter" (método de escrita/alteração)
    # permitindo colocar validações antes de alterar o valor.
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite: float):
        """Permite alterar o limite apenas se for um valor positivo e até R$ 1000."""
        if novo_limite < 0:
            print("Erro: O limite não pode ser negativo.")
        elif novo_limite > 1000:
            print("Erro: O limite máximo para conta estudante é R$ 1.000,00.")
        else:
            self.__limite = novo_limite
            print(f"Limite atualizado para R$ {self.__limite:.2f}")


# ==============================================================================
# 2. HERANÇA E POLIMORFISMO (Inheritance & Polymorphism)
# ==============================================================================
# Herança: Permite que uma classe filha herde atributos e métodos de uma classe pai.
# Polimorfismo: Permite que classes diferentes tenham métodos com o mesmo nome,
# mas com comportamentos (implementações) diferentes.

class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        """Método genérico que será sobrescrito pelas classes filhas."""
        print("O veículo está se movendo de alguma forma.")


class Carro(Veiculo):
    def mover(self):
        # Sobrescrita de método (Polimorfismo)
        print(f"O carro {self.marca} {self.modelo} está acelerando nas quatro rodas pela rodovia!")


class Moto(Veiculo):
    def mover(self):
        # Sobrescrita de método (Polimorfismo)
        print(f"A moto {self.marca} {self.modelo} está acelerando sobre duas rodas cortando o trânsito!")


# ==============================================================================
# 3. ABSTRAÇÃO (Abstraction)
# ==============================================================================
# A abstração foca em esconder a complexidade de uma implementação externa,
# fornecendo apenas a interface/modelo essencial.
# Em Python, usamos a biblioteca nativa `abc` (Abstract Base Classes) para isso.
# Uma classe abstrata NÃO pode ser instanciada diretamente e serve como molde.

class CanalNotificacao(abc.ABC):
    
    @abc.abstractmethod
    def enviar(self, mensagem: str, destinatario: str):
        """Qualquer classe que herdar de CanalNotificacao DEVE implementar este método."""
        pass


class EnviarEmail(CanalNotificacao):
    def enviar(self, mensagem: str, destinatario: str):
        print(f"📧 Enviando E-mail para [{destinatario}]: {mensagem}")


class EnviarSMS(CanalNotificacao):
    def enviar(self, mensagem: str, destinatario: str):
        print(f"💬 Enviando SMS para [{destinatario}]: {mensagem}")


# ==============================================================================
# 4. MÉTODOS MÁGICOS / DUNDER METHODS (Magic Methods)
# ==============================================================================
# Métodos mágicos (começam e terminam com dois underlines) permitem que nossas
# classes personalizadas interajam com operadores e funções nativas do Python
# (como print(), len(), +, ==, etc.).

class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # __str__ define o que é exibido ao rodar print(objeto) ou str(objeto)
    def __str__(self):
        return f"'{self.titulo}' escrito por {self.autor} ({self.paginas} páginas)"

    # __len__ permite usar a função nativa len(objeto)
    def __len__(self):
        return self.paginas

    # __eq__ permite comparar dois objetos usando o operador de igualdade (==)
    def __eq__(self, outro_livro):
        if not isinstance(outro_livro, Livro):
            return False
        return self.titulo == outro_livro.titulo and self.autor == outro_livro.autor


# ==============================================================================
# 🧪 CÓDIGO DE TESTE/EXECUÇÃO (Demonstração dos conceitos)
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. Testando Encapsulamento ===")
    conta = ContaEstudante("Patrick", 150.0)
    
    # print(conta.__saldo) # Descomentar esta linha causará um erro (AttributeError)
    print(f"Titular: {conta.titular}")
    print(f"Saldo (via property getter): R$ {conta.saldo:.2f}")
    
    print("\nTentando alterar limite de forma inválida:")
    conta.limite = 1500.0  # Passa do limite estudante
    print("Tentando alterar limite de forma válida:")
    conta.limite = 800.0   # Válido

    print("\n" + "=" * 40 + "\n")

    print("=== 2. Testando Herança e Polimorfismo ===")
    veiculos = [
        Carro("Chevrolet", "Onix"),
        Moto("Honda", "CB 500")
    ]
    
    # Executamos o mesmo método 'mover()', mas cada um se comporta de maneira diferente (Polimorfismo)
    for v in veiculos:
        v.mover()

    print("\n" + "=" * 40 + "\n")

    print("=== 3. Testando Abstração ===")
    # notificador = CanalNotificacao() # Descomentar esta linha dará erro de TypeError (abstrata)
    
    canais = [
        EnviarEmail(),
        EnviarSMS()
    ]
    
    for canal in canais:
        canal.enviar("Sua fatura foi fechada com sucesso!", "cliente@provedor.com")

    print("\n" + "=" * 40 + "\n")

    print("=== 4. Testando Métodos Mágicos (Dunder) ===")
    livro1 = Livro("Pense em Python", "Allen B. Downey", 240)
    livro2 = Livro("Pense em Python", "Allen B. Downey", 240)
    livro3 = Livro("Código Limpo", "Robert C. Martin", 425)

    # Testando __str__
    print(f"Representação em texto do livro: {livro1}")
    
    # Testando __len__
    print(f"Quantidade de páginas do livro: {len(livro1)} páginas")
    
    # Testando __eq__ (comparação ==)
    print(f"Livro 1 é igual ao Livro 2? {livro1 == livro2}")  # True
    print(f"Livro 1 é igual ao Livro 3? {livro1 == livro3}")  # False
