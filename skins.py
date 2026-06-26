import os
import sys
import argparse

def get_ansi_color(color_name):
    colors = {
        "cyan": "\033[96m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "bold": "\033[1m",
        "reset": "\033[0m"
    }
    return colors.get(color_name, "")

def print_header(title):
    cyan = get_ansi_color("cyan")
    bold = get_ansi_color("bold")
    reset = get_ansi_color("reset")
    print(f"\n{bold}{cyan}=== {title} ==={reset}")

def list_skins(target):
    skins_dir = "skins"
    if not os.path.exists(skins_dir):
        print(f"{get_ansi_color('red')}Error: 'skins' directory not found. Run 'python compiler/skins_compiler.py' first.{get_ansi_color('reset')}")
        return

    green = get_ansi_color("green")
    reset = get_ansi_color("reset")
    bold = get_ansi_color("bold")

    if target == "departments":
        print_header("AVAILABLE DEPARTMENTS")
        for dept in sorted(os.listdir(skins_dir)):
            if os.path.isdir(os.path.join(skins_dir, dept)):
                print(f"  - {green}{dept}{reset}")
    elif target == "industries":
        print_header("SUPPORTED INDUSTRY VERTICALS")
        # Scan first dept to get industries list
        depts = os.listdir(skins_dir)
        if depts:
            sample_dept = os.path.join(skins_dir, depts[0])
            for ind in sorted(os.listdir(sample_dept)):
                print(f"  - {green}{ind.upper()}{reset}")
    else:
        print(f"Unknown target: {target}. Choose 'departments' or 'industries'.")

def search_skins(query):
    skins_dir = "skins"
    query = query.lower()
    matches = []
    
    green = get_ansi_color("green")
    cyan = get_ansi_color("cyan")
    reset = get_ansi_color("reset")

    for root, dirs, files in os.walk(skins_dir):
        for file in files:
            if query in root.lower() or query in file.lower():
                # Extract relative path components
                rel = os.path.relpath(os.path.join(root, file), skins_dir)
                parts = rel.split(os.sep)
                if len(parts) >= 4:
                    dept, ind, role, filename = parts[0], parts[1], parts[2], parts[3]
                    matches.append((dept, ind, role, filename))
                    
    if not matches:
        print(f"\nNo skins matched query: '{query}'")
        return
        
    print_header(f"SEARCH RESULTS ({len(matches)} MATCHES)")
    # Limit output to 30 results to prevent flooding terminal
    for i, (dept, ind, role, filename) in enumerate(matches[:30], 1):
        framework = filename.split("_")[0]
        model = filename.split("_")[1]
        print(f"  {i}. {green}{dept}{reset} / {cyan}{ind.upper()}{reset} / {role} -> {framework} ({model})")
        
    if len(matches) > 30:
        print(f"\n  ... and {len(matches) - 30} more matches. Refine your query for specific results.")

def get_skin(dept, industry, role, framework, model):
    skins_dir = "skins"
    filepath = os.path.join(skins_dir, dept.lower(), industry.lower(), role.lower().replace(" ", "_"), f"{framework.lower()}_{model.lower()}_optimized.py")
    
    # Check fallback for TypeScript Vercel SDK
    if not os.path.exists(filepath):
        filepath = filepath.replace(".py", ".ts")
        
    if not os.path.exists(filepath):
        print(f"{get_ansi_color('red')}Error: Skin configuration not found for parameters: {dept}/{industry}/{role}/{framework}/{model}{get_ansi_color('reset')}")
        print(f"Expected path: {filepath}")
        return
        
    print_header(f"SKIN: {dept.upper()} / {industry.upper()} / {role.upper()}")
    print(f"{get_ansi_color('yellow')}Filepath: {filepath}{get_ansi_color('reset')}\n")
    
    with open(filepath, "r", encoding="utf-8") as f:
        print(f.read())

def main():
    parser = argparse.ArgumentParser(
        description="Agent-Skins Interactive CLI: Explore, search, and load 17,280+ prompt skins.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all departments or industries")
    list_parser.add_argument("target", choices=["departments", "industries"], help="Target details to list")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search skins by role name or description")
    search_parser.add_argument("query", type=str, help="Search keyword")
    
    # Get command
    get_parser = subparsers.add_parser("get", help="Fetch and print a specific skin configuration")
    get_parser.add_argument("dept", type=str, help="Department (e.g., sales, finance)")
    get_parser.add_argument("industry", type=str, help="Industry (e.g., saas, fintech)")
    get_parser.add_argument("role", type=str, help="Role ID (e.g., lead_qualifier, expense_reconciler)")
    get_parser.add_argument("framework", type=str, choices=["crewai", "langgraph", "autogen", "vercel_ai_sdk"], help="Agent framework")
    get_parser.add_argument("model", type=str, choices=["openai", "anthropic", "llama"], help="Target model optimization")

    args = parser.parse_args()
    
    if args.command == "list":
        list_skins(args.target)
    elif args.command == "search":
        search_skins(args.query)
    elif args.command == "get":
        get_skin(args.dept, args.industry, args.role, args.framework, args.model)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
