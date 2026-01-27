import cv2
import os
import time
import tkinter as tk
from tkinter import filedialog

# ==============================
# CONFIGURAÇÕES
# ==============================
ASCII_CHARS = " .:-=+*#%@"  # Caracteres do mais escuro para o mais claro
ESCALA = 0.60  # Corrige proporção vertical do CMD
LARGURA_CMD = 140  # Aumenta qualidade
FPS_LIMIT = False
CONTRASTE = 1.4


# ==============================
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def selecionar_video():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    video_path = filedialog.askopenfilename(
        title="Selecione o vídeo",
        filetypes=[
            ("Vídeos", "*.mp4 *.avi *.mov *.mkv *.wmv"),
            ("Todos os arquivos", "*.*"),
        ],
    )

    return video_path


def frame_para_ascii(frame, largura):
    altura, largura_original = frame.shape[:2]
    proporcao = altura / largura_original
    nova_altura = int(largura * proporcao * ESCALA)

    frame = cv2.resize(frame, (largura, nova_altura))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ascii_frame = []
    escala = len(ASCII_CHARS) - 1

    for linha in frame:
        for pixel in linha:
            idx = int(pixel) * escala // 255
            ascii_frame.append(ASCII_CHARS[idx])
        ascii_frame.append("\n")

    return "".join(ascii_frame)


def reproduzir_video_ascii(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1 / fps if FPS_LIMIT and fps > 0 else 0.03

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        ascii_frame = frame_para_ascii(frame, LARGURA_CMD)

        limpar_tela()
        print(ascii_frame)

        time.sleep(delay)

    cap.release()


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    video = selecionar_video()

    if not video:
        print("Nenhum vídeo selecionado.")
    else:
        reproduzir_video_ascii(video)
