# Assignment 3

In this assignment, we are containerizing our website.

Due date: April 4

## Running the container

### Building the container
Firstly, you will have to build the container. Make sure you put in the correct directory when running that line, I would recommend just cd'ing to the head of the direcory so you can just use . here.
```shell
# Build the image
docker build -t assignment3 [REPO DIR]
```

Next, all you need to do is run the image. Firstly, I have exposed the image to be on 5000, so make sure you put [your port]:5000.
Also, in order to ensure that the data you add to the backend is updated, make sure to mount the db. To do this, just mount the repo dir.
In my tests, I just did $(pwd)/instance:... but make sure that you virtually share this file on docker desktop so you can access it
from Docker -> Preferences... -> Resources -> File Sharing.
```shell
# Run the image
docker run -p [PORT]:5000 -v [REPO DIR]/instance:/app/instance systems3
```

Finally, open the website with the local website page you picked a port for, such as http://localhost:[PORT]

## Key Note
Unlike the demo provided for assignment 2, to delete a note, you have to select a note to delete on the main page. You click the `delete a note button` at the buttom of the page, then type the name of the note, and it will delete that note and all of its comments.