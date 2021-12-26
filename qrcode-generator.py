import qrcode

data = input("""Welcome to the QRcode Generator 
Please enter your Link: """)

img = qrcode.make(data)

filename = input("Awesome! Now enter the name of the file: ")

filename = filename + ".png"

img.save('/home/boto3/Desktop/'+ filename)






