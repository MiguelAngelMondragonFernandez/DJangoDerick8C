#API_REST_CON DjangoRestFramework
#5 vistas todo en uno (2 GET, UPDATE,DELETE,POST)
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #Sobreescribir el metodo para la obtencion de permisos
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT','DELETE']:
            #Retornar la funcion que checa si tenemos sesion
            return [IsAuthenticated()]
        #Dar acceso a todos los metodos
        return []

#Clase adicional para obtener el par del token
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

