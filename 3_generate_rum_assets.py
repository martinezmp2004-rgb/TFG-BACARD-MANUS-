import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de estilo
sns.set_theme(style="whitegrid")
os.makedirs('/home/ubuntu/assets', exist_ok=True)

# 1. Top 5 Marcas por Cuota (NielsenIQ 2024)
brands_data = {
    'Marca': ['Ron Barceló', 'Brugal', 'Cacique', 'Arehucas', 'Havana Club'],
    'Cuota Volumen (%)': [23.7, 18.0, 12.0, 8.0, 7.0],
    'Cuota Valor (%)': [29.9, 21.0, 10.0, 7.5, 8.5]
}
df_brands = pd.DataFrame(brands_data)
df_brands.to_csv('/home/ubuntu/assets/top_5_marcas_ron_2024.csv', index=False)

# Gráfico de Cuotas de Marca
plt.figure(figsize=(10, 6))
df_melted = df_brands.melt(id_vars='Marca', var_name='Tipo de Cuota', value_name='Porcentaje')
sns.barplot(data=df_melted, x='Porcentaje', y='Marca', hue='Tipo de Cuota', palette='viridis')
plt.title('Top 5 Marcas de Ron en España - Cuota de Mercado 2024 (NielsenIQ)')
plt.xlabel('Cuota de Mercado (%)')
plt.tight_layout()
plt.savefig('/home/ubuntu/assets/cuota_marcas_ron_2024.png')
plt.close()

# 2. Reparto On-trade vs Off-trade
channels_data = {
    'Año': [2022, 2024],
    'On-trade (%)': [50.0, 60.0],
    'Off-trade (%)': [50.0, 40.0]
}
df_channels = pd.DataFrame(channels_data)
df_channels.to_csv('/home/ubuntu/assets/reparto_canales_ron.csv', index=False)

# 3. Datos Demográficos (Mercasa 2024)
demo_data = {
    'Segmento': ['Hombres', 'Mujeres', '15-19 años', '20-24 años', '25-34 años', '35-49 años', '50-59 años', '60-75 años'],
    'Desviación (%)': [9.9, -9.8, -52.5, -37.3, -20.2, -30.7, 8.9, 70.5]
}
df_demo = pd.DataFrame(demo_data)
df_demo.to_csv('/home/ubuntu/assets/demografia_ron_espana_2024.csv', index=False)

# Gráfico Demográfico
plt.figure(figsize=(10, 6))
colors = ['green' if x > 0 else 'red' for x in df_demo['Desviación (%)']]
sns.barplot(data=df_demo, x='Desviación (%)', y='Segmento', palette=colors)
plt.title('Desviación del Consumo de Ron vs Media Nacional (Mercasa 2024)')
plt.axvline(0, color='black', linewidth=1)
plt.xlabel('Desviación (%)')
plt.tight_layout()
plt.savefig('/home/ubuntu/assets/demografia_ron_2024.png')
plt.close()

print("Activos generados exitosamente en /home/ubuntu/assets/")
