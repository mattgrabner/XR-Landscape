import subprocess
import sys


# ANSI escape code colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def print_with_color(message, color=Colors.ENDC):
    print(color + message + Colors.ENDC)

def run_scripts(database_id):
    # Run scrape-summary.py to get content from URLs in the Notion database
    subprocess.run(['python', 'scrape-summary.py', database_id], check=True)
    # Run shortsummary.py to generate short descriptions using OpenAI's GPT
    subprocess.run(['python', 'shortsummary.py', database_id], check=True)

def main():
    print_with_color("This script will update a Notion database with company descriptions.", Colors.HEADER)
    print_with_color("The database should have the following columns:", Colors.YELLOW)
    print_with_color("- 'super:Link': containing URLs to scrape content from.", Colors.CYAN)
    print_with_color("- 'Description': where the scraped content will be stored.", Colors.CYAN)
    print_with_color("- 'shortversion': where a short summary generated by GPT-4 will be stored.", Colors.CYAN)
    print_with_color("- 'Company / Organization': the name of the company.", Colors.CYAN)
    print_with_color("- 'Category': the category of the company.", Colors.CYAN)
    print_with_color("- 'Active': indicating whether the company is active or not.", Colors.CYAN)
    print("\nPlease input your Notion Database ID to begin.")
    database_id = input(f"{Colors.GREEN}Notion Database ID: {Colors.ENDC}")
    
    try:
        run_scripts(database_id)
        print_with_color("Scripts executed successfully.", Colors.GREEN)
    except subprocess.CalledProcessError as e:
        print_with_color(f"An error occurred while running the scripts: {e}", Colors.RED)
        sys.exit(1)

if __name__ == "__main__":
    main()
