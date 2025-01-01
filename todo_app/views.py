from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo


# Create your views here.
def todo_list(
    request,
):  # request is parameter. Can write any other name but 'request' is in practice
    todos = Todo.objects.all()
    return render(
        request,
        "todo_list.html",
        {"todos": todos},
    )


def todo_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")
    return render(request, "todo_create.html")


# pk = primary Key => uniquely identify
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponseRedirect("/")


def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST["title"]
        todo.title = title
        todo.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "todo_update.html", {"todo": todo})
