Title: Does Not Compute
Date: 2013-10-04 00:30
Author: Just Alfred
Tags: explaining, tech
Slug: does-not-compute

*Originally published at: [http://kwontum.blogspot.com/2013/10/does-not-compute.html](http://kwontum.blogspot.com/2013/10/does-not-compute.html)*

Let's talk about language. How amazing is it that using sounds or
symbols, we can implant in another person's mind an entirely new state?
We can describe a place that person has never seen, we can construct a
belief that person has never considered, we can convey an emotion that
person has never felt.  
  
But not without errors in transmission. Remember the game, "telephone"?
Why can't language be more precise? Let me try to explain this in an
unconventional way and see what it means for programming languages.  
<a name="more"></a>  
  
Imagine a language in which the intent of the communicator is completely
unambiguous to a qualified listener. I'll use CD audio recordings as an
illustration. With good enough equipment, a listener can hear a
soundscape that is indistinguishable from the original.  
  
But most people don't listen to CDs anymore. They listen to streaming or
downloaded music. The major difference is that these recordings are
compressed. Those parts of the audio signal that people can't hear well
are removed. This leads to degradation of the signal, but much, much
less information is required while most people never notice. So it's a
worthwhile tradeoff. In fact, there's a whole class of [probabilistic
data
structures](http://en.wikipedia.org/wiki/Category:Probabilistic_data_structures) in
computer science that sacrifice accuracy for performance and size.  
  
Likewise, human languages have each been reduced to use only a subset of
all possible
[sounds](http://en.wikipedia.org/wiki/International_Phonetic_Alphabet)
and symbols. Take the word, "hot". Here's a list of things that can be
described as hot: fire, chile pepper, horseradish, supermodel,
basketball player, a fashion trend, the color of a room. In English, we
use this single, overloaded word to represent this array of meanings.
Yet we're rarely confused due to our evolved talents for lexical
ambiguity resolution (as so wonderfully explained by my new colleague
[here](http://jennazeigen.com/lexical.jpg)).  
  
In other words, when a word can take multiple meanings, we're
terrifically adept at taking context into account to disambiguate the
intended meaning. This permits us to compress our language into a
manageable size. More importantly, it permits us to be sloppy. The
sentence, "I ain't git no donuts, but I gotta coke," is completely
understandable despite all the errors.  
  
Computers aren't like us. Computers are purely logical units that
mindlessly apply instructions to data because they have no governing
mind. At the processor level, they have no innate capacity to correct
erroneous instructions or to resolve ambiguities. This is what makes
coding hard. A sentence like "Come to the kitchen" is perfectly
understandable to us since we can guess there is supposed to be a period
at the end to indicate the sentence has ended. A computer would say the
sentence never finished so the instruction cannot be
processed. (Interestingly, there are companies that hire adults with
autism or Asperger's since they are often exceptional at handling and
debugging code.)  
  
For the beginning programmer, I think this is an obvious, but useful
insight. Sort of like realizing the center squares of a Rubik's cube
don't move: those center squares cease to be puzzle pieces and become
stationary references to guide your manipulations. The stupid silicon
insight sets an exacting reference from which one can evaluate one's own
code. Instead of wondering why the dumb computer didn't get what he was
(not) clearly telling it to do, the novice can expend that brainpower on
avoiding the typos and syntax errors whose importance he now
understands.

