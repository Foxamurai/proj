from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .forms import TextForm, FileForm, AudioForm
from rest_framework import views
from .utils.common import parse_text


class MainAPIView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/index.html'

    def get(self, request):
        return Response()


class TextAPIView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/text.html'

    def get(self, request):
        return Response({'form': TextForm()})

    def post(self, request):
        data = request.data['text'].strip()
        return Response(
            {'data': parse_text(data)}
        )


class FileAPIView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/file.html'

    def get(self, request):
        return Response({'form': FileForm()})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file'].read().decode().strip()
            return Response(
                {'data': parse_text(data)}
            )
        return Response(
            {'error_message': 'Не валидный файл'}
        )


class AudioAPIView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/audio.html'

    def get(self, request):
        return Response({'form': AudioForm()})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file'].read().decode().strip()
            return Response(
                {'data': parse_text(data)}  # parse audio
            )
        return Response(
            {'error_message': 'Не валидный файл'}
        )