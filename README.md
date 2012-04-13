# Jessilyn Brinkerhoff Portfolio

A Django application for Jessilyn Brinkerhoff's portfolio.

Visit the site at **[http://jbrinkerhoff.com][jb]**


## Cool things about this site

  * Hosted on [Heroku](http://www.heroku.com/) (using Jeremy's [Django projecttemplate for heroku](http://github.com/auzigog/django-template-heroku/))
  * Built on [Twitter Bootstrap](http://twitter.github.com/bootstrap/) (with Jeremy's [Jinja Bootstrap](https://github.com/auzigog/jinja-bootstrap) library)
  * Uses the [Flickr API](http://www.flickr.com/services/api/) to store/organize photos (via [python-flickr-api](http://code.google.com/p/python-flickr-api/))
  * Caching of Flickr API requests
  * Uses Jinja2 templates and markdown filters
  * Stores text and quotes in the database for easy editing


## Usage
When you begin working on this project, do the following:

    cd ~/Projects/thisproject/code
    source .env                     # Load the system-specific settings for this project
    ./root/manage.py syncdb         # Initialize the database
    ./root/manage.py runserver      # Launch your server. Visit http://localhost:8000/


## Possible Features
Some things we might want to implement in the future:

  * Combine front page and second page as one scroll effect


## Heroku deploy instructions

    # Follow the heroku quickstart guide to get it installed and your authentication going
    heroku apps:create --stack=cedar jbrinkerhoff
    heroku config:add FLICKR_SECRET=aaaaaaaaaaaaaaaa
    # repeat config:add for secret key and any other variables in .env
    heroku push heroku master
    # Get the db and starter data ready
    heroku run python manage.py syncdb --noinput
    heroku run python manage.py loaddata starter_data
    # Custom domains: configure your DNS as such: https://devcenter.heroku.com/articles/custom-domains
    heroku domains:add www.jbrinkerhoff.com
    heroku domains:add jbrinkerhoff.com


## Authors
Built with love! Design by [Jessilyn Brinkerhoff][jb] and code by [Jeremy Blanchard](http://blanchardjeremy.com).


[jb]: http://jbrinkerhoff.com