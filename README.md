# freestyle_project
# Freestyle project for OPAN 3244. By Bhagirath Khemka, Rohan Mistry and Dhruv Gupta

#OPAN 3244 News Prototpye: Rohan, Bhagirath, Dhruv

This prototype uses a NEWS API that pulls a specified number of breaking news articles based on an topic, news source(s), and optional keywords. Use cases can involve college students looking to get up to date very quickly on current day news, or debaters needing to get information quickly regarding a topic. Once emailing features are implemented, one specific avenue this prototype can explore is creating personalized email newsletters.

The link to the API is https://newsapi.org/

You will be required to register in order to acquire an API key. This will just require inputing a name, email, and attesting you are an individual.

This app also utilizes the Mailgun service as well. 
Steps to create a Mailgun account, register an email address, and create necessary notebook keys.

Create a Mailgun account with your business or university email address. Click the verification link sent to that address.

Login. Find and click the nav link about "Sending" email. From the domains page, note the sandbox domain provided to you by default (i.e. MAILGUN_DOMAIN like "sandbox-xyz.mailgun.org")

Click on the sandbox domain. Scroll down to "Authorized Recipients" and add any necessary email addresses.

Find and click on API Key settings link on bottom right, then on the API Keys page, scroll down and click the button to create a new API Key (i.e. MAILGUN_API_KEY). Save this API Key.

Make sure to store the sandbox domain and API key in notebook secrets in the environment, under MAILGUN_DOMAIN and MAILGUN_API_KEY, respectively.

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

Run the script:

```sh
python -m app.main
```
Website link using Render: 
https://news-snapshot-freestyle-project.onrender.com
