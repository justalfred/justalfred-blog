Title: The Role and Importance of Curiosity in Data Science
Date: 2018-04-02
Tags: humans, code
Author: Just Alfred
Summary: I've keep hearing curiosity is important in data science. I wonder why....

Curiosity: The urge to know more.
I gave a talk last year about the role of curiosity in the practice of data science,
and I share the bits I still like here.
Now, many of us in the field have acknowledged its importance to the point of screening for it in interviews.
It’s obvious to most that healthy curiosity will lead to
serendipitous discoveries and introduce us to new skills and knowledge.
But as per my last post on ambiguity, nothing is black and white.
How does curiosity help a data scientist? Can we be too curious? What are its downsides?

# Science

To start, let’s consider how curiosity assists data science:

1. The goal of science, including data science, is to create new **knowledge**
2. Science is driven by **hypotheses**
3. More hypotheses of greater variety lead to a more complete **search** of the space of possible knowledge
4. **Creativity** drives the generation of new hypotheses
5. **Curiosity** drives creativity and the testing of those hypotheses

Therefore, greater curiosity will lead to more diverse hypotheses, and we will explore them faster.
This leads to a faster accumulation of knowledge.
Without curiosity, we can only follow established procedures for generating and testing hypotheses,
and we will be limited to what we already happen to know.

Curiosity about the task at hand helps mainly in the form of motivation.
That is, it drives the testing of hypotheses.
But the jewels, the creative hypotheses, are found when we explore seemingly unrelated territory.
This is where our minds expand.

# Serendipity

One of the wonderful features of data science is its interdisciplinarity.
I have seen people apply such a range of disciplines to their work.
Those who come from adjacent fields such as statistics, CS,
or computational physics or the like can bring their experience to their practice in a direct way.
But those coming from further afield also bring important strengths.

Some may consider social science an adjacent field, but for some reason, we tend to associate physicists
(though not chemists, despite the significant overlap in their methods)
with data science more eagerly than social scientists.
Yet, most physicists work with the luxury of
controlled experiments, explanatory models, clean data, and simple, inviolable laws.
Social scientists have to deal with
uncertainty, messy data, greater difficulty acquiring data,
unknown sources of error, and the complexity of human experience.
This, in my mind, and spoken as a former physicist, makes them
[especially well-equipped](https://cacm.acm.org/magazines/2018/3/225484-computational-social-science-computer-science-social-data/fulltext)
for the demands of most data science--moreso than physicists.

More distant, take philosophy.
Ethics and epistemology have been prominent subjects of philosophical discourse for millennia,
and they are absolutely relevant to the practice.
We *can*, but *ought* we?
Are our beliefs in our analyses justifiable? Philosophy teaches us how to think and ask questions.
It should be no surprise that fluency here would enhance a data scientist’s approach to problem solving.
Our colleague reading Marx may have a stronger sense of the contingency of labels and categories than us,
and that may lead them to conduct more thorough exploratory data analysis (EDA).

Or take art.
Art is about expression.
It often involves arousing particular affects through word, sound, shape, or color.
Storytelling is often a major part of data science.
Experience with art can inform how one presents data via argument, user interface, or data visualization.
You may find Agnes Martin, Josef Albers, or Mark Rothko confounding,
but someone moved by them will probably use color and line especially effectively in their visual storytelling.


<div style="text-align:center" markdown="1">
<figure>
  <a href="https://www.flickr.com/photos/jkannenberg/3538952506/in/photostream/">
    <img src="https://farm3.staticflickr.com/2266/3538952506_0a828273ba_z_d.jpg" alt="Detail of a work by Martin showing regular, rectilinear pencil lines" width="400" height="300">
  </a>
  <a href="https://upload.wikimedia.org/wikipedia/en/2/20/Josef_Albers%27s_painting_%27Homage_to_the_Square%27%2C_1965.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/en/2/20/Josef_Albers%27s_painting_%27Homage_to_the_Square%27%2C_1965.jpg" alt="A painting by Albers with stark, nested squares of slightly different colors" width="300" height="300">
  </a>
  <figcaption>Martin, left. Alberts, right. If these intrigue you, you just might be a whiz at data viz.</figcaption>
</figure>
</div>

I would love to work with someone experienced in theater acting.
I have a feeling that someone practiced in interpreting the world
through the eyes of a fictional character would ask very different and more pertinent questions
about users or a population than I would.

Whatever your background, hobbies, or momentary fascinations,
your history informs the way you see the world, and therefore the way you do data science.

# Practice

How do we foster curiosity in practice?
I like to make sure people are checking assumptions, checking their reasoning,
poking for holes in their own and others’ analyses, and nurturing their interests outside work.
For my own problems, I often explain my problems to others.
We’ve all had the experience of getting not two minutes into an explanation before realizing a gaping hole.

I also like to lead with creativity.
Often it’s when we creatively expand a mundane problem into a field of possibilities that
people’s curiosity can perk up.
Aside from brainstorming/[brainwriting](https://www.creativityatwork.com/2011/01/10/brainwriting/),
some good prompts when research just starts or gets stuck are to ask:
“Is there an easier way to do this?”
“What would [Stakeholder] ask?"”
“Are we sure we know what we’re optimizing for?”
“What’s the worst that can happen?”
“How will this help [Stakeholder]?”
You get the picture.

And of course, the simplest way to foster curiosity is to have a diverse team to begin with.
(And if all you have is “diversity of thought”, your team’s thoughts are not as diverse as you think.)
We want there to be discord and tension in a team along with the maturity not to see these as signs of dysfunction.
This tension will perk our ears to other ways of thinking, other vantages, unknown unknowns.
It’s akin to adjusting the dial away from exploitation towards exploration,
so that our teams can sway and not break under the vicissitudes of business.

# Risks

As I hinted, curiosity can go too far.
Especially if we forget to connect things back to our work.
It’s easy for curiosity to lead to distraction.
Even if our wanderings remain related to our task, we might find ourselves down so many rabbit holes that
we forget our actual commitments.
There is always the risk of “analysis paralysis” if
we come up with so many questions and hypotheses that we’re unable to make a decision.
Then we may miss critical windows of opportunity.
To guard against these patterns, I recommend checking in frequently with stakeholders and subject matter experts.
They can often eliminate entire categories of hypotheses based on their needs or experience.
Also, though uncomfortable, meeting more frequently than we can iterate can help
save time by forcing feedback before we go too far down a bad path.

As a practical matter, curious exploration often looks like wanton scribbles.
It’s easy to end up with a huge tangle of uncommented code in a Jupyter notebook
that fails the moment we restart our kernel.
We like the output of one cell, but we can't get back to the state that generated it.
Communication and reproducibility are key to reliable science,
so we must try to keep our work traceable, even when we think we're just toying around.
The best solution will depend on a team’s culture of sharing work, code, findings, and documentation.
(A musing: I was taught since college some rules for maintaining a useful lab notebook.
Date every page.
If I write something down wrong, cross it out so I can still read it and note why and when I did so.
Start each experiment by noting what I'm trying to do and expecting.
Stuff like that.
I wonder if a similar set of guidelines for EDA notebooks would be worth stating.)

There also is the sin of hunting for low p-values across many different statistical tests over the same data.
I argue that curiosity is valuable for generating more hypotheses, yes.
We need to test these hypotheses, yes.
We have a finite reserve of data, yes.
But if we test every hypothesis on the same data,
then by chance some tests will confess spurious patterns or hide actual ones.
The more we interrogate a data set, the less we can trust the results.
If you must do this, be very careful with the results, and consider an approach to mitigate the risks.
I refer you to your local statistician for further guidance.

# The Right Questions

There are good reasons that data science in particular thrives on curiosity.
I’ve shared some ways to prompt it when you feel you need more.
But curiosity is not an absolute virtue.
It can lead to distraction.
It can motivate sloppiness.
And without the support of powers of synthesis, empathy, some domain knowledge, and grit,
it may actually spin us in spirals away from our goals.
In the end, it comes back to the hardest skill to learn in data science: asking the right questions.
