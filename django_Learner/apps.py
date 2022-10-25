from django.apps import AppConfig
import requests

class DjangoLearnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_Learner'



def apiCall():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
        "key1": "value",
        "key2": "value"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "294bc5191dmsh0a458bbf623042dp1dc879jsnd3360d3a1ad0",
        "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    text=response.text
    newText=text.split('-')
    return(newText)

