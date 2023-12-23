import cv2
from pyzbar.pyzbar import decode

# Função para decodificar os códigos de barras
def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        # Extrair as coordenadas do código de barras
        (x, y, w, h) = barcode.rect
        # Desenhar um retângulo ao redor do código de barras
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Obter os dados do código de barras
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        # Exibir os dados do código de barras
        print(f"Tipo: {barcode_type}, Dados: {barcode_data}")

# Inicializar a câmera
cap = cv2.VideoCapture(0)

while True:
    # Capturar um frame da câmera
    _, frame = cap.read()

    # Chamar a função para decodificar os códigos de barras
    read_barcodes(frame)

    # Exibir o frame
    cv2.imshow("Barcode Scanner", frame)

    # Verificar se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos da câmera e fechar a janela
cap.release()
cv2.destroyAllWindows()
