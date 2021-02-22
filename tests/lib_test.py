from apirestoolbox.lib import daily_forecast


def test_api_ping():
    assert isinstance(daily_forecast(44418, 2020, 2, 13), list)

