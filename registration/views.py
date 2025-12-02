from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserRegistration, Expense
from .serializer import RegistrationSerializer, ExpenseSerializer

# --- API: GET ONLY (Rancis) ---

@api_view(['GET'])
def expense_list(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id')
        if user_id:
            expenses = Expense.objects.filter(user=user_id).order_by('-date')
        else:
            expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)