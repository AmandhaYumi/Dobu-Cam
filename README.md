# Dobu-CAM 🐾📷

Sistema de monitoramento inteligente para pets utilizando câmera em tempo real, Visão Computacional e comunicação HTTP.

---

## 📖 Sobre o projeto

A Dobu-CAM foi criada para ajudar responsáveis a monitorarem seus pets em ambientes internos, principalmente animais que necessitam de maior acompanhamento devido à idade, problemas de saúde ou necessidade de supervisão constante.

Muitos responsáveis se preocupam em não saber se o animal apareceu recentemente em determinado ambiente ou se está se movimentando normalmente durante o dia. Pensando nisso, o projeto busca oferecer uma forma simples e acessível de acompanhamento remoto utilizando uma webcam do notebook ou um celular com aplicativo de câmera IP.

A solução utiliza técnicas de Visão Computacional para analisar os frames da câmera em tempo real com OpenCV, identificando movimentações no ambiente e registrando quando o pet foi visto pela última vez. Essas informações são enviadas por comunicação HTTP para um backend Flask, responsável por processar os dados e atualizar um dashboard web em tempo real.

O projeto demonstra, na prática, a aplicação de tecnologias de Visão Computacional e comunicação entre dispositivos conectados, simulando um sistema inteligente de monitoramento de pets.

Como prova de conceito, a aplicação já consegue:

- 🎥 Capturar vídeo em tempo real;
- 👁️ Processar imagens utilizando OpenCV;
- 🐾 Detectar movimentação no ambiente;
- 📁 Registrar eventos de entrada e saída;
- 🕒 Atualizar o status do pet em tempo real;
- 📊 Exibir o histórico e o “Last Seen” em um dashboard web.

Tecnologias utilizadas no projeto:

- 👁️ OpenCV para captura e processamento de imagem;
- 🌐 Flask para criação da API e backend;
- 📡 HTTP para comunicação entre câmera e sistema;
- 💻 HTML, CSS e JavaScript para o dashboard web;
- 🐍 Python como linguagem principal da aplicação.

Atualmente, o sistema utiliza webcam e câmera IP como forma de demonstração funcional da proposta. Futuramente, o projeto poderá evoluir para utilizar câmeras dedicadas de monitoramento e dispositivos mais robustos, tornando a solução mais próxima de um sistema real de acompanhamento inteligente para pets.

A Dobu-CAM demonstra a viabilidade técnica inicial da proposta ao integrar captura de vídeo, processamento visual, comunicação HTTP e exibição em tempo real em uma única aplicação funcional.

---

## ⚙️ Como funciona

```text
Webcam / Celular com câmera IP
                │
                │ HTTP POST
                ▼
           Backend Flask
                │
                │ HTTP GET
                ▼
           Dashboard Web
```

A câmera transmite os frames em tempo real utilizando OpenCV.

Quando há movimentação detectada:

- 🐶 O sistema considera que o pet apareceu;
- 📡 Envia uma leitura HTTP para o backend;
- 🕒 Atualiza o horário de “Última vez visto”;
- 📁 Registra eventos de entrada e saída;
- 🔄 Atualiza automaticamente o dashboard.

---

## ✨ Funcionalidades

- 📷 Captura de câmera em tempo real;
- 📱 Compatibilidade com webcam ou câmera IP/celular;
- 📊 Dashboard web atualizado em tempo real;
- 🕒 Registro de “Last Seen” do pet;
- 📁 Histórico de presença;
- 🌐 Comunicação HTTP entre os módulos;
- 👁️ Processamento de imagem com OpenCV;
- 🟩 Modo visual com caixa de detecção.

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

Durante a instalação, marque a opção:

```text
Add python.exe to PATH
```

Depois, abra um novo terminal e confirme a instalação:

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

### 3️⃣ Instalando as dependências

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Passo a passo para a aplicação funcionar

### 1️⃣ Inicie o backend

Abra um terminal na pasta do projeto:

```bash
cd C:\Dobu-Cam
python backend.py
```

Mantenha esse terminal aberto.

---

### 2️⃣ Abra o dashboard

No navegador, acesse:

```text
http://127.0.0.1:5000
```

---

### 3️⃣ Conecte a câmera

Para usar a webcam do notebook, abra outro terminal e execute:

```bash
cd C:\Dobu-Cam
python camera_iot.py --draw-detection
```

Para usar a câmera do celular:
efssd
1. 📲 Instale um aplicativo de câmera IP no celular;
2. 📶 Conecte o celular e o computador na mesma rede Wi-Fi;
3. ▶️ Inicie o servidor da câmera no aplicativo;
4. 🔗 Copie a URL de vídeo exibida pelo app;
5. 💻 Execute no segundo terminal:

```bash
cd C:\Dobu-Cam
python camera_iot.py --camera http://ip_celular/video --draw-detection
```

---

## ✅ Resultado esperado

- 📷 O dashboard mostra a imagem da câmera;
- 🟢 O status muda entre “animal presente” e “animal ausente”;
- 🕒 O campo “Última vez visto” atualiza quando o pet aparece;
- 📁 O histórico registra quando o animal entrou ou saiu do ambiente.

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

## 📷 Iniciando a câmera

### Webcam do notebook

```bash
python camera_iot.py
```

### Outra câmera USB

```bash
python camera_iot.py --camera 1
```

### Celular usando câmera IP

```bash
python camera_iot.py --camera http://192.168.0.20:8080/video
```

Você pode utilizar aplicativos de câmera IP no celular para transformar o aparelho em uma câmera em tempo real.

📶 O computador e o celular precisam estar conectados na mesma rede Wi-Fi.

---

## 📊 Dashboard

O painel web mostra:

- 🐾 Status atual do pet;
- 🕒 Última vez visto;
- 📁 Histórico de eventos;
- 📷 Fonte da câmera;
- 🎥 Vídeo processado em tempo real.

Caso a câmera ainda não esteja ativa, o sistema exibirá uma mensagem aguardando conexão.

---

## 👥 Integrantes

- Amandha Yumi Toyota Artulino — RM: 563549
- Giovanna Bardella Gomes — RM: 561439
- Erick Takeshi Nakajune — RM: 566059

---

# 🐾 Dobu-CAM

Projeto acadêmico desenvolvido para demonstração de Visão Computacional aplicada ao monitoramento inteligente de pets.