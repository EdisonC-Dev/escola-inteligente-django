import os
import uuid

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from vercel import blob

from .forms import OcorrenciaForm, EditarOcorrenciaForm
from .models import Ocorrencia


def enviar_foto_para_blob(foto):
    """
    Envia uma imagem para o Vercel Blob
    e retorna a URL pública gerada.
    """

    if not foto:
        return None

    extensao = os.path.splitext(foto.name)[1].lower()

    nome_arquivo = f"ocorrencias/{uuid.uuid4()}{extensao}"

    resultado = blob.put(
        nome_arquivo,
        foto.read(),
        access="public",
        content_type=foto.content_type,
        add_random_suffix=False,
    )

    return resultado.url


# PÁGINA INICIAL
def inicio(request):
    return render(request, 'ocorrencias/inicio.html')


# REGISTRAR NOVA OCORRÊNCIA - PÚBLICO
def criar_ocorrencia(request):

    if request.method == 'POST':

        form = OcorrenciaForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            ocorrencia = form.save(commit=False)

            foto = form.cleaned_data.get('foto_upload')

            if foto:
                ocorrencia.foto = enviar_foto_para_blob(foto)

            ocorrencia.save()

            messages.success(
                request,
                'Ocorrência registrada com sucesso!'
            )

            return redirect('sucesso')

    else:
        form = OcorrenciaForm()

    return render(
        request,
        'ocorrencias/criar_ocorrencia.html',
        {
            'form': form
        }
    )


# PÁGINA DE SUCESSO
def sucesso(request):

    return render(
        request,
        'ocorrencias/sucesso.html'
    )


# ACOMPANHAMENTO PÚBLICO
def acompanhar_ocorrencias(request):

    ocorrencias = Ocorrencia.objects.all().order_by(
        '-data_criacao'
    )

    return render(
        request,
        'ocorrencias/acompanhar_ocorrencias.html',
        {
            'ocorrencias': ocorrencias
        }
    )


# PAINEL ADMINISTRATIVO
@staff_member_required(login_url='login')
def listar_ocorrencias(request):

    pesquisa = request.GET.get('pesquisa', '')
    status = request.GET.get('status', '')
    categoria = request.GET.get('categoria', '')
    prioridade = request.GET.get('prioridade', '')

    ocorrencias = Ocorrencia.objects.all()

    if pesquisa:
        ocorrencias = ocorrencias.filter(
            local__icontains=pesquisa
        )

    if status:
        ocorrencias = ocorrencias.filter(
            status=status
        )

    if categoria:
        ocorrencias = ocorrencias.filter(
            categoria=categoria
        )

    if prioridade:
        ocorrencias = ocorrencias.filter(
            prioridade=prioridade
        )

    ocorrencias = ocorrencias.order_by(
        '-data_criacao'
    )

    return render(
        request,
        'ocorrencias/listar_ocorrencias.html',
        {
            'ocorrencias': ocorrencias,
            'pesquisa': pesquisa,
            'status_selecionado': status,
            'categoria_selecionada': categoria,
            'prioridade_selecionada': prioridade,
        }
    )


# EDITAR OCORRÊNCIA - SOMENTE ADMIN
@staff_member_required(login_url='login')
def editar_ocorrencia(request, id):

    ocorrencia = Ocorrencia.objects.get(
        id=id
    )

    if request.method == 'POST':

        form = EditarOcorrenciaForm(
            request.POST,
            request.FILES,
            instance=ocorrencia
        )

        if form.is_valid():

            ocorrencia = form.save(commit=False)

            nova_foto = form.cleaned_data.get('foto_upload')

            if nova_foto:
                ocorrencia.foto = enviar_foto_para_blob(
                    nova_foto
                )

            ocorrencia.save()

            messages.success(
                request,
                'Ocorrência atualizada com sucesso!'
            )

            return redirect(
                'listar_ocorrencias'
            )

    else:

        form = EditarOcorrenciaForm(
            instance=ocorrencia
        )

    return render(
        request,
        'ocorrencias/editar_ocorrencia.html',
        {
            'form': form,
            'ocorrencia': ocorrencia
        }
    )


# EXCLUIR OCORRÊNCIA - SOMENTE ADMIN
@staff_member_required(login_url='login')
def excluir_ocorrencia(request, id):

    ocorrencia = Ocorrencia.objects.get(
        id=id
    )

    if request.method == 'POST':

        ocorrencia.delete()

        messages.success(
            request,
            'Ocorrência excluída com sucesso!'
        )

        return redirect(
            'listar_ocorrencias'
        )

    return render(
        request,
        'ocorrencias/confirmar_exclusao.html',
        {
            'ocorrencia': ocorrencia
        }
    )