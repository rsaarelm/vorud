# Vorud: Encode 16-bit integers into pronounceable words

Vorud is an extremely simple scheme for translating between a 16-bit
integer and a reasonably human-pronouncible word in a
consonant-vowel-consonant-vowel-consonant form.

The purpose is to present things like a 32-bit seed of a random
number generator from a video game (eg. 3878844299) in a
human-readable form ("vakip-megaz")

Vorud is strongly influenced by Antti Huima's [Bubble Babble
encoding](http://wiki.yak.net/589/Bubble_Babble_Encoding.txt). Vorud
is simpler to implement and optimized for short values. Vorud
encodes 32-bit values in two words when Bubble Babble requires
three.

(2015-12 update: Turns out [Proquint](http://arxiv.org/html/0901.4016)
has the same bits to words density as Vorud and a simpler encoding
scheme. You should probably just use that instead of Vorud.)
