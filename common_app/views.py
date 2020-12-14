# Create your views here.


from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from accounts.models import Profile
from common_app.decorators import user_is_article_author_or_admin
from common_app.forms import ArticleForm, CommentForm
from common_app.models import Article, Comment


class ViewAllArticles(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "common_app/index.html"
    paginate_by = 3
    ordering = ['-date']


class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "common_app/article_create.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        article = form.save(commit=False)
        # profile = Profile.objects.get(user_id=self.request.user.id)
        article.user = self.request.user.profile
        article.save()
        return super(CreateArticleView, self).form_valid(form)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "common_app/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form

        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:

            return redirect('home')


@method_decorator(user_is_article_author_or_admin, name='dispatch')
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "common_app/article_edit.html"

    def form_valid(self, form):
        article = form.save(commit=False)
        article.save()
        return redirect('view article', article.id)


@method_decorator(user_is_article_author_or_admin, name='dispatch')
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('home')
    context_object_name = 'article'


class ArticlesUserAllView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "common_app/view_all_user_articles.html"
    paginate_by = 3

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Article.objects.filter(user_id=pk).order_by('-date')
        # queryset = super(ArticlesUserAllView, self).get_queryset()
        # return queryset.filter(user_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count
        return context


class NewCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user.profile
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        comment.article = article
        comment.save()
        return redirect('view article', pk)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "common_app/comment_edit.html"

    def form_valid(self, form):
        comment = form.save(commit=False)
        article_pk = self.kwargs['article_pk']
        article = Article.objects.get(pk=article_pk)
        comment.article = article
        comment.save()
        return redirect('view article', article_pk)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('view article', kwargs={'pk': self.kwargs['article_pk']})
