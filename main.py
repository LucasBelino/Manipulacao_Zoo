class Animal: #Classe mãe de animal
    def init(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        if self.idade < 10 and self.especie == 'Africano':
            self.som = "Paaah"
        elif self.idade >= 10 and self.especie == 'Africano':
            self.som = "PAHHHHHH"

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

class Elefante(Animal): #Classe que herda atributos de Animal
    def init(self, tamanho):
        self.tamanho = tamanho

    def trombar(self):
            print(self.emitir_som())

    def mudar_tamanho(self, novo_tamanho):
        novo_tamanho = "pequeno"
        self.tamanho = novo_tamanho


animal = Elefante()
animal.nome = input("Digite o nome do elefante: ")
animal.idade = input("Digite a idade do elefante: ")
animal.cor = input("Digite a cor do elefante: ")
animal.tamanho = input("Digite o tamanho do elefante: ")

print(animal.trombar())
print(animal.emitir_som())
print(animal.tamanho)
