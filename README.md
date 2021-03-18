# shrek-bot / @shrekframe
A Python script that first generates every Shrek frame, then tweets five frames at a time. Uses FFmpeg and Tweepy.

My most recent bot, and what I would consider, my second success in bot making. This bot works in two steps.
1. First, I decided to generate each frame of the Shrek movie, and save them into different folders (seperating each by 1000 frames). The different folders ensure that nothing crashes when you decide to open a folder containing 129,000+ images. 
2. Second, after generating, you tweet at your desired interval. I decided to take a hint [from this account](http://www.twitter.com/sbframesinorder) and tweet five frames every thirty minutes. I use a seperate text file that simply keeps track of which frame I'm on.

This bot uses crontab, a Unix tool that allows you to schedule different tasks at specified times. 

## Lastly...
To view this bot in action, [click here.](http://www.twitter.com/shrekframe)
