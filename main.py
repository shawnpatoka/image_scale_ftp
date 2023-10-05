from modules.image_processing import process_images
from modules.ftp_utils import connect_ftp, upload_images
from modules.environs import FTP_HOST, FTP_USER, FTP_PASSWORD, FTP_CWD


ORIGINAL_IMAGE_PATH = './originals/'
RESIZED_IMAGE_PATH = './resized/'


ftp = connect_ftp(FTP_HOST, FTP_USER, FTP_PASSWORD, FTP_CWD)
process_images(ORIGINAL_IMAGE_PATH)
upload_images(ftp, RESIZED_IMAGE_PATH)

ftp.quit()