# auth0project
**1.Deploying with Docker and Kuberenetes** 
Please run the below docker build command with the arguements replacing with the actual values. These values are available from AUth0 site.


**docker build --build-arg AUTH0DOMAIN="AUTH0DOMAIN" --build-arg client_id="client-id" --build-arg="client-secret" --build-arg audience="<URL>/api/v2" -t imagename:tag .**

My Image is already pushed to dockerhub. So we can directly deploy it as below.

**kubectl create deployment auth0crud --image=amith0504/auth0repo:11**

**kubectl expose deployment auth0crud --type=NodePort --port=5000**
 
 **minikube service auth0crud** 
 
_W0514 20:39:51.045633   10996 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\amith\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified._
|-----------|-----------|-------------|---------------------------|
| NAMESPACE |   NAME    | TARGET PORT |            URL            |
|-----------|-----------|-------------|---------------------------|
| default   | auth0crud |        5000 | http://192.168.49.2:30273 |
|-----------|-----------|-------------|---------------------------|
🏃  Starting tunnel for service auth0crud.
|-----------|-----------|-------------|------------------------|
| NAMESPACE |   NAME    | TARGET PORT |          URL           |
|-----------|-----------|-------------|------------------------|
| default   | auth0crud |             | http://127.0.0.1:59535 |
|-----------|-----------|-------------|------------------------|
🎉  Opening service default/auth0crud in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.


**2.Function calls**

python .\Auth0CRUDoperations.py get_users    

python .\Auth0CRUDoperations.py delete_user "auth0|6641fee9587030bfedde6b"      

python .\Auth0CRUDoperations.py create_user amithtest4@gmail.com Amith123# Username-Password-Authentication



**3.API calls**

 Get_users list
 
**curl http://localhost:5000/users**

 Create_user with the inputs
 
 **curl -Uri "http://localhost:5000/users" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body (ConvertTo-Json @{ email = "newuser1100@example.com"; password = "newpassword@123"; connection = "Username-Password-Authentication" })**

delete_user with user_id as input

**curl -Uri "http://localhost:5000/users/auth0|6641dd484d1c357206d55c6d" -Method DELETE**
  
