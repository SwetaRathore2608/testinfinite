import requests, sys

def get_status_code(url):
    try:
        r = requests.get(url)
        return r.status_code
    except:
        return 404

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'Usage: %s <url>' % sys.argv[0]
        sys.exit(0)
    print get_status_code(sys.argv[1])
