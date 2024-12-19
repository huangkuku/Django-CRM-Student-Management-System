from django.shortcuts import render, redirect
from .models import Classmate
from .form import ClassmateForm
from django.db.models import Avg
from django.db.models import F, FloatField
import plotly.express as px

# Create your views here.
def index(request):
    classmates = Classmate.objects.all()
    return render(request,'class/index.html',{'classmates': classmates})

def view_classmate(request,id):
    classmates = Classmate.objects.get(pk=id)
    return redirect('index')

# redirect()​，這個方法算是HttpResponseRedirect()和Reverse()的合體。重新定址(進入時就會自動幫你轉到特定頁面。)
def all_classmates(request):
    classmates = Classmate.objects.all()
    return render(request,'class/all_classmates.html',{'classmates': classmates})

def add_classmate(request):
    form = ClassmateForm(request.POST)
    if request.method == 'POST':
         # has post data
        if form.is_valid():
            add_it = form.save()
            return redirect('index')
    else:
        form = ClassmateForm()
        return render(request, 'class/add_classmate.html', {
            'form': ClassmateForm()
        })
        
def edit_classmate(request, id):
    if request.method == 'POST':
        student = Classmate.objects.get(pk=id)
        form = ClassmateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        student = Classmate.objects.get(pk=id)
        form = ClassmateForm(instance=student)
    return render(request, 'class/edit_classmate.html', {
        'form': form
    })

def delete_it(request, id):
    if request.method == 'POST':
        student = Classmate.objects.get(pk=id)
        student.delete()
    return redirect('index')

def dashboard_english_score_avg(request):
    target = 'english_score' # 'math_score' 'chinese_score' 'english_score'
    divid_target = 'field_of_study' # 'field_of_study' 'grade'
    score_avg=Classmate.objects.values(divid_target).annotate(avg=Avg(target))
    # 'field_of_study' : 國小、國中
    x = score_avg.values_list(divid_target, flat=True)
    y = score_avg.values_list('avg', flat=True)
    text = [f'{avg:.0f}' for avg in y]
    fig = px.bar(x=x, y=y, text=text, labels={x:divid_target, y:'avg'})
    fig.update_layout(title_text='English Score Average By Field of Study',
                          yaxis_range=[0,100])
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    chart = fig.to_html()
    return render(request, 'class/scoreAvg.html', {'chart':chart})

def dashboard_math_score_avg(request):
    target = 'math_score' # 'math_score' 'chinese_score' 'english_score'
    score_avg=Classmate.objects.values('field_of_study').annotate(avg=Avg(target))
    # 'field_of_study' : 國小、國中
    x = score_avg.values_list('field_of_study', flat=True)
    y = score_avg.values_list('avg', flat=True)
    text = [f'{avg:.0f}' for avg in y]
    fig = px.bar(x=x, y=y, text=text, labels={x:'field_of_study', y:'avg'})
    fig.update_layout(title_text='Math Score Average By Field of Study',
                          yaxis_range=[0,100])
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    math_chart = fig.to_html()
    return render(request, 'class/scoreAvg.html', {'math_chart':math_chart})

def dashboard_chinese_score_avg(request):
    target = 'chinese_score' # 'math_score' 'chinese_score' 'english_score'
    score_avg=Classmate.objects.values('field_of_study').annotate(avg=Avg(target))
    # 'field_of_study' : 國小、國中
    x = score_avg.values_list('field_of_study', flat=True)
    y = score_avg.values_list('avg', flat=True)
    text = [f'{avg:.0f}' for avg in y]
    fig = px.bar(x=x, y=y, text=text, labels={x:'field_of_study', y:'avg'})
    fig.update_layout(title_text='Chinese Score Average By Field of Study',
                          yaxis_range=[0,100])
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    chinese_chart = fig.to_html()
    return render(request, 'class/scoreAvg.html', {'chinese_chart':chinese_chart})

def dashboard_eachStudentAvg(request):
    avg_students=Classmate.objects.annotate(average_score=((F('chinese_score') + F('math_score') + F('english_score')) / 3.0))
    for avg_student in avg_students:
        average_score = '%.2f'%avg_student.average_score
        
        print(f'grade:{avg_student.grade} name:{avg_student.first_name} average: {average_score}')
    return render(request, 'class/eachStudentAvg.html', {'avg_students': avg_students})