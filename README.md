# freestyle_project
# Freestyle project for OPAN 3244. By Bhagirath Khemka, Rohan Mistry and Dhruv Gupta

#OPAN 3244 News Prototpye: Rohan, Bhagirath, Dhruv

This prototype uses a NEWS API that pulls breaking news articles based on an inputted country, topic, or news source. Use cases can involve college students looking to get up to date very quickly on current day news, or debaters needing to get information quickly regarding a topic. Once emailing features are implemented, one specific avenue this prototype can explore is creating personalized email newsletters.

The link to the API is https://newsapi.org/

You will be required to register in order to acquire an API key. This will just require inputing a name, email, and attesting you are an individual.

Create and activate a virtual environment (first time only):

```sh
conda create -n news-env-2024 python=3.10
```

Activate the environment (whenever you come back to this):

```sh
conda activate news-env-2024
```

Install packages
```sh
pip install -r requirements.txt
```

Run the unemployment script:

```sh
python -m app.main
```