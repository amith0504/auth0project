# auth0project

Please run the below docker build command with the arguements replacing with the actual values. These values are available from AUth0 site.

docker build --build-arg AUTH0DOMAIN="AUTH0DOMAIN" --build-arg client_id="client-id" --build-arg="client-secret" --build-arg audience="<URL>/api/v2" -t <imagename>:tag . 
