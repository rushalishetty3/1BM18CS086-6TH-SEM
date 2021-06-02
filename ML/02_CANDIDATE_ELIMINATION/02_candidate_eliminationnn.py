import csv

def positive(S,G,x,length):
    for i in range(length):
        if S[i]!=x[i] and S[i]!='?':
            if S[i]=='null':
                S[i] = x[i]
            else:
                S[i] = '?'
    return S,G

def negative(S,G,x,length):
    return S,G

if __name__ == "__main__":
    data = []

    # reading csv file
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        print("Data: ")
        for row in reader:
            data.append(row)
            print(row)

    len = len(data[0])
    S = ['null'] * (len-1)
    G = [['?'] * (len-1)]

    for x in data:
        if x[-1].upper() == 'YES':
            S,G = positive(S,G,x,len-1)
        else:
            S,G = negative(S,G,x,len-1)

        print(S)
        print(G)