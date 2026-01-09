def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        seen = set()
        result = []
        
        for ch in chunk:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        
        print(''.join(result))
