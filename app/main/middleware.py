from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# class AppendSlashMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if not request.path.endswith('/'):
#             return redirect(request.path + '/')
#
#
# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         login_url = reverse('user:login')
#         admin_url = reverse('admin:index')
#         public_urls = [reverse('main:about'), reverse('main:index'), reverse('users:logout')]  # Добавьте сюда общие страницы
#
#         # Проверка на аутентификацию пользователя
#         if not request.user.is_authenticated:
#             if request.path not in public_urls and request.path != login_url:
#                 return redirect('user:login')
#         else:
#             # Проверка на наличие объекта пользователя и атрибута 'company'
#             if request.user and hasattr(request.user, 'company'):
#                 company = request.user.company
#                 if company == 'dm':
#                     allowed_urls = [reverse('main:dm')] + public_urls
#                 elif company == 'cc_1':
#                     allowed_urls = [reverse('main:cc_1')] + public_urls
#                 elif company == 'cc_2':
#                     allowed_urls = [reverse('main:cc_2')] + public_urls
#                 elif company == 'og':
#                     allowed_urls = public_urls
#                 else:
#                     allowed_urls = public_urls
#
#                 # Проверка доступа к админ панели
#                 if company in ['cc_1', 'cc_2', 'dm']:
#                     allowed_urls.append(admin_url)
#                     if request.path.startswith(admin_url):
#                         return self.get_response(request)
#                 if request.path not in allowed_urls:
#                     return redirect('main:index')
#             else:
#                 return redirect('main:index')
#
#         response = self.get_response(request)
#         return response
