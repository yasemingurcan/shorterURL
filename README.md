## Installation
```bash
#Build docker image 

docker build -t imagename . 

#Create container 
 
docker run -d --name container_name -p 80:80 imagename 

#I used this image and container name

docker build -t money_image .
docker run -d --name container_money -- 80:80 money_image
```

## Endpoint Usage
```bash
Visit http://localhost/docs

#Create url shorter

url: http://localhost/url
payload: {
"target_url" : "Your url"
} 

#Redirect URL

Endpoint: http://localhost/url/{url_key}

```
