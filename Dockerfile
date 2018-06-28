FROM nginx
COPY docker-files/nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/*.conf
COPY .ebextensions/nginx/conf.d/*.conf /etc/nginx/conf.d/
COPY .ebextensions/nginx/conf.d/elasticbeanstalk /etc/nginx/conf.d/elasticbeanstalk
EXPOSE 80
