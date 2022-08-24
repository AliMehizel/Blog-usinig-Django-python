from django.urls import path
from .views import BaseView,LoginView,HomeView,SignupView,LogoutView,PostCreate
from .views import PostUpdate,PostDelete,PostDetail
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),    
    path('signup/', SignupView.as_view(), name='signup'),  
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('postcreate/', PostCreate.as_view(), name='postcreate'), 
    path('postupdate/<int:pk>', PostUpdate.as_view(), name='postupdate'), 
    path('postdelete/<int:pk>', PostDelete.as_view(), name='postdelete'), 
    path('postdetail/<int:pk>', PostDetail, name='postdetail'), 
]
