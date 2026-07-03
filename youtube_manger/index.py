import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for idx, video in enumerate(videos, start = 1):
        print(f"{idx} {video['name']} {video['time']}")
    print("\n")
    print("*" * 50)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name' : name, 'time' : time})
    save_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter video number to update: "))
    if 1 <= idx <= len(videos):
        name = input("Enter video new name: ")
        time = input("Enter video new time: ")
        videos[idx-1] = {'name': name, 'time': time}
        save_helper(videos)
        print("\n Video Added Successfully")
        
    else:
        print("Invailed input")



def delete_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter the video Number: "))
    if 1 <= idx <= len(videos):
        del videos[idx-1]
        save_helper(videos)
        print("Video Deleted Successfully")
    else:
        print("invailed video number")
    

def main():
    videos = load_data()
    while True:
        print("Youtube Manager || Choose an option")
        print("*" * 50)
        print("\n")
        print("1. List a favourate videos ")
        print("2. add a youtube videos ")
        print("3. Udpate youtube videos details")
        print("4. Delete video")
        print("5. Exit App")
        choice = input("\n Enter a your choice: ")

        match choice:
            case '1':
                # print("1. List a favourate videos ")
                list_all_videos(videos)
            case '2':
                # print("2. add a youtube videos ")
                add_video(videos)
            case '3':
                # print("3. Udpate youtube videos details")
                update_video(videos)
            case '4':
                # print("4. Delete video")
                delete_video(videos)
            case '5':
                # print("5. Exit App")
                break
            case _:
                print("Wrong choice please change")

if __name__ == "__main__":
    main()

