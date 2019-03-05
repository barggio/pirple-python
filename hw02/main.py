"""
Pirple Python HW # 2
Description:
This exercise is to create functions and use it by
creating collection of attributes getters functions.

3/4/2019
"""

# Song title (String)
Title = 'Havana'
# Length of song in seconds (Float)
DurationInSeconds = 217.391
# Name of artist (String)
Artist = 'Camila Cabello'
# Album name (String)
Album = 'Camila'
# Song's genre (String)
Genre = 'Pop'
# Year released (Integer)
Year = 2017
# Release date (String)
ReleasedDate = 'September 8, 2017'
# Track number in the album (Integer)
Track = 4
# Recording Label (string)
Label = 'Epic'
# Song's producer(s) (String)
Producers = 'Frank Dukes, Matt Beckley'


# Getter for song duration in seconds
def durationInSeconds():
    return DurationInSeconds

# Getter for Released date
def releasedDate():
    return ReleasedDate

# Getter for list of producers
def producers():
    return Producers

# Determine if the artist is also the producer
# Return boolean
def isArtistAlsoProducer():
    return Artist in Producers


print('Song is {0} seconds.'.format(durationInSeconds()))
print('Song was released on {0}.'.format(releasedDate()))
print('Song was produced by {0}.'.format(producers()))
print('Artist also helps produce: {0}.'.format(isArtistAlsoProducer()))
