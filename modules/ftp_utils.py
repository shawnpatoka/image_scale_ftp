from ftplib import FTP
import os

def connect_ftp(host, user, password, cwd):
    ftp = FTP(host)
    ftp.login(user=user, passwd=password)
    ftp.cwd(cwd)
    return ftp


def upload_images(ftp, resized_dir):
    upload_count = 0

    for upload_image in os.listdir(resized_dir):
        if upload_image.endswith(".jpeg") or upload_image.endswith(".jpg") or upload_image.endswith(".png") or upload_image.endswith(".gif"):
            local_path = os.path.join('./resized',upload_image)
            file = open(local_path,'rb')
            ftp.storbinary("STOR " + upload_image, file)
            file.close()
            print(f'[ success ] - {upload_image}')
            upload_count = upload_count + 1
        else:
            print(f'[ X nope ] - {upload_image}')
    
    print("-------------------------------")
    print("Successfully Completed!")
    print(f"Total Images Uploaded: {upload_count}")