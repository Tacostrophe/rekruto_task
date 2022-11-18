import os
from http import HTTPStatus

from django.test import Client, TestCase


def setUpModule():
    global URL_MAIN_PAGE
    URL_MAIN_PAGE = '/'


class TestMainPage(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_main_page(self):
        '''main работает так, как от нее ожидается'''
        with self.subTest(adress=URL_MAIN_PAGE):
            response = self.guest_client.get(URL_MAIN_PAGE)
            PHRASE_WITHOUT_ARGS = 'Hello Guest! Your message could be here!'
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertEqual(response.content,
                             PHRASE_WITHOUT_ARGS.encode('utf-8'))
            name = 'name'
            message = 'message'
            response = self.guest_client.get(
                os.path.join(URL_MAIN_PAGE, f'?name={name}&message={message}')
            )
            PHRASE_WITH_ARGS = f'Hello {name}! {message}!'
            self.assertEqual(response.content,
                             PHRASE_WITH_ARGS.encode('utf-8'))
