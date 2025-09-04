def sing():
    lyrics = []
    for i in range(99, 0, -1):
        bottle = "bottles" if i != 1 else "bottle"
        next_bottle = "bottles" if i-1 != 1 else "bottle" if i-1 == 1 else "no more bottles"
        next_num = str(i-1) if i-1 > 0 else "no more"
        lyrics.append(f"{i} {bottle} of beer on the wall, {i} {bottle} of beer.")
        lyrics.append(f"Take one down and pass it around, {next_num} {next_bottle} of beer on the wall.")
        
    lyrics.append("No more bottles of beer on the wall, no more bottles of beer.")
    lyrics.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return lyrics
