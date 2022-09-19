c = 200 # Valor da cosntante
mes = int(input("Digite o mês para calculo: ")) # função para capturar o mês que o cliente deseje saber o resultado.

mes = int(mes) # convertendo para númerico o mês capturado pelo input() digitado pelo cliente.
r = c * mes # Equação do primeiro grau, também chamada como função de primeiro de grau ou função linear.

print(f"\nA Quantidade de Peças á serem vendidas no mês {mes} é de: {r}") # impressão do resultado usando string interpolada, "f-string" (PEP 498).