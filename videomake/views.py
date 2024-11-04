from django.shortcuts import render
from videomake.script.video import running_string
from .models import Lines
from django.http import FileResponse, HttpResponse
import os


def main(request):
    lines = Lines.objects.all()
    context={'lines': lines}
    return render(request, 'videomake/main.html', context)


# Create your views here.
def adding(request, word):
    p = Lines.objects.create(name=word)
    lines = Lines.objects.all()
    context = {'lines': lines}
    running_string(word)

    file_path=os.path.dirname(os.path.abspath(__file__))+"\\script\\output.mp4"
    file_name = os.path.basename(file_path)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read())
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        response['Refresh'] = "0;url=/"
        return response