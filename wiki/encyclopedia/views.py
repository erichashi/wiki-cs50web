from django.shortcuts import render

from . import util
from random import choice

def check_entries(input):
    entries = util.list_entries()
    for entry in entries:
        if entry.lower() == input.lower():
            return True
    return False


def index(request):
    if request.method == "POST":
        input = request.POST["q"]
        #print('the input is: ' + input)
        entries = util.list_entries()
        results = []
        
        for entry in entries:
            #print('analysing entry '+entry)
            if entry.lower() == input.lower():
                content = util.get_entry(entry)
                return render(request, "encyclopedia/entrypage.html", {
                    "title": input.capitalize(),
                    "content": content
                })
            else:
                i=0
                for c in input.lower():
                    if c == entry.lower()[i]:
                        results.append(entry) #TODO c is only checkin gthe first letter
                    else:
                        break
                    i += 1

        return render(request, "encyclopedia/searchpage.html", {
            "input": input,
            "results": results
        })
        
    #if request.method == "GET":
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

def create_new(request):
    if request.method == "POST":
        title = request.POST["title"]
        #check if hte title is already in ency
        if(check_entries(title)):
            #print('There is a page with this title!!')
            return render(request, "encyclopedia/create.html", {
                "message": "Fail: there is already a page with this title."
            })
        #otherwise, save entry and go to entrys page
        content = request.POST["content"]
        util.save_entry(title, content)
        return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "content": content
        })

    return render(request, "encyclopedia/create.html")

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "content": content
        })
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def random(request):
    chosen = choice(util.list_entries())
    print(chosen)
    return render(request, "encyclopedia/entrypage.html", {
        "title": chosen.capitalize(),
        "content": util.get_entry(chosen)
    })

