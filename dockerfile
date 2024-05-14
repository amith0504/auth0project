FROM ubuntu:22.04

RUN apt-get update 
RUN apt install -y python3 python3-pip

# Define build-time arguments
ARG AUTH0_API_TOKEN
ARG AUTH0_DOMAIN
ARG client_id
ARG client_secret
ARG audience

# Set environment variables using build arguments
ENV AUTH0_API_TOKEN=$AUTH0_API_TOKEN
ENV AUTH0_DOMAIN=$AUTH0_DOMAIN
ENV client_id=$client_id
ENV client_secret=$client_secret
ENV audience=$audience

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Auth0CRUDoperations.py .

EXPOSE 5000
CMD ["python3", "Auth0CRUDoperations.py"]
