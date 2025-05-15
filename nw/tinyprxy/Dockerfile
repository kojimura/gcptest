# Use a lightweight Linux base image (Alpine is small and fast)
FROM alpine:latest

# Update package list and install TinyProxy
RUN apk update && apk add tinyproxy --no-cache

# Copy the custom TinyProxy configuration file into the container
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

# Expose the default TinyProxy port (8888)
# This is just documentation; actual port mapping is done with `docker run -p`
EXPOSE 8888

# Command to run TinyProxy in the foreground
# -c specifies the configuration file
CMD ["/usr/sbin/tinyproxy", "-c", "/etc/tinyproxy/tinyproxy.conf"]
