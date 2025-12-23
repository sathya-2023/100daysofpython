import qrcode
#
# url = input("enter the url: ").strip()
# file_path = "/Users/sa40132171/Desktop/qrcode.png"
#
# qr = qrcode.QRCode()
# qr.add_data(url)
#
# img = qr.make_image()
# img.save(file_path)
#
# print("Qr code is generated")

# ----------Creating function---------- #

def make_qr(data, name="qr.png"):  #add file at the end like: .png or.jpg
    import qrcode
    img = qrcode.make(data)
    img.save(name)

make_qr("youtube.com","yt.png")