````md
# 🚆 Train Tracker Telegram Bot

Un piccolo progetto nato da una cosa semplice:  
sono spesso in treno, e volevo qualcosa che mi dicesse al volo se era in ritardo oppure no, senza aprire mille app.

Così ho fatto questo bot.

---

## 💡 Cosa fa

- Monitora uno o più treni
- Recupera dati da Trenitalia (API pubbliche)
- Invia aggiornamenti su Telegram
- Mostra ritardo e stato del treno

---

## 🧠 Perché esiste

Sono pendolare.

Ogni giorno:
- controlli orari
- ritardi
- cambi improvvisi

Dopo un po’ ti stufi.

Volevo qualcosa di:
- veloce
- diretto
- senza pubblicità
- senza aprire app pesanti

Quindi ho scritto questo.

---

## ⚙️ Come funziona

- Python
- API non ufficiali Trenitalia
- Telegram Bot API

Loop semplice:
1. prende i dati
2. li elabora
3. li manda su Telegram

---

## 🚀 Setup veloce

1. Clona repo

```bash
git clone https://github.com/tuo-username/train-tracker-bot
cd train-tracker-bot
````

2. Installa dipendenze

```bash
pip install requests
```

3. Configura

Apri il file `.py` e inserisci:

```python
TOKEN = "IL_TUO_TOKEN"
CHAT_ID = "IL_TUO_CHAT_ID"
TRENI = ["1234", "5678"]
```

4. Avvia

```bash
python main.py
```

---

## 🔎 SEO / Keywords

train tracker python
trenitalia api python
telegram bot treni
monitor treni ritardo
train delay bot
python train tracker

---

## ⚠️ Nota

Questo progetto:

* NON usa API ufficiali documentate
* è fatto per uso personale / studio
* potrebbe smettere di funzionare se Trenitalia cambia qualcosa

---

## 🧩 Idee future

* notifiche solo se cambia stato
* interfaccia web
* supporto multi utente
* grafica migliore

---

## 👤 Autore

Progetto nato da necessità reale, non da teoria.

Se sei pendolare, capisci.

```
