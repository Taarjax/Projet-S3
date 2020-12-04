from rest_framework import generics
from rest_framework.views import APIView
from shaker.models import *
from .serializers import *
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from .permissions import *


class CocktailList(generics.ListCreateAPIView):
    """Tous les cocktails
    """
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


class CocktailDetail(generics.RetrieveDestroyAPIView):
    """Détail d'un cocktail spécifique
    """
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


class ContenirList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer


class FavoriList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Favori.objects.all()
    serializer_class = FavoriSerializer


class IngredientList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class NoterList(generics.ListCreateAPIView):
    """Toutes les notes de tous les cocktails
    """
    permission_classes = [NoterPermission]
    queryset = Noter.objects.all()
    serializer_class = NoterSerializer


class PreferenceList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class PreferenceListByMember(generics.ListCreateAPIView):
    permission_classes = [PreferencePermission]
    serializer_class = PreferenceSerializer

    def get_queryset(self):
        return Preference.objects.filter(idmembre=self.kwargs['idmembre'])

class StockerList(generics.ListCreateAPIView):
    permission_classes = [StockerPermission]
    queryset = Stocker.objects.all()
    serializer_class = StockerSerializer


class ProposerList(generics.ListCreateAPIView):
    """[summary]
    Liste de tous les cocktails proposé par des hôtes
    Args:
        generics ([type]): [description]
    """
    permission_classes = [ProposerPermission]
    queryset = Propose.objects.all()
    serializer_class = ProposerSerializer


class ProposerListByMember(generics.ListCreateAPIView):
    permission_classes = [ProposerPermission]
    serializer_class = ProposerSerializer

    def get_queryset(self):
        return Propose.objects.filter(idmembre=self.kwargs['idmembre'])

    '''def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'POST':
            serializer_class = ProposerSerializerWithoutMembre

        return serializer_class'''

class ProposeDetail(generics.RetrieveDestroyAPIView):
    """[summary]
    Uniquement les cocktails que nous proposons en tant qu'hôte
    Args:
        generics ([type]): [description]
    """
    permission_classes = [ProposerDetailPermission]
    queryset = Propose.objects.all()
    serializer_class = ProposerSerializer
