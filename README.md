# Dobu-CAM 🐾📷

Sistema de monitoramento inteligente para pets usando camera real, visao computacional e comunicacao HTTP.

---

## 📖 Sobre o projeto

A Dobu-CAM foi criada para ajudar responsaveis a acompanharem a presenca do pet em ambientes monitorados.

O sistema utiliza uma webcam do notebook ou um celular com aplicativo de camera IP para transmitir video em tempo real, detectar movimentacao no ambiente e registrar quando o animal foi visto pela ultima vez. Essas informacoes sao enviadas para um backend Flask e exibidas em tempo real em um dashboard web.

O projeto demonstra conceitos de:

- 👁️ Visao Computacional
- 🌐 Comunicacao HTTP
- 📊 Dashboard em tempo real
- 🔗 Integracao entre backend, camera e frontend
- 🎥 Processamento de video em tempo real

---

## ⚙️ Como funciona

```text
Webcam / Celular com camera IP
                |
                | HTTP POST
                v
           Backend Flask
                |
                | HTTP GET
                v
           Dashboard Web
```

A camera transmite os frames em tempo real utilizando OpenCV.

Quando ha movimentacao detectada:

- 🐶 o sistema considera que o pet apareceu;
- 📡 envia uma leitura HTTP para o backend;
- 🕒 atualiza o horario de "ultima vez visto";
- 📁 registra eventos de entrada e saida;
- 🔄 atualiza automaticamente o dashboard.

---

## ✨ Funcionalidades

- 📷 Camera em tempo real
- 📱 Compatibilidade com webcam ou camera IP/celular
- 📊 Dashboard web atualizado em tempo real
- 🕒 Registro de "Last Seen" do pet
- 📁 Historico de presenca
- 🌐 Comunicacao HTTP entre os modulos
- 👁️ Processamento de imagem com OpenCV
- 🟩 Modo visual com caixa de deteccao
- 🤖 Estrutura pronta para evoluir com IA

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- OpenCV
- Requests
- HTML
- CSS
- JavaScript
- HTTP

---

## 🚀 Executando o projeto

Antes de iniciar, instale o Python pelo site oficial:

```text
https://www.python.org/downloads/
```

Durante a instalacao, marque a opcao:

```text
Add python.exe to PATH
```

Depois abra um novo terminal e confirme:

```bash
python --version
```

### 1️⃣ Criando o ambiente virtual

```bash
cd C:\Dobu-Cam
python -m venv .venv
```

### 2️⃣ Ativando o ambiente

Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Instalando as dependencias

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Passo a passo para a aplicacao funcionar

### 1️⃣ Inicie o backend

Abra um terminal na pasta do projeto:

```bash
cd C:\Dobu-Cam
python backend.py
```

Mantenha esse terminal aberto.

### 2️⃣ Abra o dashboard

No navegador, acesse:

```text
http://127.0.0.1:5000
```

### 3️⃣ Conecte a camera

Para usar a webcam do notebook, abra outro terminal e rode:

```bash
cd C:\Dobu-Cam
python camera_iot.py
```

Para usar a camera do celular:

1. 📲 Instale um aplicativo de camera IP no celular.
2. 📶 Conecte o celular e o computador no mesmo Wi-Fi.
3. ▶️ Inicie o servidor da camera no aplicativo.
4. 🔗 Copie a URL de video exibida pelo app.
5. 💻 Rode no segundo terminal:

```bash
cd C:\Dobu-Cam
python camera_iot.py --camera http://IP_DO_CELULAR:8080/video
```

Exemplo:

```bash
python camera_iot.py --camera http://192.168.0.20:8080/video
```

### ✅ Resultado esperado

- 📷 O dashboard mostra a imagem da camera.
- 🟢 O status muda entre animal presente e animal ausente.
- 🕒 O campo "Ultima vez visto" atualiza quando o pet aparece.
- 📁 O historico registra quando o animal voltou e quando saiu da camera.

---

## 🖥️ Iniciando o backend

```bash
python backend.py
```

Abra no navegador:

```text
http://127.0.0.1:5000
```

---

## 📷 Iniciando a camera

### Webcam do notebook

```bash
python camera_iot.py
```

### Outra camera USB

```bash
python camera_iot.py --camera 1
```

### Celular usando camera IP

```bash
python camera_iot.py --camera http://192.168.0.20:8080/video
```

Voce pode usar aplicativos de camera IP no celular para transformar o aparelho em uma camera em tempo real.

📶 O computador e o celular precisam estar conectados na mesma rede Wi-Fi.

---

## 📊 Dashboard

O painel web mostra:

- 🐾 Status atual do pet
- 🕒 Ultima vez visto
- 📁 Historico de eventos
- 📷 Fonte da camera
- 🎥 Video processado em tempo real

Caso a camera ainda nao esteja ativa, o sistema exibe uma mensagem aguardando conexao.

---

## 🌐 Endpoints da API

### Status do sistema

```http
GET /status
```

### Registrar pet detectado

```http
POST /update/1
```

### Registrar pet ausente

```http
POST /update/0
```

### Enviar frame atual da camera

```http
POST /camera-frame
```

---

## 📄 Exemplo de resposta

```json
{
  "pet_detected": true,
  "last_seen": "2026-05-21T10:50:00-03:00",
  "confidence": 0.92,
  "source": "dobu-cam-real",
  "protocol": "HTTP",
  "telemetry": {
    "device_id": "dobu-cam-real",
    "sensor": "webcam-real"
  },
  "events": []
}
```

---

## 👥 Integrantes

- Amandha Yumi Toyota Artulino - RM: 563549
- Giovanna Bardella Gomes - RM: 561439
- Erick Takeshi Nakajune - RM: 566059

---

# 🐾 Dobu-CAM

Projeto academico desenvolvido para demonstracao de Visao Computacional aplicada ao monitoramento inteligente de pets.