import pandas as pd 

caminho_csv_books_2000 = 'caminho_csv_books_2000.csv'
caminho_csv_meta_2000 = 'caminho_csv_meta_2000.csv'

def abrir_arquivo_books(books_csv):
    books_csv = books_csv.head(2000)
    print(books_csv)
    books_csv.to_csv(caminho_csv_books_2000,  sep=';',index=False)

def abrir_arquivo_meta(meta_csv):
    meta_csv = meta_csv.head(2000)
    print(meta_csv)
    meta_csv.to_csv(caminho_csv_meta_2000 ,  sep=';',index=False)

if __name__ == "__main__":
    print("Salvando o arquivo")
    books_csv = pd.read_csv("Books2.csv", sep=';')
    abrir_arquivo_books(books_csv)
    meta_csv = pd.read_csv("Meta2.csv", sep=';')
    abrir_arquivo_meta(meta_csv)
    print("Arquivo salvo")
   
    