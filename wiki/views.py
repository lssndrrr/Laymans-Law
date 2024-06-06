from django.shortcuts import render
from .models import Law, Summarizations, Translations
from django.http import HttpResponse
import json

# Create your views here.
def lawList(request):
    laws = Law.objects.all()
    return render(request, "wiki/laborlaws.html", {"laws": laws})

def prelimW(request):
    if request.method == "GET":
        return render(request, "wiki/wiki-prelim.html")
    return render(request, "wiki/wiki-prelim.html")

def Wiki(request):
    context = {}
    if request.method == "GET":
        laws = Law.objects.all()
        context['laws'] = laws

        summaries = Summarizations.objects.all()
        summaries_dict = {summary.summary_id: summary.Summary for summary in summaries}
        context['summaries'] = json.dumps(summaries_dict)

        translations = Translations.objects.all()
        translations_dict = {translation.translation_id: translation.Bisaya_Translation for translation in translations}
        context['translations'] = json.dumps(translations_dict)

        return render(request, "wiki/wiki-prelim.html", context)

