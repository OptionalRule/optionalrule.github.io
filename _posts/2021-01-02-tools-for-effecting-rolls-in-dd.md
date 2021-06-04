---
title: 'Tools to Affect Rolls in D&D'
author: Scott
type: post
date: 2021-01-02T16:57:52+00:00
url: /2021/01/02/tools-for-effecting-rolls-in-dd/
nb_of_words:
  - 618
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
Owing to a small thread on <a rel="noreferrer noopener" href="https://twitter.com/optionalrule/status/1345183662703337472" target="_blank">twitter</a> earlier this week, I listed out the options 5th Edition Dungeons and Dragons provides for effecting rolls. This is useful for creating your own roll effecting homebrew rules, if you want to understand the relative power level compared to other elements in the ruleset.

Before diving into the list it&#8217;s important to draw a distinction between two different meta-classes of roll modifications in 5th edition. Those are modifications that **add to the result** of a die roll, and modifications that **replace the value** of the die roll. This is important for rolls that can produce a critical success, as rolls that replace a value give more opportunities to score a critical. So when ranking the value of a role modification, it&#8217;s important to know if the roll can critically succeed or not.

It&#8217;s also worth noting that not all roll benefits are equal so it&#8217;s not as straightforward to compare benefits. Advantage for instance would seem to provide a statistical equivalent lower then the +5 referenced in the system, however advantage doesn&#8217;t just provide a bonus to the roll, it turns a linear probably distribution to a slightly curved one. See the posts I link near the bottom of the article since the importance of this depends largely on the DC of the roll. The point here being not all benefits are so easily compared and it speaks a bit to the wonderful complexity of making things work in a 5th edition game.

These are the levels of dials and levers for 5th edition rolls to consider to guide your house rule design: 

**Ranked by effect on normal rolls.**

  * Bardic Inspiration (lvl 5/10/15):+d8/ +d10/+d12
  * Advantage
  * Bardic Inspiration (lvl1/5): +d6 
  * Guidance/Bless: +d4
  * Luck: (reroll 1s)
  * Bane: -d4 (and Half Cover)
  * Disadvantage (and Three-Quarters Cover)

**Ranked by effect on rolls that can have a critical success.**

<ul id="block-1280d90c-351d-4509-bc06-8bc04b502864">
  <li>
    Elven Accuracy
  </li>
  <li>
    Advantage
  </li>
  <li>
    Bardic Inspiration (All)
  </li>
  <li>
    Guidance/Bless: +d4
  </li>
  <li>
    Luck: (reroll 1s)
  </li>
  <li>
    Bane: -d4 (and Half Cover)
  </li>
  <li>
    Three-Quarters Cover
  </li>
  <li>
    Disadvantage
  </li>
</ul>

Note I&#8217;m including cover here, which doesn&#8217;t actually modify the die roll but adds to AC, which is an indirect way to modify an attack roll so I&#8217;m including it as a relative comparison.

Further note, in terms of its benefit to a roll that can critically hit, Luck is rather hard to rank as a rerolled one might actually result in a critical so there&#8217;s a good argument to be made to putting this higher on the list.

In a debate about what the actual outcome of Elven Accuracy might be, I did some quick scripting to simulate 100k rolls to find out what the median result would be of a roll, and what percentage of rolls would crit if it were an attack. Anyone interested in the sloppy code I put together to do this simulation can view it online <a rel="noreferrer noopener" href="https://onlinegdb.com/BJi8LL06D" target="_blank">here</a>. The results of that were interesting to me and might help you assess the various impact of roll modifications you might be considering for your house rules.

  * Median roll with Eleven Accuracy is 16.0 and 14% are crits.
  * Median roll with Advantage is 15.0 and 10% are crits.
  * Median roll on a normal 1d20 is 11.0 and 5% are crits.
  * Median roll with Disadvantage is 6.0 and 0% are crits.

Just a note on criticals and disadvantage, since I get the question. It&#8217;s just reading as 0%, there is actually some minimal number rounding to zero. Locally, at disadvantage the only way you crit is by rolling double 20s which is a 1 in 400 chance, so roughly 0.25%.

There&#8217;s a great additional take on rolls and outcomes by <a rel="noreferrer noopener" href="https://twitter.com/thedicemechanic" target="_blank">@TheDiceMechanic</a> over on their blog you might want to check out titled <a rel="noreferrer noopener" href="https://dicemechanic.wordpress.com/2014/09/23/advantage-to-the-max/" target="_blank">Advantage to the Max</a> as well. It explores another important consideration in roll modifications, how many rolls would be below 10.