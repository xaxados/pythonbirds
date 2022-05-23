class Pessoa:

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return(f'Olá {id(self)}')

if __name__ == '__main__':
    andre = Pessoa(nome='André')
    clara = Pessoa(andre, nome='Clara')
    print(Pessoa.cumprimentar(clara))
    print(id(clara))
    print(clara.cumprimentar())
    print(clara.nome)
    print(clara.idade)
    for filho in clara.filhos:
        print(filho.nome)




