import qrcode

print("  Type the text you want to convert to QR Code\n  You can write anything, including URL links.")
txt = input("  Text: ")
img = qrcode.make(txt)
name_txt = input("  QR code PNG image name: ")
img.save(name_txt+".png")
input("  Press Enter to exit: ")
exit()