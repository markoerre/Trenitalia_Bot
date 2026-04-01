# 🚆 Train Tracker Telegram Bot

Un bot Telegram leggero per monitorare in tempo reale i ritardi dei treni tramite le API (non ufficiali) di Trenitalia. 

Nato da un'esigenza pratica: avere lo stato del proprio treno al volo, senza pubblicità e senza aprire app pesanti.

## 💡 Funzionalità

- **Monitoraggio continuo:** Controlla lo stato di uno o più treni in background.
- **Dati in tempo reale:** Recupera le informazioni di viaggio direttamente dai server Trenitalia.
- **Notifiche dirette:** Invia aggiornamenti automatici su Telegram con tratta, stato e minuti di ritardo.
- **Zero overhead:** Script essenziale in Python, veloce e senza dipendenze inutili.

## ⚙️ Requisiti

- Python 3.x
- Un bot Telegram (creato tramite [@BotFather](https://t.me/BotFather)) e il relativo `TOKEN`.
- Il tuo `CHAT_ID` di Telegram.

## 🚀 Installazione e Avvio

1. **Clona la repository**
   ```bash
   git clone [https://github.com/tuo-username/train-tracker-bot.git](https://github.com/tuo-username/train-tracker-bot.git)
   cd train-tracker-bot
   ```

2. **Installa le dipendenze**
   ```bash
   pip install requests
   ```

3. **Configurazione**
   Apri il file principale dello script e compila la sezione di configurazione con i tuoi dati:
   ```python
   TOKEN = "IL_TUO_TOKEN"
   CHAT_ID = "IL_TUO_CHAT_ID"
   TRENI = ["1234", "5678"] # Inserisci i numeri dei treni che ti interessano
   ```

4. **Esecuzione**
   Avvia il processo. Se lo fai girare su un server linux, valuta l'uso di `screen` o `systemd` per mantenerlo attivo in background.
   ```bash
   python main.py
   ```

## 🧩 Roadmap & Sviluppi Futuri

- Invio notifiche *solo* se il ritardo o lo stato cambiano (riduzione dello spam).
- Gestione sicura delle credenziali tramite variabili d'ambiente (`.env`).
- Supporto multi-utente tramite comandi Telegram (es. `/track 1234`).
- Implementazione della cache per ottimizzare le richieste HTTP.

## ⚠️ Disclaimer

Questo progetto utilizza endpoint non ufficiali di Trenitalia. È pensato per automazione personale e a scopo di studio. Le API potrebbero cambiare struttura in qualsiasi momento senza preavviso, interrompendo il funzionamento del bot.
