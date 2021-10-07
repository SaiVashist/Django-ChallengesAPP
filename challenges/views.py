from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january" : "january challenge",
    "february" : "february challenge",
    "march" : "march  challenge",
    "april" : "april challenge",
    "may" : "may challenge",
    "june" : "june challenge",
    "july" : "july challenge",
    "august" : "august challenge",
    "september": "september challenge",
    "october" : "october challenge",
    "november" : "november challenge",
    "december" : "december challenge"
}



def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenges" , args=[month])
        list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</li>"
        #"<l1><href"...."">janua it will be a long string with list items
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
        
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request , month):

    try:

        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
         return HttpResponseNotFound("This month is not supported")

    
