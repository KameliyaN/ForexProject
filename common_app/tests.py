from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase, RequestFactory

# Create your tests here.
from common_app.models import Article
from django.utils import timezone

from common_app.views import CreateArticleView, ArticleUpdateView


class ArticleTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        # self.article = Article.objects.create(title='Test title', content='My test content', user_id=self.user.id)

    def test_AddArticle_whenAuthenticatedUser_shouldReturn200StatusCode(self):
        request = self.factory.get('/create_article/')
        request.user = self.user
        response = CreateArticleView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_AddArticle_whenUnauthenticatedUser_ShouldRedirectToLogin(self):
        request = self.factory.get('/create_article/')
        request.user = AnonymousUser()
        response = CreateArticleView.as_view()(request)
        self.assertEqual(response.url, '/accounts/login/?next=/create_article/')

    def test_EditArticle_whenUserIsCreator_should(self):
        article = Article.objects.create(title='Test title', content='My test content', user_id=self.user.id)
        request = self.factory.get('/edit_article/<int:pk>/')
        request.user = self.user
        response = ArticleUpdateView.as_view()(request, **{'pk': article.pk})
        self.assertEqual(response.status_code, 200)

    def test_EditArticle_whenUserIsNotCreator_should(self):
        article = Article.objects.create(title='Test title', content='My test content', user_id=self.user.id)
        user_one = User.objects.create_user(
            username='lilia', email='lilia@…', password='top_secret_one')
        request = self.factory.get('/edit_article/<int:pk>/')
        request.user = user_one
        response = ArticleUpdateView.as_view()(request, **{'pk': article.pk})
        self.assertEqual(response.status_code, 403)
        x=8

    def tearDown(self):
        self.user.delete()
