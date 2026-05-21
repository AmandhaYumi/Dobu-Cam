import argparse
import math
import time

import requests

try:
    import cv2
    import numpy as np
except ImportError:
    cv2 = None
    np = None


API_URL = "http://127.0.0.1:5000/update"


def send_status(detected, confidence):
    value = "1" if detected else "0"
    try:
        requests.post(
            f"{API_URL}/{value}",
            data={"confidence": confidence, "source": "python-opencv-simulado"},
            timeout=1.5,
        )
    except requests.RequestException:
        print("Backend indisponivel. Inicie com: python backend.py")


def synthetic_frame(frame_index):
    frame = np.full((480, 720, 3), (246, 248, 250), dtype=np.uint8)

    cv2.rectangle(frame, (0, 350), (720, 480), (225, 229, 233), -1)
    cv2.putText(frame, "Sala monitorada - camera simulada", (24, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (45, 55, 72), 2)

    visible = (frame_index // 75) % 2 == 0
    if not visible:
        cv2.putText(frame, "Pet fora do campo de visao", (220, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (110, 118, 130), 2)
        return frame, False, 0.08, None

    x = int(90 + 420 * (0.5 + 0.5 * math.sin(frame_index / 22)))
    y = 235
    bbox = (x, y, 140, 92)

    cv2.ellipse(frame, (x + 70, y + 52), (70, 42), 0, 0, 360, (60, 82, 120), -1)
    cv2.circle(frame, (x + 112, y + 18), 28, (60, 82, 120), -1)
    cv2.circle(frame, (x + 123, y + 12), 5, (15, 23, 42), -1)
    cv2.line(frame, (x + 10, y + 52), (x - 30, y + 30), (60, 82, 120), 10)

    confidence = round(0.84 + 0.12 * (0.5 + 0.5 * math.sin(frame_index / 12)), 2)
    return frame, True, confidence, bbox


def run_visual_demo(fps):
    frame_index = 0
    last_sent = 0

    while True:
        frame, detected, confidence, bbox = synthetic_frame(frame_index)

        if bbox:
            x, y, w, h = bbox
            cv2.rectangle(frame, (x, y), (x + w, y + h), (24, 160, 88), 3)
            cv2.putText(frame, f"PET {confidence:.0%}", (x, y - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (24, 160, 88), 2)

        label = "ANIMAL PRESENTE" if detected else "ANIMAL AUSENTE"
        color = (24, 160, 88) if detected else (220, 38, 38)
        cv2.putText(frame, label, (24, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.85, color, 2)
        cv2.imshow("Dobu-CAM - deteccao visual simulada", frame)

        if time.time() - last_sent >= 2:
            send_status(detected, confidence)
            print(f"{label} | confianca={confidence:.2f}")
            last_sent = time.time()

        frame_index += 1
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


def run_headless_demo():
    detected = False
    while True:
        detected = not detected
        confidence = 0.91 if detected else 0.10
        send_status(detected, confidence)
        print(("Animal detectado" if detected else "Animal ausente") + f" | confianca={confidence:.2f}")
        time.sleep(5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulador de visao computacional da Dobu-CAM.")
    parser.add_argument("--headless", action="store_true", help="Executa sem janela visual, util para ambientes sem OpenCV/GPU.")
    parser.add_argument("--fps", type=int, default=24, help="Taxa de quadros da demonstracao visual.")
    args = parser.parse_args()

    if args.headless or cv2 is None:
        if cv2 is None:
            print("OpenCV nao encontrado. Rodando simulacao sem janela visual.")
        run_headless_demo()
    else:
        run_visual_demo(max(1, args.fps))
