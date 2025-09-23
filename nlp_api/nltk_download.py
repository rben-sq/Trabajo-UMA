import nltk
import os

nltk_data_path = "/usr/share/nltk_data"
os.makedirs(nltk_data_path, exist_ok=True)

print(f"Descargando 'punkt' a: {nltk_data_path}")
nltk.download("punkt", download_dir=nltk_data_path)

print(f"Descargando 'averaged_perceptron_tagger' a: {nltk_data_path}")
nltk.download("averaged_perceptron_tagger", download_dir=nltk_data_path)

print(f"Descargando 'punkt_tab' a: {nltk_data_path}")
nltk.download("punkt_tab", download_dir=nltk_data_path)



print(f"Contenido de {nltk_data_path}/tokenizers:")
if os.path.exists(f"{nltk_data_path}/tokenizers"):
    for item in os.listdir(f"{nltk_data_path}/tokenizers"):
        print(f"- {item}")