---
title: 'Simulating Sadness: Great Weapon Fighter Damage'
author: Scott Turnbull
layout: post
image: /assets/img/grog_by_nickroblesart-384x301.jpg
description: An breakdown and analysis of the outcomes of different options related to the Great Weapon Fight feat in 5th edition.
categories:
  - Analysis

---
I have always had a bit of doubt about the overall benefit of the Great Weapon Fighter fighting style and the Improved Critical ability for Champions in 5th Edition Dungeons and Dragons, so I dig into it a bit below. 

In terms of damage, Great Weapon fighter letting you reroll a one or two seem okay, but you have to keep the result of whatever the reroll is. Not only might this not change the result but if you roll a 2 the first time, and a 1 on the reroll you&#8217;re actually doing **LESS** damage on the roll. 

{% include imageframe.html
  figure_class="float-end ms-4 clearfix"
  src="/assets/img/grog_by_nickroblesart-384x301.jpg"
  alt="A goliath barbarian leaping in the air about to strike with their axe."
  width="384" height="301"
  caption="Image Credit Nick Robles"
 %}

The ability of Champions to score a critical on a 19 or 20 sounds fine but I think this fails Fighter classes because dice are generally not where the fighters damage is and they spread that damage out across multiple attacks as they level. This means that doubling the weapon damage dice from a critical has a relatively small effect. It also means that the increased chance of a critical is limited by relatively small number of dice bound to a single attack roll.

## The Math

I'm adding this section in June of 2021 because people complain about wanting the math instead of a simulation so I'll add that here.  Based on this thread from [rpg.stackexchange](https://rpg.stackexchange.com/questions/47172/how-much-damage-does-great-weapon-fighting-add-on-average), this is a table of the difference in damage per die type with great weapon fighting.  In the criticals it's doubling the difference 5% of the time normally and 10% of the time when a champion subclass. Simulation or math the conclusions are the same in either case.

|Die Type|Difference|
|--- |:---: |
|1d4|0.50|
|1d6|0.67|
|1d8|0.75|
|1d10|0.80|
|1d12|0.83|
|2d6|1.32|
{: .table .table-striped .table-hover .data-table .table-fluid }

***

## The Simulation

In any case, I just wanted to have a bit of fun so I setup a small bit of code to simulate a million damage rolls and calculate the mean. Below is the resulting data from that simulation. The mean of the damage output was simulated for the **Base** weapon damage, Base Weapon Damage with a chance of critical on a **20**, and Base Weapon Damage with a chance of critical on **19** and above. I did this both for a **Normal** fighter and again for a fighter with the great weapon fighting style (**GWF**)
{: .clearfix .w-100 }

**Table1.** Mean damage of two-handed weapons ***without*** Great Weapon Fighting (**Normal**)

|Weapons|Damage|Base|20|19|
|--- |--- |--- |--- |--- |
|Greatclub, Quarterstaff|1d8|4.5|4.3|4.9|
|Glaive, Halberd, Longsword, Pike, Warhammer|1d10|5.5|5.8|6.1|
|Greataxe|1d12|6.5|6.8|7.1|
|Greatsword, Maul|2d6|7.0|7.4|7.7|
{: .table .table-striped .table-hover .data-table }

***

**Table 2**. Mean damage of two-handed weapons ***with*** Great Weapon Fighting (**GWF**)

|Weapons|Damage|Base|20|19|
|--- |--- |--- |--- |--- |
|Greatclub, Quarterstaff|1d8|5.3|5.5|5.8|
|Glaive, Halberd, Longsword, Pike, Warhammer|1d10|6.3|6.1|6.9|
|Greataxe|1d12|7.3|7.7|8.1|
|Greatsword, Maul|2d6|8.3|8.8|9.2|
{: .table .table-striped .table-hover .data-table }

Given the relatively small benefit of these differences, and the general disruption of flow at the table as a player manages dice that need to be rerolled, these abilities seem questionable in value to the game. Perhaps I&#8217;m missing something about the numbers but that is my take after looking at the numbers. 

## House Rules

It&#8217;s 5th edition right? so everyone&#8217;s first response is to create a fix through a house rule. I&#8217;ve seen two house rules frequently suggested, I&#8217;m not sure if people are using them or not so drop me an <a rel="noreferrer noopener" href="https://www.twitter.com/optionalrule" target="_blank">@ on twitter</a> with your experiences if you do. The two house rules I&#8217;ve seen are:

  1. When you roll a 1 or 2 you can roll the die again and add the value to the previous roll. 
  2. When you roll a 1 or a 2 you can reroll the die, keeping the higher of the two die results.

So let&#8217;s take a look at the results of these rules.

**Table 3.** GWF house rule option &#8211; Adding the rerolled die to the original result

|Weapons|Damage|Base|20|19|
|--- |--- |--- |--- |--- |
|Greatclub, Quarterstaff|1d8|5.6|5.9|6.2|
|Glaive, Halberd, Longsword, Pike, Warhammer|1d10|6.6|6.9|7.3|
|Greataxe|1d12|7.6|8.0|8.3|
|Greatsword, Maul|2d6|9.3|9.8|10.2|
{: .table .table-striped .table-hover .data-table }


I&#8217;m not a huge fan of this, even though it&#8217;s a bit more powerful than the vanilla rule. Sure it provides a slight bump but it seems fairly weak tea compared to the single weapon Dueling fighting style that gets a flat +2 to damage and still gets to use a shield (you know that right?). 

***Table 4.*** GWF house rule option &#8211; GWF rerolling until you get a higher result.

|Weapons|Damage|Base|20|19|
|--- |--- |--- |--- |--- |
|Greatclub, Quarterstaff|1d8|5.5|5.8|6.1|
|Glaive, Halberd, Longsword, Pike, Warhammer|1d10|6.5|6.8|7.2|
|Greataxe|1d12|7.5|7.9|8.3|
|Greatsword, Maul|2d6|9.0|9.4|9.9|
{: .table .table-striped .table-hover .data-table }
  
I&#8217;m even less a fan of this rule. I honestly can&#8217;t believe people do this but I hear about it enough to think I should include it. The interruption of a player examining the outcome of each of their die rolls, rerolling and examining that, and rerolling again, seems not worth the interruption to combat turns. It makes very little comparative difference for the effort, and it only even seems a bit useful in the context of a Champion, which I would recommend become a subclass feature if I thought the rule worthwhile at all.

## Swing and a Missed Opportunity

Overall I feel like Great Weapon Fighter was a missed opportunity in 5th edition. A weak damage bonus is a counter to the notion of powerful attacks the fighting style evokes. I think this is falling victim to the notion that Battlemaster has to have all the combat maneuvers and would much rather have seen Great Weapon Fighter dominate the battlefield with abilities that pointed to power or burst damage. A fix would go beyond the complexity of a simple house rule, but I&#8217;d have preferred to see something like cleve options, knocking opponents down, or even something out of the box like a times per long rest damage add similar to a Paladin&#8217;s smite (Paladin&#8217;s still retain the upper hand since theirs overcomes damage resistance in many cases).

Regardless, I&#8217;d like to hear what you think or how you handle it so hit me up and let me know.