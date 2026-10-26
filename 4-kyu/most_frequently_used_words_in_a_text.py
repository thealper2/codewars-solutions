import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-z']+", text.lower())
    words = [w for w in words if any(c.isalpha() for c in w)]
    counts = Counter(words)
    return [w for w, _ in counts.most_common(3)]