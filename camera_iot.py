import argparse
import time

import cv2
import requests


API_BASE_URL = "http://127.0.0.1:5000"
DEVICE_ID = "dobu-cam-real"


def enviar_status(pet_detectado, nivel_movimento, origem):
    payload = {
        "device_id": DEVICE_ID,
        "sensor": origem,
        "confidence": round(nivel_movimento, 2),
    }
    try:
        requests.post(f"{API_BASE_URL}/update/{1 if pet_detectado else 0}", data=payload, timeout=1.5)
    except requests.RequestException:
        print("Backend indisponivel para envio de status.")


def enviar_frame(frame):
    ok, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 72])
    if not ok:
        return

    try:
        requests.post(
            f"{API_BASE_URL}/camera-frame",
            files={"frame": ("camera.jpg", buffer.tobytes(), "image/jpeg")},
            timeout=1.5,
        )
    except requests.RequestException:
        print("Backend indisponivel para envio da imagem.")


def abrir_camera(camera):
    if str(camera).isdigit():
        captura = cv2.VideoCapture(int(camera))
    else:
        captura = cv2.VideoCapture(camera)

    captura.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return captura


def detectar_por_movimento(camera, min_area, intervalo_envio, intervalo_frame, mostrar_janela, marcar_deteccao):
    captura = abrir_camera(camera)

    if not captura.isOpened():
        raise RuntimeError("Nao foi possivel abrir a camera. Confira o indice ou a URL informada.")

    primeiro_frame = None
    ultimo_envio = 0
    ultimo_frame_salvo = 0
    origem = "camera-celular" if str(camera).startswith("http") else "webcam-real"

    print("Dobu-CAM real iniciada.")
    print("A imagem aparece no dashboard: http://127.0.0.1:5000")
    print("Pressione Ctrl+C para parar.\n")

    try:
        while True:
            ok, frame = captura.read()
            if not ok:
                print("Falha ao acessar a câmera.")
                time.sleep(1)
                continue

            frame = cv2.resize(frame, (640, 360))
            cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cinza = cv2.GaussianBlur(cinza, (21, 21), 0)

            if primeiro_frame is None:
                primeiro_frame = cinza
                continue

            diferenca = cv2.absdiff(primeiro_frame, cinza)
            limiar = cv2.threshold(diferenca, 28, 255, cv2.THRESH_BINARY)[1]
            limiar = cv2.dilate(limiar, None, iterations=2)
            contornos, _ = cv2.findContours(limiar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            maior_area = 0
            pet_detectado = False

            for contorno in contornos:
                area = cv2.contourArea(contorno)
                if area < min_area:
                    continue

                pet_detectado = True
                maior_area = max(maior_area, area)
                if marcar_deteccao:
                    x, y, largura, altura = cv2.boundingRect(contorno)
                    cv2.rectangle(frame, (x, y), (x + largura, y + altura), (24, 160, 88), 2)

            nivel_movimento = min(0.99, maior_area / 18000) if pet_detectado else 0.08
            status = "PET/MOVIMENTO DETECTADO" if pet_detectado else "SEM DETECCAO"

            if time.time() - ultimo_frame_salvo >= intervalo_frame:
                enviar_frame(frame)
                ultimo_frame_salvo = time.time()

            if mostrar_janela:
                cv2.imshow("Dobu-CAM real", frame)

            if time.time() - ultimo_envio >= intervalo_envio:
                enviar_status(pet_detectado, nivel_movimento, origem)
                print(f"{status} | movimento={nivel_movimento:.2f}")
                ultimo_envio = time.time()

            if mostrar_janela and cv2.waitKey(1) & 0xFF == ord("q"):
                break
    except KeyboardInterrupt:
        print("\nDobu-CAM parada.")
    finally:
        captura.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dobu-CAM com camera real enviando dados IoT via HTTP.")
    parser.add_argument(
        "--camera",
        default="0",
        help="Indice da webcam, ex: 0, ou URL de camera IP/celular, ex: http://192.168.0.20:8080/video",
    )
    parser.add_argument("--min-area", type=int, default=1800, help="Area minima para considerar deteccao.")
    parser.add_argument("--intervalo", type=float, default=1.5, help="Intervalo em segundos entre envios HTTP.")
    parser.add_argument("--frame-intervalo", type=float, default=0.8, help="Intervalo em segundos para atualizar a imagem do dashboard.")
    parser.add_argument("--show-window", action="store_true", help="Mostra tambem a janela do OpenCV.")
    parser.add_argument("--draw-detection", action="store_true", help="Desenha a caixa de deteccao para demonstrar Visao Computacional.")
    args = parser.parse_args()

    detectar_por_movimento(
        args.camera,
        args.min_area,
        args.intervalo,
        args.frame_intervalo,
        args.show_window,
        args.draw_detection,
    )
