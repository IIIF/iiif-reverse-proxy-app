# IIIF Reverse Proxy config

This repo is merely for the `.ebextensions` directory to configure a nginx
reverse proxy to S3 buckets serving static content.

## Running tests:

Start nginx and run:
```./tests/TestSuite.py```

## Config files

Anything in .ebextensions/nginx/conf.d/ directory is in the http part of the nginx config.

Anything in .ebextensions/nginx/conf.d/elasticbeanstalk is in the default server part of the nginx config. 
