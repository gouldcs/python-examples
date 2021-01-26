# Variables
Look at you, being all productive and making it to part two. My goodness. Congratulations!

## Oh God, This Sounds Like Math...
Well, yes and no. The good news is that in computer programming, variables are a bit more verbose and easier to swallow. Look at this lovely snippet of code:
###### Example 2.1
```python
name = "Chris Evans"
age = 39
hotness_scale = 9.9
star_spangled = True
has_plan = True
```
So here, we've made some `variables`. These are useful because they can be stored and reused under their alias later. the `name` variable holds a
`str` value of `"Chris Evans"`, the `age` variable holds an `int` value of `39`, the `hotness_scale` (out of 10) holds a `float` value of `9.9`, the
`star_spangled` variable holds a `boolean` value of `True`, and the `has_plan` variable holds a `boolean` value of `True` as well. That's right, Chris Evans
may be 39 years old but he's still a 9.9/10 on the hotness scale. And he's the star-spangled man with a plan. Don't you forget it.

## How Do We Use These?
It's pretty simple. Create a new Repl.it project using Python, name it `CaptainAmericanPy` because this is Captain America we are working with here. Once it's
created, copy this code into it:
###### Example 2.2
```python
name = "Chris Evans"
age = 39
hotness_scale = 9.9

print(name, "is", age, "years old, but he is still a", hotness_scale, "out of 10 on the hotness scale.")
```
As you can see here, you just drop the variable names in where you want to use them, and then BOOM, they print as the values they hold. It's really nice that
this didn't print `name is age years old, but he is still a hotness_scale out of 10 ont the hotness scale.` becuase that would be so dumb and worthless. Like what
would the point in variables even be?

## I Do NOT Want to Type That Many Commas
Ok fine, I'll show you a little trick. It's called *formatting*. Watch this:
###### Example 2.3
```python
name = "Chris Evans"
age = 39
hotness_scale = (2 * 4) + 1.9

print('{0} is {1} years old, but he is still a {2} out of 10 on the hotness scale.'.format(name, age, hotness_scale))
```
WOAH, what??? Calm down, I know that those curly braces look very intimidating but they are simple when you look at everything that is going on. Let's take a
look at the very end of the line. So we give the print statement the following string: `'{0} is {1} years old, but he is still a {2} out of 10 on the hotness scale.'`
which is fine and dandy, just like a normal print statement. If that's all we did there, then it would print with all of the curly braces in it, which would be
super duper ugly. But notice that the print statement doesn't end there. there is a call to `format` and we passed in our three variables. The order in which you
place these variables into the `format` function is very important. Look at how `name` is first. Now look back at the string and see that `{0}` is replaced with the
`name` variable. That is because `name` is the first variable passed.

## But... Why Zero?
Python, and most other programming languages, do something called **zero-based numbering**. That's a fancy way of saying that the first element of any list or structure
is at *index 0*. Here is a visual aid to help you comprehend what that means:
###### Your normal, human brain type list:
1. Eggs
2. Cheese
3. Milk

###### The computer, for some reason does this instead:
0. Eggs
1. Cheese
2. Milk

We will dive deeper into this and the implications of it later. Right now, you just wanna build a solid understanding of variables.

## Important Terms
When we talk about variables, we need to sound kinda smart. Or at least communicate well so people know what we are referring to. There are a few important distinctions
you should make when talking about variables, and not all of them actually apply to Python. First off with variables, you can `Declare`, `Initialize`, and `Assign`.
Declaration isn't really a concept in Python, but it is in other languages. Declaration is when you create a variable, but it has no value. In another language called
Java, you can delcare a variable like this:
###### Example 2.4
```java
String name;
```
As you can see, we never gave the `name` variable any value here. We just said that there is a `String` variable with the alias `name` and we will define its value
later. Initialization is more Pythonic. Every variable in Python is initialized. What that means is that we give it an initial value:
###### Example 2.5
```python
name = "Chris Evans"
```
Then there is variable assignment. An assignment is when you modify a variable to be something else than what it was initialized to be:
###### Example 2.6
```python
name = "Chris Evans"
new_name = "Steve Rogers"
name = new_name
```
We initialized `name` and `new_name` and then assigned the *value* of `new_name` to be the new value of `name`... because Chris Evans is now Steve Rogers forever.

There are also things called **constants** which are the *opposite* of variables. Their value cannot be changed. Again, in other languages you can specify that
a variable is a `const` and the code will not run if you try to change a `const`. In Python, we can mimic that behavior in a more complex manner that we can get
into when we start writing more complex code. For now, the best thing to practice is to name values you *don't* want changed in all caps, with underscores replacing
spaces: `SOCIAL_SECURITY = "51...sike"`

## Speaking of Names...
Let's talk about a couple of things. Python uses *snake case*. What the hell does that mean? It's a way to keep consistency in your code. When you name variables,
make all the words lowercase, and separate the words with underscores. Like `kitchen_timer`, `actor_name`, and `is_clear`. Variable names cannot start with numbers
or symbols, always a letter or word. Variable names can include numbers in them as long as they are not at the start. Also, naming your variables is very important.
Please be fairly verbose with your variable name choice; make your names explain themselves. A good name for a variable which would store the flavor of ice cream that
a customer wants would be something like `ice_cream_flavor`, not `x` or `icf` or `ice_crm_flvr`. Do not abbreviate, but get to the point. Variable names should not be too
long. This stuff is an art, people. 

## All The Right Types
You may notice, as you start to explore the world of programming a bit more, that other languages will require you to specify the `type` of a variable like such:
###### Example 2.7
  ```java
  String name = "Steve Rogers";
  ```
  That is a snippet of a variable initialization in Java. Notice the `String` at the beginning. That's because Java does not infer the type of a variable at the time
  of initialization. Python has type inference, which means you don't specify the type. Python is smart enough to infer the type of your variables. That's also why
  you can declare variables in Java, but not Python. So it's nice, but not the best.

## Further Explorations
###### Complete the following problems to show you actually learned anything
Use the following info for the exploration problems:
`My name is Cameron. I am 21 years old. I love chocolate. My favorite number is the result of 2 * 11.`
0. Store my name, age, whether or not I love chocolate (hint: this is a yes or no question...), and my favorite number (do the calculation in the variable assignment!)
as *variables* named: `name`, `age`, `chocolate_lover`, and `favorite_number`
1. Print `Welcome to the Avengers, Cameron`
2. Now print `Cameron, you are only 21. To be an Avenger, you have to pass a test` using the `format()` function to pass in variables
3. Now, print `Cameron, at 21 you have passed the test because your favorite number is 22, and because you have a True love for chocolate.` using the `format()` function
to pass in variables. You will use EVERY variable for this last one. Look closely.
4. Name a constant variable that will store the side length of a Rubik's Cube, and then initialize it with a value of 6.
5. Does Python allow for variable declarations? If not, explain why, and what it would need in order to allow them.
