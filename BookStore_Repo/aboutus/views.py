from django.shortcuts import render

# Team members data
team_members = [
    {
        'id': 1,
        'name': 'Sarah Johnson',
        'position': 'Founder & CEO',
        'bio': 'Sarah is passionate about books and community. With over 15 years in the publishing industry, she founded Book Store to bring the joy of reading to everyone.',
        'image': '/static/aboutus/sarah.jpg'
    },
    {
        'id': 2,
        'name': 'Michael Chen',
        'position': 'Head of Content',
        'bio': 'Michael curates our collection with expertise in literature and reader preferences. His goal is to ensure we have something for every book lover.',
        'image': '/static/aboutus/michael.jpg'
    },
    {
        'id': 3,
        'name': 'Emily Rodriguez',
        'position': 'Customer Experience Manager',
        'bio': 'Emily ensures every customer has an exceptional experience. She believes customer satisfaction is at the heart of everything we do.',
        'image': '/static/aboutus/emily.jpg'
    },
    {
        'id': 4,
        'name': 'David Park',
        'position': 'Operations Director',
        'bio': 'David oversees all operational aspects, ensuring timely delivery and inventory management. He keeps our business running smoothly.',
        'image': '/static/aboutus/david.jpg'
    },
]


def index(request):
    return render(request, 'aboutus/index.html', {'team_members': team_members})
