from django.shortcuts import render
from .models import Finch


#temp finches for templates
finches = [
  {'name': 'Owl Bait', 'species': 'House Finch', 'description': 'loud, very loud', 'age': 3},
  {'name': 'Chihuaha', 'breed': 'Desert Finch', 'description': 'thinks he is an eagle', 'age': 2},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

#about route
def about(request):
  return render(request, 'about.html')

#index route for finches
def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {'finches': finches })

# detail route for finches
# finch_id is defined, expecting an integer, in our url
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    return render(request, 'finches/detail.html', { 'finch': finch })


