comida = [["estrogonofe", "lasanha"],[11, 8]]
bebida = [["refrigerante","suco"],[3, 2.5]]
comidaesc = input()
bebidaesc = input()
for pedido1 in range(2):
    if comidaesc.lower() == comida[0][pedido1]:
        for pedido2 in range(2):
            if bebidaesc.lower() == bebida[0][pedido2]:
                total = comida[1][pedido1] + bebida[1][pedido2]
    
print("%.2f" %total)