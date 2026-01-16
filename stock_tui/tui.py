import curses
from investors.buffett import BuffettInvestor
from investors.munger import MungerInvestor

def display_header(window, message):
    window.clear()
    window.addstr(0, 0, message)
    window.refresh()

def get_investor_choice(window):
    # Prompt the user to select an investor
    window.addstr(2, 0, "Select an investor for stock evaluation:")
    window.addstr(3, 0, "1. Buffett")
    window.addstr(4, 0, "2. Munger")
    window.addstr(5, 0, "3. Both")
    window.refresh()

    choice = window.getch()  # Get user input (1, 2, or 3)
    
    # Map the choice to an investor selection
    if choice == ord('1'):
        return ['Buffett']
    elif choice == ord('2'):
        return ['Munger']
    elif choice == ord('3'):
        return ['Buffett', 'Munger']
    else:
        return []  # Default to empty (no selection)

def get_ticker_input(window):
    # Ask user to input a stock ticker symbol
    window.addstr(7, 0, "Enter ticker symbol: ")
    window.refresh()

    # Clear the input line before getting input
    window.move(8, 0)  # Move cursor to line 8, starting from column 0
    ticker = ""
    
    while True:
        char = window.getch()  # Get each character
        if char == 10:  # Enter key
            break
        elif char == 27:  # Escape key (cancel input)
            ticker = ""
            break
        elif char in (263, 127):  # Backspace key (different terminals may send 263 or 127)
            ticker = ticker[:-1]  # Remove last character
            # Clear the current input line before re-displaying
            window.move(8, 0)
            window.clrtoeol()
            window.addstr(8, 0, ticker)
            window.refresh()
        else:
            ticker += chr(char)
            window.addstr(8, len(ticker) - 1, chr(char))  # Display the character
            window.refresh()

    return ticker.upper()

def display_results(window, ticker_symbol, investor_results):
    window.clear()  # Clear the screen before displaying new content
    window.addstr(0, 0, f"Results for {ticker_symbol}:\n\n")
    line_index = 2  # Start displaying from line 2

    # Check the number of selected investors
    if len(investor_results) == 1:
        # If only one investor is selected, display every test individually
        for investor_name, results in investor_results.items():
            window.addstr(line_index, 0, f"{investor_name} Results:")
            line_index += 1
            criteria = results['criteria']
            passes = results['passes']
            window.addstr(line_index, 0, f"Overall: {'PASS' if passes else 'FAIL'}")
            line_index += 1
            for key, value in criteria.items():
                result = 'PASS' if value else 'FAIL'
                window.addstr(line_index, 0, f" - {key}: {result}")
                line_index += 1
            line_index += 1  # Add an extra blank line
    else:
        # If multiple investors are selected, show a summary for each investor
        for investor_name, results in investor_results.items():
            criteria = results['criteria']
            passed_tests = sum(1 for test in criteria.values() if test)
            total_tests = len(criteria)
            window.addstr(line_index, 0, f"{investor_name} Summary: Passed {passed_tests} out of {total_tests} tests")
            line_index += 1

    window.refresh()

def main(stdscr):
    # Set up the terminal window (curses)
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    display_header(stdscr, "Stock Evaluation TUI")

    # Get investor choice (Buffett, Munger, or Both)
    selected_investors = get_investor_choice(stdscr)

    # Check if no investor is selected
    if not selected_investors:
        stdscr.addstr(10, 0, "Invalid choice! Please select a valid option (1, 2, or 3).")
        stdscr.refresh()
        stdscr.getch()
        return

    # Get ticker symbol input
    ticker_symbol = get_ticker_input(stdscr)

    # Check if ticker symbol is empty or invalid (early exit if so)
    if not ticker_symbol:
        stdscr.addstr(10, 0, "No ticker symbol entered. Exiting...")
        stdscr.refresh()
        stdscr.getch()
        return

    # Initialize an empty dictionary for investor results
    investor_results = {}

    # Run evaluations based on selected investors
    if 'Buffett' in selected_investors:
        buffett_results = BuffettInvestor.check_requirements(ticker_symbol)
        investor_results['Buffett'] = {
            "passes": buffett_results[0],
            "criteria": buffett_results[1]
        }
    
    if 'Munger' in selected_investors:
        munger_results = MungerInvestor.check_requirements(ticker_symbol)
        investor_results['Munger'] = {
            "passes": munger_results[0],
            "criteria": munger_results[1]
        }

    # Display the results for selected investors
    if investor_results:
        display_results(stdscr, ticker_symbol, investor_results)
    else:
        stdscr.addstr(10, 0, "No investor selected! Please try again.")
        stdscr.refresh()
        stdscr.getch()

    # Wait for user to press a key before quitting
    stdscr.addstr(curses.LINES - 1, 0, "Press any key to exit.")
    stdscr.getch()

# Entry point for the TUI
if __name__ == "__main__":
    curses.wrapper(main)
