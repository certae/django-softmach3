from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Fix: 
# from protoExt.actionsbase.utils.generic_views import DirectTemplateView

from protoExt.actionsbase.protoMenu import protoGetMenuData
from protoExt.actionsbase.protoGetPci import protoGetPCI, protoSaveProtoObj, protoGetFieldTree, getFieldIncrement
from protoExt.actionsbase.protoGetDetails import protoGetDetailsTree
from protoExt.actionsbase.protoLogin import protoGetUserRights, protoLogout, protoGetPasswordRecovery, resetpassword, changepassword

from protoExt.actionsbase.protoActionList import protoList
from protoExt.actionsbase.protoActionRep  import sheetConfigRep, protoCsv
from protoExt.actionsbase.protoActionEdit  import protoCreate, protoUpdate, protoDelete
from protoExt.actionsbase.protoActions  import protoExecuteAction

# Fix:
# from protoExt.actionsbase.utils.loadFile import loadFiles

urlpatterns = patterns('',
    url(r'^protoExt$', TemplateView.as_view(template_name='protoExt.html')),
#     url(r'^protoExtReset$', DirectTemplateView.as_view(template_name='protoExt.html',extra_context={ 'isPasswordReseted': True })),

    url('protoList/$', protoList),
    url('sheetConfigRep/$', sheetConfigRep),
    url('protoCsv/$', protoCsv),

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

    url('getFieldIncrement/$', getFieldIncrement),

#     url('loadFile/$', loadFiles),
)