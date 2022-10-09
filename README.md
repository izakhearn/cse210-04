# cse210-03

## Greed The Game

The purpose of this repository is to keep the code for the Greed game.

The code has the following object and classes

## Actor Class

```python
Class       : actor
File Name   : actor.py

**Attributes**
None
**Methods**
get_color()   : Gets the Color
get_font_size()  : Gets the font size as int
get_position()    : gets position as point
get_text()    : Gets the text as string
get_velocity() : Get the velocity as int
move_next() : moves the actor to the next position
set_color() : Sets the actors color
set_position() : set the actors position
set_font_size() : sets the font size
set_text() : sets the actors text
set_velocity() : sets the actors velocity
```

-------

## Artifact Class

```python
Class       : artifact
File Name   : artifact,py

**Attributes**
    None

**Inheritance**
Parent : Actor

**Methods**
     set_message(): Sets the message of the Artifact
     get_message():  Gets the message of the Artifact
     set_position(): Sets the position of the Artifact
     get_position(): Gets the position of the Artifact     
     set_text(): Sets the text of the Artifact
     get_text(): Gets the text of the Artifact
```

-------

## Director Class

```python
Class            : Director
File Name        : director.py

**Attributes**
    None

**Methods**
start_game()     : None 
_get_inputs()    : None
_do_updates()    : None
_do_outputs()    : None
```

```python
Object      : Director

**Responsibility**
To hold an instance of the game running and print out the parachute and guessed words

**Behaviors**       **State**
 start_game         Starts running the game
```

-------

## Cast Class

```python
Class            : Cast
File Name        : cast.py

**Attributes**
    None

**Methods**
add_actor() : Adds an actor
get_actors() : gets the actor your are looking for
get_all_actors() : gets all the actors and returns them
get_first_actor(): gets just the first actor you want
remove_actor(): removes an actor
```

```python
Object      : cast

**Responsibility**
Holds all the actors in the game

**Behaviors**        **State**
add_actor() : Adds an actor
get_actors() : gets the actor your are looking for
get_all_actors() : gets all the actors and returns them
get_first_actor(): gets just the first actor you want
remove_actor(): removes an actor
```

-------

## Author : Izak Hearn

## Email : izak@gmail.com
