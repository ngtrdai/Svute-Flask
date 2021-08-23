import os
from os.path import join, splitext
import secrets
from PIL import Image
from flask import url_for, current_app
from Svute_Flask import storage


def SaveImage(form_picture, for_post = False):
    randomHex = secrets.token_hex(8)
    _, f_ext = splitext(form_picture.filename)
    picFilename = randomHex + f_ext
    if for_post == False:
        picFilePath = join(current_app.root_path, 'static/profile_pics', picFilename)
        img = Image.open(form_picture)
        width, height = img.size   # Get dimensions
        left = (width - 1000)/2
        top = (height - 1000)/2
        right = (width + 1000)/2
        bottom = (height + 1000)/2

        # Crop the center of the image
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(picFilePath)
        filePathCloud = "profile_pics" + picFilename
    else:
        picFilePath =join(current_app.root_path,'static/assets/img/posts',picFilename)
        img = Image.open(form_picture)
        img.save(picFilePath)
        filePathCloud = "assets/img/posts/" + picFilename
    storage.child(filePathCloud).put(picFilePath)
    link_img = storage.child(filePathCloud).get_url(None)
    #os.remove(picFilePath)
    return link_img

    
