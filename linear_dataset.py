import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

import pandas as pd

DATA_FILE = '../DATA/fish.csv'
fishDF = pd.read_csv(DATA_FILE)
targetDF = fishDF[fishDF.columns[:1]]
featureDF = fishDF[fishDF.columns[1:]]

# 전처리
fishName = fishDF['Species'].unique().tolist()
str2int = { name:idx for idx, name in enumerate(fishName) }
fishDF['Species'] = fishDF['Species'].replace(str2int)
targetDF=fishDF[['Species']]


class MyANN(nn.Module):
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(5, 20)
        self.hd_layer = nn.Linear(20, 10)
        self.ot_layer = nn.Linear(10, 7)


    def forward(self, x):
        output = self.in_layer(x)
        output = F.relu(output)
        output = self.hd_layer(output)
        output = F.relu(output)
        output = self.ot_layer(output)
        output = F.softmax(output)
        return output
    

class FishDataset(Dataset):
    def __init__(self, feature, target):
        super().__init__()
        self.feature = feature
        self.target = target

    def __len__(self):
        return self.feature.shape[0]

    def __getitem__(self, idx):
        x = self.feature.iloc[idx].values
        y = self.target.iloc[idx].values
        x = torch.tensor(x, dtype=torch.float32)
        y = torch.tensor(y)
        return x, y
    

    
fishDS = FishDataset(featureDF, targetDF)

print(f'{len(fishDS)}개의 데이터셋이 생성되었습니다.')
print(f'{fishDS[0]}')