from django.conf.urls import patterns, url


# FUTURE : Secuences  getFieldIncrement
# url('getFieldIncrement/$', getFieldIncrement),

from protoExt.views.protoMenu import protoGetMenuData
from protoExt.views.protoGetPci import protoGetPCI 

from protoExt.views.protoSaveProtoObj import protoSaveProtoObj
from protoExt.views.protoGetPciFieldTree import  protoGetFieldTree
from protoExt.views.protoGetPciDetailsTree import protoGetDetailsTree

from protoExt.views.protoLogin import protoGetUserRights, protoLogout, protoGetPasswordRecovery, resetpassword, changepassword

from protoExt.views.protoActionList import protoList
from protoExt.views.protoActionExport  import protoExport
from protoExt.views.protoActionEdit  import protoCreate, protoUpdate, protoDelete
from protoExt.utils.loadFile import loadFiles
from protoExt.views.protoActionWiki import protoWiki
from protoExt.views.protoActionAction import protoExecuteAction


urlpatterns = patterns('',

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

    url('loadFile/$', loadFiles),
)


    # url(r'^protoExt$', TemplateView.as_view(template_name='protoExt.html')),
