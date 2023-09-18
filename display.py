import os


def progress_bar(iterable, prefix ='', suffix ='', decimals = 1, length = 100, fill ='█', print_end ="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def print_progress_bar (iteration):
        # percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + ' ' * (length - filled_length)
        print(f'\r|{bar}| ', end = print_end)
    # Initial Call
    print_progress_bar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)
    # Print New Line on Complete
    print()

class ClearScreen:
    def __init__ (self):
        self.cmd = 'clear' if os.name == 'posix' else 'cls'
    
    def wait_and_clear(self, content = ""):
        input(content)
        os.system(self.cmd)
    
    def clear(self):
        os.system(self.cmd)