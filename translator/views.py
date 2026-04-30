from django.shortcuts import render
from googletrans import Translator

translator = Translator()

def home(request):
    result = ""

    if request.method == "POST":
        text = request.POST.get("text")
        lang = request.POST.get("lang")

        # 🔥 FIX: validate input
        if text and lang:
            translated = translator.translate(text, dest=lang)
            result = translated.text
        else:
            result = "Please enter text"

    return render(request, "index.html", {"result": result})