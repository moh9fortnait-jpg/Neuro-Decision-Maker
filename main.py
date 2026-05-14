# Project 08: Neuro-Resource Allocator
# A logical tool to distribute limited resources across multiple targets

def distribute_resources(total_units, targets):
    print("\n--- Resource Allocation Plan ---")
    total_weight = sum(targets.values())
    
    for name, weight in targets.items():
        # Logic: Percentage-based distribution
        share = (weight / total_weight) * total_units
        print(f"Target: {name:15} | Allocation: {share:.2f} units ({ (weight/total_weight)*100:.1f}%)")

def main():
    print("--- Neuro-Resource Allocator v1.0 ---")
    try:
        total_resource = float(input("Enter total available units (e.g., hours, money): "))
        
        targets = {}
        print("Enter targets and their importance (1-10). Type 'done' to calculate.")
        
        while True:
            name = input("Target Name: ")
            if name.lower() == 'done': break
            importance = float(input(f"Importance weight for {name}: "))
            targets[name] = importance
            
        if targets:
            distribute_resources(total_resource, targets)
        else:
            print("No targets defined.")
            
    except ValueError:
        print("Error: Input must be a valid number.")

if __name__ == "__main__":
    main()