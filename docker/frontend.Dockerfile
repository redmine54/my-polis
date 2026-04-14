# docker/frontend.Dockerfile
# frontend はビルドして dist を作る
#FROM node:18-alpine AS build
#WORKDIR /app
#COPY ./frontend .
#RUN npm install
#RUN npm run build

# nginx でビルドした dist を配信する
#FROM nginx:1.27.1-alpine
#COPY ./docker/nginx.conf /etc/nginx/nginx.conf
#COPY --from=build /app/dist /usr/share/nginx/html

# 静的ファイル読み込み
FROM nginx:1.27.1-alpine
COPY ./frontend /usr/share/nginx/html
RUN echo "=== ./frontendの内容 ===" && ls -R /usr/share/nginx/html
