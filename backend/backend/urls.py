"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movies.views import PrivateGraphQLView
from graphene_django.views import GraphQLView

import backend.views as views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin', admin.site.urls),
    # prod login-required
    path('graphql', PrivateGraphQLView.as_view(graphiql=True)),
    # dev
    path('dev/graphql', GraphQLView.as_view(graphiql=True)),
]
