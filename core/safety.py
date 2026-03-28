BLOCKED = ['nsfw', 'nude', 'naked', 'explicit', 'porn', 'xxx', 'adult content']

def safe(text):
    return not any(w in text.lower() for w in BLOCKED)