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

## Todo

* Vorud would make a nicer stream encoder if it could handle any
  number of bytes, not just 16-bit chunks. Vorud chunks encode a
  68600 element space, which leaves 3064 non-encoding values that
  can be used for special purposes. A simple enhancement would be to
  use the first 256 values above 65535 to denote "first byte has
  this value, stream ends after first byte".
