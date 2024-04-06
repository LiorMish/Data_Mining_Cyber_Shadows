import json
import pandas as pd
import requests
from tqdm import tqdm
from tqdm.auto import tqdm
tqdm.pandas()

def get_ip_country_name(ip_address):
    # Create the URL
    request_url = 'https://api.country.is/' + ip_address

    # Send the GET request
    response = requests.get(request_url)

    # Extract the JSON response content
    result = response.content.decode()

    # Parse the JSON response
    result = json.loads(result)

    # Return only the country name
    return result.get('country', 'Not Found')

def main():
    cyber_attacks_df = pd.read_csv('/home/mishutin/data_mining_project/cyber_attacks_dataset/cybersecurity_attacks.csv')
    cyber_attacks_df = cyber_attacks_df.dropna(subset=['Source IP Address', 'Destination IP Address'])


    # Add 'source_location' column by applying the function to 'Source IP Address'
    cyber_attacks_df['source_location'] = cyber_attacks_df['Source IP Address'].progress_apply(get_ip_country_name)
    # Add 'target_location' column by applying the function to 'Destination IP Address'
    cyber_attacks_df['target_location'] = cyber_attacks_df['Destination IP Address'].progress_apply(get_ip_country_name)

    # Dump the DataFrame to a pickle file
    cyber_attacks_df.to_pickle('/home/mishutin/data_mining_project/cyber_attacks_dataset/cyber_attacks.pkl')


if __name__ == '__main__':
    main()