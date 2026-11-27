import sys
from rich import print

name = sys.argv[1] if len(sys.argv) > 1 else "world"
print(f"[bold green] Hello, {name}![/bold green]")