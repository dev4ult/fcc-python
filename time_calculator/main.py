# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

if __name__ == "__main__":
  print(add_time("11:59 PM", "24:05"))

# Run unit tests automatically
main(module='test_module', exit=False)
