from django.shortcuts import render

class RedirectToComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #if not request.path.startswith('/admin/') and not request.path.startswith('/api/'):
        if not request.path.startswith('/admin/'):
            return render(request, 'coming_soon.html')
                
        response = self.get_response(request)
        return response