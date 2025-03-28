from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Username

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

