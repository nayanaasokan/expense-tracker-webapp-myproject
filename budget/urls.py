from django.urls import path
from budget import views

urlpatterns=[
    path("transactions/add/",views.TransactionCreateView.as_view(),name="transaction-add"),
    path("transactions/all/",views.TransactionListview.as_view(),name="transaction-list"),
    path("transactions/<int:pk>/change/",views.TransactionUpdateView.as_view(),name="transaction-edit"),
    path("transactions/<int:pk>/remove/",views.TransactionDeleteView.as_view(),name="transaction-delete"),
    path("transactions/<int:pk>/",views.TransactionDetailview.as_view(),name="transaction-detail"),
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.SignInView.as_view(),name="signin"),
    path("signout/",views.SignOutView.as_view(),name="signout")
]