# Import necessary modules
import pyfiglet  # Used to print ASCII art text
import platform  # Used to get system information
from colorama import init, Fore  # Used to add colors to the console output
import psutil  # Used to get memory information

init()  # Initialize colorama module for colored output

# Print the OS logo
result = pyfiglet.figlet_format("Your System")
print(result)

# Print the OS information
print(Fore.WHITE + "===== Operating System Information ==============")
# Print the operating system name
print(Fore.CYAN + f"OS Name: {platform.system()}")
# Print the operating system version
print(Fore.CYAN + f"OS Version: {platform.release()}")

# Print the memory information
memory = psutil.virtual_memory()
# Calculate free memory percentage
free_memory_percent = round(memory.available / memory.total * 100, 2)

print(Fore.WHITE + "===== Memory Information ========================")
# Print the total memory
print(Fore.GREEN + f"Total Memory: {round(memory.total / (1024 ** 3), 2)} GB")
# Print the used memory
print(Fore.GREEN + f"Used Memory: {round(memory.used / (1024 ** 3), 2)} GB")
# Print the free memory and its percentage
print(Fore.GREEN +
      f"Free Memory: {round(memory.free / (1024 ** 3), 2)} GB ({free_memory_percent}%)")

# Print the hardware information
print(Fore.WHITE + "===== Hardware Information ======================")
# Print the processor information
print(Fore.RED + f"Processor: {platform.processor()}")
# Print the architecture of the platform
print(Fore.RED + f"Architecture: {platform.architecture()[0]}")
print(Fore.RED + f"Machine: {platform.machine()}")  # Print the machine type
# Print the system's node name
print(Fore.RED + f"Node Name: {platform.node()}")
# Print the Python version running on the system
print(Fore.RED + f"Python Version: {platform.python_version()}")
