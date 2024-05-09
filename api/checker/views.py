import errno
import stat

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .yolo_detector import Detector
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import os
from django.conf import settings
import uuid
import shutil



yolo = Detector()


def save_all_images(files, save_path):
    for file in files:
        file_path = os.path.join(save_path, file.name)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)


def delete_all_images(files):
    for file in files:
        default_storage.delete(file.name)





def generatefolder():
    folder_name = str(uuid.uuid4())
    url = os.path.join(settings.BASE_DIR, 'media', folder_name)
    os.mkdir(url)
    return url


def delete_all_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)




@api_view(['POST'])
@csrf_exempt
def single_image_prediction(request):
    url = generatefolder()

    files = request.FILES.getlist('image')
    print(files)
    save_all_images(files, url)
    res = yolo.single_image_prediction(url)
    delete_all_folder(url)
    return Response(res)


