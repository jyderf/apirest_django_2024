from django.urls import path, include
from rest_framework import routers
from tareas_app import views

router = routers.DefaultRouter()
router.register(r'personas', views.PersonaViewSet)
router.register(r'proyectos', views.ProyectoViewSet)
router.register(r'tareas', views.TareaViewSet)
router.register(r'tipo_documentos', views.Tipo_DocumentoViewSet)
router.register(r'estado_tareas', views.Estado_TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
