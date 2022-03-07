```
 _ __ ___   __ _ _ __ __ _ _ __   __ _ 
| '_ ` _ \ / _` | '__/ _` | '_ \ / _` |
| | | | | | (_| | | | (_| | | | | (_| |
|_| |_| |_|\__,_|_|  \__,_|_| |_|\__,_|

```
![example workflow](https://github.com/adammccartney/marana/actions/workflows/main.yml/badge.svg)

A package for compiling [lilypond](https://lilypond.org) music notation. Relies
on [abjad v3.6](https://abjad.github.io) and [python 3.10](https://www.python.org/downloads/release/python-3100/)

Project is in pre-alpha and under ongoing development.


## Introduction

*marana* is a word in the Irish language that was suggested to me while I was
searching for a title for a short piece of orchestral music. I was looking for
a way to translate the word meditation, having read that meditation has been
used on occasion by some composers as a title for a short orchestral piece. The
piece itself was supposed to be written and performed by the NSO in Dublin in
2020. Then covid happened and it's now 2022, so there was plenty of time to
contemplate the piece in the interim. If I had wrote the piece in 2020, it
would have been difference and this readme would probably not be introducing a
more general purpose scripting libary for writing notated music. It's worth
noting at the outset that I think that whatever way you approach it, writing
music seems to be highly idiomatic. On some level this fact is surprising,
largely because of music's universal appeal. Nevertheless, I think it can't be
avoided that any approach to writing music will be highly colored by the
composer's own particular experience and the ways that they have come to
contemplate and imagine the music itself.  

## structure of this repository

I haven't really decided how to structure this repo yet. I've tried out a
couple of different approaches in the past. I'm starting to get an idea of what
works, so it's probably safe to mention a few general outlines: the functionality 
of the library is very much shaped by the I/O model that I use myself while writing 
music. This typically begins with some harmonic/melodic sketches on the piano, that 
map out the regions of sound to explore and then couple these with some sort of
rhythmic structure and finally dynamic. The input therefor is simply lilypond
strings representing pitch classes and typically some sequences of real numbers to
represent rhythm.

## pitch queries and pitch data

