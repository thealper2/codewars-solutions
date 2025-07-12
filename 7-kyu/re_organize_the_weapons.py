def identify_weapon(character):
    characters = {
        "Laval": "Laval-Shado Valious",
        "Cragger": "Cragger-Vengdualize",
        "Lagravis": "Lagravis-Blazeprowlor",
        "Crominus": "Crominus-Grandorius",
        "Tormak": "Tormak-Tygafyre",
        "LiElla": "LiElla-Roarburn"
    }
    
    return characters.get(character, "Not a character")