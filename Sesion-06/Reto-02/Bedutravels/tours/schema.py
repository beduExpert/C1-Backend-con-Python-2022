import graphene

from graphene_django.types import DjangoObjectType
from .models import User, Zona, Tour, Opinion, Salida


class UserType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo User """
    class Meta:
        # Se relaciona con el origen de la data en models.User
        model = User

class ZonaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Zona """
    class Meta:
        # Se relaciona con el origen de la data en models.Zona
        model = Zona

class TourType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Tour """
    class Meta:
        # Se relaciona con el origen de la data en models.Tour
        model = Tour

class SalidaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Salida """
    class Meta:
        # Se relaciona con el origen de la data en models.Salida
        model = Salida


class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_users = graphene.List(UserType)  # allUsers
    all_zonas = graphene.List(ZonaType)  # allZonas
    all_tours = graphene.List(TourType)  # allTours
    all_salidas = graphene.List(SalidaType)  # allSalidas

    # Se define las respuestas para cada campo definido
    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros
        return User.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Zona.objects.all()

    def resolve_all_tours(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Tour.objects.all()

    def resolve_all_salidas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Salida.objects.all()

# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query)
