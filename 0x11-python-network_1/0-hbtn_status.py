#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using urllib
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        html = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf-8 content: {}'.format(html.decode('utf-8')))