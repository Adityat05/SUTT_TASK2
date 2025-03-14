from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template=loader.get_template("polls/index.html")
#     context={
#         "latest_question_list":latest_question_list
#     }
#     #output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(template.render(context, request))

#can do index and applying template by method above but method below is a shortcut

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)



# def detail(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/details.html", {"question":question}) # %question_id makes the question id into a string the HTTP command can only take string
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question":question})
#as these codes are too redundant and common we replace by shortcut



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5] #lte means less than or equal to


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
# Create your views here.
