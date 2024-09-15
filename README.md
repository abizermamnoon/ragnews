Install Packages
```
$ pip install -r requirements.txt
$ pip install ./metahtml
```

Create a .env file and add your GROQ_API_KEY
```
GROQ_API_KEY=your_api_key_here
```

```
$ export $(cat .env)
```

```
$ python3 -i ragnews.py
ragnews> when did the presidential debate take place?
While it's isn't explicitly stated,  The article mentions that the Supermartes (super Tuesday) which is a major election event, will take place on the 6th of February. However, the article does not explicitly state the date of the debate or when the presidential debate take place.
```

The data consists of news articles from the US Presidential debate in 2024. You can ask questions about the data
