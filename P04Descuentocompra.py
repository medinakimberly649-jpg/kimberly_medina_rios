compra = float(input("Ingresa el total de la compra: "))

if compra >= 1000:
    descuento = compra * 0.20
elif compra >= 500:
    descuento = compra * 0.10
else:
    descuento = 0

total = compra - descuento

print("Descuento aplicado:", descuento)
print("Total a pagar:", total)