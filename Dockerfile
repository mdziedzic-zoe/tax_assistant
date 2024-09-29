# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files
COPY pyproject.toml ./
COPY poetry.lock* ./

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Add the current directory to PYTHONPATH
ENV PYTHONPATH=/app:$PYTHONPATH

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "-m", "tax_assistant.main"]