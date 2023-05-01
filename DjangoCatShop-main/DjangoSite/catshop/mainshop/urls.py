
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.main_page, name = "home"),
    path("create",views.create, name = "create"),
    path("<int:pk>", views.CatsDetail.as_view(), name="cats-detail"),
    path("<int:pk>/update", views.CatsUpdate.as_view(), name="cats-update"),
    path("<int:pk>/delete", views.CatsDelete.as_view(), name="cats-delete")
    #path("<int:pk>", admin.site.urls),
]
