from django.shortcuts import render

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


