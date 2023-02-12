import requests

def test_api_status_value_check():
    """Check if API is running"""
    payload = {'stock':'89','time_id':'32654'}
    r = requests.get('http://127.0.0.1:8000/?',params=payload)
    a = r.json()
    assert a['bid_price_difference']['0']==0.0003531000000001

#pytest -v tests/test_api.py
