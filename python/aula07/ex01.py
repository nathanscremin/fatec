palabras = input("Insira um texto, com ou sem 'Python': ")
text = palabras # salva o texto

palabras = palabras.upper() #transforma o texto no texto normal
palabras = palabras.count("PYTHON")

print(f"Seu texto tem: {palabras}x Python.")
print(text) # printa o texto original