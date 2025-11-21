# Step 1: Use Python runtime as the base image
FROM python:3.10-slim

# Step 2: Set working directory in the container
WORKDIR /app

# Step 3: Copy all project files into container
COPY . /app

# Step 4: Install dependencies if you have a requirements file
# (Only include this if you created requirements.txt)
# RUN pip install -r requirements.txt

# Step 5: Command to run your app
CMD ["python", "Converter.py"]