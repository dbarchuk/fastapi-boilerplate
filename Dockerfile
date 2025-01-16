# Stage 1: Build dependencies
FROM python:3.13-slim as builder

ENV PYTHONDONTWRITEBYTECODE=1

# Install poetry
RUN pip install poetry

# Copy only dependency files
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Export dependencies to requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Stage 2: Final image
FROM python:3.13-slim

WORKDIR /app

# Copy requirements from builder stage
COPY --from=builder /app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app ./app

# Expose port
EXPOSE 8000

# Command to run the application
ARG CMD_COMMAND
ENV CMD_COMMAND=${CMD_COMMAND}
CMD ${CMD_COMMAND}