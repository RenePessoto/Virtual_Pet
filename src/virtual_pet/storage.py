import json
import os
from virtual_pet.core import Pet

def salvar_pet(pet: Pet, caminho: str = "pet_data.json"):
    dados = {
        "nome": pet.nome,
        "nivel": pet.nivel,
        "xp": pet.xp,
        "energia": pet.energia,
        "forca": pet.forca,
        "agilidade": pet.agilidade,
        "inteligencia": pet.inteligencia,
        "afinidade": pet.afinidade,
    }
    with open(caminho, "w") as f:
        json.dump(dados, f)

def carregar_pet(caminho: str = "pet_data.json") -> Pet:
    if os.path.exists(caminho):
        with open(caminho, "r") as f:
            dados = json.load(f)
        pet = Pet(nome=dados["nome"])
        pet.nivel = dados["nivel"]
        pet.xp = dados["xp"]
        pet.energia = dados["energia"]
        pet.forca = dados["forca"]
        pet.agilidade = dados["agilidade"]
        pet.inteligencia = dados["inteligencia"]
        pet.afinidade = dados.get("afinidade","neutro")  # Padrão "neutro" se não houver afinidade
        return pet
    return Pet("SemNome")  # Retorna um pet vazio se o arquivo não existir
