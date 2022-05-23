class Pessoa:
    olhos = 2

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
    clara.sobrenome = 'Barroso'
    print(clara.sobrenome)
    del clara.sobrenome
    print(clara.__dict__)
    print(andre.__dict__)
    print(Pessoa.olhos)
    print(andre.olhos)
    print(clara.olhos)
