from django.shortcuts import render, redirect
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .collage import auth_url, create_collage
from .forms import TokenForm, ParamForm
from spotipy.oauth2 import SpotifyOauthError
from django.utils.http import urlsafe_base64_encode
import base64
import cStringIO
from PIL import Image
from io import BytesIO

def index(request):
    if request.method == 'POST':
        form = ParamForm(request.POST)
        if form.is_valid():
            request.session['dim'] = int(form.cleaned_data['grid_size'])
            request.session['time_range'] = form.cleaned_data['time_range']

            return redirect(auth_url())

    return render(request, 'generator/index.html', {'form': ParamForm()})

def generate_image(request):
    form = TokenForm(request.GET)

    if form.is_valid():
        token = form.cleaned_data['code']

    try:
        collage = create_collage(token,
            request.session['dim'],
            request.session['time_range'])

        buffer = cStringIO.StringIO()
        collage.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue())

        request.session['img_str'] = img_str

    except SpotifyOauthError:
        return redirect('/')

    return redirect('/')

def get_image(request):

    try:
        collage = Image.open(BytesIO(base64.b64decode(request.session['img_str'])))
    except KeyError:
        collage = Image.new('RGB', (300, 300))

    response = HttpResponse(content_type="image/png")
    collage.save(response, "PNG")
    return response
