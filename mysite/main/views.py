from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .forms import TextForm
from rest_framework import views


class MainApiView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/index.html'

    def get(self, request):
        return Response()

class FileApiView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/text.html'

    def get(self, request):
        form = TextForm()
        context = {
            'form': form,
        }
        return Response(context)

    def post(self, request):
        return Response()












# def index(request):
#     return render(request, 'main/index.html')
#
#
# def text(request):
#     error = ''
#     if request.method == 'POST':
#         form = TextForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data.get("text"))
#         else:
#             error = 'Ошибка отправки данных'
#
#     form = TextForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/text.html', context)
