from django.conf.urls import url, include
from rest_framework import routers
from views import .

router = routers.DefaultRouter()
router.register(r'alunos', views.AlunosViewSet)
router.register(r'turmas', views.TurmasViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]