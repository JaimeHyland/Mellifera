![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Mellifera
A simple B2C ecommerce website for the online sale of honey-bee-related equipment, materials, tools, consumables and packaging to English-speaking German hobby beekeepers.

Code Institute - Fifth Milestone Project: Under my interpretation, the requirements for this project would be satisfied as follows:

Build a Full-Stack e-commerce website that facilitates the online sale of and payment for a range of beekeeping-related goods based on a business logic that reflects the variety and taxonomy of that range of goods, satisfying the expectations of both an imaginaray online store owner and of their imaginary customers.

I believe that completing such a project would satisfy the requirements listed for the fifth porfolio project in Code Institute's LMS, i.e. to show  an appropriate level of understanding on my part of a number of different concepts, technologies and disciplines related to Full-Stack programming in the e-commerce sector:

-- Django development on a cloud-based IDE (using Django-3.x on a VS Studio IDE hosted on Gitpod).
-- The creation and maintenance of database models, implemented using Django, running on Postgresql.
-- Use of agile methodologies via the project features available in GitHub, associated with the repository for this portfolio project.
-- Creation of UI elements outside Django's admin panel to allow users to create and update records in database tables.
-- The use of robots.txt and sitemap.xml files.
-- The use and purpose of descriptive metatags in HTML code.
-- How to link to external resources using the Rel attribute.
-- How to make a custom 404 error page.
-- The use of social media, using the instance of Facebook as an example.
-- Creation of a newsletter signup form.
-- The use of DEBUG mode, and in particular the need to turn it off before deploying.
-- The Django functionality allowing users to log in and out of the project application.
-- The use of Stripe together with Django, bootstrap and bespoke HTML, CSS, JavaScript and Python code to demonstrate a working online purchasing system
-- The correct use of linting to check code formatting.
-- Detailed human-made logs of testing processes.
-- Appropriate use of online research and problem-solving resources publicly available on the Internet.


![Behives in autumn](/assets/documentation/beehives_in_autumn.webp)

*Traditional beehives on an autumn evening*

## An apologetic note for the examiner
I do not expect this portfolio project to achieve the pass criteria in its current state. A number of the requirements listed in the instructions for it have not yet been implemented. I am obviously not a very fast coder yet, for which I apologise. In my defence, I should say that I feel that, out of the three options for the final module of the course, at least the e-commerce option &mdash;and in particular the walkthrough for the boutique-ado ecommerce website&mdash; involves a good deal more work (rather than simply more complexity) than the first four modules and, though I was to some extent forewarned of this, I didn't expect the difference in terms of time required to be _quite_ as big as it has turned out to be. There were a number of other circumstances, including a short bout of illness, that contributed to my inability to finish on time, but those circumstances paled into insignificance beside the widely recognised technical flaws and continuity gaps in the final walkthrough, as well as its sheer length.

I am determined however, to get this final part of the course done properly if given a reasonable amount of time to complete the job. I realise that my failure to complete the 5th project on time will put a pass ceiling on my efforts, but my priority has always been to learn the skills I need to learn rather than to receive an especially impressive certificate.

I'm very grateful to the tutors for their ongoing help in getting through this very challenging section of the course (though they were just as supportive, encouraging, patient and competent in earlier parts of the course) and to my customer care person for their encouragement and advice.

[TOC]

## The user story

### The initial proposition

The very fictional Elise Knolle is a Berlin-based amateur beekeeper who, while on an equally fictional skiiing holiday in mountainous Northern Bohemia a few months ago, met an imaginary woodworker who makes high-quality beehive boxes and honey frames in the spruce and pine lumber local to area. He makes a good living selling his wooden products at very competitive retail prices. He also makes higher quality cedar boxes at a higher, though still relatively attractive retail prices. Elise (who had, with some relief, just completed an online course in Full-Stack Development at the famous Irish training company, Code Institute) hit it off immediately with the Czech woodworker on meeting him one evening during the apres-ski, and after a generous helping of excellent food, washed down with an excellent Pilsner beer and a glass of homemade herbal schnapps, the conversation, as often happens in such circumstances, turned to business.

Tomáš (for that's his name) has a good deal of experience sending his wares by DHL around the Czech Republic, Poland and Slovakia, and is the proud owner of some very expensive and sorely under-exploited woodworking machinery. As such, he's keen to expand his geographical market. Early in his conversation with Elise (neither spoke the other's native language, so they communicated in English), he learnt two facts that made his ears prick up: firstly, that there are no less than 150,000 hobby beekeepers in Germany, and secondly, that Elise is currently having to buy beehive boxes of what she considers inferior quality from a Brandenburg-based specialist at a significantly higher price (after conversion into Euros).

As the conversation went on, Elise, who is not rolling in money (skiing is rather cheaper in Czechia than in Austria), and is tempermentally unsuited to working as anyone's employee, began outlining  to Tomáš (with increasing excitement) the training she had so recently received from the Dublin-based training firm, suddenly interrupting her own monologue, taking a deep breath and tentatively putting a hypothetical question to Tomáš: if she were ever in a position to pass on orders for his wares to him from the DACH area (Germany, Austria and Switzerland), would he be prepared to pay her a commission with a guarantee of no diminution in quality. He, cottoning on to what it was she was (still hypothetically) hinting at, replied that he'd be very happy with such an arrangement. Given the lateness of the evening, though, perhaps they ought to meet in the morning to talk about the matter further.

The following day they met for coffee at the bottom of the ski slope (Elise was happy to give up her skiing for the day to continue her conversation with Tomáš), they came to the following arrangement:

Within six weeks of arriving back in Berlin, Elise should put together a proof-of-concept version of a B2C e-commerce website designed to sell Tomáš' wares to German beekeepers and would return to Czechia to show Tomáš the results of her efforts and to discuss how much work still needed to be done to get the website up and running. They could then discuss what, if anything, Tomáš would be willing to contribute to the completion and final deployment of the website, including its localisation into German, its internationalisation for the Swiss and Austrian markets (at least) and the simple web-marketing, security and analytical functionality that the system would be likely to require.

The project that I will be presenting in a few weeks' time (and I apologise sincerely for being unable to present a fully functional project fulfilling all the above requirements in time for the project's 8 August deadline &m-dash; see my explanation above) should be considered the test website that Elise build and turned up two months later (she was a little delayed too, as we'll see below!) to present to Tomáš.

### Elise's thought process
Even as the train trundled along across the border on its way back home to Berlin, Elise had already begun mulling over the complications that might face her in her coding efforts.

For one thing, different beekeepers all over the world use a variety different standard sizes in their hives and they'd have to be very convinced they were buying the right sizes for their particular configuration before they'd be remotely likely to buy from an unfamiliar website. For another, the standard measurements for hive boxes that developed over the history of beekeeping generally relate to the interior dimensions of such boxes, which are governed by whatever standard-sized bee frames beekeepers have chosen for their system.

While Tomáš had reassured her that he can make hive boxes to whatever size she might want, Elise realised she wasn't very clear herself on the variety of exterior measurements of boxes used by German beekeepers. While the critical measurements for hive boxes are the interior measurements, getting the exterior sizes right may well help beekeepers combine their newly purchased boxes with the ones they already have tidily. Though boxes with thinner or thicker walls can usually be placed on top of one another, any lips or ledges left may look a little untidy, and might even shorten the useful life of the bee boxes, as such lips can allow water to lie in nooks and crannies &mdash; and standing water will significantly accelerate rotting processes in wood, especially since the wood used in beekeeping, for obvious reasons, can't be treated with anti-rot chemicals of any sort.

Thankfully, the standard frames that are hung inside such boxes are slightly less complicated, varying only in terms of length and depth to match only the interior measurements of that box. The actual thickness of the timber used to make such frames is a fairly standard 9.5 mm (or about 3/8 of an inch for the old-fashioned among us).

Despite this little mercy, all this seemed like worrying complications. It was nothing she couldn't handle (thought she) by adjusting her data models and workflow to take account of it, relying on Tomáš' reassurances.

## Initial design
So, almost as soon as she got back to Berlin, Elise got to work, starting by sketching out a wireframe using the Balsamiq app in test version on the cloud.

As you can see from the pictures she sketched out, she concieved it as a pretty standard B2C e-commerce website in which the user is greeted on a homepage and immediately invited to scroll through the list of products available in the shop, albeit with a fairly specialised multi-layer filtering system to help the user hone in on the precise products with the precise interior measurements and wall thicknesses they need.

The usual options allowing the user to register, log in and log out are also available (in the sketch only, so far). 

While Elise is conscious of the benefits of using a mobile-first design philosophy, she decided to base her wireframe on small laptop or tablet screen (with a resolution of 1024 x 786 pixels), knowing as she does from experience that most beekeepers would use their household laptop or tablet to make their online beekeeping purchases. However, she also makes a couple of sketches for a standard mobile app.

![Elisa's initial wireframe for her project homepage](/assets/documentation/readme_assets/Mellifera_wireframe_home.png)

*Elisa's initial wireframe for her project homepage*

The wireframe she made is largely for her reference, as well as to show her friends in the local beekeeping society

- - -

<!-- TOC --><a name="system-design"></a>
## System design

![Some flow charts portraying a selection of important witch-hazel worklflows](assets/readme_assets/hamamelis.gif)

*Some flow charts portraying a selection of important witch-hazel worklflows*



Accordingly, I prepared a series of outline flow charts in consultation with Laura and Donal on the basis of the needs they described to me. Once they'd approved the charts, I began thinking about actually programming the various functionalities.

For simplicity's sake, and because I thought the data was not enormously complex, I decided to store it all on a single google spreadsheet, which I simply named 'hamamelis'. It contains three worksheets.
- rootstock
- grafts-year-zero
- plants

The data should be read as follows.

<!-- TOC --><a name="the-rootstock-worksheet"></a>
### The 'rootstock' worksheet 
- The first column (A) is a label to tell the witch-hazel program what year the figures in the corresponding row refer to. The current year is at the top. 
- The top figure in the second column (B) shows the number of cuttings that the couple plan to take in the autumn of the current year minus one. The figures below that represent the number of cuttings that the couple planned to take in each relevant year minus one in the past.
- The third column (C) shows the number of cuttings that they actually took in the relevant year.
- The fourth column (D) shows the number of cuttings that rooted successfully and were potted up during the spring. It is a representation of work done, and does not increase when immature rootstocks are acquired from an outside source, nor does it reduce when such rootstocks are lost through disease or damage, or when they are used up to in the grafting process. Notice the change in nomenclature: successfully rooted _cuttings_ begin to be referred to as _rootstocks_ as soon as they've planted in pots (potted up).
- The fifth column (E) contains at most two non-zero values: one in E1, which represents the figure for rootstocks in stock this year to become available for use as next year as rootstocks. It is equivalent to the value in D1 minus any losses and plus any acquisitions. The value in E2 represents the total number of rootstocks now available for use in this year's grafting. Every time a grafting session is recorded, this value goes down by the number of grafts made. 
Any rootstocks left over after the year's grafting campaign is finished remain in the system until they are set to zero upon creation of a new year. The reason for this is that two-year-old rootstocks will rarely be suitable for grafting when the time comes around again in the new year. They are generally physically disposed of (recycling the pots and compost) when the opportunity arises during the course of the new year.
![The rootstock worksheet the end of a year](assets/readme_assets/rootstock_old_year.png)

*The rootstock worksheet as it might look towards the end of a growing year*

<!-- TOC --><a name="the-grafts-year-zero-worksheet"></a>
### The 'grafts-year-zero' worksheet
The grafts-year-zero worksheet contains two more columns than the number of cultivars of _Hamamelis_ currently cultivated by the Witch Hazel nursery. 
- The first column identifies the year to which the data in the corresponding row refers.
- The second column tells any human or machine reader whether the figures in the corresponding row refer to numbers of grafted plants that the couple originally planned ('planned'), that they actually made ('grafted') and that they currently have in stock ('stock'). The 'stock' figure for the current year refers to the number of plants of the given category currently in stock (i.e., the number of grafts originally made of the relevant cultivar in the current year minus any losses recorded since then, plus any gains since then). When a new year is created, the relevant numbers are passed into the 'plants' worksheet, three new rows are created for the current year and the figures for 'planned' and 'grafted' for previous years can no longer be edited. 
- Each subsequent column gives the figures described above for the cultivar labelled in the topmost cell.
![The grafts-year-zero worksheet the end of a year](assets/readme_assets/grafts-year-zero_old_year.png)

*The grafts-year-zero worksheet as it might look towards the end of a growing year*

<!-- TOC --><a name="the-plants-worksheet"></a>
### The 'plants' worksheet
The plants worksheet is a little simpler. It shows the current stocks of each cultivar of each age group &ndash; i.e.: the total number of grafts of that age currently in stock, adjusted according to the losses and gains subsequently recorded by the couple in the witch-hazel program using the record_loss, record_gain, hold_back and bring_forward functions (see below).
![The plants worksheet towards the end of a year](assets/readme_assets/plants_old_year.png)

*The plants worksheet as it might look towards the end of a growing year*


- - - 

<!-- TOC --><a name="the-programs-original-workflow-and-the-technical-issues-with-the-technology-used"></a>
## The program's original workflow and the technical issues with the technology used

At the outset of programming, I wanted the app to call a run.py file in the usual way but to attach an argument after a blank space on the command line, depending on the task that the user wished to do at that time. Unfortunately, the Heroku pseudo terminal on which the app is destined to run does not allow the use of command-line arguments (or at least I have been unable to find a way of implementing such a command-line-argument-based design). Due to some issues with my implementation of the Heroku architecture, I discovered this limitation rather late in the day. As a result I was forced redesign the app at the last-minuteto follow a different (and in my opinion much less elegant) logic. Originally, the user would have typed the run.py file name on the terminal, followed by a space and then a short string indicating what they wanted the app to do.

For example, they would have typed ``run.py plan_cuttings`` to plan their campaign of taking and preparing cuttings. But the Heroku pseudo-terminal automatically runs the ``run.py`` file without any arguments immediately upon opening, so everything must be based on an argument-free initial call. The description of the workflow below is based on my last-minute changes due to this difficulty. It should be understood, however, that workflow described below was not my first choice.

The time used dealing with this problem at the last minute may have affected some of the finishing work on the program. For example, it was my original intention to connect each task to the next in their logical order, asking the user if they wished to go on to the next task. Sadly, the user now needs to restart the program every time they wish to complete a new task. 

- - - 

<!-- TOC --><a name="the-programs-workflow"></a>
## The program's workflow:

<!-- TOC --><a name="seasonal-tasks-in-order"></a>
### Seasonal tasks in order
Typically towards the autumn of every year, the owners will want to close out the figures they have entered over the previous year, begin a new year and start work on planning their campaign of taking H. Virginiana cuttings. They begin this task by running the app and choosing option ``1`` (``Create new year/Close out current year``). This function adds the required new lines for the new current year on each worksheet, and copies the data on graft stocks for the old current year to date from the ``grafts-year-zero`` worksheet to the ``plants`` worksheet. This has the effect of putting the data for the previous year out of reach of the seasonal tasks.

Also within the ``Create new year/Close out current year`` function, users can choose either to enter the figure for cuttings that they anticipate taking this year or opt to leave that job for later.

![The rootstock worksheet straight after the user executes the ``Create new year/Close out current year`` function](assets/readme_assets/rootstock_new_year.png)

*The rootstock worksheet straight after the user executes the ``Create new year/Close out current year`` function. Note that the user has chosen to enter a value for planned cuttings of 2800. That value can be changed at any time during the year by running Option 2 ``Plan this year's cutting campaign``.*

- - -

![The grafts-year-zero worksheet straight after the user executes the ``Create new year/Close out current year`` function](assets/readme_assets/grafts-year-zero_new_year.png)

*The grafts-year-zero worksheet straight after the user executes the ``Create new year/Close out current year`` function.*

- - -

![The plants worksheet straight after the user executes the ``Create new year/Close out current year`` function](assets/readme_assets/plants_new_year.png)

*The plants worksheet straight after the user executes the ``Create new year/Close out current year`` function.*

Then, whether or not they have entered a figure for planned cuttings, they can run app option ``2`` ``Plan this year's cutting campaign`` to revise that figure. If they have already recorded a figure for cuttings actually made, they are given a warning to tell them that the cutting campaign has already started and asked to confirm whether they want to replace the planned figure with a new total. The new figure is not added to the old one; it simply replaced it. This is the case with all planning functions.

When they run app option ``3`` (``Record cuttings taken``), they are asked to enter a number of cuttings actually taken. They are given the already existing figure for cuttings taken and warned not to enter a number for cuttings unless that number has already been physically taken, prepared and inserted in the cuttings bed. It tells the user when the number of cuttings taken exceeds the number of cuttings planned.

The new figure entered by the user is added to the already existing number. In the nursery, the cuttings campaign takes several days, the owners typically entering the day's figure for cutting production in the evening of the relevant day. The user receives a message on the command line when the figure exceeds the planned figure. The logic behind the difference between planned figures (each of which simply replaces the previous one) and the actually taken figures is that the latter are usually totted up for each day in the cutting/grafting campaigns, and the user should expect the app to remember the numbers recorded from previous days.

Option ``4`` (``Record rooted cuttings potted up``) instructs the user to enter a figure for the number of successfully rooted cuttings actually potted up. As another figure indicating for work actually done (usually daily), it functions in a similar cumulative way to option ``3`` (``Record cuttings taken``, as do all functions designed to record work actually done). It informs the user when the total number of potted cuttings recorded has reached or exceeded the total number of cuttings taken.

Option ``5`` (``Plan grafts for this year``) displays the number of rootstocks (i.e. the figure for cuttings successfully potted up in the previous year, minus losses, plus gains) asks the user what cultivar they want to graft and how many grafts they want to make of that cultivar. The function keeps a running total of the rootstocks required and issues a notification/warning if and when the total number of planned cuttings exceeds the number of rootstocks available. As the function is about planning numbers, new numbers simply overwrite old ones the second and subsequent time the user runs the option for a particular cultivar.

Option ``6`` (``Record grafts taken``) argument asks the user which cultivar they want to record grafts for. The owners typically enter the day's figure for graft production separately for each cultivar in the evening of the relevant day. The user receives a message on the command line if and when any figure exceeds the associated planned figure. As for other options recording work actually done, new figures are added to old figures creating a new total. Each time a grafting session is recorded in this way, the current stock of rootstocks is reduced by the corresponding amount.

_N.B.: In order to record total work done separately from current stocks (i.e., total work done minus losses plus gains) all the following numbers are recorded separately:_
- _cuttings taken vs total rootstocks_
- _grafts taken vs total plants in stock (recorded for each cultivar separately)_

<!-- TOC --><a name="ad-hoc-tasks"></a>
### ad-hoc tasks
Option ``7`` (``Record plant losses``) asks the user the cultivar and age of the plants they want to record as lost (including year-zero rooted cuttings), showing them the current figure for that cultivar and age. The user is prevented from entering a number greater than that figure. It gives a confirmation message before writing the data entered by the user to the spreadsheet.

Option ``8`` (``Record plant gains``) works similarly, adding instead of subtracting. It does not impose any restriction on the number added.

Option ``9`` (``Hold over plants for one year``) asks the user to identify the cultivar and age of the plants they want to hold back, shows the user the current number of those plants and subtracts the number given by the user from the current age category, adding the same number to the category one year younger. As with ``record_loss``, the user can't move more plants than the recorded number for the relevant category in any direction. The system also prevents the user from entering a value less than two, as it is impossible to hold year-one plants over to year-zero. The year zero values are not recorded in the ``plants`` worksheet at all. They have ther own worksheet (``grafts-year-zero``)

Option ``10`` (``Bring plants forward one year``) does the same in the opposite direction. Again, the appropriate restriction on numbers moved applies. In contrast to the previous option, the user can choose the value ``1`` for year cohort, as the same problem doesn't apply here.

In exceptional cases where the user wishes to hold back or bring forward a number of plants by more than a year, they must run the relevant process twice.

Unfortunately, due to the time restraints, I was unable to implement option ``11`` (``Add new cultivar``). I have, however prepared much of the groundwork to introducing it in the future. For example, I have implemented a system by which the functions that involve cultivars identify those cultivars dynamically.

Reductions in plant stocks through _sales_ are not recorded in this app. The couple tell me that this may be the next step once they have this work planning system bedded in.

The same can be said of a number of other parts of the nursery workflow.

<!-- TOC --><a name="bug-fixes-and-warning-resolution"></a>
## Bug fixes and warning resolution
<!-- TOC --><a name="bugs"></a>
### Bugs
Bugs were fixed as they arose during smoke testing.

As far as practicable, all Bugs are resolved separately and the Bug resolution is recorded in Git commits separately, prefixing the commit text with "Bug: ".


<!-- TOC --><a name="warnings"></a>
### Warnings
pycodestyle issues (all warnings) were closed shortly before submitting the app project.

Two warnings could not be resolved, but appear not affect the functioning, reading or comprehension of the program in any way! They were:
```
$ pip install pycodestyle
$ pycodestyle ...

  warnings.warn(
run.py:318:22: E231 missing whitespace after ':'
run.py:318:22: E701 multiple statements on one line (colon)
run.py:428:80: E501 line too long (82 > 79 characters)
```

In reality there are at least a dozen warnings relating to lines that are too long, but they do not affect the Heroku pseudo-terminal and do not appear to affect the readability of the code. I corrected them, saw that the caused bugs in the presentation, and even in the running of the code itself, and reversed them (one by one).

<!-- TOC --><a name="app-robustness"></a>
## App robustness

<!-- TOC --><a name="numerical-vs-characterstring-entries"></a>
### Numerical vs character/string entries
Aside from the restrictions on user entries mentioned above, the user must not enter either a negative number or an entry that cannot be rendered as an integer. Sadly, in most cases, I have not had the time to resolve all issues relating to the user entering characters and strings that cannot be converted into integers yet, but I have put the necessary software in place in some functions (notably the opening menu function and functions 6, 7, 8 and 9). I have told the users to be careful not to make non-numerical entries where numerical entries are expected.

<!-- TOC --><a name="out-of-range-numbers"></a>
### Out of range numbers
The app has been designed so that integers entered outside the valid range of values are handled elegantly without the program havin to shut down. Users are shown an appropriate message repeatedly until they make a valid entry.

<!-- TOC --><a name="yes-or-no-responses"></a>
### Yes or no responses
The app is designed so that the user can respond to yes or know answers by entering 'y' or 'Y' for yes; entering any other value than 'y' or 'Y' is interpreted as a no.

---
<!-- TOC --><a name="programming-philosophy"></a>
## Programming philosophy

Being an app generally modelling a procedural series of steps, little use was made of the concepts of OOP in its design. Few custom classes were specifically designed for the app. This was deliberate and should not be taken for any absence of understanding of the basic concepts of OOP.  It may, however, be useful to look at other programs created for a similar purpose when the time comes to refactor this code, and to use the advantages of OOD/OOP to make the code more efficient and more comprehensible.

<!-- TOC --><a name="sharing-the-hamamelis-google-spreadsheet"></a>
## Sharing the hamamelis google spreadsheet

This section is work in progress.

<!-- TOC --><a name="registering-for-heroku-and-using-it"></a>
## Registering for Heroku and using it

This section is work in progress.

<!-- TOC --><a name="lessons-learned"></a>
## Lessons learned

This section is work in progress.

<!-- TOC --><a name="other-unresolved-issues-and-future-development"></a>
## Other unresolved issues and future development

This section is work in progress.

<!-- TOC --><a name="credits"></a>
## Credits

This section is work in progress.


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
