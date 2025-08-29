 1. README.md ajustado a tu `importos.py`


# 🤖 Bot de frases esenciales en alemán 🇩🇪

¡Hallo! 👋  
Soy Josué, estudiante de Educación en Idiomas. He creado este bot de Telegram con el propósito de **aprender frases esenciales en alemán** organizadas en categorías temáticas.

---

## 📌 Características
- Frases divididas en categorías (saludos, viajes, restaurante, compras, emergencias, conversación).
- Puedes pedir frases aleatorias o elegir una categoría con botones.
- Útil para estudiantes principiantes de alemán. 🇩🇪

---

## ⚙️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Yato-12/telegram_bot.git
   cd telegram_bot
````

2. (Opcional) Crea un entorno virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # En Windows
   source venv/bin/activate   # En Linux/Mac
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto con tu token de Telegram:

   ```
   TELEGRAM_TOKEN=tu_token_aqui
   ```

---

## ▶️ Ejecución

Inicia el bot con:

```bash
python importos.py
```

Si el `.json` no existe, el bot lo generará automáticamente.

---

## 💬 Ejemplo de uso en Telegram

* Escribe `/start` → muestra el menú con botones de categorías.
* Escribe `/frase` → muestra una frase aleatoria de cualquier categoría.
* Pulsa un botón (ejemplo: *Saludos*) → muestra una frase dentro de esa categoría.

---

## 📚 Propósito educativo

Este bot no busca reemplazar un curso completo de alemán, sino servir como **herramienta práctica** para memorizar y practicar frases útiles en el día a día.

---

👨‍💻 Autor

Creado por Josué, estudiante de Educación en Idiomas (Universidad Nacional de Trujillo).

