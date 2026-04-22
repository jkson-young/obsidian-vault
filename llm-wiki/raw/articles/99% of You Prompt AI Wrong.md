---
title: "99% of You Prompt AI Wrong"
source: "https://www.youtube.com/watch?v=VnEoS2eQXsw"
author:
  - "[[Varun Mayya]]"
published: 2025-12-02
created: 2026-04-22
description: "In this video, we’re going over some of the best prompt tips I’ve come to know. We first look at how prompt engineering is kinda like “world-building” where ..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=VnEoS2eQXsw)

## Transcript

### Introduction

**0:00** · So if you remember my conversation with Sam Alman from earlier this year, we were talking about what new jobs has AI created. Sam responded, well, the first example we saw of that was prompt engineer.

**0:10** · When he said that, I think some of the responses were, hey, maybe this is actually a new job. And some of the other responses are like no way this is a job. Like how can you call just prompting, typing out sentences, it doesn't feel like you're doing any work.

**0:22** · It's not a big deal. But actually, as I've been looking at people at my own company and now 500 people plus, right?

**0:27** · Some of them work very closely with AI.

**0:29** · Some of them don't use AI. I've just seen that the difference between somebody who can communicate what they want very very clearly to an AI knows how all these models are very different from each other and that \[music\] different prompt patterns give you different outputs. I can now tell the kind of people in the company who can consistently \[music\] create awesome stuff with or without AI and at the same time I can see the people who can't actually use AI to its maximum benefit. And strangely enough the people who are capable of using AI and do wonderful stuff are also very good managers. Right?

**0:57** · So there is some overlap between the skill of a manager and a prompt engineer. \[music\] And what I wanted to do is I actually want to make two videos. This is the first one on how you can think about two different topics, right? One is prompting, the other one is writing. But this video I want to do about how to prompt. So if you are thinking about generating text, watch this video because I'll tell you a lot of what I figured out with prompting.

**1:21** · Quick shout out to today's sponsor, which is Intel. I'm going to show you all these prompts on an AI PC powered by Intel Core Ultra processors because the thing is today it doesn't really matter if you're using, you know, the best model in the world or an open source model. I feel that good prompters will get used to each of these models.

**1:37** · They're all slightly different from each other. The way you would prompt GPT is different from the way you' prompt Kimmy is different from the way you'd prompt Gemini. So, we're going to try showing you as many prompts that are generalized across all the models and then maybe one or two examples of specific ideas.

### World Building

**1:53** · A lot of prompting, and we'll cover this deeply in my writing video, but a lot of prompting is actually about world building. I want you to think of a story, a world where everything is made out of sand. It's a very dry world.

**2:07** · Moisture is a problem in this world. So, people wear suits to absorb moisture from the air. Now in this world there are big mountains made of sand \[music\] and there are four or five waring clans who are waring for some special \[music\] resource in the sand. Now I haven't given you much more data than this but if I asked you especially somebody who's a movie watcher if this world had giant creatures what would those creatures be?

**2:39** · Now if you answered the word sandworms then you are correct and not only would you have answered sandworms so would GPT or any other AI model. So what is \[music\] happening here? I gave you enough references of the world. I gave you you know some small piece of the puzzle little bit of the world. I gave you like piece here. I gave you piece here. I gave you a piece here. And I'm asking your brain to fill the rest of it in. What are you going to fill the rest of it in with? You're going to fill the rest of it with movies you've watched.

**3:02** · Right? You would have seen Dune at some point. and you've seen the trailers at some point and you'll be like, I remember what it's like. I've given you three pieces of puzzle. I'm prompting you. What just happened was me prompting you to use your brain to fill in the rest. Which is exactly what AI does, right? The more pieces of the puzzle you give, the more of the world you build on its behalf, the more it can fill in with something that matches your vision. The less of these puzzle pieces I give you, for example, let's say I never told you any of the first three pieces of information and I just told you there's a world and there are giant creatures in the world. What is the likelihood you would have said worm? The likelihood would have been nearly \[clears throat\] zero, right?

**3:33** · Just like AI, if you just told AI, hey, there's a world. Give me an idea for a big creature in the world.

**3:37** · It would have said some troll or cyclops or something else, right? But it wouldn't have immediately thought about sandworm. Now, either you can go in and say, give me a world like Dune because you know the word Dune because you watch the movies or you've read the books or you give it these pieces that it can stitch the world from. And I feel 99% of prompt engineering is stitching this world, which is a shocker because when I see people prompt engineering, it's this lazy prompt engineering, right? It's like, hey, just give me five ways to edit this video or give me five ideas for this. you know, you're not giving any of the puzzle pieces \[music\] and then you're expecting AI to give you exactly what you want and it's giving you something totally different.

**4:08** · So, what's happening, and you'll see this with a lot of people who make, you know, generic AI videos or generic AI text. It's \[music\] just you're not giving it enough information to fill in a world for you. And therefore, it is going to the most generic world it can think of, which is why everyone's AI output is starting to look the same because they're not putting any effort giving it the puzzle pieces in the first place.

**4:27** · This is the first thing you need to take away from this video, \[music\] which is it's your responsibility to world build, not the AIs. And the more pieces of the puzzle you give it, the more unique your world becomes. So I would always encourage people to first think about what they want from the AI and then think about the world. Now the way to give AI these puzzle pieces, there are many ways to do it. But the best way I found is just give it examples.

**4:45** · In fact, if you see most of the system prompts, whether you know it be some of these agents that are out there or you see some of these customized models that are out there, if you see Harvey, which is the legal AI, if you see system prompts for some of these, if you see system prompt for Bing and you study them, you realize it's a lot about example giving.

**5:01** · You'll say, "Hey, if the user asks you for this, reject it. If the user asks you for information on guns and bombs, don't respond or respond politely saying no." Right? It's just a series of sentences. And it's not actually very different from if else sentences we used to have in code, which is if the user says this, don't do this. But it's kind \[music\] of the same, but you're giving verbal instructions instead of writing syntax with if else. And I think this is very critical because giving examples \[music\] of what the user should do, what the user shouldn't do for system prompts actually makes or breaks the entire system. It's what actually makes some of these wrapper models different from each other.

**5:31** · You know, the system prompt shapes your direction of the user.

**5:34** · You're doing a little bit of world building in the system prompt, right?

**5:37** · You know, Bing has already made this wrapper saying this is my world. Now, you are constrained to the world that I've given you so that you know, you don't make crazy searches or whatever. I want to switch direction here and go into more prompting tips. I want this video to be more about specific things you can do with specific parts of AI.

### Deep Research

**5:53** · So, let's move on to the next piece, which is deep research. The way I use deep research is actually for summaries.

**5:59** · I will have this book. Okay, it'll be like 300, 400, 500 pages and maybe today I just want a summary of that book. So what I do is I put the name of the book into deep research. I'll go in there and I'll be like here's the book. I want three things from you. Firstly, summarize the book. Secondly, give me all the red pill insights. \[music\] What are the deep insights? Pull out those deep insights for me. And thirdly, give me actionable evidence from those insights. It gave me some wonderful insights. And I feel like if you don't go with this prompt, deep research will give you something very generic. It'll just give you like this soup of facts and there's nothing you can do about it.

**6:29** · You can't take anything back. Half of it is stuff you'll already know. That's why I asked for red pill insights, things that are slightly different from what other people believe in. And sometimes I ask this question in deep research as well, right? When you're giving me these outputs, give me things that most of the world doesn't believe in, but the book believes in. If you look at when I talk to CEOs, when I interview them, one of the questions I always ask is, what do you believe in that your peers don't believe in? Because I'm trying to find out how's the difference between what you think and what everybody else thinks. And I think that matters most, right? for success. It's almost like the differences lead to \[music\] success. So, I try to figure that out. I urge everyone, especially topics you don't know enough about, go to AI and ask you to break it down.

**7:00** · Break down the costs of everything. And I do this very often.

**7:03** · I just keep breaking down the cost of things. Like, for example, you have a lot of people on Reddit say, "Oh, aa game requires $100 million or whatever, right?" You can go to GPD today and you can say, "Break that $100 million down for me." And I've done this before, right? I'll tell you very quickly what it'll tell you. It'll tell you that $25 million goes into development budget, $75 million goes in marketing budget.

**7:20** · out of the $25 million you can break down the salaries one by one by one by one and you can see all the people and then you can ask it well if you were in India what are the salaries like now then it'll give you each of those salaries for those specific roles and what it'll do is it'll go look for the credits of multiple different games it'll see all their roles it will go find out the average salary of that role in the US then it'll find out the average salary of that role in India then it'll give you the totals and you do that you'll be like wait let's say a fresher computer science engineer in the US makes 150 to $200,000 a year about 1

**7:45** · to1 a half crores let's say in India a fresher would make generously \[music\] 6 to 10 lakhs a year Okay, as a fresher software engineer, this rule applies to all jobs, especially digital jobs in India, right? A designer costs much lesser in India than it costs in the US and so on and so forth. Why do you think it's not true for gamedev? So you find that the $25 million of gamedev budget is actually much cheaper in India to a factor of anywhere between 5 and 10. And then you say, wait, if these people are getting the exact same talent, then it's possible to do this at a much cheaper price. And then you can go break down the other $75 million of marketing budget and you can ask the $75 million, how much how many views does it get? How many wish list does it get? How many downloads does it end up leading to?

**8:16** · And you get out all those numbers. It'll go do deep research. It'll find out Mafia the game, for example, had 2 \[music\] million wish lists. Probably got 100 million impressions, right, across the internet to get through those 2 million wish lists. And then that 2 million wish list led to whatever, $30 million in revenue. You can do this math. And I think this is very, very important for you to do because we often say things that we don't understand. \[music\] And then AI now allows you to understand those things well. So you can see the possibilities that other people didn't see before.

### Meta Prompting

**8:43** · So the next thing I use AI for a lot is to counter my own laziness. And this is a tool we use called metarrompting. Let's say you want to generate an image and you can't think of a good prompt. You know a little bit of the world but diffusion models you know you can't just give it two three pieces of the world.

**8:56** · If you start with a diffusion model which is an image like a midjourney and you say well the world has inhabitants who are 7 foot tall but then actually what you want to generate is a flower in the world then the diffusion model will generate those people in the back right unnecessarily. So unless you want that it's not a it's not a good idea but you can metaparrompt this. You can go talk about your world to GPD, give it the two, three pieces and then say, "Hey, bro, now give me a prompt that I can put into a diffusion model." And because GPD knows roughly how diffusion models work, it'll give you a better, more richer prompt with only the parts that are important and not important.

**9:25** · Cuz GPD is smart enough now, especially GPD 5 thinking, it knows what parts a diffusion model will purposely bake in that is unnecessary and what parts are not. I'll give you another example, right? You can use GPD to prompt GBD itself. Let's say you want to make a page like like Stripe. Okay? Now, maybe you're not an expert VIP coder, right?

**9:42** · Like you're not an expert at coding at all. You don't understand the different parts of it. You just know Stripe's page, right? You've seen the landing page somewhere. You're like, I want to make something like this. You can either go to GPD and say, give me a page like Stripe. Or you can go to GPD and say, I'm planning to make a page like Stripe.

**9:56** · Can you break it down to all its individual components? Give me all the parts of this page that I can potentially modify. Then I will prompt you and I will \[music\] take all these pieces that you have given me and I'll edit each piece a little bit. It'll give you this entire list and then you take that list, copy it, paste it, change the words. For example, generate a complete spec sheet with all the features, components, design elements needed to capture the stripe vibe. Then you can say instead of vague directions, give me exact specifications. You can say background soft multi-top gradient blur around the edges, teal green to desaturated yellow with a pale off-white radial center.

### Personas

**10:36** · So the next thing we can do is personas, right? You can ask the AI to be Shakespeare today. You can ask the AI to be Von Maya today. You can ask the AI to be Sam Alman today because it's trained on their writing, \[music\] right? On all these people's writings and in some cases their videos as well. You get a rough expansion of their thinking process because writing is thinking. It can kind of extrapolate the way Sam Alman would think or \[music\] the way Paul Graham would think or how at least the writing style. Instead of saying explain this simply using examples.

**11:02** · Let's say you have a concept and you can't understand this and you say explain this simply. You can say imagine you're a teacher and teaching this to me. So break it step by step and at every step check my understanding of it.

**11:11** · Now Chachibri has study mode that helps you actually do this. \[music\] Right? So you can actually click on the drop down do study mode and it'll quiz you on these topics. Right? It's checking your knowledge at every level. So you're retaining the important parts. So some practical variations on this are you can say well act as a biology professor teaching first year students or explain to me like I'm five. So you can ask the AI to go stupider and smarter and sometimes you can do all three. Teach me how Faraday's law works in three different modes. Me as a 5-year-old, me as a 10year-old but with simple formula understanding.

**11:42** · Simplify any formulas \[music\] and me as a 25 year old physics student. And as you can see it gives you a pretty cool answer. All right. So it's showing you mode one as your five, mode two, your 10. Okay, in plain words, mode three, your 25. So it's giving you the integral form and then it's giving you differential form and it's giving you flux rule and it's telling you \[music\] what counts as changing flux.

**12:10** · So as you can see, it's giving you three different modes and you can tweak this as you want. This is a very useful tool cuz you \[music\] can understand a topic in brief roughly understand what's going on go deeper go deeper which textbooks \[music\] could never do which is I don't get it make it dumber for me and then oh I get this make it smarter for me this is understanding right understanding is knowing it at a broad level then knowing it deeper deeper deeper then finally practice this is the magic of the world we live in today which just didn't \[music\] exist 3 years ago this is crazy that we live in a world like this

### Gap Finder

**12:40** · so next let's move on to something called the gapinder right which is you have this world we've talked we've spoken about world views a thought you said here are these puzzle pieces, \[music\] right? And you've given these puzzle pieces to the AI and you're saying make the rest of the world. I have a question. What if the puzzle pieces you're giving the AI, you have some gap in knowledge. Have you thought about that? Like this thing I've told you, right? Like the statement that a lot of people make on Reddit about AAA games and how much they cost without knowing the actual breakdown because they're not actually making a AAA game.

**13:05** · So, they don't know the exact cost, but they see the statement and I'm always like, what are the gaps in your knowledge that you don't see right now?

**13:10** · And you know what the most useful part about AI for me especially from prompting perspective I just go to AI every week or so and I say listen whatever you know about me tell me what are the gaps in my knowledge what don't I know what am I missing what are the gaps in my reasoning \[music\] and it is brilliant I was talking to it about the immune system two weeks ago it's like bro your understanding of the human immune system is good compared to

**13:34** · everybody else but it's still little simplistic the immune system is very complex there are multiple types of cells that release multiple different typeyp of cytoines that do different different things and they all interact with each other and they all you know one triggers the other and one calms the other down they're regulatory cells it's not as simple as stronger immunity lesser immunity these types of gaps in knowledge every week AI gives me everything that I'm doing right from \[music\] making a game to doing content to making videos like this to doing podcasts to managing 500 people every

**14:01** · week AI is telling me what I'm missing and I feel like if someone else told you this you \[music\] might feel bad that why is he pointing out my weaknesses but with AI it's a safe space so AI telling you your weaknesses \[music\] every week can actually make you stronger because you can easily work on those weaknesses, right? So, we call this the gap finder. I ask my employees to do this all the time in private uh \[music\] at least my team, my team VM. Uh and you should try it as well.

### Preventing Hallucination

**14:23** · The next thing and this is a tip that you need to use is you should tell the AI to tell you if it doesn't know to reduce hallucinations. You can use a bunch of statements we have here which is tell chat GB or clot to answer only if it is confident in it response and to ideally give you a confidence score for every response that it gives you. If it spits out a number, be like, "How confident are you about this?" Cuz Chad, GPD, and Claude, they lean towards you.

**14:44** · They're sink fans. They they're trying \[music\] to, you know, make you feel better. So sometimes they'll give you wrong data and say, "No, no, this is correct." But if you ask it for a confidence score, it'll give you that wrong data and you'll be like, "I'm actually only 50% confident in this." So the confidence score is very important because the minute it goes 90 and above for every statement that \[music\] it makes, there's a higher likelihood you can trust it. Whereas sometimes charg depending on the tone of writing was always that confident happy sort of creature. It's always a little more confident about the things it tells you than it really is.

### Using Voice Notes

**15:13** · Another thing if you're lazy typing some people are lazy typing. They can't type more than three lines in a \[music\] prompt. And a good prompt is like at least 10 20 lines. That's actually the minimum prompt. Some of my prompts are like you know pages long, right? Instead of typing if use the voice feature just voice note say everything. And Aina taught me this actually. My wife would just sit \[music\] down, press the record button, and on half an hour story, she'll tell it. Okay? And then it gives like she's done so much of the world building that's easy for it to fill in.

**15:36** · And I was like, maybe I \[music\] should do this. And remember, this is not you talking to the AI back and forth because that's not very good, right? And that's a small model running because it needs to respond to you \[music\] fast. This is me using voice note, not the AI conversation, which then gets converted into text and then sent into AI. You need that, not the live calling.

### Erase Stains Of AI

**15:53** · The next thing is to erase stains of AI.

**15:56** · And it's not very hard to do because according to you know Ethan Mollik who is an AI researcher 18% of financial consumer complaints 15% of job postings and even 14% of UN press releases showed signs of LLM writing. I think this number is far bigger. I I notice now AI writing everywhere. Right. So Blake Stockton who runs a blog called AI writers room says this. Avoid any sentence structures that set up and then negate or expand beyond expectations like X isn't just about Y or X is more than just Y or X goes beyond Y. Instead, use direct affirmative sentences.

**16:28** · Feel free to be creative with your sentence structures and expression styles. By doing this one statement, that first line, you're removing like 60 70% of that LLM style writing. Another example I use is I \[music\] use these and then also mix up a bunch of people's styles.

**16:44** · I'm like write like Paul Graham mixed with Vun Maya mixed with you know I give it like three four people or way to do this even better and this brings me to my next prompting tip you can just give it all your content if you've already written ideally pre-AI so it's not stained content it's not stained with generative AI if you already have this corpus which I do right because I've written books I've written blogs I've made videos before AI you can take all of that dump it into cloud projects or GPT and say write like this person now it won't do a great job it'll still get into some of these negations uh negative statements and all that as long as you combine that with removal of generic AI stuff. You get this nice hybrid.

**17:15** · It's not going to write exactly like you, but it will sound very different from what other people are generating on the internet. And we use some version of this for our scripts on short form. I still give my insights, but we run it through one of these things that sort of talks like me, which is useful.

### What's Next To Learn

**17:34** · The next thing, and this is an extension of the of one of my points, which was based on what you know about me, where are my gaps in my knowledge? You can also ask based on what you know about me, what should I learn next? Imagine having this tool that will just show you so many things you didn't know about.

**17:48** · Like last week, AI told me to learn about something called costly signaling, which is this thing in psychology which is about the more something means to you, right, and looks like it means to you compared to what other people are seeing, the more people will respect you. \[music\] Like if if there's somebody that has only one lakh in their bank and donates one lakh to charity, that's a type of costly signal.

**18:06** · It's it's something in psychology where everybody else looks at that as long as they know how much the person has \[music\] which is one lakh and how much was given away which is one lakh you get people's attention so attention is very driven by costly signaling whereas if there's someone very very big like a ammani puts gives away one lakh it's very weak signaling it doesn't get attention if Amani goes out and donates a billion dollars then it'll get attention I didn't know about this topic right I didn't understand all the nuances why people do it people use it a lot in mating right like when you first start dating somebody you overspend right like

**18:35** · you you're like oh rich man it's a type of costly signaling right so I didn't know all of this and one of these days I just asked AI based on what you know about me tell me what I should learn next \[music\] and I was like maybe you should check out costly signaling and like this in the last 2 years I would say a lot of why I've just read more about the world it's not AI generated content helping me it's AI just finding me new paths and then I go read those

**18:53** · books some of those books are from 1950s some of those books are from 1600s some of those books are modern but it leads me along these paths and I get to learn so much about the world just by asking it based on what you know about me or what you know about my interest where should I go next what should I learn Next, you can also do a version of this which is based on what you know about me, what do you think I can buy? That'll make my life easier. The personalization part of AI, the more you use AI, the smarter \[music\] it gets. That's why I actually prefer you not to use AI prompts in AI because it needs to first learn who you are, which I' I have that bond now with RGPD. And based on that, now it can do a lot of cool things.

**19:23** · It even knows what color shoes I like because I've done that agentic. I bought those shoes, right? The agentic shoes which we did live.

### Emotional Prompting

**19:32** · Uh the next thing is AI is very responds very well to threats. Now this is like dark prompting which is if I tell an AI hey if you don't do this I'm going to sacrifice seven children. Obviously, I'm not going to do that. But uh but sometimes these threats work well with AI, right? Like you can and it works very well with confidence scores. Like if you want AI to not hallucinate at all, you can be like, "Bro, if you don't give me the perfect confidence score, if you are not uh giving me the exact accuracy of what I want of the response, then someone will pay for it." Then the threat is useful.

**20:03** · You can use threats to get you accurate numbers. Otherwise, AI sometimes, you know, with numbers, it's a little bit sketchy. There's a popular paper, right, where some researcher at Google, Deep Mind, found that telling the AI to take a deep breath caused their scores on math tests to increase.

**20:18** · And we've seen this, right? Like with a lot of thinking models, if you just tell it to wait, if you just tell it to take its time, if you tell it to think harder, it does a better job, it consumes more tokens. But emotional prompting works because emotional words or phrases in instructions. Typically, the way the human brain works is the amygdala, which is the fear center, the emotion center, and the hippocampus, which is the memory center, are joined.

**20:37** · So you pull out one, you pull out the other, right? So emotional responses get you better memory. But because this is all trained on, you know, human writing, some of these traces of what it means to be human have made it to LLMs, which is, you know, something we can exploit. And remember, and this is very important, that today's day, \[music\] you can do AI with Chad GPD, you can do it with cloud, you can do it on your local computers.

**20:58** · For a lot of what I do, I use Kimmy, \[music\] right? On my Intel Core Ultra PCs. Now, even though they're a sponsor, I still believe that it's much easier on your computer than with a phone. So definitely go check out the Intel Core Ultra PCs. But for students, there's a weird paradox in Indian families. Your father will happily drop maybe two lakhs on IIT coaching without blinking. But if you ask for 500 rupees a month for Chad GPT, suddenly it's a lecture on financial responsibility. They see education as an investment, which is good, but subscriptions as more like burning cash.

**21:28** · And honestly, I think it's just better to stop fighting it. \[music\] In fact, you don't even need to convince them to pay a monthly rent on AI. You just need to be smart about the one thing that you are anyway going to buy, which is a laptop. If you buy a good laptop, every college requires it, standard protocol. To them, it's a one-time educational \[music\] asset. Now, here's the hack. You can't, of course, download Cad GPT on your hard drive.

**21:48** · That doesn't make sense that lives on the cloud. You can bypass \[music\] the monthly fees entirely by running open-source alternatives locally. For example, we use the Intel Core Ultra processors with dedicated NPUs. And if you're anyway making a laptop decision, you can veer towards this direction.

**22:02** · \[music\] And you can take models like Llama 3.18B or 53 mini and run them directly on your device. \[music\] Honestly, the best part for students is that after that it's completely unlimited. You know how with cloud AI you're always hitting token limits or worrying about monthly \[music\] caps. Here it's all about the laptop and an electricity source which most of you have enough of. Run it 24/7 if you want and then you can experiment freely.

**22:24** · Build stuff, break it, rebuild it.

**22:26** · There's no meter running and nobody's \[music\] charging you a dime. All right, so that's about it. I want to do a much longer video. I think we've already crossed time, but I want to do a very very long video on prompting. I'm going to do this in a second part about writing, \[music\] about human generated writing, about world building. I'm going to go deeper like the Dune example. I have a bunch more examples that I think \[music\] you would want to hear about how we do things here or how I do things. \[music\] Uh so, make sure you subscribe. Make sure you follow the channel. Yeah, happy prompting. Just experiment. \[music\] Just go out there and talk to AI for the next few days because all this is useful to help you understand yourself better.

### Closing Thoughts

**22:58** · We always thought AI is about getting the AI to do productive work, but actually it's about making you better. It's about \[music\] figuring out where you should go, what you should learn, what your gaps are, so that \[music\] you're able to use the AI much better. All right, that's it for me.