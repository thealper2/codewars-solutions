def recycle(a):
    bins = {
        "paper": [],
        "glass": [],
        "organic": [],
        "plastic": [],
    }
    
    for item in a:
        bins[item["material"]].append(item["type"])
        
        if "secondMaterial" in item:
            bins[item["secondMaterial"]].append(item["type"])
            
    return (
        bins["paper"],
        bins["glass"],
        bins["organic"],
        bins["plastic"],
    )