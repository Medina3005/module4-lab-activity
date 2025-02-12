# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print(f"{author} died in {date}.")


# Errors:
# Dictionary variable was incorrectly named (authrs → authors).
# Missing closing curly brace (}).
# Incorrect dictionary iteration syntax (for author date in authors.items{} → for author, date in authors.items():).
# Incorrect string formatting.