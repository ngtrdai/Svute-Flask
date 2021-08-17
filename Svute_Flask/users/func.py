import os
from os.path import join, splitext
import secrets
from PIL import Image
from flask import url_for, current_app


def SaveImage(form_picture, for_post = False):
    randomHex = secrets.token_hex(8)
    _, f_ext = splitext(form_picture.filename)
    picFilename = randomHex + f_ext
    if for_post == False:
        picFilePath = join(current_app.root_path, 'static/profile_pics', picFilename)
        outputSize = (400, 400)
        img = Image.open(form_picture)
        img.thumbnail(outputSize)
    else:
        picFilePath =join(current_app.root_path,'static/assets/img/posts',picFilename)
        img = Image.open(form_picture)
    img.save(picFilePath)
    return picFilename

    
