import unittest
import weather.app
import httpretty


@httpretty.activate
class TestApp(unittest.TestCase):

    def setUp(self):
        URL = 'https://api.darksky.net/forecast/API/LAT,LON'
        httpretty.register_uri(httpretty.GET, URL,
                               content_type='application/json',
                               body='{"currently": {"icon":"rain"}, "hourly": {"summary":"summary"}}')

    def test_mocked_get_request(self):
        config = {"api": "API", 'lat': 'LAT', "lon": "LON"}
        icon, summary = weather.app.get_forecast(config)
        assert icon == 'rain'
        assert summary == 'summary'


if __name__ == '__main__':
    unittest.main()
