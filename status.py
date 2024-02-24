import requests  
import argparse  
import sys  
from datetime import datetime

parser = argparse.ArgumentParser(description="🌐 HTTP Status Checker by Darreus 🛠️")  

parser.add_argument('-w', '--wordlist', type=str, required=True, help="📄 Path to the wordlist file")  
parser.add_argument('-u', '--url', type=str, required=True, help="🎯 Target URL to check")  
args = parser.parse_args()  

print("📋 Wordlist: ", args.wordlist)  
print("🔗 URL: ", args.url)  

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',  
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',  
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
]

file = open(args.wordlist, 'r')  
lines = file.readlines()  

if ('http' in args.url) or ('https' in args.url):  
    pass  
else:
    print('❌ Please enter a URL Schema')  
    sys.exit()  

try:
    results = []  # List to store results
    for line in lines:  
        line = line.strip("\n")  
        for user_agent in user_agents:  
            headers = {'User-Agent': user_agent}  
            r = requests.get(args.url+'/'+line, headers=headers)  
            if(r.status_code != 404):  
                result = f"{args.url+'/'+line} : {r.status_code}"
                results.append(result)  # Append result to the list
                print(result)  
                break  
    # Saving results to a text file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"results_{timestamp}.txt"
    with open(filename, 'w') as f:
        for result in results:
            f.write(result + '\n')
    print(f"✅ Results saved to '{filename}'")
except Exception as e:
    print("❌ Error Occurred:", str(e))  
