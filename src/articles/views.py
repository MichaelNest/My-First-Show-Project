from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Article
from .forms import CommentForm

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    paginate_by = 3
    # login_url = 'login'

# class ArticleMyListView(ListView):
#     model = Article
#     user = request.user
#     queryset = Article.objects.filter(author=user)
#     template_name = 'articles/article_list.html'
#     paginate_by = 3

def article_my_list(request):
    object_list = Article.objects.filter(author=request.user)
    context = {'object_list': object_list}
    return render(request, 'articles/article_list.html', context)


# class ArticleDetailView(LoginRequiredMixin, FormMixin, DetailView):
class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('articles:article_detail', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        # context['form'] = CommentForm(initial={
        #     'article': self.object})
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.filter(moderat=True)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body', 'image']
    template_name = 'articles/article_edit.html'
    login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles:article_list')
    login_url = 'login'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body', 'image']
    template_name = 'articles/article_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)