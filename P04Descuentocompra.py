# Kimberly Medina Ríos

compra = float(input("Ingresa el total de tu compra: "))
es_cliente_vip = input("¿Eres cliente VIP? (s/n): ").lower() == "s"

if (compra > 1000 and not es_cliente_vip == False) or (compra > 500 and es_cliente_vip):
    print(" Tienes descuento")
else:
    print(" No tienes descuento")