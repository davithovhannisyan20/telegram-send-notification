FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy
# ↑ Use a ready-made image that already has Python + Chromium built in
#   (saves you from installing them manually)

WORKDIR /app
# ↑ Create a folder called /app inside the container to work in

COPY requirements.txt .
RUN pip install -r requirements.txt
# ↑ Copy your requirements file in and install httpx + playwright

COPY main.py .
# ↑ Copy your script into the container

CMD ["python", "main.py"]
# ↑ When the container starts, run the script