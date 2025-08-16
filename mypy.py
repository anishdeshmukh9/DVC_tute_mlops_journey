import pandas as pd
import os

def create_initial_data():
    """
    Creates an initial simple DataFrame and saves it to 'data/data.csv'.
    """
    print("Step 1: Creating initial dataset 'data/data.csv'...")
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    
    data = {
        'id': [1, 2, 3],
        'product': ['apple', 'banana', 'cherry'],
        'price': [0.5, 0.3, 0.8]
    }
    df = pd.DataFrame(data)
    df.to_csv('data/data.csv', index=False)
    print("Initial 'data/data.csv' created.")
    
    # --- DVC/Git Instructions ---
    print("\n--- DVC & Git Commands to run for Step 1 ---")
    print("1. dvc add data/data.csv")
    print("2. git add data/data.csv.dvc .gitignore")
    print("3. git commit -m 'Add initial version of data'")
    print("4. dvc push")
    print("------------------------------------------")

def append_new_data():
    """
    Appends new data to the existing 'data/data.csv' to simulate a change.
    """
    print("\nStep 2: Appending new data to 'data/data.csv'...")
    try:
        # Load the existing data
        df = pd.read_csv('data/data.csv')
        
        # New data to append
        new_data = {
            'id': [4, 5],
            'product': ['grape', 'orange'],
            'price': [0.6, 0.4]
        }
        new_df = pd.DataFrame(new_data)
        
        # Append the new data to the original DataFrame
        updated_df = pd.concat([df, new_df], ignore_index=True)
        updated_df.to_csv('data/data.csv', index=False)
        print("New data has been appended to 'data/data.csv'.")
        
        # --- DVC/Git Instructions ---
        print("\n--- DVC & Git Commands to run for Step 2 ---")
        print("1. dvc add data/data.csv")
        print("2. git add data/data.csv.dvc")
        print("3. git commit -m 'Append new product data'")
        print("4. dvc push")
        print("------------------------------------------")

    except FileNotFoundError:
        print("Error: 'data/data.csv' not found. Please run create_initial_data() first.")

def main():
    """
    Main function to run the demo steps.
    """
    # Create the initial data file
    create_initial_data()
    
    # Pause for user to run DVC/Git commands
    input("\nPress Enter to proceed to the next step and append new data...")
    
    # Append the new data
    append_new_data()

    print("\nDemo complete. You can now use 'dvc diff' to see the changes between the two versions.")
    print("To revert to the initial version, you can run 'git checkout <commit_hash> data/data.csv.dvc' followed by 'dvc checkout'.")

if __name__ == "__main__":
    # Clean up any existing files for a fresh demo run
    if os.path.exists('data/data.csv'):
        os.remove('data/data.csv')
    if os.path.exists('data/data.csv.dvc'):
        os.remove('data/data.csv.dvc')
    if os.path.exists('data'):
        os.rmdir('data')
    
    main()
