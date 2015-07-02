# -*- encoding: UTF-8 -*-

import json
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.template import loader

from protoLib.getStuff import getUserProfile, getUserLanguage
from protoExt.utils.utilsWeb import JsonError, JsonSuccess 
from protoExt.utils.utilsBase import getReadableError
import traceback


def protoGetUserRights(request):
    """ return usr rights 
    """
    
    if request.method != 'POST':
        return JsonError( 'invalid message' ) 

    userName = request.POST['login']
    userPwd  = request.POST['password']

    errMsg = ''
    success = False
    language = None   

    try:
        pUser = authenticate(username = userName, password = userPwd )
    except:
        pUser = None
        
    userInfo = { 'userName' : userName } 
                 
    if pUser is not None:
        if pUser.is_active:
            login(request, pUser)
            success = True
            userInfo[ 'isStaff' ] = pUser.is_staff  
            userInfo[ 'isSuperUser' ] = pUser.is_superuser  
            userInfo[ 'fullName' ] = pUser.get_full_name()  

            # Si es login retorna la lengua del usuario  
            userProfile = getUserProfile( pUser )
            language = getUserLanguage( userProfile.language or 'en' ) 
            
        else:
            # Return a 'disabled account' error message
            errMsg =  "Cet utilisateur est desactiv&eacute;"   

    else:
        # Return an 'invalid login' error message.
        errMsg =  "Mauvais utilisateur ou mot de passe"  
    
    
    jsondict = {
        'success': success,
        'message': errMsg,
        'userInfo' : userInfo,
        'language' : language  
    }
    
    # Encode json 
    context = json.dumps( jsondict)
    return HttpResponse(context, content_type="application/json")


def protoGetPasswordRecovery(request):
    baseURI = request.build_absolute_uri('..')
                
    if request.POST.get('email') and request.POST.get('login'):
        try:
            u = User.objects.get(email = request.POST['email'], username = request.POST['login'])
            token = user_token(u)
            
            try: 
                baseURI = 'http://' + settings.HOST_DOMAIN
            except: baseURI = request.get_host() 
            baseURI += '/protoLib/'

            link = baseURI + 'resetpassword?a=%s&t=%s' % (u.pk, token)
            
            email_template_name = 'recovery/recovery_email.txt'
            body = loader.render_to_string(email_template_name).strip()
            message = _(body)
            message += ' %s\n\n%s : %s' % (link, _(u'Utilisateur'), request.POST['login'])
            message += ' \n\n%s' % (_(u'Si vous ne voulez pas réinitialiser votre mot de passe, il suffit d\'ignorer ce message et il va rester inchangé'))
            u.email_user( _('Nouveau mot de passe'), message)
            return JsonSuccess()  
        except Exception as e:
            traceback.print_exc()
            return JsonError(getReadableError(e))  
    
    return HttpResponseRedirect('/')

def resetpassword(request):
    link = '../protoExtReset'
    if request.GET.get('a') and request.GET.get('t'):
        user = User.objects.get(pk = request.GET['a'])
        token = user_token(user)
        if request.GET['t'] == token:
            newpass =  User.objects.make_random_password(length=8)
            user.set_password(newpass)
            user.save()
            message = _(u'Votre mot de passe a été réinitialisé ') +' : %s' % (newpass) 
            message += ' \n\n%s : %s' % (_(u'Utilisateur'), user)
            user.email_user( _('Nouveau mot de passe'), message)
            
            response = HttpResponseRedirect(link)
            return response
    return HttpResponseRedirect(link)

def changepassword(request):
    
    if request.method != 'POST':
        return JsonError( 'invalid message' ) 
    
    newpass1 = request.POST['newPassword1']
    newpass2 = request.POST['newPassword2']
    userName = request.POST['login']
    userPwd  = request.POST['current']
    
    try:
        pUser = authenticate(username = userName, password = userPwd )
    except:
        pUser = None
    
    errMsg =  "Mauvais utilisateur ou mot de passe"
    if pUser is not None:
        if newpass1==newpass2:
            user = User.objects.get(username = userName)
            user.set_password(newpass1)
            user.save()
            if user.email:
                try:
                    message = _(u'Votre mot de passe a été réinitialisé ') +' : %s' % (newpass1) 
                    message += ' \n\n%s : %s' % (_(u'Utilisateur'), user)
                    user.email_user(_( 'Nouveau mot de passe'), message)
                except:
                    pass
            return JsonSuccess()
        else:
            errMsg = 'Les mots de passe ne correspondent pas!'
    return JsonError(_(errMsg))


def user_token(user):
    import hashlib
    salt = user.email + settings.SECRET_KEY
    localHash = hashlib.md5( salt.encode('utf-8') ).hexdigest()
    return localHash


def protoLogout(request):
    
    logout(request)
    return JsonSuccess( { 'message': 'Ok' } )