from const import FilePath
from misc.pickle_io import load_pickle, save_pickle


def webhook_io(**kwargs):
    webhook_path = FilePath.webhook
    webhooks = load_pickle(webhook_path)

    if webhooks is None:
        webhooks = dict()

    if kwargs["func"] == "append":
        webhooks[kwargs["name"]] = kwargs["url"]
    elif kwargs["func"] == "retrieve":
        print(webhooks[kwargs["name"]])
    elif kwargs["func"] == "remove":
        webhooks.pop(kwargs["name"])
    else:
        return False

    save_pickle(webhooks, webhook_path)
    return True


if __name__ == '__main__':
    while True:
        print("\nSelect menu")
        print("1: Appends webhook url")
        print("2: Retrieves webhook url")
        print("3: Removes webhook url")
        print("Else: Quit\n")

        menu = int(input())
        if menu == 1:
            print("name: ", end='')
            name = str(input())
            print("url: ", end='')
            url = str(input())

            param = {"func": "append", "name": name, "url": url}
            print(param)
            webhook_io(**param)
        elif menu == 2:
            print("name: ", end='')
            name = str(input())

            param = {"func": "retrieve", "name": name}
            webhook_io(**param)
        elif menu == 3:
            print("name: ", end='')
            name = str(input())
            print("Do you really REMOVE " + name + "? [YES/NO]")
            yn = str(input()).upper()

            if yn == "YES" or yn == "Y":
                param = {"func": "remove", "name": name}
                webhook_io(**param)
                print("Done.")
            else:
                print("Canceled.")
        else:
            break
