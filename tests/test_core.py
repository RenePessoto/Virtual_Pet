from src.virtual_pet.core import Pet

def test_alimentar():
    pet = Pet("Testinho")
    energia_anterior = pet.energia
    pet.alimentar()
    assert pet.energia >= energia_anterior
    assert pet.xp == 10

def test_brincar():
    pet = Pet("Testinho")
    pet.energia = 20
    agilidade_anterior = pet.agilidade
    pet.brincar()
    assert pet.agilidade == agilidade_anterior + 1
    assert pet.energia == 10
    assert pet.xp == 15

def test_estudar():
    pet = Pet("Testinho")
    pet.energia = 20
    inteligencia_anterior = pet.inteligencia
    pet.estudar()
    assert pet.inteligencia == inteligencia_anterior + 1
    assert pet.energia == 5
    assert pet.xp == 20

def test_dormir():
    pet = Pet("Testinho")
    pet.energia = 40
    pet.dormir()
    assert pet.energia == 100
    assert pet.xp == 5

def test_evolucao_de_nivel():
    pet = Pet("Testinho")
    pet.ganhar_xp(100)
    assert pet.nivel == 2
    assert pet.xp == 0
