import qrcode

data = input("""Welcome to the QRcode Generator 
Please enter your Link: """)

img = qrcode.make(data)

filename = input("Awesome! Now enter the name of the file: ")

filename = filename + ".png"

location = input("""Please enter the file location: 
ex. Windows PC would look like C:/Users/Yourprofilename/Desktop
(Remember Windows default backslashes (\) need to be swapped with (/)
Linux would look like /home/Yourprofilename//Desktop
Enter Location here: """)

location = location + ("/")

img.save(location + filename)







