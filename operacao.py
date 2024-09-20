import math


class Operacao:


    def __init__(self):  #Construtor
        self.dias = 0
        self.altura = 0
        self.base = 0
        self.limite = 0
        self.num1 = 0
        self.num2 = 0
        self.a = 20
        self.b = 10
        self.base = 0
        self.altura = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.num10 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def somar(self, num1, num2):
        self.coletar(num1, num2)  #utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossivel dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        self.coletar(num)
        return math.sqrt(num)

    def coletarMultiplos(self, num):
        for num in range(1, self.limite + 1):
            if 5 != 0: continue


    #EXERCICIO 1

    def variavel(self, a, b, c):
        self.coletar(a, b, c)
        self.a <- 20

        self.b <- 10

        self.c <- self.a
        self.a <- self.b
        self.b <- self.c

    def antecessor(self, num3):
        self.coletar(num3)

    def areaRetangulo (self,base, altura, area):
        self.coletar(base, altura, area)
        self.base = float(input('Digite a base do retângulo: '))
        self.altura = float(input("Digite a altura do retângulo: "))
        return self.base * self.altura

    def calcularIdade(self, anos, meses, dias):
        self.coletar(anos, meses, dias)
        total = (self.anos * 365) + (self.meses * 30) + self.dias
        return total
        print("Calcular Idade em Dias")
        self.anos = int(input("Digite a idade em anos: "))
        self.meses = int(input("Digite os meses adicionais: "))
        self.dias = int(input("Digite os dias adicionais: "))
        return self.anos, self.meses, self.dias

    def eleicao(self,eleitores, brancos, nulos, validos,):
        self.coletar(eleitores, brancos, nulos, validos)
        self.eleitores = int(input("Digite o número total de eleitores do município: "))
        self.brancos = int(input("Digite o número de votos brancos: "))
        self.nulos = int(input("Digite o número de votos nulos: "))
        self.validos = int(input("Digite o número de votos válidos: "))
        self.bran = (self.brancos / self.eleitores) * 100
        self.nul = (self.nulos / self.eleitores) * 100
        self.val = (self.validos / self.eleitores) * 100

    def novoSalario(self, atual, reajuste,):
        self.coletar(atual, reajuste)
        try:
            self.atual = float(input(f'Digite o salário mensal atual do funcionário: '))
            self.reajuste = float(input(f'Digite o percentual de reajuste (em decimal): '))

        finally:
            self.novo = (self.atual * (1 + self.reajuste))

    def custoCarro(self,fabrica):
        self.coletar(fabrica)
        try:
            self.fabrica = float(input(int(f'Digite o custo de fábrica do carro: ')))
        finally:
            self.distribuidor = 0.28
            self.impostos = 0.45
        self.distribuidor = self.fabrica * self.distribuidor
        self.impostos = self.fabrica * self.impostos
        self.final = self.fabrica + self.distribuidor + self.impostos

    def mediaAluno(self, media, nota1, nota2, nota3):
        self.coletar(nota1, nota2, nota3, media)

        nota1 = input("Digite a primeira nota do aluno: ")
        nota2 = input("Digite a segunda nota do aluno: ")
        nota3 = input("Digite a terceira nota do aluno: ")

        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)

        self.media = (self.nota1 + self.nota2 + self.nota3) / 3

    def ordenadorValores(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
        self.coletar(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
        while(self.coletar) < 10:
            novo_valor = int(input(f"Digite o {len(self.coletar) + 1}º valor: "))
            if novo_valor not in self.coletar:
                self.coletar.append(novo_valor)
            else:
                print("Valor repetido. Por favor, insira um valor diferente.")