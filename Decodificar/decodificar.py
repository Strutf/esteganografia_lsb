from PIL import Image

def decode_message(image_path):
    # Abrir a imagem com a mensagem escondida
    image = Image.open(image_path)
    width, height = image.size

    # Obter os pixels da imagem
    pixels = image.load()

    # Extrair os bits menos significativos dos componentes RGB de cada pixel
    binary_message = ''
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Extrair o bit menos significativo de cada componente RGB
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Converter a sequência binária em caracteres ASCII
    chars = []
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        chars.append(chr(int(byte, 2)))

    # Juntar os caracteres para formar a mensagem decodificada
    decoded_message = ''.join(chars)
    return decoded_message

i=input("Voce quer saber a mensagem secreta?")
while i!="Sim" and i!="sim":
    i=input("Voce quer saber a mensagem secreta? ")
image_path = 'secret.png'
# Decodificar a mensagem da imagem
decoded_message = decode_message(image_path)
print("Mensagem decodificada: ", decoded_message)
input()