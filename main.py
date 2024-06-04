import json
import pandas as pd
from analise_sentimento import tratamento_de_texto

def abrir_arquivo(arquivo):
    with open(arquivo, encoding='utf-8-sig') as f:
         for line in fp:
           print(json.loads(line.strip()))
        
if __name__ == "__main__":
    arquivo = "Books.jsonl"
    abrir_arquivo(arquivo)
    # tratamento_de_texto()
    
