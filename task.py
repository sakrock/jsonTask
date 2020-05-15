import json, requests

def ifSubstring(s1, s2):
    if s1.find(s2) == -1 or s2.find(s1) == -1:
        return False
    else:
        return True    
        
def showData(data, types):
    for item in data[types]:
        s = item["confName"] + " "+ item["confStartDate"] + " " + item["city"] + "," + item["country"] + " " + item["entryType"] + " " + item["confUrl"]
        print(s)

def check_exact_duplicate(data, type):
    d = {}
    ans = []
    for item in data[type]:
        s = item["confName"] + " "+ item["confStartDate"] + " " + item["city"] + "," + item["country"] + " " + item["entryType"] + " " + item["confUrl"]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    for i in list(d.keys()):
        if d[i] > 1:
            ans.append(i)        
        
    print(*ans, sep="\n")


if __name__ == "__main__":
    req = requests.get("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")

    req_text = req.text

    data = json.loads(req_text)
    
    showData(data, "paid")
    
    check_exact_duplicate(data, "paid")
