---
title: "Software Testing Course – Playwright, E2E, and AI Agents"
source: "https://www.youtube.com/watch?v=jydYq7oAtD8"
author:
  - "[[freeCodeCamp.org]]"
published: 2026-03-19
created: 2026-04-23
description: "Learn the essentials of software testing, from fundamental concepts like the testing pyramid to hands-on automation using Playwright. You will explore real-w..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=jydYq7oAtD8)

## Transcript

### Course Introduction and Overview

**0:00** · Hello and welcome to this software testing course. I'm Bo KS and I created this course. In this tutorial, you'll learn all about software testing from the fundamental concepts to writing your own automated tests and finally how modern AI powered tools are transforming the way teams approach testing. And here's what we'll cover. First, we'll explore why testing matters and look at some real world examples of what happens when software isn't properly tested.

**0:30** · Then, we'll dive into testing fundamentals, the different types of tests, when to use each one, and the famous testing pyramid. After that, we'll get hands-on. We'll build automated tests using Playright, one of the most popular JavaScript testing frameworks. You'll write real tests for a real application. And finally, we'll explore how AI is changing testing. I'll show you can AI from TestMU, an AI powered testing tool that lets you write tests using plain English instead of code.

**1:01** · Test MU provided a grant to make this course possible. And I'll demonstrate how it can make testing more accessible and efficient. By the end of this course, you'll have a solid foundation in software testing and practical skills you can apply immediately. Let's get started. Before we write a single line of test code, let's talk about why testing matters.

### Why Software Testing Matters

**1:24** · Because honestly, writing tests takes time. And when you're under pressure to ship features, it can feel like tests are slowing you down. But here's the thing. The cost of not testing is almost always higher than the cost of testing.

**1:38** · So, let me share some real world examples that illustrate this point.

### Case Studies: Knight Capital & Therac-25

**1:43** · First, I want to talk about Night Capital. So in 2012, Night Capital, one of the largest trading firms in the US, developed a software update to their trading system. But due to a bug that wasn't caught in testing, their system started making erratic trades. And then in just 45 minutes, they lost $440 million. So that's not a typo. $440 million in 45 minutes. The company never recovered and was eventually sold. An even more serious example is the the 25.

**2:20** · It's a radiation therapy machine from the 1980s. Software bugs in the system caused it to deliver massive radiation overdoses to patients. Several people died and others were seriously injured.

**2:34** · These bugs could have been caught with proper testing. Then we have the the Boeing 7 uh 7 737 Max. Software issues in the Boeing 737 Max's flight control system contributed to two fatal crashes.

### The Boeing 737 Max & The Cost of Everyday Bugs

**2:50** · Inadequate testing of how the software would behave in certain scenarios was a major factor. Now, most of us aren't building trading systems or medical devices or airplanes, but bugs in everyday applications cost money, too. a bug that causes users to abandon their shopping cart. A login issue that prevents customers from accessing your service. A data corruption bug that requires hours of manual cleanup.

**3:19** · Security vulnerabilities that lead to data breaches. So studies consistently show that that that finding and fixing a bug in production is 10 to 100 times more expensive than finding it during development. That's because production bugs require things like emergency debugging under pressure, hot fix deployments, customer support costs, potential loss of user trust, sometimes legal consequences. So, think of testing as insurance for your code.

### Testing as "Insurance" for Your Code

**3:49** · You pay a small cost upfront, which is the time to write tests, but then you can avoid potentially massive costs later. But testing isn't just about catching bugs.

**4:05** · Good tests also serve as your documentation for how your code should work. G give you confidence to refactor and improve code. Help onboard new team members faster. Enable continuous integration and deployment. Reduce stress of releasing new features. So now that we understand why testing matters, let's dive into the fundamentals. So let's build a solid foundation by understanding the different types of tests and when to use each one. So here is the testing pyramid.

### The Testing Pyramid: Unit, Integration, & E2E

**4:36** · One of the most important concepts in testing is this testing pyramid. This model uh popularized by Mike Conn helps us understand how to balance different types of tests. So picture a pyramid with three levels. At the bottom the wildest part we have unit tests. These are fast focused tests that check individual functions or components in isolation. In the middle we have integration tests.

**5:06** · These verify that different parts of your system work together correctly. And then at the top the smallest part we have in toend tests also called E2E tests. The these test your entire application from the user's perspective. So why a pyramid? The pyramid shape tells us something important. We should have many unit tests, some integration tests, and even fewer end to-end tests.

**5:34** · Because as you move up the pyramid, tests become slower to run. They become expensive to maintain and more brittle and prone to breaking. Unit tests run in milliseconds. Ed tests might take minutes. Let's look at each level in detail. Unit tests focus on testing a single unit of code, usually a function, method, or class, and they're tested in complete isolation.

**6:02** · For example, if you have a function that calculates the total price of a shopping cart, a unit test would call that function with specific inputs and verify it returns the correct output. Unit tests are fast.

**6:18** · You can run thousands and seconds.

**6:20** · They're reliable. They don't depend on any external systems and they're precise. When they fail, you know exactly where the problem is. So here's an an example. It's basically a simple unit test and this is what it might look like in JavaScript. So we we call this function the the the sum function or actually the the calculate total function. We call it with known inputs.

**6:48** · That's these items here that we we've created this items array. So after we pass in these known inputs, we assert that the output matches what we expect.

**7:02** · So we expect the total to be 25. We expect that after we call this function, it's going to return the correct sum.

**7:11** · Now moving up the pyramid, integration tests verify that different components work together correctly. For example, an integration test might test that your API endpoint correctly reads from and writes to the database or maybe it may test your front that your front end correctly communicates with your backend or that your payment system integrates properly with a payment provider.

**7:36** · Integration tests catch bugs that unit tests miss. Bugs that only appear when components interact. So an integration for an API may may look like this. So I didn't say this before, but this is basically the name of the test right here. And we are doing a post request to this API with this specific data. And then we're getting a response. Then we're expecting the response status, the status of that response to be 200.

**8:06** · And then we're going to verify it was actually in in the database. So we're going to call database.getcart to get the cart. And we're going to expect the items to have length one. We're going to expect that this item is now in the database. So it involves multiple components. The API endpoint, the database, and their interaction. At the top of the pyramid, in toend tests simulate real user behavior.

**8:32** · They interact with your application through the same interface your user your users do by clicking buttons, filling forms, navigating pages. End tests are powerful because they test your entire system working together, but they're also slower, more complex, and more prone to breaking when your UI changes. So here's an intend test example using playwright.

**9:00** · So playwright is a JavaScript library that can basically programmatically interact with a website. So in this case uh it's about user can complete a checkout. So we're going to the homepage. We're clicking the element that has the text add to cart. Then we're clicking the element that has the text checkout. We're filling in this text field with this ID and we're using this email.

**9:30** · And then we're filling in the other text, the other text box with this ID card with this number. Then we're clicking the element that has the text place order. And then we're going to expect that the text order confirmed.

**9:47** · There's going to be an element with order confirmed is going to be visible.

**9:51** · So basically this is walking through an entire user generate journey just like a real customer would. So beyond these three main categories there are other specialized test types. A smoke test that's quick tests that verify basic functionality works like checking if the application starts at all. Regression tests these are tests that ensure previously working features haven't broken after changes. Performance tests, tests that measure how fast your application responds under load.

**10:25** · Security tests, tests that check for vulnerabilities, like SQL injection or cross-sight scripting. Accessibility tests are tests that verify your application works for users with disabilities. Common question is, what should I test? So, here's a practical framework. Test the happy path. That's the main way users interact with your feature. test edge cases like in inputs, maximum values, special characters.

**10:54** · Basically, you don't know what a user is going to really do. So, you have to test all these potential edge cases that maybe would be less common. Then test error handling. So, what happens when things go wrong? Also, test business critical features, which are features where bugs would be the most costly. You don't always need to test everything.

**11:16** · Just focus on what matters most. You might have heard of testdriven development or TDD. This is a practice where you first write a failing test.

### Test-Driven Development (TDD) Explained

**11:27** · Then next you write the minimum code to make it pass. And then finally you refactor the code while keeping your tests green. Green means they're passing. So TDD can lead to better design code, but it's not always practical. Use it when it helps, but don't force it when it doesn't. So, let's summarize what we've learned. Uh, the testing pyramid, many unit, many unit tests, some integration test, fewer end tests. Unit tests are fast and precise.

**11:58** · Integration tests are verify components work together. End tests simulate real user behavior. Focus your testing on what matters most. Now, let's put this knowledge into practice. All right, now let's get hands-on. I've created a simple e-commerce application called TechMart that we'll use throughout the rest of this course. It's a simple store where users can browse products, add items to a cart, and complete checkout. So, I have all the code in on GitHub. You can just check out the link in the description.

### Hands-on: Setting Up the TechMart Sample App

**12:30** · We go into the sample app directory, and then I'll just do mpm install. And then to start it, we'll just do mpm start. Okay.

**12:41** · So now let's just open a browser. We can go to this URL and then we can just have a look at our application. Okay. Here's our TechMart store. Basically, we have a homepage with these product listings.

**12:56** · We have a filter. Um, so we can basically filter by max price. We can sort.

**13:05** · We can go to different categories.

**13:07** · electronics or accessories.

**13:09** · We can even um search for products. So, I can just type in mouse up here.

**13:17** · We also have a login. There's a demo account information we can use to log in. And then after we've logged in, it says, "Hi, demo user up here." And I can add some items to my cart.

**13:34** · And then I can go to my cart. see my cart page. I can proceed to checkout. So basically we also have the the the user registration, the checkout process. This is a real working application with a backend API. It has products, a cart system, user authentication, all things you would find in a real ecommerce site.

**13:56** · So we're going to write tests for all these features. Now let's set up our testing framework. So, I'm just going to go back to our root, our root directory for this course. And then I'm going to go to this folder cdest/traditional.

### Playwright Framework Installation & Setup

**14:12** · We're going to be using Playright, which is one of the most was one of the best testing frameworks available. It's created by Microsoft and supports testing across Chrome, Firefox, and Safari. So, I'm just going to do mpm install. MPM install. And this is going to install Playwright and all of its dependencies. Now, let me show you that my Playright config.js file. This is in that folder we were just in. And this configuration file tells Playright a few things.

**14:43** · First, where all of our tests are located. Also, it tells what browsers to test against. uh what we have this down here, Chromium, Fire uh Fox, WebKit, Mobile, Chrome, Mobile Safari, and so on. And then it's going to tell where our local service where our application is running and whether to start our application before the tests.

**15:09** · This configuration also sets up uh useful features like screenshots on failure. So that's what this is a screenshot on failure and then video on failure. So basically it will record video for debugging. So let's run our test to make sure everything is set up correctly. And now another thing I have to do before trying out the tests is to install the playright browsers. So I'll just do mpx playright install.

**15:39** · And so this will install all the correct browsers that will be required to run the tests. Okay. Now I can just run mpm test to run all the tests that we've that are already created for our application. And then I just have to wait. Uh there are 265 tests already created. So I just have to wait for them to all run. Okay. And we can see they've all passed.

**16:10** · And then we can see the report with MPX playright and then show report. And then it's just going to open it into our web browser. So now it's going to show every test that and then it shows the browser that it was test on like WebKit, mobile, Chrome, and we can search the tests. We can see which ones passed. None of them were failed, flaky, or skipped. But if there was, we could test that out. We could like search through them.

**16:41** · Now I'm going to open up my test and my home ba homepage.spec.js.

### Understanding Playwright Test Structure & Assertions

**16:48** · And now we're going to understand the test structure and we're going to start writing tests. Every playright test file follows a similar structure. We're just going to walk through this one that I just opened the homepage uh spec. So first we have this first line. First we're going to import test and expect from playright. Test is used to define test cases and expect is used to make assertions.

**17:20** · So we have this test.escribe homepage. So this is going the test.escribe is going to group related tests together. So this whole block contains all our homepage tests like everything basically all this stuff here. Now we have this section test before each. This runs every before every test in this block. So here we're going to navigate to the homepage.

**17:52** · Basically, we're going to clear the cart and then it goes to the the homepage before each test with an empty cart.

**18:01** · That way, every test starts from a clean slate. Now, let's look at an actual test. So, we have the test and then this is the description and this is going to define a single test case. Now we have a sync where it says a sync page that's going to give us access to the page object. And this line right here is is go it asserts that the page title contains techart.

**18:33** · So the page object is like a remote control for the browser.

**18:39** · We can use it to navigate, click, type, and verify elements. Now, let's let me show you how to write a test from scratch. Let me let's say you want to test the search functionality. So, I'm going to go to the end of all these tests. There's already a bunch of them here. Should display product information correctly. Should have a working search bar. Again, all this is in the description if you want to or the code is in the description. So, you can open this yourself and just check and just look at how the tests are look.

**19:10** · But I'm going to add an all new test here. So I'm going to do test uh should filter products when searching. And we get the page object again. Now the first step is to find the search in input. So do const search input. And then I'm just going to set this equal to page.locator.

### Writing a Search Functionality Test from Scratch

**19:33** · And then I'm going to add an ID search input. So basically when whenever we use page.locator it finds elements on the page then we use CSS selectors or we can use text content or other strategies to identify elements. So in this case we just use the ID. So the next step would be to type our search term. Remember we're simulating a user here. So I'm going to do await search input.

**20:01** · So that's the the selector that we just got. fill. So what are we going to fill the text box with? Well, we're going to type in keyboard. So this time we are doing an action. And so actions in this case we're using fill. Could also use click or type. This is just a way to interact with elements just like a user would. So after we've filled that, we're going to do another action.

**20:31** · So here we have page.locator. And now we're combining our searching for an element.

**20:38** · the search button element and the action the click into one line of code clicking the button that has the ID search button. Now we're going to wait. So I'll do await pagew wait for timeout and we want to just give it some time. We'll give it 500 milliseconds. So sometimes we need to wait for a page to update. So this is one way, but playright also has other waiting mechanisms.

**21:08** · And then we're just going to do some testing now that we've got the setup. So here we get the products by doing page.locators and then we look for product card the class. And we're going to expect products to have count of one. So, there should just be one product because we've added one product to the pro the page based on searching for one a keyboard and there should only be one keyboard on the page.

**21:40** · Now, we'll do one last expect and we're going to expect we're going to do page.locator and then find the exact element on the page and we expect it to contain the text keyboard. And that's the entire test. So I need a a closing bracket here and that test is complete.

**21:58** · Okay, let me talk a little bit more about locator strategies.

### Strategic Locators: Finding Elements Effectively

**22:02** · Basically, I mean how to find elements on a page. This is one of the most important skills in testing. Now I'm just going to put some code right in here just just for now so I can explain something to you. So you can locate by ID, by class, by text content by just doing text equals add to cart, uh by ro or accessibility.

**22:24** · So that with the role of the button with the name login, by placeholder text or by combining selectors, basically any CSS you can put in there. My recommendation, prefer locators that are stable and meaningful.

**22:43** · IDs and data test ID attributes are great. Text content works well for buttons and links. Avoid brittle selectors that depend on exact CSS structure. So, let me just delete all this for now. We'll save this. Now, we're going to look at another test file. I'm going to go into the cart.spec.js JS and we're going to look at a more complex uh test which is testing the shopping cart.

### Testing Complex Shopping Cart Logic

**23:13** · So we have the stuff before like the imports describe the the block name shopping cart. We have the before each which is always going to be the same. And let's look at this should this test called should add item to cart. So notice how there's a few different elements. The first is to perform an action. So basically this is the action is to add to cart.

**23:39** · So basically we click to add to cart on the first product. Then we're going to verify the immediate action. This is uh uh or the the media immediate feedback.

**23:56** · We're verifying the feedback which is the toast message. And then finally we are verifying verifying the state change which is the cart count has been updated. This pattern which is action followed by verification is fundamental to good testing and we can look through this testing file. We can see a lot more tests that are following that same pattern. So like for instance we are navigating to the cart.

**24:27** · We're verifying that there's been uh some immediate feedback and then we're verifying the state change. So when you're creating tests, that's a very good pattern to follow. Again, you can uh check this out yourself to see the other tests on here. Okay, let's talk let's look at another testing file. I'm going to go into the o.spec.js.

### Login Forms, Validations, & Error Handling

**24:53** · Forms are everywhere in web applications. So here we're going to look at testing the login form. So it's going to start very similar to our other test files. Now I'm going to just scroll down here to this one right here. Should login successfully with valid credentials. We're going to follow the same pattern as before. Uh one thing to see though is that we're on a different page. We're on the login page here because we have this before each here.

**25:24** · So, first we're going to fill in uh valid demo credentials into the login page. We're going to submit the form.

**25:31** · We're going to perform the action. Now, we just verify the feedback. And then we verify the state change, which is that it's been redirected to the homepage.

**25:42** · Well, I guess we're not verifying any.

**25:44** · Yeah. Yeah, we are verifying. It's not even though Okay, this is something important to say. Even though we don't have the expect, it's still checking that this happened. The test will fail if it never gets to this URL even though it's not a specific expect uh to contain or or something like that. Uh if one of these actions doesn't work, the test fails. And then and then we are going to go down to this test here. Should show error for mismatched passwords.

**26:18** · Like I said, it's important to test for error handling. Now, this is going to follow the exact same pattern as before, but using different credentials. So, it first it fills a password, but then it confirms a password with a different password. And then we are check we are expecting the error message to be visible and then it should say passwords do not match. Testing both success and failure scenarios is important.

**26:50** · Happy path tests verify things work. Error handling tests verify things fail gracefully. Now I'm going to go into another test file which is the checkout spec.js.

**27:06** · Let's look at a full end toend test which is the checkout flow. So I'm going to go down here to should complete checkout successfully. So this is a very long test because it's going through the entire flow. So it's going to fill out an entire multi-step form. So uh you can see how we use checkout or I mean we use we use um the fill for test inputs. We use select option for dropdowns.

### Full End-to-End Checkout Flow Walkthrough

**27:41** · We're still filling here, filling here.

**27:43** · And then we are going to use multiple assertions to verify the outcome. So a bunch of fills and then we have to assert multiple things to verify the outcome. Now let's open another test file which is the API spec.js.

**28:00** · Playright isn't just for UI testing. It can also test APIs directly. So here we have the base URL of our API. And then we have our first test. We're testing a git request to a/ API/ products and we want to check if it returns all products. So we're going to await this get request to the URL. Uh we want to expect that the response okay that's going to be truthy.

**28:30** · So it's going to have a good request and that the status is going to be 200. We're also going to await the the JSON response. We're going to expect that it is an array of products and then we're going to expect that the length is going to be six. that we got six products when we go to this uh API URL. And then if we go down here, we can look at another one. We have the should add item to cart.

**28:57** · API tests are faster than UI tests and great for testing back in OB logic. So before um we were testing basically simulating the browser, but here we're not simulating the browser at all. We're just making sure the API can handle adding items to to the cart.

**29:19** · So, we're going to the URL and then so we're we're posting at the URL sending this data which is going to it should add the item to the to the cart. Then we check to make sure the the response says add to cart. We check to make sure the data.length is one because that should have be been added. And then we check that the data the product ID and the quantity have been added correctly to the data.

**29:48** · So combining UI and API tests gives you comprehensive coverage. Let's talk more about running tests and how to run them effectively.

### Direct API Testing with Playwright

**30:02** · So I already showed you running mpm test to run all tests. But there's different ways to run tests. We can do npm run test but I can put uh headed. So this is going to run in headed mode which will show a browser. Okay, you can see that the browsers are opening uh the browser opens and you can actually see the browser running in headed mo headed mode and you can see what's actually happening in the tests. You can see how quickly the tests are running. They're running very quickly. So the first few tests were just of the API.

**30:34** · So there was no browser that popped up, but a bunch of them will actually use the browser when the tests are running. And then we can also run tests with UI mode interactive. So I do mpm run test and then just do UI and then we'll see how this can be an interactive mode. So basically it's opening Google Chrome for testing and then we can basically interact. We can run different tests.

**31:02** · So I had to click hit the play to to run all the tests in this block here. And this is just going to give you a lot more information about your tests. We'll close this for now. You can also just run a specific test file. So I can do mpx playright tests tests slashcart.spec.js.

**31:29** · But before I run this, I'm going to go into the tests and I'm just going to change one of the tests. So, let's say that we're expecting it to say item added to cart instead of added to cart.

**31:48** · Uh, now the test is going to fail because it's not going to say item add to cart. It's going to say test added to cart. I I just want to show you an example of a failed test also. So now we're only going to run that test file instead of every file in the in the test directory. And sometimes the test will take a little while to run. So you can see we now have a failed test. Our first test is failed, but the rest of them that we did not change are still passing.

### Debugging Tests in Headed and UI Interactive Modes

**32:18** · So sometimes uh you would have some failed tests, some pass tests. So, we actually have uh multiple failed tests because the first time it's running all the tests on Chromium, then it's running all the tests on Firefox, then it's running all the tests on WebKit, and every time it's running that test. That's a failed test. Okay. Now, it's going to open up our our report.

**32:43** · And you can also just do mpm run test colon report to open up this if you somehow closed it or it didn't open correctly. And now this is where we can see we have some failed tests. The failures are coming to the top here. We can sort by failures or sort by pass passes past tests. But if I do all, it's going to have our failures at the the top. Again, it's it's that one test, but it's being run on different types of browsers and it failed every time.

**33:13** · Another thing we can do is to run tests that's matching a pattern. I'm just going to I'm not going to run it this time. It's just showing I'm just showing that we can do MPX playwright test-g login. So, it's going to basically run all the tests that has the word login.

**33:27** · Now, I'm back to the the website that's showing the tests. I'm going to click into this. And when we click into the failed tests, we can see a lot more information. So, we can see the expected substring, the string, it got the call log. We can see the test actual code here. Now we can see the test steps and within the test steps we can see a lot more details but we can also have a screenshot this time.

**33:58** · It looks like it's having trouble showing the screen screenshot. We also have this error context which is going to be a markdown file with all the errors that you can use for additional debugging. Now that you know the basics of writing tests, let's level up. In this section, we'll cover three important techniques that separate beginner testers from experienced ones. There's testing edge cases and error handling, mocking API responses, and accessibility testing.

### Testing Edge Cases and Security (XSS) Vulnerabilities

**34:29** · These are the techniques you'll actually use on real projects. So, let's dive in.

**34:34** · The tests we wrote earlier cover what we call the happy path. Everything works as expected. But real users do unexpected things. They submit empty forms. They doubleclick buttons. They paste weird characters into search boxes. So let's write tests that catch these scenarios.

**34:52** · So if you're following along with the code with in in the description, we have this edge cases spec.js.

**34:59** · So let's look at these edge cases edge case tests. So let me walk you through what makes these tests valuable. So first we have these search edge cases.

**35:10** · So should handle empty search gracefully. Basically it's going to click the button without typing anything first. And we should we should expect the product cards to have count six. So meaning that they're all the products are still there. So this is actually a common thing that people do. They search without typing anything. So some apps can would crash or show errors but ours should show all products. Then we have this special characters test.

**35:41** · So should show no results for nonsense search. So here we're just typing in some uh random characters. So this next one is all about showing no results if there's just some nonsense search. So, if we just search for some uh some random characters, we should show that there's going to be zero product cards. We also want to search for special characters to make sure we handle that.

**36:11** · So, we're we're searching for adding basically a a script a JavaScript JavaScript script or code to a search box. Basically, this is a basic security check. So, if someone types HTML or JavaScript into the search box, it should not execute. This is testing for cross-sight scripting, which is one of the most common web vulnerabilities.

**36:41** · So, we should just have no results and the page should still be visible. And we have a few other ones like handle search with only whites space um adding product multiple times. Um not allowing checkout with empty cart. So it's actually going to fill out the form and try to create a checkout, but we want this toast to be visible. Basically the error about the empty cart.

**37:08** · You'd be surprised by how many real e-commerce sites have had the have had this bug where someone could try to check out with an empty cart. So, there's a few other ones that you can kind of read through on your own. So, the the golden rule of edge case testing is think about what could could go wrong and then write a test a test for it.

### Mocking API Responses and Simulating Slow Networks

**37:29** · Now, let's talk about mocking an API response, which basically means sending a fake API response. Uh sometimes you want to test how your application handles situations that are hard to reproduce naturally. What if the API is what if the API is down? What if it returns unexpected data? What if a product is out of stock? Playright lets us intercept network requests and return custom responses. This is called mocking and it's very powerful.

**37:59** · So I'm going to open up my mocking.spec.js JS and we have some tests in here for application. So let's talk a little bit about what's happening here. So page.oute is the key method. It lets us intercept any network request matching a URL pattern and decide what response to send back.

**38:25** · So in this first test, we're going to simulate the API being completely down, returning a 500 error. So we're doing this route and we're returning this status 500 and returning this body internal server error. And then if we kind of scroll down, we can see the rest of this. The product grid should be empty. So there should be zero product cards.

**38:56** · This tests whether you know the app handles failure gracefully instead of showing a blank page or crashing.

**39:06** · Then we have one that's going to test should handle slow API responses gracefully. So we can see we're going to intercept this route and then we are going to set a timeout. So, it's going to take three seconds basically before it continues. It it's it's going to add a 3 second delay. This is great for testing loading states. Does your app show a spinner? Does it remain interactive while waiting?

**39:33** · And we eventually are going to just test that it's still usable during loading and that products should eventually appear.

**39:45** · So, eventually we want to show all the products. And then we have one that's going to test um the out of stock.

**39:52** · Basically, this lets us control exactly what data the API returns. So in this case, we're returning this data and we can see it's putting stock zero for the wireless headphones. So we don't have to actually modify the database. We just mock the response. This makes testing specific scenarios much easier.

**40:15** · And then we can just uh show that there's two products and that it's going to contain uh out of stock the out of stock indicator. And the final one I'm going to just talk about right now is the add to cart failure. This test only intercepts uh the post request.

**40:39** · So letting get requests through normally but the post request will be mocked. So this uh this selective mocking is powerful for testing specific failure points and we can see what happens uh when when we do that. So when should you mock? Well when testing error states that are hard to reproduce.

**41:00** · When the real API is slow, flaky or costs money per request. when you need precise control over the data when testing thirdparty integrations you don't control and when you should not mock is when you need to verify the real API works and you should use integration test for that also when mocking would make the test meaningless. Now let's talk about accessibility testing.

### Accessibility Testing for Screen Readers & Keyboards

**41:28** · There's a lot of people in the world that live with some sort of disability.

**41:33** · If your website isn't accessible, you're exu excluding a huge number of potential users. And in many countries, accessibility is actually the law. The good news is that Playright makes basic accessibility testing straightforward.

**41:48** · The most common accessibility issues are missing alt text on images, poor color contrast, missing form labels, keyboard navigation doesn't work, and the screen readers cannot understand the page structure. So let's open up our accessibility spec.js and talk about some accessibility tests.

**42:10** · So if we look at this one, all images should have alt test or alt text. This checks every image on the page. Screen readers depend on alt text to describe images to blind users. If an image has no alt text, a screen reader just says image, which is useless. So, this is just going to go through all of them and just make sure they all have the alt text. The next one is all form inputs should have labels.

**42:40** · The form labels test verifies that every input has a way for assistive technology to identify it.

**42:49** · Without labels, a blind user encounters a text box with no context. They don't know if it's for their email, password, or search query. So, here we're going to expect that they all have a label. Next up is a p the page should have proper heading hierarchy. This basically checks that your headings make logical sense.

**43:14** · Screen reader users often navigate by headings, sometimes jumping from H1 to H2 to H3. So if you skip from H1 to H3, it's it can be confusing like a book with like chapter 1 and then chapter 3 but no chapter 2. So this is just going to just make sure that all the headings don't they they don't skip levels. And then the final one we're going to talk about is that we're going to check if interactive element uh we're going to check that interactive elements are keyboard accessible.

**43:46** · The keyboard navigation test verifies that users who can't use a mouse can still navigate.

**43:56** · Many people with motor disabilities rely on keyboard navigation. If your buttons and links aren't reachable by pressing tab, they're basically invisible. Okay, my terminal open. I'm running the command to run these tests. And we can see most of them are passing, but a few of them are actually failing. That's actually a good thing. It means we found real accessibility issues that need fixing. So this is the power of accessibility testing. It catches problems that visual inspection misses.

**44:28** · For a more comprehensive accessibility testing, you can use tools like Axe Core with Playright. It automatically scans for WCAG violations. You can use LighthouseCI, which is Google's accessibility auditing tool. um pi which is a command line accessibility testing.

**44:47** · Here's just a quick example of using axe core with playright. This single test checks for dozens of accessibility issues automatically.

**44:58** · So just as a quick recap uh for ex edge cases you need to just test the unexpected empty input special characters rapid interactions and error states. These are where real world bugs hide. Also mocking is important. Control your test environment by intercepting API calls. Test failure states. Slow networks and edge case data without modifying your back end. And accessibility test that your that everyone can use your application. Check for alt text, labels, uh heading structure, and keyboard navigation.

**45:30** · These three techniques will make your test suites dramatically more effective.

**45:35** · Okay. Now, let's talk about challenges of traditional testing. So now that you've seen how to write tests with playwrights, I'm going to be honest about some of the challenges. First, there's a significant learning curve. To write effective tests, you need to know a programming language, JavaScript, Python, etc. The testing frameworks API, CSS selectors, or other locator strategies, a sync, await, and promises, best practices for reliable tests. This takes time to learn and not everyone on a team may have those skills.

### Challenges: Learning Curves and Maintenance Burdens

**46:08** · Also, there's the maintenance burden.

**46:12** · Basically, tests need maintenance. When your UI changes, selectors might break, test flows might need updating, assertions might become invalid. A single UI redesign can break uh like tons of tests, dozens of tests. We also have the flaky test problem. So, end to-end tests are often flaky, which means they sometimes pass and sometimes fail without any code changes. This can happen because of things like timing issues, network variability, browser inconsistencies, dynamic content.

**46:41** · Flaky tests can erode trust in your test suite. Also, writing tests take time takes time. Uh for the checkout test, we saw I had to identify every form field, figure out the right selectors, handle the form submission, write assertions for success, test error cases. This was about 50 lines of code for one flow.

**47:07** · Multiply that by every feature in your application. So I want to basically tell you about a different way of writing tests, which is AI powered testing.

### Introduction to AI-Powered Software Testing

**47:18** · Artificial intelligence is transforming many aspects of software development and testing is no exception. So AI powered testing basically uses tools like machine learning and natural language processing to generate tests from plain English descriptions automatically identify elements on the page maintain tests when the UI changes detect potential bugs and issues.

**47:39** · So instead of writing things like page.locator locator uh and then putting the ID first name field and then putting what what you're trying to fill in with. You might just say enter John in the first name field.

**47:56** · So AI testing has some benefits uh accessibility. So team members who can't code can still write tests like QA QA analysts, product managers, uh any stakeholders. We have their speed.

**48:08** · Describing a test in English is faster than coding it manually. maintenance. AI can adapt to UI changes automatically, reducing the maintenance burden and then coverage. More people creating tests means better coverage. So, there's a few ways to um write tests with AI, including just going to an like chat GPT and asking for tests. But in this course, we're going to be using Kane AI from Tesmu.

**48:36** · They're a a gen a native testing agent that lets you create and run tests using natural language. And like I mentioned earlier, Keen AI provided a grant to make this course possible. And I'm going to give you a hands-on look at how it works. So Keenai um there's a few things that make it interesting. You can write tests in plain English. It supports web and mobile applications. It exports to multiple programming languages.

**49:04** · It autoheals tests when the UI changes and it integrates with CI/CD pipelines. Now, something to keep in mind, uh, AI testing tools are powerful assistants, but they don't replace human judgment.

**49:20** · You'll still need to decide what to test, review AI generated tests for accuracy, handle complex edge cases, and understands what the tests are actually doing. So think of AI testing tools as a productivity multiplier, not a replacement for testing knowledge. So let me show you how can AI works in practice.

**49:45** · So I have my techart application and we're going to use KI cane AI to do some testing. Now normally KI is going to be working on uh websites are all already live on production. So, we're going to have to have like a live URL. Right now, this one is just running on local host.

**50:06** · So, I need a way to get my localhost website to be accessible from the internet so I can test it using test mu and keeai. So, I'm just going to use cloudflared to create a cloudflare tunnel. Now, if you already have your website hosted somewhere, the problem solved.

### Hands-on with KaneAI: Authoring Tests in Plain English

**50:27** · I can do brew install cloudflared and then we still have our server running on my other terminal tab and then we're just going to do cloudflared tunnel- url and then localhost 3000.

**50:47** · Now it's hopefully getting everything set up right now. Okay. And if I zoom out a little bit, this will be easier to read, but it says your quick tunnel has been created. And then it gives me a URL. So, let's test this out. Okay, it's working. We have a publicly accessible URL for our website that's running locally. Okay, now I'm over on testmai.com and you can either do get started free or log in.

**51:18** · Okay. And there's tons of different types of testing you can do on here, but we're gonna go over to Cane AI. I'm specifically going to go over to the agent. And here is where we can just use natural language to create tests. And we can test on a desktop browser, mobile app, or mobile browser. So, I'm just going to keep it on desktop browser.

**51:45** · Okay. I just put in all this. So, first go to this website. Then make sure the title car the title contains techar.

**51:52** · Check that the text welcome to techart is visible. Then scroll down and make sure at least four product cards are visible. And then I just click this button to start the session. And we we're going to see that we have our browser on the right side and then what's happening is on the left side.

**52:13** · So, it's giving us our test plan. We can make some changes if we want, but we'll just approve this test plan and then we'll see what it comes up with. So, you can see it's opening the website and it's and it's a sample browser that it has. Okay, now it finished creating all the tests and we can see system idle.

**52:36** · So, it basically went to the website. It checked that welcome to tech mark is visible. Scroll down. It ver verified that at least four product cards were visible. And so I'm going to save this test. Okay, now we can see all the different steps. So go to the URL, check if the heading contains tech mark, assert that that title equals true. Then check to see if that text on the page.

**53:04** · Assert that it's true. Scroll down, get a count, and then assert that that count is greater than or equal to four. So now we can go into the code. This just this actually writes real code. So we can actually just go and view the code here.

**53:24** · Now it is uh Python code. It's not JavaScript code like we were talking about before, but a lot all the same principles apply in this Python code and using Selenium. Now, you're never going to really have to do anything with the code, but just know that it has code so to make sure that it can rerun the test the exact same way every time. And we can always execute the test again. If we go to the test summary, we can now uh execute the test.

**53:54** · So if we make changes to the site, we just execute the test again. So we can make sure that the that the tests all pass and it it's going to automatically create a description of the tests and then we can set some preconditions.

**54:13** · But uh all this stuff uh we can like add settings, we can add uh tags and we can go into the issues, the suggested issues. And this is a potential issue we could have. And then we can also have different versions of the test. So we have our version history there. Now I'm going to add t a tag which is just going to be techart. And we'll save. Now we have a tag associated with this. Now I'm going to try creating another test that's going to have some more uh user user interactivity. Okay.

**54:45** · This time we're going to go to the website again.

**54:50** · Click on the search input field. Type keyboard in the search box. Click the search button. Make sure only one product card is visible after searching and that the product should be the mechanical keyboard. So I'll just start the process here and then it'll give me a test plan and I can just approve it. Or if I want to change it first, I could.

**55:13** · And now I'll just wait as it goes through and tests everything and creates the test.

**55:22** · And you can see it's continuing to do everything and test everything just like I described.

**55:29** · Okay, it finished and it created all the tests. So I can just save this test and it'll take me to the page where it's going to show all the different steps to do all the interaction on the page. And then we have the the description here.

**55:46** · Again, we have the code. um the code generation is still in progress. So we we basically have to wait till it's done and then eventually we can rerun the test by just clicking execute test. For now I'm going to add a tag to this and we'll save the changes. And here we can actually sort our tests. So, I have all my TechMart tests in my TechMart folder, and that'll make it easier to get all of them together.

**56:16** · Now, let me show you another really cool thing over on the code tab. So, it automatically generates code in Python, but uh let's say we want to generate code in something else like like playright. That's what we were learning earlier in this tutorial. We just click generate new code. Now, this is this is a feature that's about to be implemented. Not quite yet, but we choose a framework and then you this is this is going to be coming soon.

### Natural Language Code Generation & Auto-Healing Tests

**56:42** · You can just click the the playwright and then choose JavaScript and then you can create the JavaScript code. So, it's a code that you're more familiar with for your project. Then that allows you to review and customize this generated code, integrate into existing test suites, run in your CI/CD pipeline. And we can already download the code. We can already download the current code, the Python. I just click this button to download the Python code. Now, one of KI's powerful features is the auto healing.

**57:14** · So basically, imagine our developers change an ID like we have this input. What if we change the ID of the input to a different ID? Well, in traditional testing, this would break our tests. But cane AI understands the intent of the test, not just the exact selector. So when it can't find the original element, it looks for alternatives that match the original purpose. This really reduces test maintenance. Now, we can also use KAI for API testing.

**57:45** · So let me show you how we can add an API in a web test. First of all, instead of typing into this box here, I'm going to click the author browser test. And I'm just going to keep uh keep the default options. Now, this is also a way how you can test on specific mobile devices, but I'm going to just click author test and then it's going to get everything set up here.

### Executing API Tests Using AI Agents

**58:11** · Okay. Now, I'm have manual interaction turned on. Now, there's two things we can use this for. We can use the manual interaction to actually manually go to a website, manually try things out, and then Kane AI will actually record everything we're doing and create a test based on our manual interaction. But I'm not going to do that. I'm going to actually do an API test. So, I put a I put a slash to open up these uh special commands I can do.

**58:42** · And I'm going to do add an API. And now I'm just going to paste in my URL here which is at slash API slash products and we have it as a get request. Now this is basically the curl command. Um now we can also set up the parameters authorization headers body settings uh for this API. We actually don't have to do any of that.

**59:08** · We're just doing a get request. And then we will just click send. And then to actually execute the API, I'll turn off the manual interaction and it'll execute the API and it returned a 200 response.

**59:23** · So in this case that would be a successful test because the the API returned a 200. So now I can just save the test and then it says the user performed the necessary steps to execute an API request. So now we can make sure so the test will pass if the API request is successful. So that's how you can test APIs with KAI. So I can build comprehensive API tests this way and combine them with UI tests for complete coverage.

**59:54** · Okay, let's wrap up with some best practices that apply whether you're writing tests manually or using AI tools. First, you're going to want to write make your tests readable. Anyone looking at a test should understand one, what it's testing, two, how it tests it, and three, what the expected outcome is.

### Professional Best Practices: CI/CD & Page Objects

**1:00:15** · So, good test names help like should display error when password is too short. That's way better than just like test one, two, three. You also want to keep tests independent. It one test should not depend on the outcome of another test. This means that each test sets up its own data. Each test cleans up after itself and test can run in any order. Also, you want to use page object pattern. So for larger test suites, consider you you should use the page object pattern.

**1:00:47** · Basically, instead of interacting with elements directly, you create objects that represent pages. So you can see this example on the screen right now. This makes tests cleaner and maintenance easier. You also want to integrate with CI/CD. Tests are most valuable when they run automatically.

**1:01:09** · You can integrate your tests with your CI/CD pipeline so they run on every code change. KI actually makes this pretty easy with its API. You can trigger test runs from GitHub actions, Jenkins, or any CI tool. Finally, remember that automated tests don't replace all testing. You still need exploratory testing for finding unwanted issues, usability testing for user experience, security testing by experts. Automated tests catch regressions. Humans find new problems. So, here's a practical guide.

**1:01:43** · So, you can use traditional playright tests when you need precise control over test logic. You're testing complex edge cases. You want test in your codebase.

**1:01:50** · But Keni Keni can be helpful when you want to prototype tests quickly.

**1:01:54** · Non-developers need to create tests. You want reduced maintenance overhead. You need cross browser testing at scale. And many teams can use both approaches together. Okay, let's wrap up what we've learned in this course. We started by understanding why testing matters. Bugs are expensive and testing is your insurance against costly mistakes. We learned the testing pyramid. Unit tests at the base, integration tests in the middle, and end toend tests at the top.

### Final Takeaways: When to Use Manual vs. AI Tools

**1:02:24** · Each type serves a purpose, and a healthy test suite includes all three.

**1:02:28** · We got hands-on with playright, writing tests for our techart application. You learned how to navigate pages, interact with elements, and verify outcomes using assertions. And we explored AI powered testing with KAI. You saw how natural language can be converted into working tests and how features like autohealing reduce maintenance burden. Here are my key takeaways.

**1:02:52** · Start testing now. Don't wait until your application is complete. The sooner you start testing, the more value you get.

**1:03:00** · Focus on what matters. You don't need to test everything. Prioritize the features where bugs would be most costly. Use the right tool for the job. Manual coding for precision, AI tool for speed and accessibility. They complement each other. Integrate your tests into your workflow. Tests that don't run regularly don't provide value. Automate your test execution. Thanks for watching this course. Happy testing.