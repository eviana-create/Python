codigo_compra = int(input(f"Insira Codigo do Produto "))

if codigo_compra == 5222:
    print(f"Compra á Vista")
elif codigo_compra == 5333:
    print(f"Compra á Prazo no Boleto")
elif codigo_compra == 5444:
    print(f"Compra á Prazo no Cartão")
else:
    print(f"Codigo não Cadastrado, Entre em contato com o suporte.")
