# DiscBot
DiscBot is a simple and easy-to-use Discord Bot designer.
It uses [Discord.py](https://github.com/Rapptz/discord.py) which is for python.

```
ping:
  say("Pong!")
  say("Latency: `", concat(latency(), "`"))
```

# Installation
```sh
wget https://github.com/dlvdls18/DiscBot.git
pip install discord.py
```
```
  |— res
  |   |— token.txt
  |— src
  |   |— Bot.dbot
  |— base.py
  |— lang.py
  |— README.md
  |— export.py
  |— temp.py
```


# Getting Started
## Language
```
say:
  say(message(1))
  say(concat("- ", mention())
```

You need to learn about dbot language.
DBot uses python and convert itself to python.
DBot Files are placed in `src/`

You don't need to indent when using DBot,
It automatically indent for you.



### Parts
DBot have 2 parts:
- Commands
- Objects

With these parts, you can create a dbot language.
It is very simple and easy to learn.

### Commands
The format of a command is `command_name:`.
Command will be executed if it matches the user message.
```
ping:
  say("Pong!")
  say("Latency: ", latency())
coinflip:
  if(equals(random(1, 2), 1))
    say("Head")
  else()
    say("Tail")
  end()
me:
  say(mention())
say:
  say(message(1))
  say(concat("- ", mention())
```

If you want to make your bot respond when a
user use the command `--status`, create a command named `--status`:
```
--status:
  say("Active!")
```

### Objects
Objects can be inside the commands or inside the listener.
The format of an object is `obj_name(args)`.
```
set("random", random(1, 3))
if(equals(get("random"), 1))
  say("Rock")
elseif(equals(get("random"), 2))
  say("Paper")
else()
  say("Scissors")
end()
```

Objects are instructions for the bot, you can:

- send and edit a message `say("Hello!")`
- check for conditions `if(and(true, not(equals(2, 5))))`
- save and load variables `set("hello", "world")`
- do math `div(add(3, multi(80, 9)), 2)`
and more.


### Listener
Listener is a command without a name.
meaning that listener will be executed whenever a user say something.
Listener is executed after the commands.

To add objects to the listener,
add it before the command.
```
say("Okay")      <-- In listener
ping:
  say("Pong!")   <-- Not in listener
```

## Exporting
This translate your dbot files to python and export them.

### Token
Paste your bot token in `res/token.txt`.
Without this, an error will raise.

Take a look at <https://discord.com/developers/applications/>.

### Export
To export your bot files, run the file `export.py`.
This will translate dbot files and copy to `dev/`.

Other files and folders will not be translated since it's not a dbot file.
You need to manually copy the other files and folders.
Also, dbot files inside a folder does not translate too.

I will improve `export.py` soon.


# API Reference
## Messages
### send()
Send a message.
#### Arguments
String - message to send
#### Returns
Integer - message id

### edit()
Edit a message
#### Arguments
Integer - message id
String - text

### edited()
Check if the message is edited
#### Arguments
Integer - message id
#### Returns
Boolean

### message()
Get the message
#### Returns
String - message

### mention()
Get the author's mention
NOTE: Using @myname will not work.
#### Returns
String - mention text

### author()
Get the author name
#### Returns
String - username

### channel()
Get the channel name
#### Returns
String - channel name


## Variable
### set()
Set a variable
#### Arguments
String - name
Any - value

### get()
Set a variable
#### Arguments
String - name
#### Returns
Any - value


## Conditions
### equals()
Check if arg1 and arg2 are equal
#### Arguments
Any - arg1
Any - arg2
#### Returns
Boolean - equal

### greater()
Check if the arg1 is greater than arg2
#### Arguments
Any - arg1
Any - arg2
#### Returns
Boolean - greater

### lesser()
Check if arg1 is lesser than arg2
#### Arguments
Any - arg1
Any - arg2
#### Returns
Boolean - lesser

### not()
Toggle the boolean
#### Arguments
Boolean - arg1
#### Returns
Boolean - result

### and()
Check if arg1 and arg2 is true
#### Arguments
Boolean - arg1
Boolean - arg2
#### Returns
Boolean - result

### or()
Check if arg1 or arg2 is true
#### Arguments
Boolean - arg1
Boolean - arg2
#### Returns
Boolean - result

### contains()
Check if the arg1 contains arg2
#### Arguments
String - arg1
String - arg2
#### Returns
Boolean - result


## Math
### add()
Add 2 numbers
#### Arguments
Integer - num1
Integer - num2
#### Returns
Integer - result

### sub()
Subtract 2 numbers
#### Arguments
Integer - num1
Integer - num2
#### Returns
Integer - result

### multi()
Multiply 2 numbers
#### Arguments
Integer - num1
Integer - num2
#### Returns
Integer - result

### div()
Divide 2 numbers
#### Arguments
Integer - num1
Integer - num2
#### Returns
Integer - result

### mod()
Modulo 2 numbers
#### Arguments
Integer - num1
Integer - num2
#### Returns
Integer - result

### inc()
Increment number
#### Arguments
Integer - num1
#### Returns
Integer - result

### dec()
Decrement number
#### Arguments
Integer - num1
#### Returns
Integer - result


## Statements
### if()
Execute the objects when condition is true
#### Arguments
Boolean - condition

### elseif()
Execute the objects when condition is true
#### Arguments
Boolean - condition

### else()
Execute the objects when the last condition is false

### try()
Ignore error

### catch()
Execute when error is raised

### end()
End a statement

### pass()
Pass a statement


## Functions
### define()
Define a function
#### Arguments
String - name

### call()
Call a function
#### Arguments
String - name


## Utilities
### length()
Get the length of given argument
#### Arguments
Any - arg1
#### Returns
Integer - length

### type()
Get the type of given argument
#### Arguments
Any - arg1
#### Returns
String - type

### char()
Convert integer to ASCII character
#### Arguments
Integer - arg1
#### Returns
String - char

### cut()
Cut a string by it's start and end index
#### Arguments
String - text
Integer - start
Integer - end
#### Returns
String - text

### trim()
Cut the spaces from start and end
#### Arguments
String - text
#### Returns
String - text

### random()
Get a random number
#### Arguments
Integer - min
Integer - max
#### Returns
Integer - num

### lower()
Convert text to lowercase
#### Arguments
String - text
#### Returns
String - text

### upper()
Convert text to uppercase
#### Arguments
String - text
#### Returns
String - text

### repeat()
Repeat the string
#### Arguments
String - text
Integer - times
#### Returns
String - text

### date()
Get the date
#### Returns
String - text

### now()
Get the date as milliseconds
#### Returns
Integer - ms


## Others
### wait()
Wait n seconds
#### Arguments
Integer - sec

### server()
Get the server name
#### Returns
String - name

### latency()
Get the bot latency
#### Returns
Float - latency

### print()
Print something
#### Arguments
Any - value

### include()
Import py file
#### Arguments
String - name

### note()
Comment
#### Arguments
String - text

### source()
Python source code
#### Arguments
String - text