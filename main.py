
paciente = {
  "nombre": "Paulo Londres",
  "edad": 24,
  "genero": "Fluido",
  "altura": 1.80,
  "enfermedades": ["Influenza", "COVID", "Diabetes", "Hipertencion", "Cancer"],
  "vive": False
}

# 1. Imprimir el nombre del paciente
print("Nombre:", paciente["nombre"])

# 2. Imprimir el genero y la altura
print("Genero:", paciente["genero"])
print("Altura:", paciente["altura"], "m")

# 3. Imprimir enfermedades
print("Enfermedades:", paciente["enfermedades"])

# 4. Imprimir si el paciente esta vivo "Vive"
if paciente["vive"]:
  print("Esta vivo")
else:
  print("Esta muerto")

# 5. Si tiene Cancer mandar a cuidados intensivos
if "Cancer" in paciente["enfermedades"]:
  print("Mandar el paciente a la tumba")
else:
  print("Madarlo a mimir con paracetamol")

# 6. Nos pieden cambiar la edad de un paciente y luego imprimir la edad nueva
paciente["edad"] = 25
print(paciente)
