# About
It's a simple Flask-API that scrap google news site and gets the news. You can search for any specific news and filter with source and with any past hour/day/week/year, READ Documentation.

# Requirements
```
pip install BeautifulSoup4
pip install requests
pip install flask
```

# Documentation
### from this endpoint you can get all the information like:
#### /news/everything/?q=Messi

- Search for any news by keywords
- Filter with date and time example:
  - /news/everything/?q=Messi when:1h
  - when:1h past hour
  - when:1d past day
  - when:7d past week
  - when:1y past year
- Filter with specific source (CNN, New York times etc)
  - /news/everything/?q=Messi cnn
- Merge all filters 
  - /news/everything/?q=Messi cnn when:1h

#### Response
```json
{
  "total_results": 89,
  "query": "messi",
  "data": [
    {
      "title": "...",
      "url": "...",
      "img": "...",
      "author": "...",
      "source": "...",
      "date": ""
    }
  ]
}
```

# Deploy Public API
If you want to deploy it online for free Check this youtube video to deploy it public [Youtube Link](https://www.youtube.com/watch?v=D2GLVoiEZyE), In every request the script will go to google news and scrap the searched news it takes 1 second.
  
