from datetime import datetime

class Pet:
    def __init__(self, nome: str):
        self.nome = nome
        self.nivel = 1
        self.xp = 0
        self.energia = 100
        self.forca = 5
        self.agilidade = 5
        self.inteligencia = 5
        self.afinidade = "neutro"

    def atualizar_afinidade(self, acao:str):
        hora = datetime.now().hour
        # Define a afinidade com base na ação e hora do dia
        if acao == "alimentar" and 6<= hora < 12:
            self.afinidade = "terra"
        elif acao == "brincar" and 12 <= hora < 18:
            self.afinidade = "ar"  
        elif acao == "estudar" and 18 <= hora < 22:
            self.afinidade = "água"
        elif acao == "treinar" and (hora >= 22 or hora < 6):
            self.afinidade = "fogo"

    def ganhar_xp(self, quantidade:int):
        self.xp += quantidade
        self.verificar_evolucao()

    def verificar_evolucao(self):
        while self.xp >= 100 * self.nivel:
            self.xp -= 100 * self.nivel
            self.nivel += 1
            print(f"[bold yellow]{self.nome} subiu para o nível {self.nivel}![/bold yellow]")
            self.aplicar_mutacao()

    def aplicar_mutacao(self):
        if self.nivel == 5:
            print(f"{self.nome} se tornou uma criança mágica!")
        elif self.nivel == 10:
            print(f"{self.nome} ganhou uma nova forma! Escolha uma mutação.")


    def alimentar(self):
        self.energia = min(100, self.energia + 10)
        self.ganhar_xp(5)
        self.atualizar_afinidade("alimentar")

    def brincar(self):
        if self.energia >= 10:
            self.agilidade += 1
            self.energia -= 10
            self.ganhar_xp(5)
            self.atualizar_afinidade("brincar")
        else:
            print("[red]TRÊMULO!! O pet está cansado demais para brincar.[/red]")

    def estudar(self):
        if self.energia >= 15:
            self.inteligencia += 1
            self.energia -= 15
            self.ganhar_xp(5)
            self.atualizar_afinidade("estudar")
        else:
            print("[red]CONFUSO!! O pet está muito cansado para aprender algo novo.[/red]")

    def treinar(self):
        if self.energia >= 20:
            self.forca += 1
            self.energia -= 20
            self.ganhar_xp(5)
            self.atualizar_afinidade("treinar")
        else:
            print("[red]CANSADO!! O pet está muito cansado para treinar.[/red]")
    
    def dormir(self):
        self.energia = 100
        self.ganhar_xp(5)

    def status(self):
        return (
            f"[bold blue]{self.nome}[/bold blue] - Nível {self.nivel}\n"
            f"XP: {self.xp}/{self.nivel * 100}\n"
            f"Energia: {self.energia}\n"
            f"Força: {self.forca}\n"
            f"Agilidade: {self.agilidade}\n"
            f"Inteligência: {self.inteligencia}\n"
            f"Afinidade: {self.afinidade}"
        )
