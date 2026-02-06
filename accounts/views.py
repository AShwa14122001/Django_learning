from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User,Group
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

@login_required
def role_redirect(request):
    user = request.user

    if user.groups.filter(name="admin").exists():
        return redirect('/admin-dashboard/')

    elif user.groups.filter(name="manager").exists():
        return redirect('/manager-dashboard/')

    else:
        return redirect('/user-dashboard/')


def is_admin(user):
    return user.groups.filter(name="admin").exists()

def is_manager(user):
    return user.groups.filter(name="manager").exists()

@login_required
@user_passes_test
def create_user(request,role):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username = username,
            password = password
        )

        group = Group.objects.get(name=role)
        user.groups.add(group)

        return redirect('/admin-dashboard/')
    return render(request,"create_user.html",{"role": role})


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    admins = User.objects.filter(groups__name='admin')
    managers = User.objects.filter(groups__name='manager')
    users = User.objects.filter(groups__name='user')

    context = {
        "admin": admins,
        "manager": managers,
        "user": users,
    }

    return render(request, 'admin_dashboard.html', context)


@login_required
@user_passes_test(is_manager)
def manager_dashboard(request):
    return HttpResponse("Manager Dashboard")

@login_required
def user_dashboard(request):
    return HttpResponse("User Dashboard")

class createUserApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        if not request.user.group.filter(name='admin').exists():
            return Response(
                {"Error":"Only admin can create users"},
                    status = status.HTTP_403_FORBIDDEN)

        serializer = CreateUserSerializer(data=request.data)
        if serializer is valid():
            serializer.save()
            return response(
                {"message":"User Created Successfully"},
                status = status.HTTP_200_SUCCESS
            )
        return responses(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
