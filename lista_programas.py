class Programa:
    def __init__(self,nome,ano): 
        self._nome = nome.title() 
        self.ano = ano
        self._likes = 0  

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    
    @property 
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self, novo_nome): 
        self._nome = novo_nome.title()

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes')

class Filme(Programa): 
    def __init__(self,nome,ano,duracao):
        super().__init__(nome, ano) 
        self.duracao = duracao

    # Faz necessario criar outros imprimes por que tem valoresdiferentes
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} Minutos- {self._likes} Likes')

class Serie(Programa):  
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)  
        self.temporadas = temporadas

     
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes')


django = Filme('Django', 2018, 160) 
django.dar_likes()


atlanta = Serie('Atlanta', 2016, 5) 
atlanta.dar_likes()

dark = Serie('Dark', 2018, 3) 
dark.dar_likes()


filmes_e_series = [django, atlanta, dark]

for programa in filmes_e_series:
    programa.imprime()
