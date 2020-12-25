import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flaskPracticalWebapp import mail
from flask_mail import Message

def save_profile_pic(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_filename)
    output_size = (125, 125)
    resized_pic = Image.open(form_picture)
    resized_pic.thumbnail(output_size)
    resized_pic.save(picture_path)
    return picture_filename

# Function that sends a reset email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Pasword Reset Request", sender="info@demo.com", recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for("users.reset_token", token=token, _external=True)}

If you did not make this request, please ignore this email and no changes will be made to your account.
'''
    mail.send(msg)
