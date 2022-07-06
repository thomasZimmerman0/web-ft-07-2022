# Homework

## Python 101

#### 1. Tip Calculator

Your task is to write a program that calculates how much of a tip to leave at a restaurant.

Prompt the user for two things:

- The total bill amount
- The level of service, which can be one of the following: good, fair, or bad

Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

- good -> 20%
- fair -> 15%
- bad -> 10%

Example session:

```
$ python3 tip_calc.py
Total bill amount? 100
Level of service? good
Tip amount: $20.00
Total amount: $120.00
```

```
$ python3 tip_calc.py
Total bill amount? 48
Level of service? bad
Tip amount: $4.80
Total amount: $52.80
```

Hints:

- Remember that you need to convert the input from the user input to floats instead of ints. Use the `float` function instead of the `int` function.
- To format a float number as a dollar value, use Python's formatting syntax: `"%.2f" % amount`

#### 2. Tip Calculator 2

Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:

```
$ python3 tip_calc2.py
Total bill amount? 100
Level of service? good
Split how many ways? 5
Tip amount: $20.00
Total amount: $120.00
Amount per person: $24.00
```

#### 3. How many coins?

Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:

```
$ python3 coins.py
You have 0 coins.
Do you want another? yes
You have 1 coins.
Do you want another? yes
You have 2 coins.
Do you want another? no
Bye
```

#### 4. Print a Box

Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

```
$ python3 box.py
Width? 6
Height? 4
******
*    *
*    *
******
```

#### 5. Print a Triangle

Print a triangle consisting of * characters like this:

```
   *
  ***
 *****
*******
```

#### 6. Multiplication Table

Print the multiplication table for numbers from 1 up to 10. Example output:

```
$ python3 multiplication_table.py
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
...
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
...
10 X 8 = 80
10 X 9 = 90
10 X 10 = 100
```

## Submit Homework
- Create an issue
- Title issue: Python101_[YourName] i.e. Python101_VeronicaLino