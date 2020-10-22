Title: Getting Started with Pelican on Github Pages
Date: 2018-06-09
Tags: explaining, tech
Author: Just Alfred
Summary: How I got this site started

I want more people to blog.
I want more people to give voice to their experiences.
Especially those people who think they have nothing to say.
It's not that I think we need more noise on the internet.
It's that the conversations out there are often dominated by a few loud voices that are often not representative of the masses.
It's that sometimes the most helpful thing for you to hear is that someone out there has gone through what you're going through and can tell you something about the experience.
I want more people to blog.

# Intent

There are many great, full-featured blogging platforms out there.
For me, I wanted stronger ownership over my content.
I wanted a blogging platform that allows me to draft in Markdown
so I could easily share code or data-related work (though in retrospect, I've hardly done any of that).
I didn't want to pay much money, and I wanted to avoid maintaining a server.
After a few months of indecision, I settled on using Pelican to generate a static website which I would host on Github Pages.
Pelican has the advantage of being well supported and in a language that I like (Python).
It's similar to Jekyll for those who are familiar.
Github Pages is free and allows me to use a custom domain with [enforced https](https://help.github.com/articles/securing-your-github-pages-site-with-https/).
In the end, I have a blog that I feel secure about and that costs me nothing more than the domain registration.
About $10-20 a year.

There are various guides out there that show how easy it is to get started publishing with Pelican.
My problem is that I don't like uncertainty, and these guides typically explain 'what', but not 'why'.
What are all these auto-generated files for?
How do I customize the look and organization?
How can I be sure I don't expose more information than I want?
Because of my insecurity, it took me a lot longer to get started than I wanted.
Here is my summary of the steps I ended up taking, and an explanation of what each step does.
Hopefully this will save the reader time bouncing around various tutorials, blog posts, and documentation.

# Pelican

If you're not familiar with the terminology so far, Pelican is a Python library that lets you generate static websites from templates.
By static, we mean that the content served is the same for everyone because it's generated in advance.
Blogs are typically static while ecommerce sites (where you login, have an account, order history, etc.) are typically not.
Templates save the blogger from having to muck about with verbose HTML.
[Markdown](http://daringfireball.net/projects/markdown/) and [reStructuredText](http://docutils.sourceforge.net/rst.html) are two templating formats that Pelican handles well.
As an example, Markdown lets you specify a link with:

    :::
    [a link](https://blog.justalfred.com)

instead of:

    :::html
    <a href="https://blog.justalfred.com">a link</a>

Pelican itself is highly customizable and extensible.
You'll want to be somewhat familiar with Python and git to have an easy time following along.
I've been working in Linux, but these instructions will probably work in OSX as well.
Windows users will have to interpret the commands and paths accordingly.

# Install

So let's get started.
You can create a new python virtual environment if you want.
If you're sloppy and lazy like me, just go ahead and install a few packages.

```
$ pip install pelican Markdown typogrify
```

Markdown is, of course, only necessary if you want to use Markdown.
[Typogrify](https://github.com/mintchaos/typogrify)
makes things a little prettier by converting straight quotes into curly quotes and such.
It's also optional, but consider that the last commit is from 2014.
I have had no problems with it.

# Generate the initial boilerplate

The first thing to do now is to use the quickstart script to generate a skeleton for your blog.
This step doesn't make your blog, but it makes the files you'll use later to make your blog.
If you mess up, you can delete the generated files and just start right over.
For most of the prompts, you can just accept the default.
For most of the rest, you can always change those settings later if you change your mind.
In particular, though, I strongly recommend generating the Makefile.

```bash
$ pelican-quickstart
Welcome to pelican-quickstart v3.7.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.] $PICK_A_DIR
> What will be the title of this web site? $PICK_A_TITLE
> Who will be the author of this web site? $PICK_A_NAME
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) 
> What is your URL prefix? (see above example; no trailing slash) https://blog.justalfred.com
> Do you want to enable article pagination? (Y/n) 
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Paris] 
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
> Do you want to upload your website using FTP? (y/N) 
> Do you want to upload your website using SSH? (y/N) 
> Do you want to upload your website using Dropbox? (y/N) 
> Do you want to upload your website using S3? (y/N) 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) 
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at $PICK_A_DIR
```

At this point, Pelican has put new files and folders into the folder you specified (`$PICK_A_DIR`),
creating the folder if it didn't already exist.
You can navigate to this folder and find the following:

* develop_server.sh - This is a very useful shell script for seeing the effects of your updates and is called by the Makefile.
* Makefile - This file defines `make` commands that perform the most important tasks like generating your site and starting a local http server.
* pelicanconf.py - This file contains settings to customize your site.
* publishconf.py - This file contains settings that are only used when you're ready to publish to the web.
* content/ - This folder is where you'll put the templates and files that will be translated into the content of your site.
* output/ - This folder might not exist until you convert your content into html. By default, the translated website lands here.
* fabfile.py - This has something to do with [fabric](http://www.fabfile.org/) which I don't use.

Some of these are discussed in further detail later.

# Initial content

You'll want to add some [content](http://docs.getpelican.com/en/latest/content.html) now.
There are two major types of content to distinguish: articles and pages.
Articles are the main content of your site, like blog posts.
Pages are relatively static, like 'about' or 'contact' pages.
Let's start with one of each.

Create a file called, `content/cat1/test.md`, and give it the following contents:

```
Title: Test Post
Date: 1997-08-29 02:14
Tags: testtag
Author: My Name
Summary: This is an article

"Hope" is the thing with feathers -
...
```

Next, create a folder, `content/pages/`, make a new file called, `about.md`, and give it the following contents:

```
Title: About
Author: My Name

Bonjour, wilkommen a kono blog.
```

You should, of course, eventually replace all of that with your own information.

Notice how the files begin with metadata that are not Markdown syntax.
Pelican will interpret these fields when it translates the Markdown into HTML.
You can read more about this section [here](http://docs.getpelican.com/en/latest/content.html).

You now have a few different ways of generating the html of your shiny new website.
The most direct is to run `pelican content/` (supposing you're in the project's root folder).
This will populate the folder, `output/`, (or generate a new one wherever you are)
with the static html and other assets for your blog.
Equivalently, you can run `make html` with the same result.
What these commands do is examine the files in `content/` and the settings in `pelicanconf.py` to translate everything into your new website.
There are a few settings at the top of `Makefile` that you may wish to edit, but the defaults are probably fine.
Eventually, you'll send the contents of `output` to wherever the files will be hosted--GitHub Pages, in my case.
But not yet.

Once you've done this, to view this in a web browser, you'll need to start a webserver from within the `output` folder.
Fortunately, Python comes with one.
Navigate to the `output/` folder.
If you're running python 2 you can run `python -m SimpleHTTPServer`.
If you're running python 3 (good for you), the command is `python3 -m http.server`.
Easier for most, you can run `make serve` from the root folder of your project.

Now open a web browser, navigate to `http://localhost:8000` and see the results of your work so far!

Of course, the authors of Pelican have provided even more convenience for you.
Given this workflow so far, every time you update a file, you have to regenerate the html to see the updates in your web browser.
Meaning, stop the webserver, save, `make html`, `make serve` after every change.
Instead, you can run `make devserver` once which does three things.
First, it generates the html of your site.
Second, it starts a webserver at port 8000 as before.
Third, it detects when content gets updated and will regenerate the html automatically.
All you have to do is save content then refresh your browser to see the latest.
When you're done editing and want to stop the webserver process, run `make stopserver`.

Finally, a couple more content concepts.
As you click around, it may be hard to tell the difference between all the pages since they look so similar with so little content.
But there are various index pages as well as the one article page and one about page so far.
The top-level index is what you see first.
Try creating other dummy articles to see how it looks.
Along the top, you see a link to the About page you made as well as a link to a category index, cat1.
Articles can belong to a single category, defined by the folder structure within the `content/` folder.
Articles can have multiple tags, though, defined in the metadata.
Use this to your advantage to keep your site organized.

# Version control

It's not necessary, but it's probably a good idea to keep a version history of your blog contents.
If you're familiar with git, github, and creating new repositories,
then I advise putting `cache/`, `output/`, `*.pyc`, and `*.pid` in `.gitignore` at minimum.
My blog contents are [here](https://github.com/justalfred/justalfred-blog).
You can view my source code if anything in this tutorial needs clarification.

If you're not familiar with version control, don't worry--the site doesn't depend on it.

# [Custom domain](http://docs.getpelican.com/en/latest/tips.html#extra-tips)

If you own a domain that you'd like to use, this is how.
Otherwise skip this section.
First, create a file called `CNAME` in a new folder, `content/extra/`.
Edit the file so the only contents are the domain you want to use, e.g.: `blog.justalfred.com`.
Next, edit your `pelicanconf.py` to add the following lines.
Note how they refer to the file you just created.:

```python
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
```

Now, all the links that pelican generates (e.g. from an article to the home page)
will use your CNAME as the domain!
Or, it will once we're ready to publish.
For now, everything still links to localhost.
You can regenerate your site and see where the CNAME file ends up if you're curious.
Of course, there's nothing special about the folder, `extra/`, but this seems to be the convention.

# [robots.txt](http://docs.getpelican.com/en/latest/tips.html#extra-tips)

If you care about web crawlers indexing certain portions of your site, you can create a file, `extra/robots.txt`.
This [establishes a policy](http://www.robotstxt.org/robotstxt.html) that web crawlers are recommended to follow.
The major ones will respect your settings.
Mine has the following contents:

```
User-agent: *
Disallow: /drafts/
Disallow: /theme/
```

If you didn't follow the last portion, you will have to add the following to your `pelicanconf.py`:

```python
STATIC_PATHS = ['extra/robots.txt']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}
```

If you did, edit the relevant lines to:

```python
STATIC_PATHS = ['extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'},
                       }
```

# Typogrify

If you chose to install `typogrify` earlier, you'll want to enable it.
Add the following to your `pelicanconf.py`:

```python
TYPOGRIFY = True
```

# Pelican themes

If you want to customize the look of your site, you can get pretty far by using one of the [packaged themes](https://github.com/getpelican/pelican-themes).
I chose the '[pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)' theme because of its completeness and simplicity.
It has a minimalist aeshthetic, it's responsive, it recognizes a host of extra settings.
It can be further customized by editing a custom CSS file as described [here](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3#custom-cssjs).
Good luck if you try. Every time I touch CSS, I lose hours of my life.
Whichever theme you choose, clone the 'pelican-themes' repo, and add the following to your `pelicanconf.py`:

```
THEME = 'path/to/pelican-themes/chosen-theme'
```

I have the repo cloned outside of the blog, to avoid overlap weirdness with git, so for me, it looks like:

```
THEME = '../pelican-themes/pelican-bootstrap3'
```

Note that some of the themes have extra installation instructions, including my chosen one.
Check the `README.md` files for more.

# Time zone

You will probably want to set the time zone that your site uses.
This [seems](http://docs.getpelican.com/en/latest/settings.html#timezone) to be mostly important if you set up RSS or Atom feeds later on (which I recommend--I love RSS).
Simply add the following to your `pelicanconf.py` with the appropriate [time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones):

```python
TIMEZONE = 'America/New_York'
```

# publishconf.py

As mentioned earlier, `publishconf.py` is much like `pelicanconf.py`, but the settings listed there are only applied for final conversion.
For instance, you might have noticed that all the internal links on your site point to `localhost` instead of the actual domain.
`publishconf.py` is where you'll specify to pelican to use the actual domain.

You probably also don't want to include Google Analytics tracking in the draft versions of your site.
To add Google Analytics tracking, [set up GA](https://support.google.com/analytics/answer/1008015?hl=en) and add the tracking ID to `publishconf.py`:

```python
GOOGLE_ANALYTICS = "UA-XXXXXXXX-X"
```

Note that I've chosen to remove GA tracking to give my readers a tracker-free experience.

If you want to generate RSS feeds (some of us still use RSS) you can do that quite simply in `publishconf.py`:

```python
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
```

If you want to use [Disqus](https://disqus.com/) to enable comments, you can
[add the sitename](http://docs.getpelican.com/en/latest/settings.html#DISQUS_SITENAME) in this file as well.
Note that I've chosen to eschew Disqus for privacy reasons, too.

Once you're ready to share your site with the world, you can generate a final version of your site.
`pelican content -s publishconf.py` and `make publish` are equivalent commands to do this.
Guess which one I use.
It's a good idea to delete the output folder first.
Everything will be regenerated, but if you made changes that left behind some old versions of old files, you want to be sure to clear those.
Note: when your site gets beyond a certain point, you may want to speed up the conversion process by having Pelican [only read modified content](http://docs.getpelican.com/en/latest/settings.html#reading-only-modified-content).
I haven't tried this yet.

Once you've run one of those two publish commands, you can upload your content to wherever they will be hosted.
If you're using GitHub Pages like me, you'll want to create a repository named, `USERNAME.github.io`, with your username.
Any repo following this naming scheme will be [recognized and served automatically](https://pages.github.com/).
You can then simply push your content to the master branch of that repo, and wait a few minutes to see it appear at `https://USERNAME.github.io`!
(Please take care to [enforce https](https://help.github.com/articles/securing-your-github-pages-site-with-https/)).

Note, if you set up a CNAME earlier, you'll also need to do a few extra steps [with Github](https://help.github.com/articles/quick-start-setting-up-a-custom-domain/)
and with your domain registrar.
Check their documentation for specific instructions.

# Import old blog

Since I was migrating posts out of Blogger, I did this in a three-step process.
First, I used Blogger's [export XML functionality](https://support.google.com/blogger/answer/97416?hl=en) to retrieve my content.
Second, I ran the following command to convert the XML to Markdown.

```bash
pelican-import -m markdown --feed --dir-page blog___.xml --dir-cat
```

Third, I wrote a python script to do a bit of cleanup.
That's admittedly a hand-wavy magic answer, but it was a very specific need.
If you're doing the same, you can see my script [here](https://github.com/justalfred/justalfred-blog/blob/master/convert.py) and edit it to suit your needs.

# Next steps

As I mentioned, Pelican is easily extended and customized.
Check out [pelican plugins](https://github.com/getpelican/pelican-plugins) for a large collection of extensions.
At the time of publishing this, I'm only using `tag_cloud` and `i18n_subsites` for my theme.
I also recommend going through all the available [settings](http://docs.getpelican.com/en/latest/settings.html)
to see if you might like some non-default behavior and the
[FAQ](http://docs.getpelican.com/en/stable/faq.html) and [tips](http://docs.getpelican.com/en/stable/tips.html) for other tips.
The particular theme that you choose may have other settings as well.
Finally, you can edit style to your heart's content.
Or not at all.

If anything didn't work quite right or if you'd like me to expand on any section, please email me or tweet at me.
Happy Blogging!
