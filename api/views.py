from django.http import JsonResponse

def api_root(request):
    """
    API root view showing available endpoints.
    """
    return JsonResponse({
        'status': 'ok',
        'endpoints': [
            '/api/users/',
            '/api/data/'
        ]
    })

def user_list(request):
    """
    API view for listing users.
    """
    # This would typically fetch data from a database
    users = [
        {'id': 1, 'username': 'user1'},
        {'id': 2, 'username': 'user2'}
    ]
    return JsonResponse({'users': users})

def data_list(request):
    """
    API view for listing data.
    """
    # This would typically fetch data from a database
    data = [
        {'id': 1, 'name': 'Item 1', 'value': 100},
        {'id': 2, 'name': 'Item 2', 'value': 200}
    ]
    return JsonResponse({'data': data})