from src.virtual_pet.core import Pet

def test_ganhar_xp_evolui():
    pet = Pet("Testinho")
    pet.ganhar_xp(100)
    assert pet.nivel == 2
    
def afinidade_alimentar_manha(monkeypatch):
    from datetime import datetime
    pet = Pet("Testinho")

    class FakeDatetime(datetime):
        @classmethod
        def now(cls):
            return cls(2025, 8, 1, 8) # 8h da manhã
        
    monkeypatch.setattr("virtual_pet.core.datetime", FakeDatetime)
    pet.atualizar_afinidade("alimentar")
    assert pet.afinidade == "terra"
       

def test_alimentar():
    pet = Pet("Testinho")
    energia_anterior = pet.energia
    pet.alimentar()
    assert pet.energia >= energia_anterior
    assert pet.xp == 5

def test_brincar():
    pet = Pet("Testinho")
    pet.energia = 20
    agilidade_anterior = pet.agilidade
    pet.brincar()
    assert pet.agilidade == agilidade_anterior + 1
    assert pet.energia == 10
    assert pet.xp == 5

def test_estudar():
    pet = Pet("Testinho")
    pet.energia = 20
    inteligencia_anterior = pet.inteligencia
    pet.estudar()
    assert pet.inteligencia == inteligencia_anterior + 1
    assert pet.energia == 5
    assert pet.xp == 5

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
