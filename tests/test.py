""" Testing the API
"""
import unittest
import requests
import httpretty


class RestTest(unittest.TestCase):
    """ Testing Class
    """

    @httpretty.activate
    def test_one(self):
        """ Testing GET Request
        """
        httpretty.register_uri(httpretty.GET, "http://127.0.0.1:5000/",
                               body="{\"message\": \"This is SMS spam detection model. Use the format {'message': 'SMS message'} and POST to get prediction.\"}")  # pylint: disable=line-too-long

        response = requests.get('http://127.0.0.1:5000/')

        print(response)
        assert response.text == "{\"message\": \"This is SMS spam detection model. Use the format {'message': 'SMS message'} and POST to get prediction.\"}"  # pylint: disable=line-too-long

    def test_two(self):
        """ Testing POST Request
        """
        httpretty.register_uri(
            httpretty.POST, "http://127.0.0.1:5000/")

        response = requests.post('http://127.0.0.1:5000/',
                                 headers={'Content-Type': 'application/json'}, data='{"message": "Welcome home"}')  # pylint: disable=line-too-long
        assert str(response.json()
                   ) == "{'results': 'This is not a spam, It is a ham'}"


if __name__ == '__main__':
    unittest.main()
