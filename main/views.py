from django.shortcuts import render

def show_main(request):
    context = {
        'makanan' : 'nasi kucing',
        'minuman': 'soda gembira',
        'snack': 'sate cihuahua'
    }

    return render(request, "main.html", context)
