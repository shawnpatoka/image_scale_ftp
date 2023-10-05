from PIL import Image
import os

BASE_WIDTH = 570
PORTRAIT_HEIGHT = 450
IMG_RATIO = .7


def getFileName(file_path):
    base_name = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(base_name)
    return file_name


def max_height(file_name, img):
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    wpercent = (PORTRAIT_HEIGHT / float(img.size[1]))
    hsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((hsize, PORTRAIT_HEIGHT))
    img.save(f'./resized/{file_name}.jpg')
    return img


def max_width(file_name, img):
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    wpercent = (BASE_WIDTH / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((BASE_WIDTH, hsize))
    img.save(f'./resized/{file_name}.jpg')
    return img


def ask_for_scale_options(file_name):
    print(f'\n"{file_name}" is a tall image.\nDo you want to constrain height to 450px? (Y/N)')
    user_input = input('')
    return user_input


def tall_image_conditional(file_name, img):
    user_input = ask_for_scale_options(file_name)
    if user_input.upper() == 'Y':
        max_height(file_name, img)
    elif user_input.upper() =='N':
        max_width(file_name, img)
    while user_input.upper() != 'Y' and user_input.upper() != 'N':
        print("\nInvalid response. Please try again...")
        user_input = ask_for_scale_options(file_name)
        if user_input.upper() == 'Y':
            max_height(file_name, img)
        elif user_input.upper() =='N':
            max_width(file_name, img)


def process_images(original_dir):
    orig_images = []

    for file in os.listdir(original_dir):
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
            orig_path = os.path.join('./originals', file)
            orig_images.append(orig_path)

    for image in orig_images:
        file_name = getFileName(image)
        img = Image.open(image)
        if (img.width < 570 and img.height < 570):
            img = img.convert("RGB")
            img.save(f'./resized/{file_name}.jpg')
        else:
            if (img.width/img.height) >= IMG_RATIO:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                max_width(file_name, img)
            elif (img.width/img.height) < IMG_RATIO:
                tall_image_conditional(file_name, img)
            
