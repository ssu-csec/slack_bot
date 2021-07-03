from pickle import load, dump


def load_pickle(save_path):
    try:
        f = open(save_path, "rb")
    except FileNotFoundError:
        return None

    load_content = load(f)
    f.close()
    return load_content


def save_pickle(save_content, save_path):
    f = open(save_path, "wb")
    dump(save_content, f)
    f.close()