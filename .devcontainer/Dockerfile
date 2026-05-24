# Використовуємо стабільний образ Node.js v22 (згідно з Файлом №78)
FROM mcr.microsoft.com/devcontainers/javascript-node:22

# Встановлення Hugo Extended та залежностей (Go, Dart Sass, CGO)
RUN apt-get update && apt-get install -y \
    golang-go \
    dart-sass \
    && curl -L https://github.com/gohugoio/hugo/releases/download/v0.161.0/hugo_extended_0.161.0_linux-64bit.tar.gz | tar -xz \
    && mv hugo /usr/local/bin/

# Налаштування робочої директорії
WORKDIR /workspaces/1705
