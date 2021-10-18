class Eleicao:
    def __init__(self, totalEleitores, votosValidos, votosBranco, VotosNulos):
        self.totalEleitores = totalEleitores
        self.votosValidos = votosValidos
        self.votosBranco = votosBranco
        self.VotosNulos = VotosNulos

    def percentualValidosTotalEleitores (self):
        return print(int((self.votosValidos/self.totalEleitores)*100),"% dos votos são validos")

    def percentualBrancoTotalEletores (self):
        return print(int((self.votosBranco/self.totalEleitores)*100),"% dos votos são em branco")

    def percentualNuloTotalEletores (self):
        return print(int((self.VotosNulos/self.totalEleitores)*100),"% dos votos são nulos")

contagem = Eleicao(1000,800,150,50)
contagem.percentualValidosTotalEleitores()
contagem.percentualBrancoTotalEletores()
contagem.percentualNuloTotalEletores()