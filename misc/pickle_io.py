import pickle


def load_list(save_path):
    try:
        f = open(save_path, "rb")
    except FileNotFoundError:
        return None

    loading_list = pickle.load(f)
    f.close()
    return loading_list


def save_list(saving_list, save_path):
    f = open(save_path, "wb")
    pickle.dump(saving_list, f)
    f.close()