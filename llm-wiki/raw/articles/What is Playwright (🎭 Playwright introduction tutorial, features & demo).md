---
title: "What is Playwright? (🎭 Playwright introduction tutorial, features & demo)"
source: "https://www.youtube.com/watch?v=wGr5rz8WGCE"
author:
  - "[[Testopic]]"
published: 2021-06-02
created: 2026-04-23
description: "In this episode, we take a look at a relatively new automation tool called 🎭Playwright: what it is, how to install it, how to generate scripts without writing code, how to interact with elements on t"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=wGr5rz8WGCE)

In this episode, we take a look at a relatively new automation tool called 🎭Playwright: what it is, how to install it, how to generate scripts without writing code, how to interact with elements on the screen, and finally, how to take screenshots and videos of your run. During the demo, we'll have a go at the Playwright Inspector as well. Oh, and it's a beginner tutorial, so you don't need any coding experience to follow through.  
  
Head over to http://testopic.com/playwright to join Playwright NTTN.  
  
Chapters:  
00:00 Intro  
00:40 About Playwright  
02:09 Installation  
04:36 Code Generator / Inspector  
07:20 Code structure  
08:28 Running scripts  
08:53 Take Screenshot  
09:39 Record Video  
11:45 Outro

## Transcript

### Intro

**0:00** · Hello Clever People! I hope you’re having an  amazing day! I’m Victor and in the next 15 minutes, I’ll help you get started with a cool  new automation tool called Playwright. By the end of this video you’ll know: what Playwright  is, how to install IT and its dependencies, how to generate automation scripts without  writing a single line of code, how to interact with elements on the screen, and how to take  screenshots or record the whole thing as a video.

**0:29** · We’ll be seeing some code, but I’ll  take you through it step by step.

**0:33** · And it’s going to be mostly auto-generated,  so don’t worry if you don’t speak code.

**0:38** · So, let’s get it on! First, allow me to attempt the shortest Playwright introduction ever Playwright is essentially a Node.js library made for browser automation. It’s free, open-source and it’s backed up by Microsoft Some of the team members used to work for Google at a different automation  tool called Puppeteer. In the meantime, they moved to Microsoft and became the Playwright  team. So they have plenty of experience.

### About Playwright

**1:08** · They are incredibly responsive with resolving  bugs and answering questions. They have a usual triage time of less than 48 hours and have  already addressed more than 1600 issues.

**1:23** · A small disclaimer: this video is not sponsored  and I don’t have any affiliation with the team, I just really like the tool they are building. It supports 3 browser engines that together cover all the popular browsers like Google  Chrome, Microsoft Edge, Apple Safari, Opera, Mozilla Firefox etc.

**1:38** · It can be used with the most popular languages out there like Typescript  & Javascript, C#, Java, or Python And it has some cool Perks as well. It can: automatically download the browsers it needs record videos of your test intercept and modify network requests emulate devices, location, locale, timezone, etc. And it has a cool Code Generator and Debugger which I’ll show you in a minute In a nutshell, Playwright is awesome.

### Installation

**2:09** · Let’s get on with installing it. It’s a fairly  easy process. We only need 3 things: Node.js, Playwright, and code editor. As an operating  system, I’ll be using Windows. You’ll be fine with a Linux or a Mac OS as Playwright is compatible  with those as well. So, 1st, let’s Install Node We'll do this by going to Nodejs.org  and clicking the LTS version.

**2:39** · Ok, we'll just do a next next next  install with most of the default setup.

**2:52** · It's a quick installation.

**3:00** · And then, by going to code.visualstudio.com we  can start the installation for Visual Studio Code.

**3:16** · It's going to be another next,  next, next installation.

**3:26** · Ok, so once Visual Studio Code is installed, we'll need a new folder. Visual Studio basically  works with folders as projects so, just create a new folder for this project.  It's going to be playwright-test.

**3:44** · Once we have this, we can open it up from VS  Code. File > Open Folder > Click Select Folder.

**3:55** · Now, all there is to do is install Playwright  which we can easily do by starting a Console Terminal > New Terminal. Write "npm  i -D playwright". -D stands for Dev.

**4:21** · It's going to take a minute or so. That was it with the installation process.

**4:28** · Let me know in the comments below if you ever  used a code editor or an IDE before, and if so, which one do you prefer. Let’s continue  with creating a simple automation script.

### Code Generator / Inspector

**4:42** · So let's create a new file. Right-click -  new file. We'll call it hello-platywright.js.

**4:52** · I promised you we won't be writing any  code so this is the perfect moment to start Playwright's inspector. We can do that by  writing "npx playwright codegen". We can launch this directly or we can give it a  website, let's say http://wikipedia.org.

**5:22** · It's going to start a browser window  and the actual inspector. We can see the browser window here, and the inspector  here. This is already recording, so each time we do an action in the browser  window we will see a new line of code in the inspector. So let's make this  a bit smaller so we can see better.

**5:45** · So let's say we want to automate wikipedia.org. So  let's go to English > Final Fantasy 9 > Combat and character progression. Let's take a look at the  generated script here, on the right side. It has generated Javascript Code because Javascript  is selected by default, but we can select any of the 4 languages it supports (actually 5):  Javascript, Java, Python, async Python, and C#.

**6:16** · The structure is going to be the same for  any language. So if we take a look at the code for just a bit, it first starts a browser,  it then starts the context, then starts a page,

**6:31** · and then it navigates to the Wikipedia  website, it then clicks on the English Language and so on and so forth. If we change this to Java,  even after we recorded everything, then we will see the same structure again. It first starts the  browser, then starts the context, then it starts a new page. Any Playwright script that starts  from scratch it's going to start the same, so Browser > Context > Page. We'll go through  these in just a minute. So let's go to Javascript, copy everything and go to our code  editor. Paste everything here.

**7:18** · Amazing, you can already run this.  But before that, let’s take a minute and understand what happens in detail. So, as I mentioned, the first thing that it does is start the browser. The browser in  Playwright is similar to a real-life browser.

### Code structure

**7:33** · So think about this as starting a new browser  window. It then goes on to start a new context.

**7:40** · It's kind of like starting a new window inside  an existing browser. We already have this browser here, and we use it to launch a new completely  independent window. If you start 5 contexts, for example, they are going to be completely  independent of each other. And then, we have a new tab. So, browser ... window ... tab. Just like in  real life. And then, you are going to find some

**8:10** · familiar actions here. So, we opened up Wikipedia,  we clicked the English Language articles, then we went to the Final Fantasy IX article, and  we clicked on the Combat and Character progression link. So let's what we have here, by running  it. We'll run it by using this simple command: "node hello-playwright.js".

### Running scripts

**8:46** · We see the browser running, clicking ... and ...  that's it. I hope you caught it. Let's modify it a bit. Let's see what it can do for us. For  example, we can easily take a screenshot: page.screenshot and we just have to give it  a path to the screenshot. Let's call this one wiki\_screen.png. And let's run  it again using the same command.

### Take Screenshot

**9:24** · And let's see what happened. We'll just go to our  File Explorer here, and we see the new screenshot here. We'll see exactly what we expect, so  it actually navigated to the anchor that we clicked last. Another cool thing that Playwright  can do is record videos of the whole execution.

### Record Video

**9:46** · So for this, we just need to change the properties  of the context. If we go to the context here, we create a new object and we say recordVideo.  And we just have to give it a path through this dir property, so let's  say ... videos. Save and run it again.

**10:22** · At the end, we should see ... yes,  so we have a new videos folder here and it has a file in it.  Let me open it in explorer.

**10:35** · So if we go to Videos, we see this video  here. Let's run it, and as expected, everything that Playwright  does is actually recorded.

**10:49** · So before we finish off, I want to show you  just another thing. Playwright is headless by default. This means that the  browser runs, but you can't see it.

**11:03** · In our case, because we took the code from the  Inspector which generates the code automatically, they actually added this automatically  for us. So ... "headless: false".

**11:14** · This means that the browser won't actually  run headlessly. But if we run this, and ... let's say I delete this videos  folder so that we know it actually runs.

**11:31** · And if we run it again, you can see it created Videos again... and ... it  finished. I just wanted to show you how a headless run looks like ... You don't see anything :) That’s it. Let me know in the comments below if you plan on using Playwright in the  future and for what kind of project?

### Outro

**11:51** · I maintain a small newsletter about Playwright, so  make sure to head over to testopic.com/playwright if you want to be updated when I post a new  video, cheatsheets, or other interesting stuff about this amazing tool. Cheers, and have a good one!