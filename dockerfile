
# Use an official Python runtime as a parent image
FROM python:3.8
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY requirements.txt app/requirements.txt

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN  pip install  --no-cache-dir -r app/requirements.txt
EXPOSE 5001

# Run app.py when the container launches
ENTRYPOINT ["python"]
CMD ["app.py" ]
