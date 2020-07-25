from django.shortcuts import render

from . import util


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
        
        


        return render(request, "encyclopedia/searchpage.html", {
            "input": input,
            "results": []
    
        })


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

