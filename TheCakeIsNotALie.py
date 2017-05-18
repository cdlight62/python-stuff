total_mms = "aaa"


def string_split(mm_pattern="", count=1):
    if not mm_pattern:
        mm_pattern = total_mms[:1]
    if len(mm_pattern) * total_mms.count(mm_pattern) == len(total_mms):
        return total_mms.count(mm_pattern)
    if total_mms.count(mm_pattern) >= 1:
        count += 1
        sequence = total_mms[:count]
        return string_split(sequence, count)

print(string_split())