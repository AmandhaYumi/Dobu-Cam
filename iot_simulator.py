import random
import time

import requests


API_BASE_URL = "http://127.0.0.1:5000"
DEVICE_ID = "dobu-cam-esp32-sim"


def enviar_leitura(pet_detectado):
    payload = {
        "device_id": DEVICE_ID,
        "sensor": "PIR/camera-simulada",
        "confidence": round(random.uniform(0.82, 0.97) if pet_detectado else random.uniform(0.04, 0.18), 2),
    }

    resposta = requests.post(f"{API_BASE_URL}/update/{1 if pet_detectado else 0}", data=payload, timeout=2)
    resposta.raise_for_status()
    return resposta.json()


def main():
    pet_detectado = False
    print("Simulador IoT Dobu-CAM iniciado.")
    print("Enviando leituras HTTP para http://127.0.0.1:5000/update/<0|1>")
    print("Pressione Ctrl+C para parar.\n")

    while True:
        pet_detectado = not pet_detectado
        dados = enviar_leitura(pet_detectado)
        status = "PRESENTE" if dados["pet_detected"] else "AUSENTE"
        print(f"Pet {status} | movimento={dados['confidence']:.2f}")
        time.sleep(5)


if __name__ == "__main__":
    main()
