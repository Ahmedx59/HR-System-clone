from django.urls import path
from .views import branchDetails , branches


app_name = 'company'

# company/
urlpatterns = [
    path('',branches, name = "branches"),
    path('<int:id>',branchDetails,name="branchesDetails"),

]