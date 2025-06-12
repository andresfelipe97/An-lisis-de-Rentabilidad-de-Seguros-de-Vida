import pandas as pd
import numpy as np
import random
from faker import Faker

# Inicializar Faker
fake = Faker()
np.random.seed(42)

# Opciones del dataset
productos = ['Vida Básico', 'Vida Plus', 'Vida Premium', 'Protección Familiar']
canales = ['Agente', 'Broker', 'Digital', 'Call Center']
estados_poliza = ['Activa', 'Cancelada', 'Vencida']
regiones = ['Bogotá', 'Antioquia', 'Valle del Cauca', 'Santander', 'Cundinamarca', 'Atlántico']

# Generar datos
n = 5000
data = []

for i in range(n):
    fecha_contratacion = fake.date_between(start_date='-3y', end_date='today')
    producto = random.choice(productos)
    canal = random.choice(canales)
    edad = np.random.randint(18, 75)
    sexo = random.choice(['Masculino', 'Femenino'])
    ingreso = np.random.normal(loc=3500, scale=1200)
    ingreso = max(1000, round(ingreso, 2))
    
    prima = round(np.random.normal(loc=900, scale=300), 2)
    prima = max(200, prima)
    
    monto_asegurado = prima * random.randint(20, 200)
    estado = random.choices(estados_poliza, weights=[0.7, 0.2, 0.1])[0]
    region = random.choice(regiones)

    # Siniestros
    siniestro = random.choices(['Sí', 'No'], weights=[0.1, 0.9])[0]
    monto_siniestro = 0
    if siniestro == 'Sí':
        monto_siniestro = round(np.random.uniform(5000, monto_asegurado), 2)

    data.append([
        f'POL{i+1:05d}', fecha_contratacion, producto, canal, prima,
        monto_asegurado, edad, sexo, ingreso,
        siniestro, monto_siniestro, estado, region
    ])

# Crear DataFrame
columns = [
    'ID_Poliza', 'Fecha_Contratacion', 'Producto', 'Canal_Venta', 'Prima_Anual',
    'Monto_Asegurado', 'Cliente_Edad', 'Cliente_Sexo', 'Cliente_Ingreso_Mensual',
    'Siniestro_Reportado', 'Monto_Siniestro', 'Estado_Poliza', 'Región'
]

df = pd.DataFrame(data, columns=columns)

# Exportar a CSV
df.to_csv("seguros_vida.csv", index=False)

print("✅ Dataset generado y guardado como 'seguros_vida.csv'")
