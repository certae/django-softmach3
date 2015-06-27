from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Fix: Login Change pwd 
# from protoExt.views.utils.generic_views import DirectTemplateView

# FUTURE : Secuences  getFieldIncrement

from protoExt.views.protoMenu import protoGetMenuData
from protoExt.views.protoGetPci import protoGetPCI 

from protoExt.views.protoSaveProtoObj import protoSaveProtoObj
from protoExt.views.protoGetPciFieldTree import  protoGetFieldTree
from protoExt.views.protoGetPciDetailsTree import protoGetDetailsTree

from protoExt.views.protoLogin import protoGetUserRights, protoLogout, protoGetPasswordRecovery, resetpassword, changepassword

from protoExt.views.protoActionList import protoList
from protoExt.views.protoActionExport  import protoExport
from protoExt.views.protoActionEdit  import protoCreate, protoUpdate, protoDelete
from protoExt.views import protoExecuteAction
from protoExt.utils.loadFile import loadFiles
from protoExt.views.protoActionRep import protoWiki

urlpatterns = patterns('',
    url(r'^protoExt$', TemplateView.as_view(template_name='protoExt.html')),
#     url(r'^protoExtReset$', DirectTemplateView.as_view(template_name='protoExt.html',extra_context={ 'isPasswordReseted': True })),

    url('protoList/$', protoList),
    url('protoExport/$', protoExport),
    url('protoWiki/$', protoWiki),

    url('protoDoActions/$', protoExecuteAction),

    url('protoAdd/$', protoCreate),
    url('protoUpd/$', protoUpdate),
    url('protoDel/$', protoDelete),

    url('protoGetMenuData/$', protoGetMenuData),
    url('protoGetPCI/$', protoGetPCI),

    url('protoSaveProtoObj/$', protoSaveProtoObj),
    url('protoGetFieldTree/$', protoGetFieldTree),
    url('protoGetDetailsTree/$', protoGetDetailsTree),

    url('protoGetUserRights/$', protoGetUserRights),
    url('protoGetPasswordRecovery/$', protoGetPasswordRecovery),
    url('resetpassword/$', resetpassword),
    url('submitChangePassword/$', changepassword),
    url('protoLogout/$', protoLogout),

#     url('getFieldIncrement/$', getFieldIncrement),
    url('loadFile/$', loadFiles),
)