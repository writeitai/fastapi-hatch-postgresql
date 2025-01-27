# Use a Debian base image with apt-get
FROM python:3.11.9-slim-bookworm

# Install hatch
RUN pip install --no-cache-dir hatch

WORKDIR /app

COPY ./pyproject.toml ./

RUN hatch dep show requirements > ./requirements.txt && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code into the container
COPY ./src ./src
