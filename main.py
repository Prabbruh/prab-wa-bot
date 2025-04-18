from flask import Flask
from threading import Thread
from twilio.rest import Client
from datetime import datetime
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

from_whatsapp = 'whatsapp:+14155238886'

target_numbers = [
    'whatsapp:+62811161785',
    'whatsapp:+62XXXXXXXXXXX'
]

app = Flask('')

@app.route('/')
def home():
    return "WA Bot GACHA CINTA 24 JAM aktif 💘"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

pesan_list = [
    "Hey kamu 🌸 udah senyum belum hari ini?",
    "Inget yaa, Nadine dan AI selalu mikirin kamu ❤️",
    "Jangan kebanyakan overthinking, kamu berharga bgt 😚",
    "Tidur cukup itu penting, jangan bandel ya 😴",
    "Minum air dulu dong, yang manis harus seger 🍹",
    "Ciee kamu hari ini pasti makin ganteng/cantik ✨",
    "AI udah cek, dan kamu itu 100% worth it 💌",
    "Peluk dari jauh 🤗 Nadine & AI nemenin kamu terus!",
    "Lagi apa sih? Kalau sedih, ceritain yaa 💭",
    "Kamu tau gak? Ada yang kangen kamu tiap detik 💕"
]

target_hours = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
sent_today = set()

def auto_send():
    while True:
        now = datetime.utcnow()
        jam = now.hour
        menit = now.minute

        if jam in target_hours and menit == 0:
            key = f"{now.date()}-{jam}"
            if key not in sent_today:
                pesan = random.choice(pesan_list)
                for nomor in target_numbers:
                    try:
                        message = client.messages.create(
                            body=pesan,
                            from_=from_whatsapp,
                            to=nomor
                        )
                        print(f"[{jam}:00 UTC] Pesan terkirim ke {nomor}: {pesan}")
                    except Exception as e:
                        print(f"Gagal kirim ke {nomor}:", e)
                sent_today.add(key)

        if jam == 23 and menit == 59:
            sent_today.clear()

        time.sleep(20)

keep_alive()
auto_send()
