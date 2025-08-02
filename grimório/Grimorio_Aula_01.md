# 🧙‍♂️ Grimório de Sessão - Aula 01

## Projeto: Virtual Pet - En-Sabbah-Tur

---

## 📅 Data da Sessão
28 de Julho de 2025

## 🕹️ Objetivos
- Preparar ambiente com Poetry corretamente
- Criar estrutura do projeto com `typer`
- Implementar comandos CLI iniciais: criar, status, alimentar, brincar, estudar, dormir
- Persistir estado do pet com `pet_data.json`
- Compreender `global`, escopo, e ciclo de vida do pet

## ⚖️ Comandos Utilizados
```bash
# Ambiente
poetry new virtual_pet
poetry shell
poetry install

# Executar CLI
poetry run python -m virtual_pet.cli criar
poetry run python -m virtual_pet.cli alimentar
poetry run python -m virtual_pet.cli status
poetry run python -m virtual_pet.cli estudar
```

## 📈 Ações esperadas dos comandos
| Comando     | Efeito                                           |
|-------------|--------------------------------------------------|
| criar       | Cria um novo pet com nome personalizado         |
| status      | Exibe XP, atributos e energia do pet             |
| alimentar   | +energia, +XP                                    |
| brincar     | +agilidade, -energia, +XP                        |
| estudar     | +inteligência, -energia, +XP                    |
| dormir      | energia = 100, +XP                               |
| salvar      | Salva manualmente o pet                          |
| carregar    | Recarrega o pet salvo em disco                   |

## 📃 Persistência
- Pet é salvo em `pet_data.json` automaticamente após cada interação
- Corrigido bug onde nome fixo "En-Sabbah-Tur" impedia evolução real

## ✨ Melhoria aplicada
- Removido `pet = Pet(nome="En_Sabbah-Tur")` hardcoded
- Função `carregar_pet` agora usa dados do JSON

## ⚔️ Missões futuras
- Criar sistema de afinidade elemental com base nas ações
- Adicionar evolução física ao atingir certos níveis
- Suportar múltiplos pets (perfil por nome)
- Interface visual no terminal com barras (usando `rich`)

## 👾 Conquista Desbloqueada
✨ "Domador de CLI Nível 1" - criaste e interagiste com teu primeiro pet persistente

---

Feito por [RenePessoto](https://github.com/RenePessoto)