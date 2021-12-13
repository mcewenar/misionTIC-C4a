sudo heroku login
sudo heroku create nous-apigateway
sudo heroku container:login
heroku container:push web --app name_appheroku
heroku container:release web --app name_appheroku
