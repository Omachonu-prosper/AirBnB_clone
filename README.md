# 0x00. AirBnB clone - The console

![hbnb logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230511%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230511T014400Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9c0740d47e8fc5e0cb22ac3226a0abecc8e5d4a349e7f6917f0412a37f0ff18e)

## Background Context
### Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

#### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## More Info
### Execution
Your shell should work like this in interactive mode:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$
But also in non-interactive mode: (like the Shell project in C)

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

All tests should also pass in non-interactive mode: `code($ echo "python3 -m unittest discover tests" | bash)`

![Current stage in app development process](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230511%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230511T014400Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8f66fc1de7cc2e50c11258d323a49b35b494ae3514f6a26b708a2521b2bb3ac2)