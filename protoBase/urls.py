
from django.conf.urls import  include, url
from django.contrib import admin
admin.autodiscover()


from django.views.generic import TemplateView

# from protoBase.settings import PPATH


# Uncoment to use xadmin
# import xadmin
# xadmin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#   url(r'^admin/', include(xadmin.site.urls)),

    url(r'^main$', TemplateView.as_view(template_name='index.html')),
    url(r'^debug$', TemplateView.as_view(template_name='debug.html')),

    url(r'^protoLib/', include('protoExt.urls')),

#   Use for production instalation and for load json configuration files
#     url(r'static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PPATH + '/static'}),
#     url(r'resources/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PPATH + '/static'}),
#     url(r'media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PPATH + '/static'}),

#   Generated files
    url(r'getFile/(?P<path>.*)$', 'protoExt.utils.downloadFile.getFile', {}),

#   Pour executer les tests avec Jasmine
    # url(r'^protoDiagram/', include('dbDesigner.urls')),
    # url(r'^extjs-tests', TemplateView.as_view(template_name='extjs-tests.html')),
    
]