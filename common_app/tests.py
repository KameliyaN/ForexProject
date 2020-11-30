from django.test import TestCase

# Create your tests here.
from common_app.models import Article
from django.utils import timezone


# class ArticleTests(TestCase):
#     test_title = 'Test title'
#     test_content = '<p>Welcome to my site</p>'
#     test_date = timezone.now()
#
#     def setUp(self):
#         self.article = Article.objects.create(title=self.test_title, content=self.test_content, )
#
#     def test_blogentry_list(self):
#         response = self.client.get(reverse('blog:blogentry_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.test_title)
#         self.assertContains(response, self.test_entry)
