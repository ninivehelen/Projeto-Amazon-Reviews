import pandas as pd 
import json

arquivo_jsonl_books = "Books.jsonl"
arquivo_jsonl_meta = "meta_Books.jsonl"
caminho_csv_books = "Books.csv"
caminho_csv_meta = "Meta.csv"

def abrir_converte_books(arquivo_jsonl_books):
    with open(arquivo_jsonl_books, 'r') as f:
        print("Abrindo o arquivo")
        for linha in f:
            linha_json = json.loads(linha)
            df = pd.DataFrame.from_dict([linha_json])
            df.to_csv(caminho_csv_books, mode='a', sep=';',index=False)
        print("Csv de book criado")

def abrir_converte_meta(arquivo_jsonl_meta):
    with open(arquivo_jsonl_meta, 'r') as f:
        print("Abrindo o arquivo")
        for linha in f:
            linha_json = json.loads(linha)
            df = pd.DataFrame.from_dict([linha_json])
            df.to_csv(caminho_csv_meta, mode='a', sep=';',index=False)
        print("Csv de meta criado")

if __name__ == "__main__":
    abrir_converte(arquivo_jsonl_books)
    abrir_converte_meta(arquivo_jsonl_meta)
    
   

  