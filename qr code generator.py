import pyqrcode # pip install pyqrcode
from pyzbar.pyzbar import decode #pip install pyzbar
from PIL import Image #pip install pillow

qr=pyqrcode.create("Kartik")
qr.png("myCode.png",scale=8) #converting code to qr code png

d=decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))