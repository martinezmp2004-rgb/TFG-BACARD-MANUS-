
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# 1. Evolution of Rum Volume in Spain (2022-2024)
years = ['2022', '2023', '2024 (Est.)']
volumes = [33.1, 30.48, 28.8] # Million Liters

plt.figure(figsize=(10, 6))
plt.plot(years, volumes, marker='o', linestyle='-', color='teal', linewidth=2, markersize=8)
plt.title('Evolución del Volumen de Ron en España (2022-2024)', fontsize=14, fontweight='bold')
plt.ylabel('Millones de Litros', fontsize=12)
plt.xlabel('Año', fontsize=12)
plt.ylim(25, 35)
for i, txt in enumerate(volumes):
    plt.annotate(f"{txt}M", (years[i], volumes[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.savefig('/home/ubuntu/rum_volume_evolution.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Market Segmentation by Preference (Premium vs Standard)
labels = ['Rones Añejos/Premium', 'Rones Estándar']
sizes = [64, 36]
colors = ['#d4af37', '#c0c0c0'] # Gold and Silver/Grey

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0.1, 0), shadow=True)
plt.title('Preferencia de Consumo: Premium vs Estándar', fontsize=14, fontweight='bold')
plt.savefig('/home/ubuntu/rum_preference_segmentation.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Market Share of Digital Attention (2024) - Top Competitors
competitors = ['Ron Barceló', 'Bacardí (Est.)', 'Havana Club (Est.)', 'Otros']
shares = [2.72, 2.5, 1.8, 92.98] # DAI shares

plt.figure(figsize=(10, 6))
sns.barplot(x=competitors[:3], y=shares[:3], palette='viridis')
plt.title('Cuota de Atención Digital (DAI) - 2024', fontsize=14, fontweight='bold')
plt.ylabel('% DAI', fontsize=12)
plt.savefig('/home/ubuntu/digital_attention_share.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualizations generated successfully.")
