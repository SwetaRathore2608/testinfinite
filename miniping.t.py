from miniping import get_status_code

def test_get_status_code():
    url1 = 'http://www.google.com'
    url2 = 'http://www.bing.com'
    url3 = 'http://foofle.com'
    assert get_status_code(url1) == 200
    assert get_status_code(url2) == 200
    assert get_status_code(url3) == 404

if __name__ == '__main__':
    test_get_status_code()
