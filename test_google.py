import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)