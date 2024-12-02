import pandas as pd 
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

caminho_csv_books_2000 = 'caminho_csv_books_2000_treinado.csv'
caminho_csv_books_classificado = 'caminho_csv_books_2000_classificado.csv'

def classificar_texto(books_csv):
    print("Iniciando função..")
    df_text = books_csv['text'].tolist()
    lista_classifica = []
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    
    for text in df_text:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            logits = model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        model.config.id2label[predicted_class_id]
        if predicted_class_id == 1:
           lista_classifica.append('Positivo')
        else:
           lista_classifica.append('Negativo')
    print(lista_classifica)

    #inserindo a lista no dataFrame
    books_csv['Sentimento'] = lista_classifica
    print(books_csv)
    print("Função finalizada..")
    books_csv.to_csv(caminho_csv_books_classificado,  sep=';',index=False)

if __name__ == "__main__":
    books_csv = pd.read_csv("caminho_csv_books_2000.csv", sep=';')
    classificar_texto(books_csv)
    


