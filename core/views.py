from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')

def soma(request, num1, num2):
    return HttpResponse(f'<h1>A Soma de {num1} e {num2} é: {num1 + num2} </h1>')

def multiplicacao(request, num1, num2):
    return HttpResponse(f'<h1>A Multiplicação de {num1} e {num2} é: {num1 * num2}</h1>')

def divisao(request, num1, num2):
    return HttpResponse(f'<h1>A Divisão de {num1} e {num2} é: {num1 / num2}</h1>')

def subtracao(request, num1, num2):
    subtracao = num1 - num2
    return HttpResponse(f'<h1>A Subtração de {num1} e {num2} é: {subtracao}</h1>')
