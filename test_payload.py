import unittest
import json
from payload import app
from pathlib import Path



class FlaskTestCase(unittest.TestCase):

    def test_download(self):
        tester = app.test_client(self)
        response = tester.post('/manage_file', data=json.dumps(dict({"action":"download"})), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_read(self):
        tester = app.test_client(self)
        response = tester.post('/manage_file', data=json.dumps(dict({"action":"read"})), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_manage_file(self):
        tester = app.test_client(self)
        response = tester.post('/manage_file', data=json.dumps(dict({"action":"test"})), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_manage_file_error(self):
        tester = app.test_client(self)
        response = tester.get('/manage_file', content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_file(self):
        path = Path('sample-text-file.txt')
        assert path.is_file()


if __name__ == '__main__':
    unittest.main()