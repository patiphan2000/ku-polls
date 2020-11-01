from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
 
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Choice, Question, Vote


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        try:
            question = Question.objects.get(pk=kwargs['pk'])
            if (question.can_vote()):
                return HttpResponseRedirect('vote')
            else:
                messages.error(request, "You're not allows to vote that question.")
                return HttpResponseRedirect(reverse('polls:index'))
        except:
            messages.error(request, "Question doesn't exist.")
            return HttpResponseRedirect(reverse('polls:index'))


    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if Vote.objects.filter(choice=selected_choice, voter=request.user):
            messages.error(request,"Already Voted on this choice")
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            Vote.objects.create(choice=selected_choice, voter=request.user)
            messages.success(request, "Your choice successfully recorded.")
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def go_to_index(request):
    return IndexView.as_view()