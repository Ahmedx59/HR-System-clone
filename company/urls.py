from django.urls import path
from .views import branch_details , branches, branch_create , branch_edit


app_name = 'company'

# company/
urlpatterns = [
    path('', branches, name = "branches"),
    path('create-branch', branch_create, name="branch-create"),
    path('<int:branch_id>', branch_details, name="branchesDetails"),
    path('edit-branch/<int:id>', branch_edit, name="branch_edit"),


]