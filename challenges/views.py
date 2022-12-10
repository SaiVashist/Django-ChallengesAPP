from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
monthly_cha = {
    "january": "This is January month",
    "february": "This is February",
    "march": "This is march",
    "april": "This is april",
    "may": "This is May",
    "june": "This is June",
    "july": "This is july",
    "august": "this is Aug",
    "sep": "This is Sep",
    "Oct": "This is OCT",
    "Nov": "This is Nov",
    "Dec": None
}


def index(request):
    list_items = ""
    months = list(monthly_cha.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_cha.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!!")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):

    try:
        challenge_text = monthly_cha[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, "month": month
        })
    except:
        raise Http404()
