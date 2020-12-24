import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskPracticalWebapp.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                        PracticalForm, RequestResetForm, ResetPasswordForm)
from flaskPracticalWebapp.models import User, Practical
from flaskPracticalWebapp import app, db, bcrypt, mail
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
