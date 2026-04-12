# docker/nginx.Dockerfile
FROM nginx:1.27.1-alpine

COPY ./docker/nginx.conf /etc/nginx/nginx.conf
