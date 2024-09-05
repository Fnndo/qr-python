import qrcode


imagem = qrcode.make("https://github.com/Fnndo")


imagem.save("qrcode.png")


print("Successfully generated")
