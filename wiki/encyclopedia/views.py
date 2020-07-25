from django.shortcuts import render

from . import util


def index(request):
 

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, title):
    content = util.get_entry(title)
    if content == None:    
        return render(request, "encyclopedia/pagenotfound.html")
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "title": title.capitalize(),
            "content": content
        })

