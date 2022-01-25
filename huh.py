from collections import Counter
import enchant

def permute():
    d = enchant.Dict("en_US")
    avail = Counter()

    # Assuming all remaining letters appearing once
    avail['q'] = 1
    avail['t'] = 1
    avail['y'] = 1
    avail['u'] = 1
    avail['a'] = 1
    avail['g'] = 1
    avail['h'] = 1
    avail['j'] = 1
    avail['l'] = 1
    avail['z'] = 1
    avail['x'] = 1
    avail['v'] = 1
    avail['m'] = 1
    
    start = 's'
    end = 'r'

    # First slot
    for let1 in avail:
        if not avail[let1] > 0:
            continue
        avail[let1] -= 1
        # Second slot
        for let2 in avail:
            
            if not avail[let2] > 0:
                continue
            avail[let2] -= 1
            # Third slot
            for let3 in avail:
                
                if not avail[let3] > 0:
                    continue
                avail[let3] -= 1
                word = start + let1 + let2 + let3 + end
                if d.check(word):
                    print(word)
                avail[let3] += 1
            avail[let2] += 1
        avail[let1] += 1
                
permute()