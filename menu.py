from operacao import Operacao


class Menu:
    def __init__(self):
        self.num = 50
        self.opcao = -1
        self.exer = Operacao()
        self.num1 = 0
        self.num2 = 0
        self.a = 20
        self.b = 10
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.num10 = 0
        self.valores = []
        self.base = 0
        self.altura = 0
        self.reajuste = 0
        self.media = 0
        self.nota1 = 3
        self.nota2 = 7
        self.nota3 = 10

    def mostrarMenu(self):
        print("\n---- MENU ----\n\n"            +
              'Escolha uma das opções abaixo: ' +
              '\n0. SAIR'                       +
              '\n1. SOMAR'                      +
              '\n2. SUBTRAIR'                   +
              '\n3. DIVIDIR'                    +
              '\n4. MULTIPLICAR'                +
              '\n5. POTÊNCIA'                   +
              '\n6. RAIZ'                       +
              '\n7. TABUADA'                    +
              '\n8. NUMERAL'                    +
              '\n9. SOMA DE 1 ATÉ 100'          +
              '\n10. VARIAVEL'                  +
              '\n11. ANTECESSOR'                +
              '\n12. AREA DE UM RETÂNGULO'      +
              '\n13. IDADE EM DIAS'             +
              '\n14. ELEIÇÕES'                  +
              '\n15. NOVO SALARIO'              +
              '\n16. MEDIA DOS ALUNOS'          +
              '\n17. NÚMEROS EM ORDEM CRESCENTE')

    def coletar(self) -> object:
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print(f'Obrigado! :)')
            elif self.opcao == 1:
                self.coletar() #Chamando o input por meio do coletar
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos números é: {self.exer.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos números é: {self.exer.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos números é: {self.exer.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A potência dos números é: {self.exer.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'A raiz dos números é: {self.exer.raiz(self.num1)}')
                print(f'A raiz dos números é: {self.exer.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada de {self.num1} é: {self.exer.tabuada(self.num1)}')
                print(f'A tabuada de {self.num2} é: {self.exer.tabuada(self.num2)}')
            elif self.opcao == 8:
                print(f' 1, 2, 3, 4, 5, 6, 7, 8, 9, 10')

            elif self.opcao == 9:
                print(f"A soma dos números de 1 a 100 é: {self.num}")

            elif self.opcao == 10:
                print(f'A = {self.a}, B = {self.b}')

            elif self.opcao == 11:
                self.coletar()
                print(f'O antecessor de {self.num3} é {self.num3 - 1}')

            elif self.opcao == 12:
                self.coletar()
                print(f'A área do retângulo é {self.exer.multiplicar(self.base, self.altura)} ')

            elif self.opcao == 13:
                self.coletar()
                print(f"A idade total em dias é: {self.exer.calcularIdade(self.total)}")

            elif self.opcao == 14:
                self.coletar()
                print(f'Percentual de votos brancos: {self.brancos:.2f}%')
                print(f'Percentual de votos nulos: {self.nulos:.2f}%')
                print(f'Percentual de votos válidos: {self.validos:.2f}%')

            elif self.opcao == 15:
                self.coletar()
                print(f'O novo salário do funcionário após o reajuste é: R${self.exer.novoSalario(self.reajuste)}')
            elif self.opcao == 16:
                self.coletar()
                print(f"A média final do aluno é: {self.exer.mediaAluno(self.media, self.nota1,self.nota2, self.nota3)}")

            elif self.opcao == 17:
                self.coletar()
                print("Valores em ordem crescente:")
                for valor in self.valores:
                    print(valor, end=' ')