import numpy as np


class Dataset(object):
    def __init__(self, method):
        self.type = {}
        class_dim = 0
        embeds = {}
        with open('results/cora/' + method + '/result.csv', 'r') as f:
            f.readline()
            for line in f.readlines():
                node = line.split()[0]
                embed = list(map(float, line.split()[1:]))
                embeds[node] = embed
        X, y = [], []
        with open('data/cora/cora.content', 'r') as f:
            for line in f.readlines():
                node = line.split()[0]
                type = line.split()[-1]
                if type not in self.type:
                    class_dim += 1
                    self.type[type] = class_dim
                X.append(embeds[node])
                y.append(self.type[type])
        # data_len = len(y)
        # permutation = np.random.permutation(data_len)
        # train_split = int(0.7 * data_len)
        # X, y = np.array(X), np.array(y)
        # self.train_X, self.train_y = X[permutation[:train_split]], y[permutation[:train_split]]
        # self.test_X, self.test_y = X[permutation[train_split:]], y[permutation[train_split:]]
        X, y = np.array(X), np.array(y)
        self.train_X, self.train_y = X[:200], y[:200]
        self.valid_X, self.valid_y = X[200: 500], y[200: 500]
        self.X = np.concatenate([self.train_X, self.valid_X])
        self.y = np.concatenate([self.train_y, self.valid_y])
        self.test_X, self.test_y = X[500: 1500], y[500: 1500]


if __name__ == '__main__':
    data = Dataset('node2vec')  # DeepWalk, LINE, node2vec
