texto = '''A inserção de comentários no código do programa é uma pratica normal. Em função disso, toda linguagem de 
programação tem alguma maneira de permitir que comentários sejám inseridos nos programas. o objetivo é adicionar 
descrições em partes do código, sejá para documenta-lo ou para adcionar uma descrição do algoritmo implementado(
BANNING, p. 45, 2018 ) '''

for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Vogal '{c}', Encontrada na Posição {i}")
    else:
        continue