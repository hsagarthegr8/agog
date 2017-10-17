import os
from django.conf import settings
from pathlib import Path


def get_image_path(instance, filename):
    user_id = instance.user.id
    print(settings.MEDIA_ROOT)
    path = os.path.join(settings.MEDIA_ROOT,'photos',str(user_id))
    ensure_dir(path)
    file = str(len(os.listdir(path)))
    file_ext = Path(filename).suffix
    filename = file + file_ext
    return os.path.join('photos', str(user_id), filename)


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)