from django.shortcuts import render


def index(request):
    user = request.user
    title = 'Strona glowna'
    ctx = {'title': title,
           'user': user}
    return render(request, 'main_page.html', ctx)
