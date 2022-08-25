import qrcode 


data = 'https://stackoverflow.com/questions/33123726/python-qrcode-error-no-module-named-image'

img = qrcode.make(data)
img.save('C:/image/myqrcode.png')
