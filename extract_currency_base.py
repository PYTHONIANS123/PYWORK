import pandas as pd

def extract_currency_code(csv_file, column_name):
    # READ THE CSV FILE
    df=pd.read_csv(csv_file)
    
    # Extract the specified column
    currency_codes=df[column_name].tolist()
    return currency_codes

def save_to_text(data, filename):
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")
            
    
def main():
    csv_file="codes-all.csv"
    column_name="AlphabeticCode"
    try:
        #Extract currency codes
        currency_codes= extract_currency_code(csv_file=csv_file, column_name=column_name)
        # save to a text file
        save_to_text(currency_codes, "currency_codes.txt")
        print("Currency codes saved to currency_codes.txt") 
    except Exception as e:
        print(e) 
    
### Good opening the file remove duplicate and turn it back to list and save to file
def reSort():
    with open("currency_codes.txt", "r") as file:
        currency_code=file.readlines()
      
    unique=set(currency_code)  
    with open("Currency_codes.txt", "w") as file:
       for code in unique:
           file.write(code)

    
reSort()