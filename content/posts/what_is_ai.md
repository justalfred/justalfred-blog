Title: What is AI?
Date: 2020-10-23
Tags: explaining, tech
Author: Just Alfred
Summary: There's a lot of nonsense around AI floating around. Time to vent.

OK. I keep getting into conversations with people talking about AI,
and because I've worked in the field, I want to write up what I wish people knew.
Starting with: what are people talking about when they say 'AI'?

I have an [old rambly post]({filename}2018_thoughts.md) about AI which starts with a brief history.
Here's a briefer one.
AI originally referred to the study of how to create artificial systems that exhibit intelligence.
From this field was born many a science fiction story
(the best being Terminator 2, obviously)
which typically imagined anthropomorphic intelligences.
In practice, for the most part, there were *expert systems*
which attempted to encode rules of reason,
and there was *machine learning* (ML)
which used data to come to a statistical understanding of 'correct'.
ML is conceptually the same as fitting a trendline to a scatter plot in Excel,
but with more input dimensions than just the one horizontal axis and with wigglier lines.
And like Excel trendlines, it's useful for stuff that have nothing to do with emulating intelligence.

One of these ML techniques, artificial neural networks (ANNs),
was inspired by the way neurons in a brain are connected.
(Inspired by. They are not anything like simulated brains. Don't be fooled.)
Deep learning algorithms are variations on these.
They proved really good at an impressive variety of tasks,
resulting in a flurry of excitement that started a few years ago.
Back then, some companies were starting to brag about
how their data scientists were using ML to make automated predictions or decisions at large scale.
When deep learning started to become accessible, since it came from AI research, and AI sounds advanced,
the bragging went from being about data science to AI.

It's kind of like if a baker started using a super-yeast, and said they were using biochemistry,
and then suddenly every bakery is advertising their biochemistry.
It's not totally wrong, and it's absurd, and hardly any of these bakers would be advancing the field.
But we would get used to it like we got used to digestive biscuits.

So AI is deep learning? Nope.
Deep learning was just the initial hook that pulled the term 'AI' into the places where ML was being used.
Notice how ML started as a subset of academic AI research, but now, thanks to marketing,
AI refers to commercial and industrial applications of ML.
Sort of.
Typically, when companies claim to be using AI, there's an expectation that something is happening automatically.
So I like to say commercial AI means "ML in production".
(Production here means infrastructure actually in use, not some experimental test server.)

Let's say you want to use AI to detect fraudulent transactions.
First, you need a bunch of examples of transactions where the fraudulent ones are labeled.
Maybe you decorate this data by connecting other data sets.
The age of the account or the number of prior legitimate transactions might be informative,
so stick it on to your transaction data.
Now the same way you choose a linear or quadratic or logarithmic trendline in Excel,
you have to pick an ML algorithm to fit to your data.
Depending on what you try, you might need to do further data munging.
Maybe you scale all the dollar amounts down between 0 and 1.
Maybe you convert account opening dates into zodiac signs.
For deep learning, you might spend more time trying different architectures.
How deep? How connected?
At this point, you're trying lots of different things to see what will yield the best model for flagging fraud.

The point is that there's a lot of manual work, and
in the end, you have one model that takes decorated,
munged transaction data as input, and says fraud or not fraud as its output.
Great, put it production, and you have an AI.
Now that you have an intelligence, let's use it to call customers and tell them about the fraud it found!

That's absurd.
When you fit a trendline in Excel, it's good for that one task and nothing else.
Same with AI.
There are multitask models that can generalize to some degree, but always within a tight class of problems.
The point is, every time you have a new task,
you're going to develop a new model to perform that task,
even if that means fine-tuning an off-the-shelf model for your needs.
There isn't a Google or Amazon AI floating in the cloud that's
sucking up our data and getting steadily smarter and smarter.
AI is not one thing.

In fact, a lot of the time, it's not even AI.
It's some over-promised, under-delivering model that
kicks the hard stuff over to an invisible group of underpaid human laborers to make a decision.
Or it's just the humans.
So AI is "ML in production, except when it's actually poor people".

But if you do manage to put a model in production to decide whether new transactions are fraudulent or not,
what do you do with that?
That's a separate question.
Do you block those transactions?
Do you notify the customer after the fact?
Do you just record these and review accounts with too many?
Or do you alert the authorities?
What are the consequences when the model incorrectly flags fraud?
When it misses fraud?
Is it wrong more often for certain groups of people?
Do you inform your customers how your model may affect them?
Do you allow customers to opt-out of the system?

None of those are technical questions.
You can call them product, design, or ethical questions.
And they have far more influence on the impact of an AI system than the AI component itself.
Quite often AI systems are sociotechnical in nature, and understanding that wider context
requires a very different perspective from the one necessary to optimize a model.

Once we understand that AI is not one thing,
that every implementation is unique and highly specific,
and that the hardest part of deploying AI is often not technical,
many other common beliefs about AI fall apart.
That discussion is for another day.

Postscript: No one says "cognitive" anything unless IBM's been selling to them.
And there's nothing cognitive about any of it.
And if your company keeps talking about "robotics", that just means code like we've always had code.
