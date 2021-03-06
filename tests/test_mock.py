# -*- coding: utf-8 -*-

import requests
import requests_mock

def test_mock():
    with requests_mock.Mocker() as m:
        m.get('http://mock.com/hello', text='Hello, Mock')

        res = requests.get('http://mock.com/hello')

        assert isinstance(str(res.text), str)
        assert str(res.text) == 'Hello, Mock'
