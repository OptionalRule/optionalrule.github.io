---
layout: post
title: On Die Averages and Hit Points in 5e
date: 2021-06-22 09:32
category: Analysis
author: Scott Turnbull
summary: A breakdown of how we arrive at die result average numbers, and how that can cause errors in rolling HP and designing monsters.
image: /assets/img/skillcheck-480x363.jpg
---
I've had a few conversations in the passing months about average values on dice and how that relates to hit points in 5e. Word of warning, this is about to lean hard into some nerd stuff.  However, as esoteric as this may seem, it directly effects monster design and play frequently. The biggest impact it seems to have is when people try to anticipate the outcome of a roll, worse if they design a rule around it. Also, this can result in either getting player hit points or monster hit points wrong when using average results.  The solution isn't as complex as this is going to make it seem, I'm just laying out the specifics so it's all apparent.

**aside** I'm using the output from a simple Jupyter notebook script to demonstrate some of the math. Thanks for indulging me a bit, but I hope this makes the math clear. Also, I just kind of wanted to see if I could write a whole blog post in Jupyter.

```python
import pandas as pd
import numpy as np
```

## Dice Averages

A common point of confusion for people are the values given for averages on various dice.  People see the average of 1d6 listed at 3.5 or 4 and seem confused as some expect the value to be 3. This is a common logical error people make because they are just dividing 6 by 2 in their head and getting 3, but that's now what an average is.  An average is the sum of all possible results divided by the total number of values. In this case 1 through 6. Lets demonstrate below:

### D8 Done Wrong
This is an example of the math where people can go wrong.  Just dividing by 2 isn't an average and has the effect of assuming 
zero is included in the set of numbers, obviously that isn't true.  (Even on a d10, as the 0 usually represents 10)
{% include imageframe.html
  figure_class="float-end ms-4"
  src="/assets/img/skillcheck-480x363.jpg"
  alt="A group of adventurers leaning over a table, seemingly confused by a map they are looking at"
  height="363" width="480"
  caption="Image credit Wizards of the Coast"
 %}
```python
# Quick pandas code
# Using incorrect assumptions on 1d8
d8_wrong = [0, 1, 2, 3, 4, 5, 6, 7, 8]
d8w = pd.Series(d8_wrong)
d8w.mean()
```
    > mean     4.000000

### D8 Done Right
```python
# The correct way, listing only actual results on the die.
d8_right = [1, 2, 3, 4, 5, 6, 7, 8]
d8 = pd.Series(d8_right)
d8.mean()
```
    > mean     4.50000


This same pattern is repeated for every die type in the game. (i.e. 1d8, 1d10 ...).  Obviously a die can't roll a half value, 
so on any single result the value for average is rounded to the nearest, which is 5 in this case. That's how the average
roll on 1d8 is determined to be a 5.

## Single Rolls vs Multiple Dice Rolls

It's important to understand that while the average applies to a single die roll, it is not so when totaling multiple dice.  That is to say that the average of 3d6 is not 12 (3 * 4) but 11 (3 * 3.5 rounded up).  This difference introduces some confusion between determining average player hit points and average monster hit points.  The TLDR answer is that players calculate hit points discretely every level, while monsters are just determined at their CR. (Though frankly if you're a
TLDR kind of person, I don't know how you got down here)

## The confusion of Hit Points

In using these values, a bit of confusion comes in when we start to talk about how average Player Hit Points are
calculated as opposed to how average Monster Hit Points are determined.  The general difference is that player Hit
Points are calculated discreetly per level, whereas Monster Hit Points are just a sum of the average.

This is less confusing than it sounds and just means that players add the total of a hit die rolled at each level, while
monsters are just a quick sum of all their hit dice.  Taking the example of 1d8 for player hit points, they use the max
value at 1st level, so this is 8. If the player takes the average value, that means every level thereafter they would
add the average of 1d8, which is 4.5.  Since 4.5 isn't an actual value on 1d8 they round up; this is one of the
exceptions to the rounding rules in 5e.

### Example Average Player Hit Points

Lets start with an example that assumes a 5th level player with a +1 con mod. They apply the max roll at 1st level, then
add the average value of the HD rounded up at each subsequent level, and add 5 for their con bonus.


```python
player_hp = d8.max() + 4.0 * np.ceil(d8.mean()) + 5.0
player_hp
```
    33.0

Since the average of 4.5 is rounded up each roll to 5, this gives players taking the average hit points every level a
slight mathematical advantage over players who roll *on average*. However, the rolled set is so low and variance so high
that real world results are going to differ on a character by character basis.

A house rule I use in my own games is that players can either take the average hit points per level *OR* roll, but they
all have to choose the same method.  I also allow the to reroll any 1s. This creates an interesting social dynamic for
me as a DM.  This feels good for the players and is about the same in terms of the average expected roll, the mean of 1d8 shifts only from 4.5 to 4.93 and both round up to 5.  However there is a *slight* decrease in the chance of a low result and the same chance of a high result so the low end risk is a bit more shallow.

```python
d8_house_rule_values = [4.5, 2, 3, 4, 5, 6, 7, 8]
d8_house_rule = pd.Series(d8_house_rule_values)
d8_house_rule.max() + 4.0 * np.ceil(d8_house_rule.mean()) + 5.0
```
    33.0

However, it's not so simple from a players point of view.  Perceptions of agency, risk vs reward, and the gamblers
fallacy all combine to make an interesting party debate. They **feel** a sense of tension about this choice, and as if 
something good was given them, which I think is generally good for a game.  The metagame benefit I get as a DM is that 
this gives the players something to debate right out of the gate in a new campaign. Which means they start working out how to negotiate as a party
immediately.

### Example Average Monster Hit Points

The average monster hit points are much more simple.  However, the difference in how these are determined and how player
average hit points are determined causes some confusion. In this case we don't worry about determining the actual hit
points at each level or maxing out at first.  Monsters aren't supposed to be that complex.  Therefore, all we do is
multiply the average hit die value by the number of monster HD.

For consistency, lets take a Bugbear as an example. They are 5d8 HD creature with a +1 con mod, but the average hit
points will be different from that of a player character.

```python
bugbear_hp = 5.0 * d8.mean() + 5.0
np.floor(bugbear_hp)
```
    27.0

# Conclusion
 That seems like a lot but it's really just expressing the core ideas about why some misunderstandings arise and design faults creep in.  Once you get the right concept framed in your head it's not all that difficult but walking through the details can help some folks understand.  Having had this coversation several times recently, I thought I'd take the quick code I used during one of those discussions to throw up a blog post.