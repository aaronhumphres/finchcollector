from django.shortcuts import render


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


