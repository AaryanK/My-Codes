from django.contrib import admin
from django.urls import path,include
from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.home ,name="home"),
    path("login/",views.login ,name="login"),
    # # path("nextlogin/",views.nextlogin ,name="nextlogin"),
    path("register/",views.register ,name="register"),
    # path("logout/",views.logout ,name="logout"),
    # # path("testfortype/",views.test,name="test"),
    # path("fdkdagdgdga/",views.errorpage,name="404"),
    # path("course=<str:name>/",views.course,name="course"),
    # path("enroll=<str:name>/",views.enroll,name="enroll"),
    # path("customize=<str:name>/",views.customize_course_desc,name="ccustomize"),
    # path('reset/<str:uid>',views.verify,name="reset_user_password"),
    # path('reset/<str:uid>/<str:token>/',views.final_change,name="reset_change_password"),
    # path("dashboard/",views.dashboard,name="dashboard"),
    # path("dashboard/courses_enrolled/",views.dashboard_courses,name="user_courses"),
    # path("dashboard/user_profile/",views.dashboard_user_profile,name="user_profile"),
    # path("reset_password/",views.reset_password,name="reset_password"),
    # path("dashboard/pricing",views.pricing,name="pricing"),
    # path("browse_courses/",views.browse_course,name="browse_courses"),
    # path('dashboard/change-password/',views.change_password,name='change_password'),
    # path('dashboard/add_course',views.add_course,name="add_course"),   
    # path('dashboard/settings',views.dashboard_settings,name="user_settings"),
    # path('dashboard/performance',views.dashboard_performance,name="user_performance"),
    # path('learn=<str:name>',views.learn,name="learn"),
    # path('maintainance/',views.maintainance,name="503") 

    

    # path("coursechange=<str:name>/",views.course_change,name="coursechange")
]

 # path('password-reset/',auth_views.PasswordResetView.as_view(template_name='templates/password/password_reset.html'),name='password_reset'),
 #    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='templates/password/password_reset_done.html'),name='password_reset_done'),
 #    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='templates/password/password_reset_confirm.html'),name='password_reset_confirm'),
 #    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='templates/password/password_reset_complete.html'),name='password_reset_complete')