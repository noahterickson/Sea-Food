import json


def main():
    with open("20181202.json",'r') as f:
        datastore = json.load(f)
    data = datastore['items']

    for track in data:
        print("Track name: {0} was added to the playlist on {1}".format(track["track"]["name"], track["added_at"]))

    print(type(datastore['items'][0]))
    #print(datastore)

if __name__ == "__main__":
    main()
