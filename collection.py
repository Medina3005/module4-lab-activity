# collection.py
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program stores and prints a collection of famous authors and their death years.

# Dictionary of authors and the year they passed away
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

# Loop through dictionary and print each author's information
for author, date in authors.items():
    print(f"{author} died in {date}.")


# Errors:
# Dictionary variable was incorrectly named (authrs → authors).
# Missing closing curly brace (}).
# Incorrect dictionary iteration syntax (for author date in authors.items{} → for author, date in authors.items():).
# Incorrect string formatting.
