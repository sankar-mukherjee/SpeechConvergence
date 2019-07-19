---
layout: post
title: Introduction
---

<img src="/SpeechConvergence/img/Convergence-thumbnail.png" align="right" hspace="20">

<p style="text-align: justify;text-justify: inter-word;">
When people engage in verbal interaction, they adjust their speech in order to accommodate to each other. This phenomenon is called Speech Convergence. It is an emergent phenomenon happens during conversation. Although convergence is a well-known phenomenon, its quantitative assessment is still an open area of research. Here, we developed a method using automatic speaker verification technique (GMM-UBM) in order to measure speech convergence. We quantified participants' initial phonetic fingerprints and tracked their phonetic convergence during the verbal interaction.
</p>

-------
### Theory

<details><summary></summary>

<img src="/SpeechConvergence/img/speech_alignment.png" width="600" align="center">

<p style="text-align: justify;text-justify: inter-word;">
The dynamical process of mutual adaptation which occurs at multiple levels is a key component of natural linguistic interaction that is crucially missing in classical laboratory tasks. One interesting phenomenon during linguistic interaction is that of Alignment. Figure illustrates an abstract representation of the process of alignment. It shows that interlocutor’s linguistic representation interact at multiple levels. The interaction takes place through priming. In simple terms, subjects engaged in a conversation, via a process of automatic imitation tends to accommodate their utterances to their interlocutor at the lexical, phonetic, semantic, and discourse levels simultaneously.

As conversation progress interlocutors simultaneously affect each others mental states. Conversational success is indeed characterized by the shared understanding of the spoken content, speakers’ mutual likability, background environment, etc. (Menenti et al. (2012); Garnier et al. (2013)). More interestingly, people involved in a dialogue automatically and implicitly converge at multiple linguistic levels (Bilous and Krauss (1988); Pardo et al.
(2010)) as well as with co-verbal bodily gestures (Turner and West (2010)). For instance, agreeing interlocutors tend to copy each other’s choices of sounds, words, grammatical constructions as well as the temporal characteristics of speech. Nevertheless, this form of implicit behavioral alignment is still poorly understood, especially regarding its effects on communication efficacy, social and contextual determinants, and neural underpinnings (Stolket al. (2016)).
</p>
</details>

Convergence happens in multiple levels (phonetic, word, sentence, prosodic, discourse).

### Goal

Quantifying speech convergence and mark the time points in the conversation.

### Experiment

We created a simple interactive task which allows better experimental control. In the task subjects involved in a relatively constrained interactive task where they were asked to take turns in chaining words according to a phonetic rhyming rule. 

<p>
<img src="/SpeechConvergence/img/domino.png" align="middle">

<div class="message">
The first syllable of a word has to rhyme with the last syllable of the previous word.
</div>

<img src="/SpeechConvergence/img/convergence_protocol.png" width="500" align="middle">

{% highlight text %}
Experiment Protocol
{% endhighlight %}

</p>

### Steps

The steps are -

#### GMM-UBM Modeling

We quantified participants' initial phonetic fingerprints and tracked their phonetic convergence during the interaction via a robust and automatic speaker verification technique.

[NoteBook](https://nbviewer.jupyter.org/github/sankar-mukherjee/SpeechConvergence/blob/master/GMM-UBM.ipynb){:target="_blank"}

#### Convergence Measurment

Convergence is computed on word pairs. For a word pair to be a convergent one, the acoustic properties of the words for the two speakers must be similar to each other, as well as these properties must be significantly different than the speakers original speech.

[NoteBook](https://nbviewer.jupyter.org/github/sankar-mukherjee/SpeechConvergence/blob/master/convergence.ipynb){:target="_blank"}

### Conclusion

Speech Convergence can be measured using a speaker identification technique during a well constrained task such as the Domino. Importantly, we introduced several analysis features to make the estimation of Convergence more robust. For instance, we tested modelling performance and verified its validity. We also evaluated if Convergence scores were attributable to random fluctuations in the data or were the true effect of dyadic interaction by testing them against surrogate dyads. Results show that the nature of speech Convergence is sparse, i.e., it is not evenly distributed on all the dyads. Some dyads show higher degree of Convergence while
others rarely converge at all. A possible factor in this sparseness may be due to subjects’ attention, familiarity with the content and their likability towards each other.

-----
### Publication

> Mukherjee, S., D'Ausilio, A., Nguyen, N., Fadiga, L. and Badino, L., 2017, August. The Relationship Between F0 Synchrony and Speech Convergence in Dyadic Interaction. In Interspeech 2017. [Link](https://hal.archives-ouvertes.fr/hal-01579789/document)

> Mukherjee, S., Badino, L., M. Hilt, P., Tomassini, A., Inuggi, A., Fadiga, L., Nguyen, N. and D'Ausilio, A., 2018. The neural oscillatory markers of phonetic convergence during verbal interaction. Human brain mapping. [Link](https://www.ncbi.nlm.nih.gov/pubmed/30240542)
 





