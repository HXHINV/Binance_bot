# HxH PAXG — Bot EMA (Binance Spot)

Bot de trading desarrollado en Python para operar el par PAXG/USDT en el mercado Spot de Binance.  
Utiliza una estrategia basada en el cruce de Medias Móviles Exponenciales (EMA) y está diseñado para ejecución continua en entornos de servidor (VPS), con una estructura sobria, modular y orientada a producción.

---

## Estrategia de Trading

La estrategia implementada es EMA Crossover aplicada a PAXG (oro tokenizado):

- BUY: cuando la EMA de corto plazo cruza por encima de la EMA de largo plazo.
- SELL: cuando la EMA de corto plazo cruza por debajo de la EMA de largo plazo.
- HOLD: cuando no existe un cruce válido.

El bot evita operaciones duplicadas y solo ejecuta órdenes cuando existe un cambio real de señal.

---

## Mercado y Activo

- Exchange: Binance  
- Mercado: Spot  
- Par: PAXGUSDT  
- Tipo de órdenes: Market  

Documentación oficial utilizada:  
https://developers.binance.com/docs/binance-spot-api-docs

---

## Estructura del Proyecto

hxh-paxg-bot/
- main.py            → Bucle principal del bot  
- config.py          → Configuración general y claves API  
- strategy.py        → Estrategia EMA  
- binance_client.py  → Cliente Binance Spot  
- requirements.txt   → Dependencias  
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

Contenido de requirements.txt:

python-binance  
pandas  

---

## Configuración

Editar el archivo config.py con tus credenciales y parámetros:

API_KEY = "TU_API_KEY"  
API_SECRET = "TU_API_SECRET"  

SYMBOL = "PAXGUSDT"  
INTERVAL = "1h"  

SHORT_EMA = 12  
LONG_EMA = 26  

TRADE_QUANTITY = 0.01  

Nunca publiques tus claves API en repositorios públicos.  
En producción se recomienda usar variables de entorno.

---

## Ejecución

Ejecutar el bot desde consola:

python main.py  

Flujo de ejecución:
1. Obtiene velas OHLC desde Binance.
2. Calcula las EMAs.
3. Evalúa la señal.
4. Ejecuta orden de compra o venta si corresponde.
5. Espera el siguiente intervalo.

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

- PAXG es un activo de baja volatilidad comparado con otros pares.
- La estrategia EMA funciona mejor en tendencias definidas.
- El bot no incluye stop-loss ni take-profit por defecto.
- El tamaño de posición es fijo y no utiliza gestión de riesgo avanzada.

---

## Advertencia

Este software se proporciona con fines técnicos y educativos.  
El trading con criptomonedas implica riesgos financieros.  
El autor no asume responsabilidad por pérdidas derivadas del uso de este bot.

---

Autor: HxH  
Bot de trading Spot para PAXG
