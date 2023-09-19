from PIL import Image

def encode_message(image_path, message):
    # Abrir a imagem
    image = Image.open(image_path)
    width, height = image.size

    # Verificar se a mensagem cabe na imagem
    max_chars = width * height * 3 // 8
    if len(message) > max_chars:
        raise ValueError("A mensagem é muito longa para a imagem fornecida.")

    # Converter a mensagem em uma lista de caracteres ASCII
    chars = [ord(c) for c in message]

    # Adicionar um caractere nulo para indicar o final da mensagem
    chars.append(0)

    # Converter os caracteres em uma sequência binária
    binary_message = ''.join(format(char, '08b') for char in chars)

    # Obter os pixels da imagem
    pixels = image.load()

    # Esconder a mensagem nos bits menos significativos dos componentes RGB de cada pixel
    index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Substituir o bit menos significativo de cada componente RGB com um bit da mensagem
            if index < len(binary_message):
                r = (r & 0xFE) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                g = (g & 0xFE) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                b = (b & 0xFE) | int(binary_message[index])
                index += 1

            # Atualizar o pixel com os novos componentes RGB
            pixels[x, y] = (r, g, b)

    # Salvar a imagem com a mensagem escondida
    encoded_image_path = 'secret.png'
    image.save(encoded_image_path)
    return encoded_image_path

# Exemplo de uso:
image_path = 'imagem.png'
message = 'te amo'

# Codificar a mensagem na imagem
encoded_image_path = encode_message(image_path, message)
print("Imagem com a mensagem escondida: ", encoded_image_path)