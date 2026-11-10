from django.urls import path,include
from .static import views


urlpatterns = [
    path('', views.home, name='home'),
      path('task1/', views.home1, name='home'),
       path('task2/', views.home2, name='home'),
        path('task3/', views.home3, name='home'),
        path('task4/', views.home4, name='home'),
        path('task5/', views.home5, name='home'),
        path('task6/', views.home6, name='home'),
           path('task7/', views.home7, name='home'),
            path('task8/', views.home8, name='home'),
              path('task9/', views.home9, name='home'),
                path('task10/', views.home10, name='home'),
                 path('task11/', views.home11, name='home'),
                  path('task12/', views.home12, name='home'),
                    path('task13/', views.home13, name='home'),
                     path('task14/', views.home14, name='home'),
                     path('task15/', views.home15, name='home'),
                      path('task16/', views.home16, name='home'),
                      path('task17/', views.home17, name='home'),
                       path('task18/', views.home18, name='home'),
                       path('task19/', views.vasu19, name='home'),
                       path('successfull/', views.successfully, name='home'),
                       path('task20/', views.vasu20, name='home'),
                         path('',include('stdmng.urls')),
            
 
                       

]