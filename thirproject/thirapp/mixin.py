# from django.core.exceptions import PermissionDenied
# from django.http import JsonResponse
# from rest_framework import status
#
#
# class GroupRequiredMixin(object):
#     group_required = [u'manager', u'user']
#
#     def dispatch(self, request, *args, **kwargs):
#
#         if not request.user.is_authenticated:
#             raise PermissionDenied
#         group_name = []
#         for group in request.user.groups.all():
#             group_name.append(group.name)
#         if len(group_name) <= 0:
#             raise PermissionDenied
#         elif request.method != "GET":
#             if 'manager' not in group_name:
#                 return JsonResponse(data={"error": "you dont have a permission"}, status=status.HTTP_403_FORBIDDEN)
#             else:
#                 return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
#         else:
#             return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
