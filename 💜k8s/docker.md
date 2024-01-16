
```bash
sudo yum -y install docker

sudo systemctl start docker


# Verify the docker group exists by searching for it in the groups file:
grep docker /etc/group

# Add your user to the docker group:
sudo gpasswd -a $USER docker

# Verify that your user can successfully issue Docker commands by entering:
docker info



# Server:
#  Containers: 0
#   Running: 0
#   Paused: 0
#   Stopped: 0

docker system --help

# Commands:
#   df          Show docker disk usage
#   events      Get real time events from the server
#   info        Display system-wide information
#   prune       Remove unused data

docker image --help


# Commands:
#   build       Build an image from a Dockerfile
#   history     Show the history of an image
#   import      Import the contents from a tarball to create a filesystem image
#   inspect     Display detailed information on one or more images
#   load        Load an image from a tar archive or STDIN
#   ls          List images
#   prune       Remove unused images
#   pull        Pull an image or a repository from a registry
#   push        Push an image or a repository to a registry
#   rm          Remove one or more images
#   save        Save one or more images to a tar archive (streamed to STDOUT by default)
#   tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE



docker container --help

# Commands:
#   attach      Attach local standard input, output, and error streams to a running container
#   commit      Create a new image from a container's changes
#   cp          Copy files/folders between a container and the local filesystem
#   create      Create a new container
#   diff        Inspect changes to files or directories on a container's filesystem
#   exec        Run a command in a running container
#   export      Export a container's filesystem as a tar archive
#   inspect     Display detailed information on one or more containers
#   kill        Kill one or more running containers
#   logs        Fetch the logs of a container
#   ls          List containers
#   pause       Pause all processes within one or more containers
#   port        List port mappings or a specific mapping for the container
#   prune       Remove all stopped containers
#   rename      Rename a container
#   restart     Restart one or more containers
#   rm          Remove one or more containers
#   run         Run a command in a new container
#   start       Start one or more stopped containers
#   stats       Display a live stream of container(s) resource usage statistics
#   stop        Stop one or more running containers
#   top         Display the running processes of a container
#   unpause     Unpause all processes within one or more containers
#   update      Update configuration of one or more containers
#   wait        Block until one or more containers stop, then print their exit codes

```

how to search Docker Hub, pull images, and work with containers running on top of the images. 

```bash
docker run hello-world

docker run --name web-server -d -p 8080:80 nginx:1.12

# --name container_name: Label the container container_name. In the command above, the container is labeled web-server. 

# -d: Detach the container by running it in the background and print its container id. Without this, the shell would be attached to the running container command and you wouldn't have the shell returned to you to enter more commands.

# -p: host_port:container_port: Publish the container's port number container_port to the host's port number host_port. This connects the host's port 8080 to the container port 80 (http) in the nginx command.


# To list all running containers
docker ps

# see a list of all running and stopped containers:
docker ps -a

#  The -it options tell Docker to handle your keyboard events in the container.
docker exec -it web-server /bin/bash


# Search for an image that you don't know the exact name of, say an image for Microsoft .NET Core, by entering:
docker search "Microsoft .NET Core"



```



create


```bash
sudo yum -y install git


nano Dockerfile

# The -t tells Docker to tag the image with the name flask-content-advisor and tag latest. The . at the end tells Docker to look for a Dockerfile in the current directory. Docker will report what it's doing to build the image. 
docker build -t flask-content-advisor:latest .

# Record your VM's public IP address:
curl ipecho.net/plain; echo

# runs a container named advisor and maps the container's port 5000 to the host's port 80 (http). 
docker run --name advisor -p 80:5000 flask-content-advisor
# add -d to run in detached mode. 
```

```Dockerfile

# Python v3 base layer
FROM python:3
# Set the working directory in the image's file system
WORKDIR /usr/src/app
# Copy everything in the host working directory to the container's directory
COPY . .
# Install code dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Indicate that the server will be listening on port 5000
EXPOSE 5000
# Set the default command to run the app
CMD [ "python", "src/app.py" ]


# FROM sets the base layer image
# COPY . . copies all of the files in the code repository into the container's /usr/src/app directory
# RUN executes a command in a new layer at the top of the image
# EXPOSE only indicates what port the container will be listening on, it doesn't automatically open the port on the container
# CMD sets the default command to run when a container is made from the image

```

