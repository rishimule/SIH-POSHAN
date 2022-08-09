from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django import template
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout



def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data)|Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested @ SIH"
                    plaintext = template.loader.get_template('accounts/password_reset_email.txt')
                    htmltemp = template.loader.get_template('accounts/password_reset_email.html')
                    c = { 
                    "email":user.email,
                    'domain':request.META['HTTP_HOST'],
                    'site_name': 'Team Merakii',
                    # "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': request.scheme ,
                    }
                    print(request.scheme)
                    text_content = plaintext.render(c)
                    html_content = htmltemp.render(c)
                    try:
                        msg = EmailMultiAlternatives(subject, text_content, 'Team Merakii <admin@example.com>', [user.email], headers = {'Reply-To': 'support@teammerakii.com'})
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.info(request, "Password reset instructions have been sent to the email address entered.")
                    return redirect ("home")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset.html", context={"form":password_reset_form})