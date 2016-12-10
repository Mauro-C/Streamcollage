import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
import urllib
import cStringIO
from collections import OrderedDict
from django.conf import settings

sp_auth = SpotifyOAuth(
    settings.SPOTIFY_CLIENT_ID,
    settings.SPOTIFY_CLIENT_SECRET,
    settings.SPOTIFY_REDIRECT_URI,
    scope='user-top-read')

def auth_url():
    return sp_auth.get_authorize_url()

def create_collage(code, dim, time_range):

    token = sp_auth.get_access_token(code)

    if token:
        MAX_QUERY = 50
        sp = spotipy.Spotify(auth=token['access_token'])
        result=sp.current_user_top_tracks(
            limit=MAX_QUERY, offset=0, time_range=time_range)

        STEP = 300
        if dim == 5:
            STEP = 240
        WIDTH = STEP * dim
        HEIGHT = WIDTH

        url_list = get_top_albums(result['items']).values()
        collage = get_collage(url_list, HEIGHT, WIDTH, STEP)

        return collage

    else:
        return None

def get_collage(url_list, HEIGHT, WIDTH, STEP):
    new_im = Image.new('RGB', (HEIGHT, WIDTH))
    index = 0
    for i in xrange(0, HEIGHT, STEP):
        for j in xrange(0, HEIGHT, STEP):
            if index < len(url_list):
                cur_url = url_list[index]
                im = pil_img_gen(cur_url, STEP)
                new_im.paste(im, (j, i))
                index += 1

    return new_im

def get_top_albums(items):
    res = OrderedDict()
    for item in items:
        album_name = item['album']['name']
        url = item['album']['images'][1]['url']
        if album_name not in res:
            res[album_name] = url

    return res

def pil_img_gen(URL, STEP):
    file = cStringIO.StringIO(urllib.urlopen(URL).read())
    img = Image.open(file)
    if STEP == 240:
        img.thumbnail((240, 240))

    return img
