from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json

# Create your views here
def home(request):
    context = {'categories': Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'home.html', context)

def quiz(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs = list(question_objs)
        data = []
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "answers": question_obj.get_answers()
            })
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    except Exception as e:
        print("Error in get_quiz:", e)
    return HttpResponse("Something went wrong")

def submit_quiz(request):
    if request.method != 'POST':
        return JsonResponse({'status': False, 'message': 'Invalid request method'})
    
    try:
        data = json.loads(request.body)
        answers = data.get('answers', [])
        
        # Initialize counts for each representational system
        v_count = 0
        a_count = 0
        k_count = 0
        o_count = 0
        g_count = 0
        ad_count = 0
        
        # Process each answer
        for answer_data in answers:
            answer_uid = answer_data.get('answer_uid')
            try:
                answer = Answer.objects.get(uid=answer_uid)
                # Increment the appropriate counter based on rep_system
                if answer.rep_system == 'V':
                    v_count += 1
                elif answer.rep_system == 'A':
                    a_count += 1
                elif answer.rep_system == 'K':
                    k_count += 1
                elif answer.rep_system == 'O':
                    o_count += 1
                elif answer.rep_system == 'G':
                    g_count += 1
                elif answer.rep_system == 'AD':
                    ad_count += 1
            except Answer.DoesNotExist:
                continue
        
        # Create and save the quiz result
        quiz_result = QuizResult(
            visual_count=v_count,
            auditory_count=a_count,
            kinesthetic_count=k_count,
            olfactory_count=o_count,
            gustatory_count=g_count,
            auditory_digital_count=ad_count
        )
        quiz_result.save()
        
        # Return the result ID for redirection
        return JsonResponse({
            'status': True, 
            'result_id': str(quiz_result.uid)
        })
    
    except Exception as e:
        print("Error in submit_quiz:", e)
        return JsonResponse({'status': False, 'message': str(e)})

def result(request):
    result_id = request.GET.get('id')
    if not result_id:
        return redirect('home')
    
    try:
        quiz_result = QuizResult.objects.get(uid=result_id)
        context = {
            'dominant_system': quiz_result.get_dominant_system(),
            'counts': quiz_result.get_all_counts(),
            'quiz_result': quiz_result
        }
        return render(request, 'result.html', context)
    except QuizResult.DoesNotExist:
        return redirect('home')
