import json
import pathlib

ARQUIVO_DADOS = "despesas.json"

# Funcao le_dados, verifica se ARQUIVO_DADOS ja existe


def le_dados():
    
    if not pathlib.Path(ARQUIVO_DADOS).exists():
        novo_dados = {"proximo_id": 1, "despesas":[]}
        return novo_dados
    
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arq:
        dados = json.load(arq)
        return dados

# Bloco Principal


if __name__ == "__main__":
    print(le_dados())