def check_inclusion(s1: str, s2: str) -> bool:
    s1_dict = {}
    window_dict = {}
    l = 0

    for s in s1:
        s1_dict[s] = s1_dict.get(s,0)+1

    for r in range(len(s2)):
        window_dict[s2[r]] = window_dict.get(s2[r],0)+1

        if r - l + 1 == len(s1):
            if s1_dict == window_dict:
                return True

            window_dict[s2[l]] -=1
            if window_dict[s2[l]] == 0:
                del window_dict[s2[l]]
            l+=1

    return False