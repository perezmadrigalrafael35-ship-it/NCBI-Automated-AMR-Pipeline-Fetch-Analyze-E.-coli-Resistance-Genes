import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos que descargamos del NCBI
print("Cargando los datos de resistencia...")
df = pd.read_csv("datos_amr_ecoli.csv")

# 2. Limpieza de datos (Lo que hace un verdadero Data Analyst)
# Filtramos las filas donde la longitud del ADN sea mayor a 0 (para quitar los vacíos)
df_valido = df[df['Longitud_ADN'] > 0].copy()
# Filtramos los datos para quitar los genomas completos (mayores a 2000 pb)
# y solo dejar los genes aislados que son comparables
df_grafica = df_valido[df_valido['Longitud_ADN'] < 2000].copy()

# Ahora graficamos usando df_grafica en lugar de df_valido
plt.figure(figsize=(10, 6))
plt.bar(df_grafica['ID_NCBI'].astype(str), df_grafica['Longitud_ADN'], color='green', edgecolor='black')

plt.title('Longitud de secuencias del gen blaCTX-M en E. coli (Genes aislados)', fontsize=14, fontweight='bold')
plt.xlabel('ID de la secuencia en NCBI', fontsize=12)
plt.ylabel('Longitud (pares de bases)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("grafica_resistencia_ecoli.png", dpi=300)
plt.show()
print(f"De {len(df)} secuencias, se encontraron {len(df_valido)} con datos de ADN válidos.")

# 3. Análisis Exploratorio (EDA)
print("\n--- ESTADÍSTICAS DE LAS SECUENCIAS DE RESISTENCIA ---")
# Ver la longitud máxima, mínima y promedio
print(f"Longitud mínima: {df_valido['Longitud_ADN'].min()} pares de bases")
print(f"Longitud máxima: {df_valido['Longitud_ADN'].max()} pares de bases")
print(f"Longitud promedio: {df_valido['Longitud_ADN'].mean():.2f} pares de bases")

# 4. Generar una gráfica profesional
plt.figure(figsize=(10, 6))
# Hacemos un gráfico de barras con las longitudes de cada ID
plt.bar(df_valido['ID_NCBI'].astype(str), df_valido['Longitud_ADN'], color='skyblue', edgecolor='black')

# Personalizar la gráfica
plt.title('Longitud de secuencias del gen blaCTX-M en E. coli', fontsize=14, fontweight='bold')
plt.xlabel('ID de la secuencia en NCBI', fontsize=12)
plt.ylabel('Longitud (pares de bases)', fontsize=12)
plt.xticks(rotation=45) # Rotamos los IDs para que se lean bien
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 5. Guardar la gráfica como imagen
plt.tight_layout()
plt.savefig("grafica_resistencia_ecoli.png", dpi=300)
print("\n¡Gráfica guardada como 'grafica_resistencia_ecoli.png'!")

# Mostrarla en pantalla
plt.show()