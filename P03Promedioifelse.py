# Kimberly Medina Ríos
cal1 = float(input("Calificación 1: "))
cal2 = float(input("Calificación 2: "))
cal3 = float(input("Calificación 3: "))

promedio = (cal1 + cal2 + cal3) / 3

if promedio >= 6:
    print("Aprobado")
else:
    print("Reprobado")