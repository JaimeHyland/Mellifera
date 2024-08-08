![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Mellifera
A simple B2C ecommerce website for the online sale of honey-bee-related equipment, materials, tools, consumables and packaging to English-speaking German hobby beekeepers.

Code Institute - Fifth Milestone Project: Under my interpretation, the requirements for this project would be satisfied as follows:

Build a Full-Stack e-commerce website that facilitates the online sale of and payment for a range of beekeeping-related goods based on a business logic that reflects the variety and taxonomy of that range of goods, satisfying the expectations of both an imaginaray online store owner and of their imaginary customers.

I believe that completing such a project would satisfy the requirements listed for the fifth porfolio project in Code Institute's LMS, i.e. to show  an appropriate level of understanding on my part of a number of different concepts, technologies and disciplines related to Full-Stack programming in the e-commerce sector:

- Django development on a cloud-based IDE (using Django-3.x on a VS Studio IDE hosted on Gitpod).
- The creation, maintenance and use in Python code of database models, implemented using Django, running on Postgresql.
- Use of agile methodologies via the project features available in GitHub, associated with the repository for this portfolio project.
- Creation of UI elements outside Django's admin panel to allow users to create and update records in database tables.
- The use of robots.txt and sitemap.xml files.
- The use and purpose of descriptive metatags in HTML code.
- How to link to external resources using the Rel attribute.
- How to make a custom 404 error page.
- The use of social media, using the instance of Facebook as an example.
- Creation of a newsletter signup form.
- The use of DEBUG mode, and in particular the need to turn it off before deploying.
- The Django functionality allowing users to log in and out of the project application.
- The use of Stripe together with Django, bootstrap and bespoke HTML, CSS, JavaScript and Python code to demonstrate a(n almost) working online purchasing system
- The correct use of linting to check code formatting.
- Detailed human-made logs of testing processes.
- Appropriate use of online research and problem-solving resources publicly available on the Internet.


![Behives in autumn](/assets/documentation/beehives_in_autumn.webp)

*Traditional beehives on an autumn evening*

## An apologetic note for the examiner
I do not expect this portfolio project to achieve the pass criteria in its current state. A number of the requirements listed in the instructions for it have not yet been implemented. I am obviously not a very fast coder yet, for which I apologise. In my defence, I should say that I feel that, out of the three options for the final module of the course, at least the e-commerce option &mdash;and in particular the walkthrough for the boutique-ado ecommerce website&mdash; involves a good deal more work (rather than simply more complexity) than the first four modules and, though I was to some extent forewarned of this, I didn't expect the difference in terms of time required to be _quite_ as big as it has turned out to be. There were a number of other circumstances, including a short bout of illness, that contributed to my inability to finish on time, but those circumstances paled into insignificance beside the widely recognised technical flaws and continuity gaps in the final walkthrough, as well as its sheer length.

I am determined however, to get this final part of the course done properly, given a reasonable amount of time to complete the job. I realise that my failure to complete the 5th project on time will put a pass ceiling on my efforts, but my priority has always been to learn the skills I need to learn rather than to receive an especially impressive grade on my certificate.

I'm very grateful to the tutors for their ongoing help in getting through this very challenging section of the course (though they were also just as supportive, encouraging, patient and competent in earlier parts of the course) and to my customer care person for their encouragement and advice. I'm grateful too to my mentor for the help he has provided so far, and I hope to benefit further from his expertise and generosity over the next couple of weeks in my efforts to finish this project.

Thanks very much to you as well for your patience!  And my sincere apologies for the unfinished state of my project!

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

![Elise's initial wireframe for her project homepage](/assets/documentation/readme_assets/Mellifera_wireframe_home.png)

*Elise's initial wireframe for her project homepage*

It had struck Elise since taking up beekeeping how her fellow beekeepers introduced themselves in beekeeping circles by mentioning the beekeeping system they used straight after giving their name.  Elise has in fact developed the habit herself: she now almost automatically starts every talk she gives to beekeepers with the words "My name's Elise Knolle and I work using Langstroth". Other users of the Langstroth measurements then know immediately that their systems work well with hers, making it easier for them to help each other with spare beehive resources when someone is short of some resource or other, or wants to expand. Indeed the expression "working out of System X" is almost a declaration of identity in beekeeping circles, and thus it quickly occurred to her that the names of such systems (Langstroth, Dadant, Zander and DNM -- _Deutsche Normalmaß-Beute_) were likely very useful keywords for marketing purposes. She therefore noted these and a number of related terms as in her notebook for short-tail keywords (see the sub-section on web marketing below).

The wireframe she made is primarily for her own reference, but also to show her friends in the local beekeeping society so they can give a little marketing-relevant feedback. I'll now discuss the feedback they and others gave her in Marketing section below.

- - -

## Product range & Marketing

### Face-to-face 'interviews'

Elise didn't actually do any formal face-to-face interviews with anyone (hence the scare quotes above), what she did was corner a number of fellow beekeepers, show them her wireframes and explain her plan in more or less detail, treating them as a sort of informal focus group. I won't reproduced the copious notes she took of these conversations; suffice it to say that the most important points they made included the following:

- Product range
>> Their expectations of such an e-commerce website were rather more ambitious than Elise's original idea: they would have expected a wider range of products to be available aside from wooden hive components. They saw it as desirable that the site should as near as possible be a "one-stop-shop" for beekeeper needs; to have in particular the capacity to offer the following categories of product:
  - plastic feeder trays, sleeves and bottles
  - varroa mite treatment equipment and chemicals
  - beekeeper tools (all the way from handtools and buckets to honey extracting machines) and protective clothing
  - honey packaging (chiefly jars and lids)
  - wax foundations for insertion into honey and brood frames
>> but ...
  - living bees
>> The one thing they seemed to agree was not necessary (or even desirable) for her to sell in her shop were packages of bees themselves: mated queen packages, hive nuclei, etc.. The consensus was that such products should be left to a specialist producer/dealer and that offering them would do little to add to the site's reputation as a reliable and professional supplier

- Filtering by basic hive design
>> Beekeepers appreciated her idea of giving them up-front on the homepage the option of filtering out hive components incompatible with their hive dimensions by clicking on their chosen system as it appeared in a horizontal bar at the bottom of the site header, which would have the effect that all their subsequent searches limit themselves to products compatible with their systems, unless and until they decided to undo their filter by clicking on the name of their chosen system again. While no beekeeping system is selected, no such filter is enforced.

- Other filters and sorting options
They also let her know that the ability to filter according to a number of different criteria would be appreciated, with the general consensus being that "the more, the better", but that the site's products should be filterable and sortable according to the categories mentioned above under "Product range".

- Added marketing discussions
  - Beekeeper's forum
>> There was some humming and hawing when Elise mentioned the possibility of adding a separate beekeeping forum attached loosely to the site: there was no clear consensus but many thought the internet were plenty of discussion fora on the internet for beekeepers and that a new one, aside from requiring an awful lot of moderation effort, would not provide much added value at the moment for potential customers.
  - Techno-beekeeping blog
>> However, some of her pals seemed at least mildly interested when she mentioned the idea of adding a little blog to her site, especially if she concentrated on the interface between apiculture and consumer software development.
  - Hive inspection app 
>> The hive inspection app that Elise had half finished using Flutter a couple of years ago, whose purpose it was to make it easier for beekeepers to note down observations while inspecting their hives, seemed to some to be a potentially useful tool on condition she managed to complete and fully test it and make it available on Google Play and/or Apple App Store. Having such a good quality tool associated with the site, many thought, could well add authority to it in its very well-defined domain. There were other products on the market, but they were all too inflexible in their workflow and, in the words of one early adopter were "not much use".  -- A page listing links to official local and national beekeeping authorities, associations and university faculties were mentioned as being possible useful service to site users.

### Phone calls and e-mails with Tomáš
Through some more or less detailed conversations with Tomáš via WhatsApp and email, she got a clearer idea of the full range of products he can supply. As well as simple bee boxes and frames, he can also supply a couple of designs for entrance and feeder boxes, queen excluders, inner covers and bee escapes, for example, and he has a business partner whose phone number he can give who makes excellent galvanised steel hive roofs in various sizes.

### Other consultations
A number of chats with relatives and non-beekeeping friends underlined the point that Elise's site is far more likely to be successful if she gets herself in a position to sell a full range of beekeeping supplies.

One enormously important area of research will of course be to see what the compeition is doing. There are already a large number of beekeeping e-commerce sites already on the internet aimed at the DACH market. Practically everyone with whom she discusses her _Mellifera_ site mentions this as an essential preparation. The obvious rubric in which to frame this information-gathering effort is to see it as a way to formally define the site's unique selling proposition (USP) on the basis of places Elise can go (with Tomáš' and perhaps others' help) that other online beekeeping suppliers can't. The initial competitive advantage she has identified is value for money at the quality end of the market, but there may well be others. She suspects, for example, she can project superior authority and expertise in the beekeeping sector through better organisation and presentation of information on compatibility and incompatibilities between popular standard beehive designs used in the DACH region.


## Elise's initial marketing conclusions

### Marketing-relevant measures for immediate action

- The first of Elise's conclusions from all this informal consultation was that she definitely needs to find suppliers for all the other commonly required beekeeping supplies. That task will have to take a high priority as soon she's successfully concluded her code demonstration for Tomáš. 

- She'll add a newsletter subscription facility early in the development process as it's likely to be relatively simple to code a GDPR-compliant subscription form and doing so won't commit her to extra work on a regular basis: she can always write up newsletters as the need and opportunity arises.

- While the site will need to be developed in English for Tomáš's sake, she'll have to keep in mind the need for it to switch the live version of the shop to German by default in a German-speaking DACH environment (it's a pretty basic marketing requirement to speak to your customer base in German), but to switch to English (and stay there) if the user expresses a preference for English. Though, depending on the time available to her, she may decide to leave internationalisation to a later stage and simply replace all the English texts with German.

- Elise will need to identify and formulate what her USP is going to be and set further marketing objectives to ensure that her chosen USP becomes and remains a reality.

- She'll need a set of logos, fonts, styles and colour schemes, which she'll develop on an ongoing basis while developing her proof-of-concept site.  She'll also consult with a designer friend of hers on how the site's look might be improved once she's completed the demo.

- Elise is a keen user of Facebook (perhaps too keen, she often thinks); she'll put together a Facebook page for _Mellifera_, render it as far as possible in the website's livery (see the previous point) and try to contribute to it occasionally, other work permitting.

- Elise reckons that by far the most important page on the website (especially in relation to Tomáš' products) is the *product detail* page, where users will expect to find all the information they need to tell whether the individual article is compatible with their beekeeping system. A well-structured product details page containing accurate information will contribute very substantially to the site's expertise, authority and trustworthiness.
  - Firstly, products incompatible with the site user's chosen filter (if any) should simply not appear on the products listing page.
  - Secondly, beebox products should show a full set of interior dimensions, along with a clear indication of the type and (especially) thickness of the timber used.
  - Where relevant, assembly instructions and any recommended wood treatments should be mentioned, as well as any additional consumables or materials needed to put the piece together. All such materials should as far as possible also be available from the site, and should be linked to from all relevant products. Bee boxes in particular will need non-toxic paints or wood treatments and honey frames will need support wires, nails and eyelets, as well as beeswax foundation sheets.
  - Assembly instructions for such standard hive components are widely available on the internet.  Elise won't necessarily therefore need to create assembly and care instructions, but she should take a look at existing tips and tricks on the internet (in youtube videos, for example) to see if any such resources are relevant and authoritative enough to be worth linking to. It might even be worth adding some of Elise's own tips and tricks.

### ... and possibly for later

- Elise won't commit for the moment to the effort of creating and maintaining a regular blog either directly on the site or linked to the site. She'll keep the option in the back of her mind.

- She has some experience in editing video from school, and has a pretty good video camera. At some stage she might consider creating some of her own material either directly for the site or designed to indirectly nudge traffic towards the site. She knows from experience, however, that this involves a lot of hard work and could well require long-term commitment. She'll therefore file that too in the back of her mind for possible future use.

- As Elise hasn't got a clue about the hive systems commonly used in countries outside the DACH area, localising to other languages can wait at least until she's got a bit of data on how beekeeping is done in other parts of Europe.

- While Elise's market is extremely well-defined and online advertising may well therefore be very easy to target, Elise's lack of resources forbids her from considering it, though she might at a later stage, depending on her initial success either use her own profits or talk to suppliers, possibly including Tomáš, about subsidising future efforts here.

- She should keep in mind the large number of youtuber and blogger beekeepers using various languages and with varying numbers of followers, possibly offering free products to the most relevant and authoritative of them, in the hope that her wares might end up being showcased on such output. She'll have to bone up on the applicable law and on platform provider rules on advertising (paid for either in cash or in kind). Again, this is something for the future rather than an immediate priority.

- Elise decided not to create a marketing survey (using Survey Monkey or any other similar online service) for the moment for three reasons:
  1. she doesn't yet have a suitable list of identifiable respondents
  2. she isn't yet sure precisely what questions she needs to ask
  3. she has other things to be getting on with (not least some pretty challenging programming)
>> She has, however, made a mental note to consider creating and sending out such a survey when she has a viable list of respondents and a bit of clarity on exactly what it is she wants to know. 

- Elise has a phobia of committing to spending money when she's not sure how much the total is going to be, so she's liable to keep clear of pay-per-click advertising until she can be very sure that it's going to substantially more than pay for itself.

- The DACH region is home to a variety of charities interested in the protection (in ascending order of specialisation) of insect life in general, of the many species of wild bee native to central Europe, of the European Honey Bee, and of central Europe's own native Dark Honey Bee sub-species (Apis _mellifera mellifera_, which has been driven to the edge of extinction through displacement and hybridisation with other sub-species of Apis _mellifera_ imported by beekeepers since the late 18th century from southern Europe). Elise has communicated with and contributed to some of these charities in the past. She may discuss a public association with one of them to help raise the authority of the site.


### CEO and the like

- Some time when she needs a change from the programming effort she'll brainstorm out a list of short- and long-tail keywords (in German mostly) to insert strategically in her site and run a few experiments with Google search to see which of them come up most frequently in searches.

- She'll have a chat with a friend who's a specialist in CEO for advice on how far to go with inserting the keywords, etc..

- She might consider shelling out the ten dollars she'll need to pay to search for keywords used outside the territories covered under the free version of Wordtracker.com.

- She'll need to draw up a list of beekeeping associations, organisations, clubs, institutes, etc., to be able to include them on a list of useful links somewhere on the site. Other uses for this information could well occur to her in the future.

- She'll have to have a chat with Tomáš (and any other possible suppliers) about the extent of product documentation, and in particular the quality and style of any immages available.

- She'll create a sitemap.xml file to ensure that crawlers get to where she wants them to look.

- She'll create a robots.txt file to ensure that crawlers don't get to where she doesn't want them to look.

- In general, she'll consider SEO when creating any content in her site, both at an initial stage and on an ongoing basis, putting herself in the shoes of Google's team of raters. In particular, she'll be careful to cite sources for any factual information included on the site, and to choose only clearly trustworthy sites as sources.

- She'll include a privacy statement, an "Impressum" (a declaration indicating who's responsible for the site contents required by German, Austrian and Swiss law) and a splashscreen allowing the user to opt out of the cookies for use in Google Analytics.


## Design of website's logic and structure

### From the user-shopper' point of view
From the point of view of a guest user, the core website will consist of nothing more than a _home_ , a _products_, a _product_details, an _order_list, an _order_, a _checkout_ and finally a checkout_success page. The _home_ page, apart from providing the usual links to routinely and legally necessary administrative pages in its footer and allowing a guest user via a dropdown list to either _Sign on_ as a registered user or _log in_ as an existing one, gives that user the option of creating an initial filter based a particular hive system or systems (see above), along with providing a number of routes to reach a _products_ overview page. This _products_ page simply lists out a number of products, each in its own cell, filtered according to any setting that the user has already chosen on the _home_ page. On the _products_ page, the user then can refine or remove the filter, thus increasing or reducing the range of the products listed on the page, or double click on a particular product, which will bring the user to that product's _product/_detail_ page. Some products will be available a variety of sizes (for example, Langstroth hive boxes will be available in _1/2_, _2/3_, _3/4_ or _1/1_ heights and protective clothing will be available in _S_, _M_, _L_ and _XL_). Other products (tools and tins of non-toxic paints) will not.

For the moment, aside from box heights and clothing sizes, any difference in other dimensions, material or special features will be dealt with by creating a separate product record.

In order to provide the flexibility to add new size scales in the future, the two size scales (bee box height and clothes size) will be stored as separate records in JSON format in the database under a simple _Size_ table connected to the relevant _Product_ records via a foreign key. For the foreseeable future, all _Size_ json records will be one-dimensional.

Thankfully, there are no products in the prospective range that require both separate heights and clothing sizes! :) However, it may be useful in the future to allow a particular product to have sub-products on two dimensions (such as say, "_1/2_, _2/3_, _3/4_" or "_1/1_" and "_with lip_" and "_without lip_"), so it might be simpler to allow the database structure to handle such issues, even if the code doesn't necessarily need to implement such a hypothetical requirement. While the Django framework that Elise is using in this project makes database updates much less difficult than using vanilla SQL, making such late changes is not without its risks.

Users can put items in their pre-order list only from that item's _product-detail_ page. Clicking on the _Add to order list_ button will put the chosen number (and the chosen size, where relevant) of that product on the _order-list_ page, giving the user a message that they have successfully done so, and returning them to the _product_ page with the chosen filters still intact. The shopper can continue to browse through that page. The top left of each page of the site will show the total monetary value the products contained in the order_list.

Clicking on the _Go to order list_ button, icon or link will bring the user to their _order list_ page. The above-mentioned message contains a link to the pre-order page, as does the pre-order icon at the top right of every page on the site. The products page will ahow a _Go to pre-order_ button at bottom right.

### From the registered user's point of view

### From the superuser point of view

### Database design

![Some flow charts portraying a selection of important Mellifera workflows](assets/readme_assets/hamamelis.gif)

*Some flow charts portraying a selection of important Mellifery worklflows*

A good proportion of the database tables required for the project were provided by Django's standard user authentication system, _django.contrib.auth_. I do not propose to discuss that system in detail.

... However, it may be useful in the future to allow a particular product to have sub-products on two dimensions (such as say, "_1/2_, _2/3_, _3/4_" or "_1/1_" and "_with lip_" and "_without lip_"), so it might be simpler to allow the database structure to handle such issues, even if the code doesn't necessarily need to implement such a hypothetical requirement. While the Django framework that Elise is using in this project makes database updates much less difficult than using vanilla SQL, making such late changes is not without its risks.

### Frameworks

### Bootstrap
### Django

### jQuery

## Setting up the environment

### Registering for Heroku and using it

### Registering for Stripe and using it

### Registering for Amazon AWS and using those services

## App robustness

### Incorrect user entries

## i10n and l10n

## Help functions

## Manual testing

### Robustness testing
The need for robustness testing was considerably eased by the fact standard Django processes provided very clear pathways for all users &mdash;whether registered or guest customers, or even superusers&mdash; to follow, leaving only a few spots where invalid entries were possible.  

### Features testing

### Device compatibility and responsiveness

## Bug fixes, warning resolution and linting

### Bugs
Bugs will be fixed as they arose during smoke testing (see below).

As far as practicable, all Bugs are resolved separately and the Bug resolution is recorded in Git commits separately, prefixing the commit text with "Bug: ".

### Warnings appearing on consoles, terminals and logs

### Linting

## Unresolved technical issues

## Lessons learned

## Other unresolved issues and future development

## Credits

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
