# shrek-bot / @shrekframe
A Python script that first generates every Shrek frame, then tweets five frames at a time. Uses FFmpeg and Tweepy.

My most recent bot, and what I would consider, my second success in bot making. This bot works in two steps.
1. First, I decided to generate each frame of the Shrek movie, and save them into different folders (seperating each by 1000 frames). The different folders ensure that nothing crashes when you decide to open a folder containing 129,000+ images. 
2. Second, after generating, you tweet at your desired interval. I decided to take a hint [from this account](http://www.twitter.com/sbframesinorder) and tweet five frames every thirty minutes. I use a seperate text file that simply keeps track of which frame I'm on.

This bot uses crontab, a Unix tool that allows you to schedule different tasks at specified times. 

## Going Viral 🦠
So far,
1. [Shrek's butt](https://twitter.com/shrekframe/status/1366599164654665740). Crude, but I'll take it. Even got a [shoutout from the DreamWorks Animation account](https://twitter.com/dreamworks/status/1367657753385205763). Over 11 million impressions, 25k tweets, and 210k likes. Not a bad day for the bot business.
2. Not as viral, but [Shrek striking a pose](https://twitter.com/shrekframe/status/1366810589595590658) still garnered significant attention. 10k retweets and a little less than 75k likes.

## Lastly...
To view this bot in action, [click here.](http://www.twitter.com/shrekframe)
