from django.shortcuts import render

# Create your views here.

def app_2(request):

    context={
        'heading':'Hello ! This is Awal in front of You',
        'bio':'Allows a user to reset their password by generating a one-time use link that can be used to reset the password, and sending that link to the user’s registered email address.This view will send an email if the following conditions are met:',
        'descriptions':'The requested user has a usable password. Users flagged with an unusable password (see set_unusable_password()) aren’t allowed to request a password reset to prevent misuse when using an external authentication source like LDAP.If any of these conditions are not met, no email will be sent, but the user won’t receive any error message either. This prevents information leaking to potential attackers. If you want to provide an error message in this case, you can subclass PasswordResetForm and use the form_class attribute.'
    }
    return render(request,'app2/app2.html',context)