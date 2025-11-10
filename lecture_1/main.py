from colorama import init, Fore, Back, Style

# Inirialize colorama for cross-platform colored terminal output
init()

# Print colored Hello Word
print(f"{Fore.RED}{Back.YELLOW}Hello Word!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hello Word in Green!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hello Word is Bright Blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hello Word with Magenta text and Cyan background!{Style.RESET_ALL}")
