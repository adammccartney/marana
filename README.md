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

## usage

The way I propose to use this library for the time being is to keep the
specific scripts used for creating a lilypond score separate - basically they
would be organized one per (instrumental) voice.

If you want to see an example of what I mean, there is a makefile included with
this repository that creates an example score. To generate a `score.pdf` simple
run:

```make``

