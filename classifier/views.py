import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from keras.applications import vgg16
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.python.keras.backend import set_session
from .models import Imgpath

def index(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
        urlf = file_url.replace('\\', '/')
        urlf = urlf[16:]
        image = load_img(file_url, target_size=(224, 224))
        numpy_array = img_to_array(image)
        image_batch = np.expand_dims(numpy_array, axis=0)
        processed_image = vgg16.preprocess_input(image_batch.copy())
        # count = Imgpath.get.object.all()
       
        # image2 = load_img(file_url, target_size=(224, 224))
        imgobject = Imgpath(image=file, imgpath=file_url)
        imgobject.save()

        with settings.GRAPH1.as_default():
            set_session(settings.SESS)
            predictions = settings.IMAGE_MODEL.predict(processed_image)

        label = decode_predictions(predictions, top=10)
        return render(request, "index.html", {"predictions": label, "image":urlf})

    else:
        return render(request, "index.html")
    
    return render(request, "index.html")