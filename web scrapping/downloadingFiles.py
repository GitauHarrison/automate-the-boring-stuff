import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# always use the raise_for_status() function after calling requests.get().
# You want to be sure that the download actually worked before your program continues