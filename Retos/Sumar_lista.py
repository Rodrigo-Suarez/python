def find_needle(haystack):
    return f"found the needle at position {haystack.index("needle")}"


array = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(array))