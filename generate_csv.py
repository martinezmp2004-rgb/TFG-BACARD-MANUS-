
import re

def parse_data_to_csv(data_string):
    # Suggested CSV header from the user's prompt
    csv_header = "source_title,source_organism,source_date,source_url,is_paid,summary,market_value_eur,market_volume_l,CAGR_pct,segment_mainstream_pct,segment_premium_pct,segment_superpremium_pct,RTD_share_pct,RTD_growth_pct,ontrade_pct,offtrade_pct,top_channels,trend_premiumization,trend_sustainability,trend_low_alcohol,demographics_notes,competitors_notes,example_SKUs,avg_price_mainstream,avg_price_premium,marketing_spend,regulatory_notes,bacardi_specifics,reliability_note,price_to_access\n"

    # Initialize data points
    data_rows = []

    # --- FEBE Data --- (Estimates for 2024, 2023, 2022)
    febe_2024_volume_total_spirits = "180 Millones de Litros"
    febe_2024_rum_share = "16.0%"
    febe_2024_rum_volume = "~28.8 Millones de Litros"

    febe_2023_volume_total_spirits = "187 Millones de Litros"
    febe_2023_rum_share = "16.3%"
    febe_2023_rum_volume = "~30.48 Millones de Litros"

    febe_2022_volume_total_spirits = "197 Millones de Litros"
    febe_2022_rum_share = "16.8%"
    febe_2022_rum_volume = "~33.1 Millones de Litros"

    # FEBE 2024 Entry
    data_rows.append({
        "source_title": "Informe Socioeconómico 2024 (Estimado)",
        "source_organism": "Espirituosos de España (FEBE)",
        "source_date": "2024",
        "source_url": "https://www.espirituosos.es/El-sector-en-cifras/comercializacion/",
        "is_paid": "No",
        "summary": f"En 2024, el consumo de bebidas espirituosas en España alcanzó los {febe_2024_volume_total_spirits}, lo que representa una caída del 3,7% en comparación con 2023. El ron representa el {febe_2024_rum_share} del volumen total, con un volumen estimado de {febe_2024_rum_volume}.",
        "market_value_eur": "",
        "market_volume_l": febe_2024_rum_volume.replace('~', '').replace(' Millones de Litros', '') + 'M',
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "Hostelería, reuniones sociales",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "Consumo ligado al ocio y entorno social, estilo de vida mediterráneo.",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Datos de asociación sectorial, fiabilidad alta para tendencias generales y volumen total de espirituosas. Estimación de volumen de ron basada en cuota.",
        "price_to_access": "Gratuito"
    })

    # FEBE 2023 Entry
    data_rows.append({
        "source_title": "Informe Socioeconómico 2023",
        "source_organism": "Espirituosos de España (FEBE)",
        "source_date": "2023",
        "source_url": "https://www.espirituosos.es/El-sector-en-cifras/comercializacion/",
        "is_paid": "No",
        "summary": f"En 2023, el consumo de bebidas espirituosas en España alcanzó los {febe_2023_volume_total_spirits}, lo que representa una caída del 5,9% en comparación con 2022. El ron representó el {febe_2023_rum_share} del volumen total, con un volumen estimado de {febe_2023_rum_volume}.",
        "market_value_eur": "",
        "market_volume_l": febe_2023_rum_volume.replace('~', '').replace(' Millones de Litros', '') + 'M',
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "Hostelería, reuniones sociales",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "Consumo ligado al ocio y entorno social, estilo de vida mediterráneo.",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Datos de asociación sectorial, fiabilidad alta para tendencias generales y volumen total de espirituosas. Estimación de volumen de ron basada en cuota.",
        "price_to_access": "Gratuito"
    })

    # GlobalData 2021 Entry
    data_rows.append({
        "source_title": "Spain Rum (Spirits) Market Assessment and Forecast to 2026",
        "source_organism": "GlobalData",
        "source_date": "2021",
        "source_url": "https://www.globaldata.com/store/report/spain-rum-market-analysis/",
        "is_paid": "Sí",
        "summary": "El mercado del ron en España registró un CAGR positivo del 0.08% durante 2016-2021, con un valor de ventas de 1.520,64 millones de euros en 2021.",
        "market_value_eur": "1520.64M",
        "market_volume_l": "",
        "CAGR_pct": "0.08% (2016-2021)",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Informe de investigación de mercado, fiabilidad media (datos de 2021).",
        "price_to_access": "De pago"
    })

    # Grand View Research (CAGR Proyectado)
    data_rows.append({
        "source_title": "Spain Rum Market Size & Outlook, 2022-2030",
        "source_organism": "Grand View Research",
        "source_date": "2023",
        "source_url": "https://www.grandviewresearch.com/horizon/outlook/rum-market/spain",
        "is_paid": "Sí",
        "summary": "El mercado del ron en España se espera que crezca a un CAGR del 6.7% de 2023 a 2030. El segmento on-trade fue el mayor generador de ingresos en 2022.",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "6.7% (2023-2030)",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "Mayor generador de ingresos en 2022",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Informe de investigación de mercado, fiabilidad media.",
        "price_to_access": "De pago"
    })

    # Mercasa/MAPA 2022 (Consumo en Hogares)
    data_rows.append({
        "source_title": "Alimentación en España 2023 (datos 2022)",
        "source_organism": "Mercasa / MAPA",
        "source_date": "2023",
        "source_url": "https://www.mercasa.es/wp-content/uploads/2023/11/ALIMENTACION-EN-ESPANA_2023.pdf",
        "is_paid": "No",
        "summary": "Consumo de ron en hogares en 2022: 38.3 millones de litros y 166.5 millones de euros, con un precio medio de 4.35 €/L.",
        "market_value_eur": "166.5M",
        "market_volume_l": "38.3M",
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "Consumo en hogares",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Informe oficial, fiabilidad alta. Nota: posible discrepancia con datos de FEBE para volumen total de ron, ya que este es solo consumo en hogares.",
        "price_to_access": "Gratuito"
    })

    # Bacardi Cocktail Trends Report 2025
    data_rows.append({
        "source_title": "Bacardi Cocktail Trends Report 2025",
        "source_organism": "Bacardi Limited",
        "source_date": "Nov 2024",
        "source_url": "https://d3bbd6es2y3ctk.cloudfront.net/wp-content/uploads/2024/11/12152833/Bacardi-Cocktail-Trends-Report-2025.pdf",
        "is_paid": "No",
        "summary": "Reporte que identifica las tendencias clave en la cultura de coctelería y la industria de espirituosos para 2025, incluyendo premiumización, experiencias y sostenibilidad. Menciona la estrategia 'The Sound of Rum' de Bacardí.",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "64% de consumidores prefieren rones añejos/premium",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "Sí",
        "trend_sustainability": "Sí",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "Bacardí Caribbean Spiced",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "Modelo Sónico 'The Sound of Rum', estrategia 'Do What Moves You', lanzamiento de Bacardí Caribbean Spiced, enfoque en sostenibilidad.",
        "reliability_note": "Informe de marca, fiabilidad alta para tendencias y estrategia de marca. Datos globales, no específicos de España.",
        "price_to_access": "Gratuito"
    })

    # Transform Magazine (The Sound of Rum)
    data_rows.append({
        "source_title": "The sound of rum: Bacardí's new sonic model",
        "source_organism": "Transform Magazine",
        "source_date": "Jan 14, 2026",
        "source_url": "https://www.transformmagazine.net/articles/2025/the-sound-of-rum-bacard%C3%ADs-new-sonic-model/",
        "is_paid": "No",
        "summary": "Artículo que detalla la estrategia de sonic branding de Bacardí, 'The Sound of Rum', y su colaboración con artistas para crear una identidad sonora evolutiva que resuene con la cultura joven.",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "Detalles de la iniciativa 'The Sound of Rum'.",
        "reliability_note": "Artículo de prensa especializada, fiabilidad alta para información de marca.",
        "price_to_access": "Gratuito"
    })

    # InfoAdex (Inversión Publicitaria)
    data_rows.append({
        "source_title": "Estudio InfoAdex de la Inversión Publicitaria en España 2024 (datos 2023)",
        "source_organism": "InfoAdex",
        "source_date": "2024",
        "source_url": "https://www.infoadex.es/es/reports/estudio-infoadex-de-la-inversin-publicitaria-en-espaa-2024",
        "is_paid": "Sí",
        "summary": "La inversión publicitaria del sector de bebidas alcohólicas en España alcanzó casi 75 millones de euros en 2023.",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "75M EUR (2023, sector bebidas alcohólicas)",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Informe de inversión publicitaria, fiabilidad alta. Cifra global del sector, no específica de ron o Bacardí.",
        "price_to_access": "De pago"
    })

    # Epsilontec (Cuota de Atención Digital)
    data_rows.append({
        "source_title": "Red Bull, Mahou, Ybarra, Ron Barceló y Coca-Cola, marcas con mayor cuota de atención digital en gran consumo en 2024",
        "source_organism": "Epsilontec",
        "source_date": "Mar 6, 2025 (datos 2024)",
        "source_url": "https://epsilontec.com/red-bull-mahou-ybarra-ron-barcelo-y-coca-cola-marcas-con-mayor-cuota-de-atencion-digital-en-gran-consumo-en-2024/",
        "is_paid": "No",
        "summary": "Ron Barceló lidera la categoría de espirituosos en atención digital con un 2.72% en 2024. Bacardí es un top spender con enfoque en medios digitales.",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "Ron Barceló (2.72% DAI), Bacardí (top spender digital)",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "Top spender digital, cerca de Ron Barceló en atención digital.",
        "reliability_note": "Artículo de prensa especializada con datos de agencia de marketing digital, fiabilidad media.",
        "price_to_access": "Gratuito"
    })

    # Regulatory Notes (General Knowledge / Synthesis)
    data_rows.append({
        "source_title": "Regulación de Bebidas Alcohólicas en España",
        "source_organism": "Síntesis de información regulatoria",
        "source_date": "2024",
        "source_url": "",
        "is_paid": "No",
        "summary": "Restricciones en publicidad para bebidas de alta graduación (>20º) en televisión, requisitos de etiquetado con advertencias sanitarias e información nutricional, e impuestos especiales sobre el alcohol.",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "",
        "example_SKUs": "",
        "avg_price_mainstream": "",
        "avg_price_premium": "",
        "marketing_spend": "",
        "regulatory_notes": "Publicidad (>20º), etiquetado (advertencias, nutrición), impuestos especiales.",
        "bacardi_specifics": "",
        "reliability_note": "Síntesis de normativa general, fiabilidad alta.",
        "price_to_access": "Gratuito"
    })

    # Competitors and Pricing (Synthesis)
    data_rows.append({
        "source_title": "Análisis de Competidores y Precios Medios",
        "source_organism": "Síntesis de información de mercado",
        "source_date": "2024",
        "source_url": "",
        "is_paid": "No",
        "summary": "Ron Barceló lidera el mercado español, seguido por Havana Club, Bacardí y Brugal. El segmento premium/super-premium muestra un crecimiento del 5-7% CAGR. Precios medios por segmento: Mainstream (12-16€), Premium (18-28€), Super-Premium (>35€).",
        "market_value_eur": "",
        "market_volume_l": "",
        "CAGR_pct": "5-7% (Premium/Super-Premium)",
        "segment_mainstream_pct": "",
        "segment_premium_pct": "",
        "segment_superpremium_pct": "",
        "RTD_share_pct": "",
        "RTD_growth_pct": "",
        "ontrade_pct": "",
        "offtrade_pct": "",
        "top_channels": "",
        "trend_premiumization": "Sí",
        "trend_sustainability": "",
        "trend_low_alcohol": "",
        "demographics_notes": "",
        "competitors_notes": "Ron Barceló (líder), Havana Club, Bacardí, Brugal, Zacapa, Diplomático, Don Papa.",
        "example_SKUs": "Mainstream: Bacardí Carta Blanca, Negrita. Premium: Barceló Añejo, Havana 7, Bacardí 8. Super-Premium: Zacapa 23, Diplomático Reserva Exclusiva.",
        "avg_price_mainstream": "12-16€",
        "avg_price_premium": "18-28€",
        "marketing_spend": "",
        "regulatory_notes": "",
        "bacardi_specifics": "",
        "reliability_note": "Síntesis de múltiples fuentes y estimaciones, fiabilidad media.",
        "price_to_access": "Gratuito"
    })

    csv_lines = [csv_header]
    for row_data in data_rows:
        csv_lines.append(','.join([f'"""' + str(row_data.get(field, '')).replace('"', '\"') + '"""' for field in csv_header.strip().split(',')]) + '\n')

    return ''.join(csv_lines)

# Read the data from the file
with open('/home/ubuntu/rum_market_spain_data.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

csv_output = parse_data_to_csv(raw_data)

with open('/home/ubuntu/rum_market_spain_analysis.csv', 'w', encoding='utf-8') as f:
    f.write(csv_output)

print("CSV file generated successfully: /home/ubuntu/rum_market_spain_analysis.csv")
