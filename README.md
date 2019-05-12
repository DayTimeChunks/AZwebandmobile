# AZ Web and Mobile

This repository shares the source code to my web page, which you can visit at  www.azwebandmobile.com 

The site is built on a Python (2.7) backend running on Google App Engine's standard environment. The front-end is based 
on HTML5 and Twitter Bootstrap v4 (CSS).

# To run

To run locally, the dev environment needs to be defined as

`source activate webdev`
`dev_appserver.py app.yaml`   

# To deploy

`source deactivate`
`gcloud app deploy --project=azwebandmobile`

