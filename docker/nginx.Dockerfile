# docker/nginx.Dockerfile
FROM nginx:1.27.1-alpine

COPY ./docker/nginx.conf /etc/nginx/nginx.conf
COPY ./frontend /usr/share/nginx/html
RUN echo "=== nginx ./frontendの内容 ===" && ls -R /usr/share/nginx/html
RUN echo "=== nginx ./conf.dの内容(1) ===" && ls -R /etc/nginx/conf.d
RUN rm -f /etc/nginx/conf.d/default.conf
RUN echo "=== nginx ./conf.dの内容(2) ===" && ls -R /etc/nginx/conf.d
