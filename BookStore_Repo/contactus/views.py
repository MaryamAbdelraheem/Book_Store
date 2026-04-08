from django.shortcuts import render, redirect

# Contact form messages (stored in memory for demo)
messages = []


def index(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Validate
        if name and email and subject and message:
            # Store message
            messages.append({
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })
            return redirect('contactus_success')
    
    return render(request, 'contactus/index.html')


def success(request):
    return render(request, 'contactus/success.html')
