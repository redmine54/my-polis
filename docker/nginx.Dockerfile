# docker/nginx.Dockerfile
# FROM nginx:1.27-alpine
FROM nginx:1.27.1-alpine

COPY nginx.conf /etc/nginx/nginx.conf
#COPY default.conf /etc/nginx/conf.d/default.conf
