# Use a lightweight Linux base image (Alpine is small and fast)
FROM alpine:latest

# Update package list and install TinyProxy
RUN apk update && apk add tinyproxy --no-cache

# Create log directory and set permissions for TinyProxy's default user (nobody)
# This is needed if you enable LogFile in tinyproxy.conf
RUN mkdir -p /var/log/tinyproxy && chown nobody:nogroup /var/log/tinyproxy

# Copy the custom TinyProxy configuration file into the container
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

# Expose the default TinyProxy port (8888)
EXPOSE 8888

# Use a shell script to run tinyproxy in daemon mode AND keep the container alive.
# This ensures PID 1 stays active, preventing the container from exiting.
# Logs will go to the file specified in tinyproxy.conf or syslog.
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["/usr/bin/tinyproxy -d -c /etc/tinyproxy/tinyproxy.conf && tail -f /dev/null"]
