from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Category
from .forms import TodoForm, CategoryForm


def index(request):
    todos = Todo.objects.all()
    categories = Category.objects.all()
    context = {'todos': todos, 'categories': categories}

    return render(request, 'index.html', context)

def category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/')

    form = CategoryForm()
    return render(request, 'category.html', {'form': form})


def todo(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/')

    form = TodoForm()
    return render(request, 'todo.html', {'form': form})



# def todo_edit(request, todo_id):
#     #profile = get_object_or_404(User, username=username)
#     todo_post = get_object_or_404(Todo, id=todo_id)
#
#
#     form = TodoForm(request.POST or None, files=request.FILES or None, instance=todo)
#     if form.is_valid():
#         edit_todo = form.save(commit=False)
#
#         edit_todo.id = post.id
#         edit_dodo.pub_date = post.pub_date
#         edit_post.save()
#         return redirect("index", post_id=post_id)

