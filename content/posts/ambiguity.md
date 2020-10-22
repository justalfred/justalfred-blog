Title: The Acceptance of Ambiguity
Date: 2018-03-26
Tags: humans, code
Author: Just Alfred
Summary: When the answer isn't clear, it might mean it doesn't need to be.

<div style="text-align:center" markdown="1">
<figure>
  <a href="https://en.wikipedia.org/wiki/File:Yin_yang.svg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Yin_yang.svg/240px-Yin_yang.svg.png" alt="Yin-Yang symbol">
  </a>
<figure>
</div>

[A little while back]({filename}/literature/literary_theory.md), I tried to illustrate the value of accepting ambiguity via Emily Dickinson and Jacob Bronowski.
Poetry and Science.
This topic bears expansion, so now I expand.
I’ve said very little to data scientists to date, even though it’s my field.
So finally, I will address you first, then share general lessons for all of us.

# Ambiguity everywhere

There is nothing profound in my saying that life is more complicated than it seems.
Yet, though a commonplace, outlining this complexity takes great effort against the culture and wisdom we receive.
For example, we like to bucket ourselves into one of two opposites, yet are these ever stable or coherent?
Female/male, gay/straight, introvert/extrovert, right/wrong, oppressor/oppressed.[^1]
Even something as seemingly fundamental as being right- or left-handed has exceptions—some are ambidextrous, others have lost their originally dominant hand.
Most of the time, when presented with a dichotomy, the answer that feels right is
“sometimes one sometimes the other” or “somewhere in between” or “a bit of both” or “neither”.
Or my favorite: “How are those opposites?”[^2]

The important work of the Post-Structuralists reminded us to consider defining concepts not by what they are, but by what they are not.
They also rejected the insistence of one, correct interpretation of a text, allowing as many interpretations as readers.
They afforded value to subjective, individual experience.
This directly gave human voice to the underrepresented.
A central concept to Post-Structuralism is Derrida’s “différance”.
He characterizes it thus: “Any exposition would expose it to disappearing as a disappearance.
It would risk appearing, thus disappearing.”

Compare to the opening lines of the Tao Te Jing[^3]: “The way you can go / isn’t the real way.
/ The name you can say / isn’t the real name.” The “way” here is the Tao.
You can’t teach someone how to follow the Tao.
You can’t describe it.
You can only find your own way.
Beyond the Tao itself, one of the central symbols is yin and yang, represented above.
Within the side of yin is a drop of yang and vice versa.
Each pole of a dichotomy contains its opposite, thus the dichotomy is false—one must consider the whole.

These are some of my favorite examples, but you are hopefully thinking of others.

# Ambiguity in Data Science

In data science, we are often concerned with uncertainty metrics.
But whereas uncertainty measures the quality of our observations or models, ambiguity is deeper.
The first classifiers we typically learn to implement are binary classifiers.
Dog or cat.
Spam or legitimate.
Sales opportunity or not.
SVM, logistic regression, naïve Bayes, there are lots of algorithms for making a binary decision based on input data, possibly with a probability associated with the output.
But by their form, an implicit assumption is that each input record represents one or the other possible output.

To embrace ambiguity in such a classification task, one might add a “neither” option, i.e.
declare ignorance if the probability/confidence is below a threshold.
One might use the probability directly.
One might change a dog/cat classifier into two: dog/not dog and cat/not cat.
Whatever the change, one will need to establish new processes or decision flows to considerately handle the ambiguous case(s).

Another implicit assumption lies in the input data.
Binary features may not truly be binary (ahem, gender, ahem).
A null value might indicate the data weren’t captured or that the available options don’t apply.
Recording these distinct possibilities means losing the compactness of binary variables, but gaining more informative inputs to your models.
In some cases, it may mean recognizing the full humanity of your users.
This carries its own weight.

Zooming way out, even the term data science is ambiguous.
What is data science? We see endless takes on this with no final definition in sight.
And while some agreement in the community may clarify certain dialogues, this ambiguity doesn’t stop data science from working! After all, we don’t have a definitive answer to: “what is science?” As with science, data science doesn’t need its bounds to be precisely drawn in order to work or grow.
In fact, to define either too strictly would restrict their evolution and advancement.[^4] They need fuzzy edges in order that those edges can adapt.[^5]

I love this freedom within this burgeoning field.
Every team I’ve worked on has had different goals, different standards, different personalities.
I occasionally read advice and ensuing debates about how best to place data science within a company, whether data scientists should own production code, how to keep data scientists happy, etc.
More often than not, these start with, “Data scientists like/need/want XYZ” I firmly object to these generalizations! If you start with an assumption of the personality and needs of a data scientist, you will only hire those who match those assumptions.
In reality, the field is diverse and its practitioners reflect this.
These articles are useful for seeing what other teams have tried and how well they work, but remember that your team probably has a different composition.
No good therapist applies generic techniques unthinkingly to every patient.
No good data science manager should unthinkingly apply generic structures.

# Ambiguity in Life

That last entreaty actually extends rather generally in life.
All the advice we find out there is great for collecting ideas.
But it will be up to each individual to decide which are useful, relevant, and helpful.
The best advice I see only provides frameworks for coming to your own decisions.
For example, reading about different communication styles opens my eyes to extra dimensions of social dynamics that I used to miss.
This helps me adapt my own communication in a more sensitive and effective way.

A corollary of this is that we should be judicious in our advice to others and our expectations of them.
As we’re all impossibly different, what works for us may not work for others.
Sometimes there are good reasons others behave so seemingly irrationally.
Yes, we should keep an eye out for harmful patterns and counter them where possible.
But let’s also celebrate humanity’s resistance to definition.

Once we accept that others are different—they have different values, contexts, histories, needs—then we have to accept another fact.
Given the diversity of people we need to account for, no single policy can cover everyone’s needs.
In an (my) ideal society, a gamut of voices will be heard, illegitimate (“A man needs his nuggs”) and antisocial (e.g.
anti-Semitic) needs will be rejected[^6], and the rest will still be found contradictory.
Finally, a compromise will be made to attempt to satisfy as many needs as possible while avoiding as many and as deep of harms as possible.
However you try to eliminate the huge grey areas, the unavoidable result is that no one will ever be completely happy.
This is not to say we should accept any shade of grey—rather it’s to set our target away from the dangerous fiction of Utopia.
Let’s remember how to compromise well.

# AmBIGuity

It’s satisfying in a primal way to be sure of the superiority of our beliefs and to subjugate the other.
(see *mansplaining*.) But life seldom offers pure, simple either/or situations.
I challenge you to think critically about every binary choice you encounter over the next few days.
I think you’ll find lots of grey middles.

This may seem a time-consuming way to live.
But perhaps not.
Maybe by accepting ambiguity, we rid ourselves of the need to force an artificial structure onto reality.
Maybe like a quantum computer, we can find new power by playing in an expanded space where many options can coexist.
We don’t have to question ourselves when we don’t fall neatly into a category.
We don’t have to pay any mind when we observe a harmless hypocrisy.
We can accept nature in all its complexity, ambiguity, and sublimity.


## Footnotes

[^1]: I’m inspired here by Eve Kosofsky Sedgwick’s
[Epistemology of the Closet](http://evekosofskysedgwick.net/writing/epistemology-of_the_closet.html)
for her trenchant takedown of such false binarisms.

[^2]: I can’t help but think of the Fear/Love scene in Donnie Darko.

[^3]: I’ve chosen
[the late Ursula Le Guin's rendition](https://www.brainpickings.org/2016/10/21/lao-tzu-tao-te-ching-ursula-k-le-guin/)
for her preservation of the ambiguity that permeates the original.

[^4]: See GOP efforts to restrict funding of certain categories of research or
the role of Stalin-era imposition of Dialectical Materialism to the Lysenko Affair.

[^5]: I am, however, of the opinion that data science needs some strict standardization and oversight.
Professional organizations, whether medical, engineering, or legal, all set explicit ethical standards.
Given the increasingly visible power of data science,
we should all take the ethics surrounding our work very seriously.
To have this dialog and debate, we need a common language.
I don’t think we’re far off.

[^6]: This does get slippery.
Who decides what needs are illegitimate or antisocial?
To preserve tolerance, at some point, intolerance must not be tolerated.
But what is that point? See Popper and the paradox of tolerance.
