# docker/nginx.Dockerfile
FROM nginx:1.27.1-alpine

COPY ./docker/nginx.conf /etc/nginx/nginx.conf
COPY ./frontend /usr/share/nginx/html
RUN echo "=== nginx ./frontendの内容 ===" && ls -R /usr/share/nginx/html
