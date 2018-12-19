from django.test import TestCase
# resolve 是django的内部函数用于解析url
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.


class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     # found.func返回所需要的示图函数
    #     self.assertEqual(found.func, home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     excepted_html = render_to_string('home.html')
    #     self.assertEqual(html, excepted_html)
    #     # 检查相应是使用哪个模板渲染的
    #     self.assertTemplateUsed(response, 'wrong_html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')