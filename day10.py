album =  (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )

album_record = {
    "title" : "he Dark Side of the Moon",
    "artist": "Pink Floyd",
    "release-year":1973,
    "tracks":[
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}


# for key,value in album_record.items():
#     if key == "tracks":
#         album_tracks = album_record["tracks"]
#         for song in album_tracks:
#             print(f"Song Name: {song}")
            
#     else:
#         print(f"{key} : {value}")

del album_record['tracks']
del album_record['release-year']

print(album_record)

album_record['date-of-release'] = 'March 1st, 1973'
print(album_record)


# print(album_record['music_company'])
# print(album_record.get('music_company'))