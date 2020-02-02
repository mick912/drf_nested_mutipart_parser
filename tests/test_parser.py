from . import test_settings

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from drf_nested_multipart_parser.parser import NestedMultipartParser


def test_multipart_parser():
    factory = APIRequestFactory()

    django_request = factory.post('/', {
        'foo[]': 'bar',
    })
    request = Request(django_request, parsers=[NestedMultipartParser()])

    # self.assertEqual(request.POST, {'foo': ['bar']})
    assert request.data == {'foo': ['bar']}

    django_request = factory.post('/', {
        'foo[test][]': 'bar',
        'name[name2][name3][name4]': 'bar2',
        'bar': 'bar3',
    })
    request = Request(django_request, parsers=[NestedMultipartParser()])

    expected = {
        'foo': {
            'test': ['bar']
        },
        'name': {
            'name2': {
                'name3': {
                    'name4': 'bar2'
                }
            }
        },
        'bar': 'bar3'
    }
    assert request.data == expected