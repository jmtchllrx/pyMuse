# Created By: Virgil Dupras
# Created On: 2007/05/12
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)

# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

MUSIC_GENRES = (
"Blues",
"Classic Rock",
"Country",
"Dance",
"Disco",
"Funk",
"Grunge",
"Hip-Hop",
"Jazz",
"Metal",
"New Age",
"Oldies",
"Other",
"Pop",
"R&B",
"Rap",
"Reggae",
"Rock",
"Techno",
"Industrial",
"Alternative",
"Ska",
"Death Metal",
"Pranks",
"Soundtrack",
"Euro-Techno",
"Ambient",
"Trip-Hop",
"Vocal",
"Jazz+Funk",
"Fusion",
"Trance",
"Classical",
"Instrumental",
"Acid",
"House",
"Game",
"Sound Clip",
"Gospel",
"Noise",
"AlternRock",
"Bass",
"Soul",
"Punk",
"Space",
"Meditative",
"Instrumental Pop",
"Instrumental Rock",
"Ethnic",
"Gothic",
"Darkwave",
"Techno-Industrial",
"Electronic",
"Pop-Folk",
"Eurodance",
"Dream",
"Southern Rock",
"Comedy",
"Cult",
"Gangsta",
"Top 40",
"Christian Rap",
"Pop/Funk",
"Jungle",
"Native American",
"Cabaret",
"New Wave",
"Psychadelic",
"Rave",
"Showtunes",
"Trailer",
"Lo-Fi",
"Tribal",
"Acid Punk",
"Acid Jazz",
"Polka",
"Retro",
"Musical",
"Rock & Roll",
"Hard Rock",

"Folk",
"Folk-Rock",
"National Folk",
"Swing",
"Fast Fusion",
"Bebob",
"Latin",
"Revival",
"Celtic",
"Bluegrass",
"Avantgarde",
"Gothic Rock",
"Progressive Rock",
"Psychedelic Rock",
"Symphonic Rock",
"Slow Rock",
"Big Band",
"Chorus",
"Easy Listening",
"Acoustic",
"Humour",
"Speech",
"Chanson",
"Opera",
"Chamber Music",
"Sonata",
"Symphony",
"Booty Bass",
"Primus",
"Porn Groove",
"Satire",
"Slow Jam",
"Club",
"Tango",
"Samba",
"Folklore",
"Ballad",
"Power Ballad",
"Rhythmic Soul",
"Freestyle",
"Duet",
"Punk Rock",
"Drum Solo",
"A capella",
"Euro-House",
"Dance Hall",
"Goa",
"Drum & Bass",
"Club-House",
"Hardcore",
"Terror",
"Indie",
"BritPop",
"Negerpunk",
"Polsk Punk",
"Beat",
"Christian",
"Heavy Metal",
"Black Metal",
"Crossover",
"Contemporary",
"Christian Rock",
"Merengue",
"Salsa",
"Thrash Metal",
"Anime",
"JPop",
"Synthpop")

def genre_by_index(index):
    return MUSIC_GENRES[index] if index >= 0 and index < len(MUSIC_GENRES) else ''

