class Pet:
    def __init__(self, nome: str):
        self.nome = nome
        self.nivel = 1
        self.xp = 0
        self.energia = 100
        self.forca = 5
        self.agilidade = 5
        self.inteligencia = 5

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= self.nivel * 100:
            self.nivel += 1
            self.xp = 0
            print(f"[bold yellow]{self.nome} subiu para o nível {self.nivel}![/bold yellow]")

    def alimentar(self):
        self.energia = min(self.energia + 20, 100)
        self.ganhar_xp(10)

    def brincar(self):
        if self.energia >= 10:
            self.agilidade += 1
            self.energia -= 10
            self.ganhar_xp(15)
        else:
            print("[red]TRÊMULO!! O pet está cansado demais para brincar.[/red]")

    def estudar(self):
        if self.energia >= 15:
            self.inteligencia += 1
            self.energia -= 15
            self.ganhar_xp(20)
        else:
            print("[red]CONFUSO!! O pet está muito cansado para aprender algo novo.[/red]")

    def treinar(self):
        if self.energia >= 20:
            self.forca += 1
            self.energia -= 20
            self.ganhar_xp(25)
        else:
            print("[red]CANSADO!! O pet está muito cansado para treinar.[/red]")
    
    def dormir(self):
        self.energia = 100
        self.ganhar_xp(5)

    def status(self):
        return (
            f"[bold blue]{self.nome}[/bold blue] - Nível {self.nivel}\n"
            f"XP: {self.xp}/100\n"
            f"Energia: {self.energia}\n"
            f"Força: {self.forca}\n"
            f"Agilidade: {self.agilidade}\n"
            f"Inteligência: {self.inteligencia}"
        )
