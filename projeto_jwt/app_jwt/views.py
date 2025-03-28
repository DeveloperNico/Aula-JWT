from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Username
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def registrar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    cpf = request.data.get('cpf')
    email = request.data.get('email')

    if not nome or not senha or not cpf or not email:
        Response({"Erro: ": "O campo nome, senha, cpf e email são obrigatórios!"}, status=status.HTTP_400_BAD_REQUEST)

    if Username.objects.filter(username=nome).exists():
        return Response({"Erro: ": "Usuário já existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Username.objects.create_user(
        username=nome,
        password=senha,
        telefone=telefone,
        email=email,
        cpf=cpf,
        endereco=endereco
    )

    return Response({"Mensagem: ": "O usuário foi cadastrado com sucesso"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')

    user = authenticate(username=nome, password=senha)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro: ': "Digite o usuário e senha corretos!"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"Mensagem: ": "OLÁ 2DS_MB15"}, status=status.HTTP_200_OK)