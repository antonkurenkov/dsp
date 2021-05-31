FROM python:3.7.9

# Switch to the target folder
WORKDIR /usr/src/app

# Copy files to the target folder
COPY server server

COPY docker-entrypoint.sh ./

# Install requirements
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r server/requirements.txt

# Apply required db migrations, loading fixtures and start the application server
CMD ["sh", "docker-entrypoint.sh"]
