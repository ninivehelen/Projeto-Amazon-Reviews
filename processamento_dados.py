import pandas as pd

colunas_books = ["title","text", "parent_asin", "helpful_vote"]

colunas_meta = ["title", "description", "price", "store", "categories", "details", "parent_asin"]

caminho_csv_books = "C:/Users/niniv/OneDrive/Documentos/projeto_amazon/Books2.csv"
caminho_csv_meta = "C:/Users/niniv/OneDrive/Documentos/projeto_amazon/Meta2.csv"

def escolhendo_colunas_books():
    books_csv = pd.read_csv("Books.csv", sep=';',)
    df_books_csv = books_csv[colunas_books]
    df_books_csv.to_csv(caminho_csv_books, sep=';', index=False)

def escolhendo_colunas_meta():
    meta_csv = pd.read_csv("Meta.csv",  sep=';',)
    df_meta_csv = meta_csv[colunas_meta]
    df_meta_csv.to_csv(caminho_csv_meta, sep=';', index=False)

if __name__ == "__main__":
  escolhendo_colunas_books()
  escolhendo_colunas_meta()

