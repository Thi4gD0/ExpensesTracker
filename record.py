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

# Funcao grava dados sobrescreve conteudo pelo dicionario recebido


def grava_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii= False)

# Bloco Principal


if __name__ == "__main__":
    info = le_dados()

    nova_despesa = { 
        "id": info["proximo_id"], 
        "descricao": "Conta de Luz", 
        "valor": 1000, 
        "data": "2026-08-10", 
        "categoria": "Servicos",
        }

    info["despesas"].append(nova_despesa)
    info["proximo_id"] += 1

    grava_dados(info)
    print(info)