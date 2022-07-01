m3, pre�o_litro = input().split()
m3 = float(m3)
pre�o_litro = float(pre�o_litro)
litros = m3 * 1000
valor_agua = pre�o_litro * litros
valor_esgoto = valor_agua * 0.80
valor_total = valor_agua + valor_esgoto
print("%.2f" %(valor_agua))
print("%.2f" %(valor_esgoto))
print("%.2f" %(valor_total))