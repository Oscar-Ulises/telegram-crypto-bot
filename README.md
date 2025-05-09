# 📊 ¿Cómo funciona?

### 1. Selección de tokens
Se analiza una lista predefinida de más de 200 criptomonedas (USDT pairs).

Se calcula el rendimiento de cada una en un marco de tiempo de 24 horas con velas de 15 minutos.

Se seleccionan las 5 con mejor rendimiento.

### 2. Análisis técnico
Cada minuto se analiza la criptomoneda con mayor rendimiento usando:

- Bandas de Bollinger (150 períodos)
- Indicador Estocástico (K y D)

Cuando se cumplen las siguientes condiciones:

- El precio actual está por debajo de la banda inferior
- K y D están por debajo de 18
- K < D

Entonces se genera una señal de compra.

### 3. Alerta por Telegram
Si se detecta una señal, se envía un mensaje por Telegram con:

- Precio de compra
- Precio estimado de salida con beneficios del 5%, 8%, 10% y 15% (menos 1% como buffer)

---

# 🧠 Estructura del Script

- `telegram_bot_sendtext(msg)`: Envía un mensaje al bot de Telegram.
- `applytechnicals(df)`: Calcula indicadores técnicos.
- `getdaydata(symbol)`: Datos históricos de 24h (15m).
- `getminutedata(symbol)`: Datos históricos recientes (1m).
- `rend(df)`: Calcula rendimiento simple.
- `getnames(cryptos)`: Ordena y retorna las top 5 por rendimiento.
- Loop principal: Evalúa condiciones cada 0.5 segundos durante 15 minutos (1800 * 0.5s = 15 mins).

---

# 📝 Ejemplo de mensaje
Buy API3USDT. Market price: 1.2345

 ->%1 price: 1.21
Tentative 5%(-1%) sell price: 1.27
Tentative 8%(-1%) sell price: 1.30
Tentative 10%(-1%) sell price: 1.32
Tentative 15%(-1%) sell price: 1.39
