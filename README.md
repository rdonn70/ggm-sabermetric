# The "Get Good Metric" (GGM) Baseball Sabermetric  
![get_good_metric](https://github.com/user-attachments/assets/a3488bac-292c-4687-8cd3-f2353f410b5f)
  
I was kind of bored one night and decided to have some fun by making this metric. Program works well enough, produces some surprising (and not so surprising) results, and heavily favors older baseball players (such as those in the late 1800s and early 1900s) before they started recording stats like SF, SH, GIDP, etc.  
You could probably simplify this equation down to the version "GGM = ((H+BB)/(AB+BB))-(SO/AB)" for all players, if you care about an "even playing field" for comparing newer players to older players.
  
## Design Philosophy  
I believe viewers of modern baseball have become disillusioned by the spectacle of home runs and big hits, while ignoring the fact that home run hitters often swing big and strike out, and I wanted to try and quantify this observation and rank players based on how much of a "pure hitter" they are.  
  
Enter the "Get Good Metric" or "GGM" for short (yeah, terrible name, feel free to name it something else). This metric takes a quasi-hybridization of OBP and adds a negative modifier to punish those who are undisciplined at the plate.  
Avoid looking at this metric as a way to define how "valuable" a player is, simply look at it as an interesting ranking of players based on their pure hitting ability... actually, maybe just avoid looking at this metric altogether...  
  
## Equation Breakdown
(H+BB+IBB) / (AB+BB) : Rewards hits, walks, and a little add-on bonus for intentional walks (because, wow, you're really intimidating to get intentionally walked!).  
-(SO+SF+SH+(2*GIDP)) / AB : Punishes the player for Strikeouts (duh), Sacrifice Flies (in my opinion, if you're gonna swing at the ball, make sure you actually hit it good), Sacrifice Hits (I don't believe in bunting), and a mega punishment for grounding into a double play (terrible, no good, very bad).  
  
This all comes together to form the Get Good Metric and produce some interesting results. Here's some examples (the higher the number, the better):
  
#1: John McGraw, 0.399407  
...  
#23: Ted Williams, 0.343083  
...  
#116: Joe DiMaggio, 0.300424   
...  
#124: Babe Ruth, 0.299494  
...  
#130: Barry Bonds, 0.298815  
...  
#159: Tony Gwynn, 0.293706  
...  
#1098: Hank Aaron, 0.220666  
...  
#1364: Rickey Henderson, 0.208686  
...  
#1844: Mickey Mantle, 0.188088  
...  
#3630: Mike Trout, 0.11997  
...  
#5546: Shohei Ohtani, 0.048731  
...  
#6497: Aaron Judge, 0.00253  
...  
#9393 Mike Thurman, -0.75235  
  
## Notes about Results...  
It should be noted that this data (seen in results.csv) was conducted using the attached python script (ggm-calculator.py) created by me, with statistical data provided by Sean Lahman (http://www.seanlahman.com/). The program I made only considers players that have at least 100 ABs. This data also has a Max Value of 0.399407 (John McGraw) and a Min Value of -0.75235 (sorry Mike Thurman).  
As previously stated, I made this in one night and spent approximately 40 minutes on this project, so if something is wrong with the program, data, reasoning, or something else entirely, please let me know. :)  
