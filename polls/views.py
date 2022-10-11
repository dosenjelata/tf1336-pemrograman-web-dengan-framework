# import from 3rd party module
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import QuestionModelForm, QuestionForm

# import from local module
from .models import Question, Choice



# Create your views here.
def index(request):
    # # tanpa template
    # return HttpResponse("Hello world, you are at the poll index page!")
    # dengan template
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {
        'latest_question_list': latest_question_list,
        'dataku': "UMS Solo",
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# class QuestionCreate(generic.CreateView):
#     model = Question
#     fields = ['question_text']
#     template_name = 'polls/question_form.html'
#     success_url = reverse_lazy('polls:index')

def buat_soal(request):
    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:  # ini bagian GET
        form = QuestionModelForm()
    return render(request, 'polls/question_form.html', {'form': form})