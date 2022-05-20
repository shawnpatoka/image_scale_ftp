from environs import Env
from PIL import Image
from ftplib import FTP_TLS
import os

env = Env()
env.read_env()

def getFileName(file_path):
    file_name = file_path.replace("./originals/","")
    if file_name.endswith(".jpg"):
        file_name = file_name.replace(".jpg","")
    if file_name.endswith(".jpeg"):
        file_name = file_name.replace(".jpeg","")
    if file_name.endswith(".png"):
        file_name = file_name.replace(".png","")
    if file_name.endswith(".gif"):
        file_name = file_name.replace(".gif","")
    return file_name


orig_images = []


for file in os.listdir("./originals/"):
    if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        orig_path = os.path.join('./originals', file)
        orig_images.append(orig_path)


for image in orig_images:
    basewidth = 570
    portrait_height = 450
    file_name = getFileName(image)
    img = Image.open(image)
    if (img.width/img.height) >= .7:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(f'./resized/{file_name}.jpg')
    elif (img.width/img.height) < .7:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        wpercent = (portrait_height / float(img.size[1]))
        hsize = int((float(img.size[0]) * float(wpercent)))
        img = img.resize((hsize, portrait_height), Image.ANTIALIAS)
        img.save(f'./resized/{file_name}.jpg')


host = env.str("FTP_HOST")
user = env.str("FTP_USER_NAME")
password = env.str("FTP_PASSWORD")
cwd = env.str("FTP_CWD")
ftp = FTP_TLS(host)
ftp.login(user=user, passwd=password)
ftp.prot_p()
ftp.cwd(cwd)

upload_count = 0


for upload_image in os.listdir('./resized/'):
    if upload_image.endswith(".jpeg") or upload_image.endswith(".jpg") or upload_image.endswith(".png") or upload_image.endswith(".gif"):
        local_path = os.path.join('./resized',upload_image)
        file = open(local_path,'rb')
        ftp.storbinary("STOR " + upload_image, file)
        file.close()
        print(f'[ success ] - {upload_image}')
        upload_count = upload_count + 1
    else:
        print(f'[ X nope ] - {upload_image}')


ftp.quit()


print("-------------------------------")
print("Successfully Completed!")
print("Total Images Uploaded: " + str(upload_count))
print("")