import pickle

class KaggleDataset():
    def __init__(self, path_of_dataset="data/Kaggle/test.pkl"):
        with open('data/Kaggle/test.pkl', 'rb') as f:
            self.data = pickle.load(f)
        self.poster_data = self.process_data()
    
    def process_data(self):
        poster = self.data['posts_text']
        label = self.data['annotations']
        label_lookup = {'E': 1, 'I': 0, 'S': 1, 'N': 0, 'T': 1, 'F': 0, 'J': 1, 'P': 0}
        poster_data = [{'posts': t, 'label0': label_lookup[list(label[i])[0]],
                        'label1': label_lookup[list(label[i])[1]], 'label2': label_lookup[list(label[i])[2]],
                        'label3': label_lookup[list(label[i])[3]]} for i, t in enumerate(poster)]
        return poster_data
    
    def clean_data(self):
        for data_line in self.poster_data:
            for post in data_line['posts']:
                pass
                



class EssayDataset():
    def __init__(self, path_of_dataset="data/Essay/test.pkl"):
        with open('data/Essay/test.pkl', 'rb') as f:
            self.data = pickle.load(f)