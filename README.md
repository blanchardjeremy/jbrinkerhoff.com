# Jessilyn Brinkerhoff Portfolio

A Django application for Jessilyn Brinkerhoff's portfolio.

Visit the site at **[http://jbrinkerhoff.com][jb]**

## Cool things about this site

  * Hosted on Heroku
  * Uses Jinja2 templates and markdown filters
  * Uses the flickr api to store/organize photos

## Dependencies

  * [python-flickr-api](http://code.google.com/p/python-flickr-api/)

## Usage
When you begin working on this project, do the following:

    cd ~/Projects/thisproject/code
    source .env                     # Load the system-specific settings for this project
    ./root/manage.py syncdb         # Initialize the database
    ./root/manage.py runserver      # Launch your server. Visit http://localhost:8000/


## Possible Features
Some things we might want to implement in the future:

  * Caching of Flickr API calls
  * Caching of Flickr images

## Heroku deploy instructions

    # Follow the heroku quickstart guide to get it installed and your authentication going
    heroku apps:create --stack=cedar jbrinkerhoff
    heroku config:add FLICKR_SECRET=aaaaaaaaaaaaaaaa
    # repeat config:add for secret key and any other variables in .env
    heroku push heroku master
    # Custom domains: configure your DNS as such: https://devcenter.heroku.com/articles/custom-domains
    heroku domains:add www.jbrinkerhoff.com
    heroku domains:add jbrinkerhoff.com



## Author
Built with love! Design by [Jessilyn Brinkerhoff][jb] and code by [Jeremy Blanchard](http://blanchardjeremy.com).


[jb]: http://jbrinkerhoff.com