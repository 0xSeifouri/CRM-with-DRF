from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from rest_framework.permissions import IsAdminUser
from rest_framework import generics

from .models import CustomerData
from .serializers import CustomerDataSerializer
from .forms import AddRecordForm


def home(request):
    customer_data = CustomerData.objects.all().order_by('-id')
    serialize = CustomerDataSerializer(customer_data, many=True)
    return render(request, 'crm/home.html', {'serialize': serialize.data})


def retrieve_data(request, pk):
    customer_data = get_object_or_404(CustomerData, pk=pk)
    serialize = CustomerDataSerializer(customer_data)
    return render(request, 'crm/detail.html', {'details': serialize.data})


def create_data(request):
    form = AddRecordForm(request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            data = form.cleaned_data
            serializer = CustomerDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, 'Data Successfully Added')
                return redirect('home')
        return render(request, 'crm/insert.html')
    else:
        messages.success(request, 'You Should be Login')
        return redirect('login')


def update_data(request, pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(CustomerData, pk=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Successfully Updated')
            return redirect('home')
        return render(request, 'crm/update.html', {'form': form})
    else:
        messages.success(request, 'You Should be Login')
        return redirect('login')


def delete_data(request, pk):
    if request.user.is_authenticated:
        delete_record = CustomerData.objects.get(pk=pk)
        delete_record.delete()
        messages.success(request, 'Data Successfully Deleted')
        return redirect('home')
    else:
        messages.success(request, 'You Should be Login')
        return redirect('login')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Successfully Logged In!')
            return redirect('home')
        messages.success(request, 'Please Enter Valid data')
    return render(request, 'crm/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You Successfully Logged Out!')
    return redirect('home')


# api Response
class ShowAll(generics.ListAPIView):
    queryset = CustomerData.objects.all().order_by('-id')
    serializer_class = CustomerDataSerializer


class Create(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomerData
    serializer_class = CustomerDataSerializer


class Retrieve(generics.RetrieveAPIView):
    queryset = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer


class Update(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer


class Destroy(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer

