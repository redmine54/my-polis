# docker/frontend.Dockerfile
FROM nginx:1.27-alpine
COPY ./frontend /usr/share/nginx/html
RUN echo "=== ./frontendの内容 ===" && ls -R /usr/share/nginx/html
