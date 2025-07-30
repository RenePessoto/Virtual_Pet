import typer
from rich import print
from virtual_pet.core import Pet
from virtual_pet.storage import salvar_pet, carregar_pet


app= typer.Typer()
pet = Pet(nome = "En_Sabbah-Tur")


@app.command()
def  criar():
    """Cria um novo pet e o salva."""
    global pet
    nome = typer.prompt("Qual será o nome do seu pet?")
    pet = Pet(nome=nome)
    salvar_pet(pet)
    print(f"[bold green]{nome} nasceu em seu mundo mágico![/bold green]")


@app.command()
def status():
    """Exibe o status atual do pet."""
    global pet
    if pet is None:
        pet = carregar_pet("En_Sabbah-Tur")
    print(pet.status())

@app.command()
def alimentar():
    """Alimenta o pet e aumenta a energia."""
    global pet
    if pet is None:
        pet = carregar_pet("En_Sabbah-Tur")
    pet.alimentar()
    salvar_pet(pet)
    print("[green]Você alimentou o pet.[/green]")

@app.command()
def brincar():
    """Brinca com o pet, aumentando agilidade e gastando energia."""
    global pet
    if pet is None:
        pet = carregar_pet("En_Sabbah-Tur")
    pet.brincar()
    salvar_pet(pet)
    print("[cyan]Você brincou com o pet![/cyan]")

@app.command()
def estudar():
    """Ensina algo novo ao pet, aumentando inteligência."""
    global pet
    if pet is None:
        pet = carregar_pet("En_Sabbah-Tur")
    pet.estudar()
    salvar_pet(pet)
    print("[magenta]Você ensinou algo novo ao pet.[/magenta]")

@app.command()
def dormir():
    """Coloca o pet para descansar e recuperar energia."""
    global pet
    if pet is None:
        pet = carregar_pet("En_Sabbah-Tur")
    pet.dormir()
    salvar_pet(pet)
    print("[blue]O pet está descansando...[/blue]")

@app.command()
def salvar():
    """Salva o estado atual do pet manualmente."""
    global pet
    if pet is None:
        pet = carregar_pet("En_Sabbah-Tur")
    salvar_pet(pet)
    print("[bold green]Pet salvo com sucesso![/bold green]")

@app.command()
def carregar():
    """Recarrega os dados salvos do pet."""
    global pet
    pet = carregar_pet("En_Sabbah-Tur")
    print("[bold yellow]Pet recarregado do arquivo![/bold yellow]")

if __name__ == "__main__":
    app()