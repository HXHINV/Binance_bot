# HxH PAXG — Bot de Trading Avanzado (Binance Spot)
Implementado por **DevYHB**

Bot de trading desarrollado en **Python** para operar el par **PAXG/USDT** en el mercado **Spot de Binance**, combinando análisis técnico clásico, análisis estructural de mercado y aprendizaje automático. El bot está diseñado para ejecución continua en entornos de servidor (VPS), con una arquitectura sobria, modular y orientada a producción.

El sistema integra **Medias Móviles Exponenciales (EMA)**, **Order Blocks**, **retrocesos de Fibonacci** y un modelo de **aprendizaje automático con TensorFlow** para la generación y validación de señales de trading.

Documentación oficial utilizada de Binance:  
https://developers.binance.com/docs/binance-spot-api-docs

---

## Descripción General

El bot obtiene datos OHLCV directamente desde la API oficial de Binance, analiza el comportamiento del precio de PAXG y ejecuta órdenes de mercado cuando se cumplen condiciones técnicas y predictivas alineadas. La lógica está pensada para reducir señales falsas, evitar sobreoperación y adaptarse al perfil de baja volatilidad de PAXG (oro tokenizado).

---

## Estrategia de Trading

La estrategia combina múltiples capas de decisión:

- **EMA (Exponential Moving Averages):**  
  Cruce de EMA corta y EMA larga para detectar cambios de tendencia primaria.

- **Order Blocks:**  
  Identificación de zonas de oferta y demanda institucional (bloques de orden) para validar entradas y salidas en áreas de alta probabilidad.

- **Fibonacci:**  
  Uso de retrocesos de Fibonacci (38.2%, 50%, 61.8%) para definir zonas técnicas de pullback, entradas óptimas y niveles de protección.

- **TensorFlow (Machine Learning):**  
  Modelo predictivo entrenado con datos históricos de PAXG que evalúa la probabilidad de continuación o reversión del movimiento. El modelo actúa como filtro y confirmación adicional de las señales técnicas.

Las órdenes solo se ejecutan cuando existe confluencia entre análisis técnico y la predicción del modelo.

---

## Mercado y Activo

- Exchange: Binance  
- Mercado: Spot  
- Par: PAXGUSDT  
- Tipo de órdenes: Market  

---

## Estructura del Proyecto

hxh-paxg-bot/  
- main.py            → Bucle principal de ejecución  
- config.py          → Configuración general y credenciales  
- strategy.py        → Lógica de EMAs, Order Blocks y Fibonacci  
- ml_model.py        → Modelo TensorFlow y predicciones  
- binance_client.py  → Cliente de Binance Spot API  
- requirements.txt   → Dependencias del proyecto  
- README.md          → Documentación  

---

## Requisitos

- Python 3.9 o superior  
- Cuenta de Binance con Spot Trading habilitado  
- API Key y Secret Key de Binance  

---

## Instalación

Clonar el repositorio e instalar dependencias:

git clone https://github.com/tu-usuario/hxh-paxg-bot.git  
cd hxh-paxg-bot  
pip install -r requirements.txt  

Dependencias principales:

python-binance  
pandas  
numpy  
tensorflow  

---

## Configuración

Editar el archivo `config.py`:

API_KEY = "TU_API_KEY"  
API_SECRET = "TU_API_SECRET"  

SYMBOL = "PAXGUSDT"  
INTERVAL = "1h"  

SHORT_EMA = 12  
LONG_EMA = 26  

TRADE_QUANTITY = 0.01  

Para entornos productivos se recomienda usar variables de entorno y no incluir claves directamente en el código.

---

## Ejecución

Ejecutar el bot desde consola:

python main.py  

Flujo de ejecución:
1. Obtiene velas OHLCV desde Binance.
2. Calcula EMAs, Order Blocks y niveles de Fibonacci.
3. Genera predicción mediante el modelo TensorFlow.
4. Evalúa confluencia de señales.
5. Ejecuta orden de compra o venta si corresponde.
6. Espera el siguiente intervalo y repite el ciclo.

---

## Despliegue en VPS

Ejemplo de ejecución en segundo plano:

nohup python main.py > hxh_paxg.log 2>&1 &  

Alternativas recomendadas:
- tmux  
- screen  
- systemd  

---

## Consideraciones Técnicas

- PAXG presenta menor volatilidad que otros criptoactivos.
- Las estrategias EMA funcionan mejor en mercados con tendencia definida.
- El uso de Order Blocks y Fibonacci mejora la precisión de entradas.
- El modelo de Machine Learning debe reentrenarse periódicamente.
- No se incluye stop-loss ni take-profit por defecto (se recomienda implementarlos).

---

## Advertencia

Este software se proporciona con fines **técnicos y educativos**.  
El trading con criptomonedas implica riesgos financieros.  
El autor e implementador no asume responsabilidad por pérdidas derivadas del uso de este bot.

---

Implementado por **DevYHB**  
HxH PAXG — Bot de Trading Avanzado para Binance Spot
