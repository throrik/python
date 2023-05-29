#! /usr/bin/python3

import aptsources.sourceslist as sl
from colorama import Fore, Style

# Initialize colorama
Fore.GREEN, Fore.YELLOW, Style.RESET_ALL

sources = sl.SourcesList()

# Iterate over each source and find flags with "disabled on upgrade"
for source in sources.list:
    if "disabled on upgrade" in source.comment.lower():
        # Display disabled PPAs in yellow
        print(f"{Fore.YELLOW}{source}{Style.RESET_ALL}")
    else:
        # Display enabled PPAs in green
        print(f"{Fore.GREEN}{source}{Style.RESET_ALL}")

