
from django.shortcuts import render, redirect
from groq import Groq
from .models import Chat
# Create your views here.


def Blog_details(request):
    return render(request,"blog-details.html")

def Blog(request):
    return render(request, "blog.html")

client = Groq(
    api_key= "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",
)


def chatbot_response(request):
    ch = Chat.objects.all()
    if request.POST:
        chat_text = request.POST.get("chat_bot")
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": chat_text+"give answer in summary",
            }
        ],
        model="llama-3.3-70b-versatile",stream=False,) 
                      
        chat=chat_completion.choices[0].message.content
        print(chat)
        c = Chat.objects.create(
            user_id = request.user,
            send=chat_text,
            recive= chat,
        )
        return redirect("chatbot_response")
    return render(request, 'chat.html',{"ch":ch})



from django.shortcuts import render
from product.models import Product_image
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image as keras_image
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import os

# Load the ResNet model
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Extract features from in-memory uploaded image
def extract_features(uploaded_file):
    img = Image.open(uploaded_file)
    img = img.convert("RGB")
    img = img.resize((224, 224))

    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    features = model.predict(img_array)
    return features.flatten()

# Find similar product vectors
def find_similar(uploaded_vector, top_k=5):
    similarities = []
    for filename in os.listdir("features/"):
        product_id = filename.split(".")[0]
        product_vector = np.load(f"features/{filename}")
        sim = cosine_similarity([uploaded_vector], [product_vector])[0][0]
        similarities.append((product_id, sim))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [int(product_id) for product_id, sim in similarities[:top_k]]

# Main view
def image_search_view(request):
    products = None
    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_file = request.FILES['image']
        features = extract_features(uploaded_file)
        similar_ids = find_similar(features)
        products = Product_image.objects.filter(id__in=similar_ids)

    return render(request, 'image_search.html', {'products': products})




