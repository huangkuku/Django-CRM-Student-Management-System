from django.urls import path
from . import views 

urlpatterns = [
    path('classmate/', views.index, name='index'),
    path('classmate/<int:id>', views.view_classmate, name='view_classmate'),    
    path('classmate/add_classmate', views.add_classmate, name='add_classmate'),
    path('classmate/edit_classmate/<int:id>', views.edit_classmate, name='edit_classmate'),
    path('classmate/delete_it/<int:id>', views.delete_it, name='delete_it'),
    path('classmate/all_classmates', views.all_classmates, name='all_classmates'),
    path('classmate/dashboard_english_score_avg', views.dashboard_english_score_avg, name='dashboard_english_score_avg'),
    path('classmate/dashboard_math_score_avg', views.dashboard_math_score_avg, name='dashboard_math_score_avg'),
    path('classmate/dashboard_chinese_score_avg', views.dashboard_chinese_score_avg, name='dashboard_chinese_score_avg'),
    path('classmate/dashboard_eachStudentAvg', views.dashboard_eachStudentAvg, name='dashboard_eachStudentAvg'),
    
]