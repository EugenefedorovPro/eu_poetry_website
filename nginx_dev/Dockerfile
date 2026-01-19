FROM nginx:latest
# rm ooriginal config, which listens to 80 port
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf
