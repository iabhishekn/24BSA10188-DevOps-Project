FROM nginx:1.27-alpine

LABEL org.opencontainers.image.title="ABC Technologies Corporate Website"
LABEL org.opencontainers.image.description="Static corporate website for DevOps Assignment Case 1"

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY *.html /usr/share/nginx/html/
COPY assets /usr/share/nginx/html/assets

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1
