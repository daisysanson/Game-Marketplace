# Game Marketplace

Simple Flask API demonstrating the use of a quicksort algorithm. The application allows users to add games to a leaderboard, which will be sorted by their rating. The quicksort sorts the game from highest to lowest. The user can also edit and delete existing entries. 

## Requirements
Python 3.7 and above





## Setting up the Enviroments
You should install a virtual enviroment and conifgure it to run on Python 3. 

To install your virtual enviroment:
```

python3 -m pip install --user virtualenv

```
To run your virtual enviroment, type in the command line:

```

source venv/bin/activate

```

You will also need to install the  `requirements.txt` file to your virtual environment on the first run. You can do this by running the following command when your environment is activated.

```

$ pip install -r requirements.txt

```

To start the application, you can then run. 

```
$ python run.py
```

It will run on Port 8080.

Click or copy and paste http://0.0.0.0:8080 into your browser, which will direct you to the home page of the application.

If you wish to close your enviroment, type in:

```
deactivate

```

## Using the Game Marketplace

You can view the current leaderboard by navigating to  http://localhost:8080/show_games,  where you can update and delete the entries.

You can add a new entry by using the form in http://localhost:8080/add_game. 
