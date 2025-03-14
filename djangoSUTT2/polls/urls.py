from django.urls import include,path #url patterns are used for us to be able to handle multiple requests of similar type by passing different parameters to the function by extracting the parameter from the user #look notes to see example
from . import views #. here means that we will import the directory from the current package only which is polls here
from debug_toolbar.toolbar import debug_toolbar_urls
app_name="polls"
urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),#" " means url will match the base URL of the polls app #views.index tells it which function to run when this url is called #name=index here defines a name to that URL pattern
    path ("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),#whatever stays in <> is what we capture from the url and the rest is URL pattern for matching it
] 