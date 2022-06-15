import urllib.request as url

print()
print()

resp = url.urlopen('https://www.forbes.com/real-time-billionaires')
# print('https://www.forbes.com/real-time-billionaires status code: ', resp.code)
data = resp.read()
html = data.decode('utf-8')
# print(html[100:200])

str_to_find = '<div ng-if="!i'
context = 10
index = html.find(str_to_find)
print(index, len(html))
print(html)
html_start = index - context
html_end = index + len(str_to_find) + context
print(html_start, html_end)
print(html[html_start:html_end])