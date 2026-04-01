# -*- coding: utf-8 -*-

# Librerie base
import requests              # Per chiamate HTTP (API Trenitalia / Telegram)
import time                  # Per gestire pause
import threading             # Per eseguire più loop insieme
from datetime import datetime  # Per gestire orari

# ========================= CONFIG =========================

# ⚠️ INSERISCI QUI I TUOI DATI (esempio finto)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# Lista treni (usa numeri di esempio)
TRENI = ["1234", "5678"]

# Tempo refresh dati (secondi)
REFRESH_SEC = 60

# Endpoint base Trenitalia (pubblico)
BASE_URL = "http://www.viaggiatreno.it/infomobilita/resteasy/viaggiatreno"

# =========================================================

# Cache per evitare chiamate inutili
_cache = {}

# ========================= UTILS =========================

def now():
    """Ritorna ora attuale in formato leggibile"""
    return datetime.now().strftime("%H:%M:%S")


def send_telegram(method, payload):
    """Invia una richiesta all'API Telegram"""
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/{method}"
        r = requests.post(url, json=payload, timeout=10)
        return r.json()
    except Exception as e:
        print(f"[{now()}] ERRORE TELEGRAM:", e)
        return {}


def format_time(ms):
    """Converte timestamp ms in HH:MM"""
    if not ms:
        return "--:--"
    return datetime.fromtimestamp(ms / 1000).strftime("%H:%M")


# ========================= FETCH TRENO =========================

def get_train_data(numero_treno):
    """
    Recupera dati treno da API Trenitalia
    (versione semplificata e riutilizzabile)
    """

    try:
        # Step 1: trova codice treno
        url = f"{BASE_URL}/cercaNumeroTrenoTrenoAutocomplete/{numero_treno}"
        r = requests.get(url, timeout=10)

        if r.status_code != 200 or not r.text:
            return None

        line = r.text.strip().splitlines()[0]

        # Parsing semplice (non troppo spiegato apposta)
        parts = line.split("|")[1]
        codice = parts.split("-")[1]
        timestamp = parts.split("-")[2]

        # Step 2: andamento treno
        url2 = f"{BASE_URL}/andamentoTreno/{codice}/{numero_treno}/{timestamp}"
        r2 = requests.get(url2, timeout=10)

        if r2.status_code == 200:
            return r2.json()

    except:
        return None

    return None


# ========================= LOGICA =========================

def calcola_ritardo(fermate):
    """Calcola ritardo medio semplice"""
    for f in reversed(fermate):
        reale = f.get("arrivoReale") or f.get("partenzaReale")
        prog = f.get("arrivoProgrammato") or f.get("partenzaProgrammata")

        if reale and prog:
            return int((reale - prog) / 60000)

    return 0


def build_message(data):
    """Costruisce messaggio leggibile per Telegram"""

    if not data:
        return "Dati non disponibili"

    fermate = data.get("fermate", [])

    if not fermate:
        return "Nessuna informazione"

    origine = fermate[0].get("stazione", "N/D")
    destinazione = data.get("destinazione", "N/D")

    ritardo = calcola_ritardo(fermate)

    # Testo semplice (non troppo perfetto apposta)
    msg = f"🚆 Treno\n"
    msg += f"{origine} -> {destinazione}\n\n"

    if ritardo > 0:
        msg += f"⏱ Ritardo: {ritardo} min\n"
    else:
        msg += "✅ In orario\n"

    return msg


# ========================= LOOP =========================

def monitor_loop():
    """Loop principale che aggiorna i treni"""

    while True:
        try:
            for treno in TRENI:

                # Recupera dati
                data = get_train_data(treno)

                # Costruisce messaggio
                msg = build_message(data)

                # Invia su Telegram
                send_telegram("sendMessage", {
                    "chat_id": CHAT_ID,
                    "text": msg
                })

                # Piccola pausa tra treni
                time.sleep(2)

        except Exception as e:
            print(f"[{now()}] ERRORE LOOP:", e)

        # Attesa prima del prossimo ciclo
        time.sleep(REFRESH_SEC)


# ========================= MAIN =========================

if __name__ == "__main__":
    print(f"[{now()}] Bot avviato...")

    # Avvia il monitor
    monitor_loop()
