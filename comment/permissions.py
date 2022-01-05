'''
Date                : 2021-12-11 20:47:21
LastEditors         : 王少帅
LastEditTime        : 2021-12-11 22:31:50
FilePath            : /drf_vue_blog/comment/permissions.py
'''
from rest_framework.permissions import BasePermission, SAFE_METHODS

# class  IsOwnerOrReadOnly(BasePermission):
#     message = 'You must be the owner to update.'
    
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True

#         return request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True

#         return obj.author == request.user
class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner to update.'

    def safe_methods_or_owner(self, request, func):
        if request.method in SAFE_METHODS:
            return True
        return func()

    def has_permission(self, request, view):
        return self.safe_methods_or_owner(
            request,
            lambda: request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return self.safe_methods_or_owner(
            request,
            lambda: obj.author == request.user
        )