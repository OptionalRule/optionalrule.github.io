---
title: 'Simulating Sadness: Great Weapon Fighter Damage'
author: Scott Turnbull
layout: post
date: 2021-01-07T15:52:51+00:00
url: /2021/01/07/simulating-great-weapon-fighter-damage/
select_gallery_type:
  - slideshow
hide_featured_image:
  - no
show_post_header:
  - yes
show_post_header_logo:
  - yes
hide_post_sidebar:
  - no
full_width_post_content:
  - no
show_in_featured_slider:
  - no
categories:
  - RPG Resources

---
I have always had a bit of doubt about the overall benefit of the Great Weapon Fighter fighting style and the Improved Critical ability for Champions in 5th Edition Dungeons and Dragons, so I dig into it a bit below. 

<div class="wp-block-image">
  <figure class="alignright size-large"><img loading="lazy" width="384" height="301" src="https://optionalrule.com/wp-content/uploads/2020/12/grog_by_nickroblesart_sm.jpg" alt="Grog by Nick Robles" class="wp-image-129" srcset="https://optionalrule.com/wp-content/uploads/2020/12/grog_by_nickroblesart_sm.jpg 384w, https://optionalrule.com/wp-content/uploads/2020/12/grog_by_nickroblesart_sm-300x235.jpg 300w" sizes="(max-width: 384px) 100vw, 384px" /></figure>
</div>

In terms of damage, Great Weapon fighter letting you reroll a one or two seem okay, but you have to keep the result of whatever the reroll is. Not only might this not change the result but if you roll a 2 the first time, and a 1 on the reroll you&#8217;re actually doing **LESS** damage on the roll. 

The ability of Champions to score a critical on a 19 or 20 sounds fine but I think this fails Fighter classes because dice are generally not where the fighters damage is and they spread that damage out across multiple attacks as they level. This means that doubling the weapon damage dice from a critical has a relatively small effect. It also means that the increased chance of a critical is limited by relatively small number of dice bound to a single attack roll.

In any case, I didn&#8217;t want to just theorize what the actual effect on average damage would be so I setup a small bit of code to simulate a million damage rolls and calculate the mean. Below is the resulting data from that simulation. The mean of the damage output was simulated for the **Base** weapon damage, Base Weapon Damage with a chance of critical on a **20**, and Base Weapon Damage with a chance of critical on **19** and above. I did this both for a **Normal** fighter and again for a fighter with the great weapon fighting style (**GWF**)

**Normal**

<div class="wp-block-getwid-table">
  <table>
    <tr>
      <td style="background-color:#abb8c3">
        <strong>Weapons</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Damage</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Base</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>20</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>19</strong>
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000;padding-right:37px">
        Greatclub, Quarterstaff
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d8
      </td>
      
      <td style="text-align:center;border-color:#000">
        4.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        4.3
      </td>
      
      <td style="text-align:center;border-color:#000">
        4.9
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Glaive, Halberd, Longsword, Pike, Warhammer
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d10
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.8
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.1
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greataxe
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d12
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.8
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.1
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greatsword, Maul
      </td>
      
      <td style="text-align:center;border-color:#000">
        2d6
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.0
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.4
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.7
      </td>
    </tr>
  </table><figcaption>
  
  <strong>Table1.</strong> Mean damage of two-handed weapons <strong><em>without</em></strong> Great Weapon Fighting (Normal)</figcaption>
</div>

**GWF**

<div class="wp-block-getwid-table">
  <table>
    <tr>
      <td style="background-color:#abb8c3">
        <strong>Weapons</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Damage</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Base</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>20</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>19</strong>
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000;padding-right:37px">
        Greatclub, Quarterstaff
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d8
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.3
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.8
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Glaive, Halberd, Longsword, Pike, Warhammer
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d10
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.3
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.1
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.9
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greataxe
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d12
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.3
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.7
      </td>
      
      <td style="text-align:center;border-color:#000">
        8.1
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greatsword, Maul
      </td>
      
      <td style="text-align:center;border-color:#000">
        2d6
      </td>
      
      <td style="text-align:center;border-color:#000">
        8.3
      </td>
      
      <td style="text-align:center;border-color:#000">
        8.8
      </td>
      
      <td style="text-align:center;border-color:#000">
        9.2
      </td>
    </tr>
  </table><figcaption>
  
  <strong>Table 2</strong>. Mean damage of two-handed weapons <strong><em>with</em></strong> Great Weapon Fighting (GWF)</figcaption>
</div>

Given the relatively small benefit of these differences, and the general disruption of flow at the table as a player manages dice that need to be rerolled, these abilities seem questionable in value to the game. Perhaps I&#8217;m missing something about the numbers but that is my take after looking at the numbers. 

## House Rules {#h-house-rules}

It&#8217;s 5th edition right? so everyone&#8217;s first response is to create a fix through a house rule. I&#8217;ve seen two house rules frequently suggested, I&#8217;m not sure if people are using them or not so drop me an <a rel="noreferrer noopener" href="https://www.twitter.com/optionalrule" target="_blank">@ on twitter</a> with your experiences if you do. The two house rules I&#8217;ve seen are:

  1. When you roll a 1 or 2 you can roll the die again and add the value to the previous roll. 
  2. When you roll a 1 or a 2 you can reroll the die, keeping the higher of the two die results.

So let&#8217;s take a look at the results of these rules.

### Adding the rerolled die to the original result  {#h-adding-the-rerolled-die-to-the-original-result}

<div class="wp-block-getwid-table">
  <table>
    <tr>
      <td style="background-color:#abb8c3">
        <strong>Weapons</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Damage</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Base</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>20</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>19</strong>
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000;padding-right:37px">
        Greatclub, Quarterstaff
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d8
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.6
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.9
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.2
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Glaive, Halberd, Longsword, Pike, Warhammer
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d10
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.6
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.9
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.3
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greataxe
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d12
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.6
      </td>
      
      <td style="text-align:center;border-color:#000">
        8.0
      </td>
      
      <td style="text-align:center;border-color:#000">
        8.3
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greatsword, Maul
      </td>
      
      <td style="text-align:center;border-color:#000">
        2d6
      </td>
      
      <td style="text-align:center;border-color:#000">
        9.3
      </td>
      
      <td style="text-align:center;border-color:#000">
        9.8
      </td>
      
      <td style="text-align:center;border-color:#000">
        10.2
      </td>
    </tr>
  </table><figcaption>
  
  <strong>Table 3.</strong> GWF house rule option &#8211; adding damage.</figcaption>
</div>

I&#8217;m not a huge fan of this, even though it&#8217;s a bit more powerful than the vanilla rule. Sure it provides a slight bump but it seems fairly weak tea compared to the single weapon Dueling fighting style that gets a flat +2 to damage and still gets to use a shield (you know that right?). 

### Rerolling until you get a higher result {#h-rerolling-until-you-get-a-higher-result}

<div class="wp-block-getwid-table">
  <table>
    <tr>
      <td style="background-color:#abb8c3">
        <strong>Weapons</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Damage</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>Base</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>20</strong>
      </td>
      
      <td style="text-align:center;background-color:#abb8c3">
        <strong>19</strong>
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000;padding-right:37px">
        Greatclub, Quarterstaff
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d8
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        5.8
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.1
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Glaive, Halberd, Longsword, Pike, Warhammer
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d10
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        6.8
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.2
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greataxe
      </td>
      
      <td style="text-align:center;border-color:#000">
        1d12
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.5
      </td>
      
      <td style="text-align:center;border-color:#000">
        7.9
      </td>
      
      <td style="text-align:center;border-color:#000">
        8.3
      </td>
    </tr>
    
    <tr>
      <td style="border-color:#000">
        Greatsword, Maul
      </td>
      
      <td style="text-align:center;border-color:#000">
        2d6
      </td>
      
      <td style="text-align:center;border-color:#000">
        9.0
      </td>
      
      <td style="text-align:center;border-color:#000">
        9.4
      </td>
      
      <td style="text-align:center;border-color:#000">
        9.9
      </td>
    </tr>
  </table><figcaption>
  
  <strong>Table 4.</strong> GWF house rule option &#8211; GWF rerolling damage.</figcaption>
</div>

I&#8217;m even less a fan of this rule. I honestly can&#8217;t believe people do this but I hear about it enough to think I should include it. The interruption of a player examining the outcome of each of their die rolls, rerolling and examining that, and rerolling again, seems not worth the interruption to combat turns. It makes very little comparative difference for the effort, and it only even seems a bit useful in the context of a Champion, which I would recommend become a subclass feature if I thought the rule worthwhile at all.

## Swing and a Missed Opportunity {#h-swing-and-a-missed-opportunity}

Overall I feel like Great Weapon Fighter was a missed opportunity in 5th edition. A weak damage bonus is a counter to the notion of powerful attacks the fighting style evokes. I think this is falling victim to the notion that Battlemaster has to have all the combat maneuvers and would much rather have seen Great Weapon Fighter dominate the battlefield with abilities that pointed to power or burst damage. A fix would go beyond the complexity of a simple house rule, but I&#8217;d have preferred to see something like cleve options, knocking opponents down, or even something out of the box like a times per long rest damage add similar to a Paladin&#8217;s smite (Paladin&#8217;s still retain the upper hand since theirs overcomes damage resistance in many cases).

Regardless, I&#8217;d like to hear what you think or how you handle it so hit me up and let me know.