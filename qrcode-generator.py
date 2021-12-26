import qrcode

#ask the user for the URL of the destination the QR code will direct them to.
data = input("""Welcome to the QRcode Generator 
Please enter your Link: """)

#Creates the qr code.
img = qrcode.make(data)

#ask th user for the desired name of the file.
filename = input("Awesome! Now enter the name of the file: ")

#Adds the .png filetype to the file name.
filename = filename + ".png"

#ask the user where they would like to save the Qr Code
location = input("""Please enter the file location: 
ex. Windows PC would look like C:/Users/Yourprofilename/Desktop
(Remember Windows default backslashes (\) need to be swapped with (/)
Linux would look like /home/Yourprofilename/Desktop
Enter Location here: """)

#Adds the forward slash to the file location.
location = location + ("/")

#Saves the file to your desired location
img.save(location + filename)







