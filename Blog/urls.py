from django.urls import path
from . import views
app_name = "detail"
urlpatterns = [
    path('detail/<slug:slug>' , views.post_detail , name = "post" ),
    path('list' , views.PostListView.as_view() , name = "post_list"),
    path('category/<int:pk>' , views.category_detail , name = "category_detail"),
    path('search/' , views.search , name = "search_post"),
    path('contactus' , views.ContactUsView.as_view() , name = "Contact_Us"),
    path('like/<slug:slug>/<int:pk>' , views.like , name = "like"),
    path('aboutus' , views.aboutus , name = "aboutus"),
]