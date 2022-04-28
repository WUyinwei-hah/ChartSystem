import numpy as np

# %% 将单个数组以二进制格式保存到磁盘
# np.load和np.save是读写磁盘数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中。
a = np.random.randint(0, 999, 50, dtype=int)
np.save('./data/test.npy', a)  # 这样在程序所在的文件夹就生成了一个test.npy文件

# 将test.npy文件中的文件读出来
a = np.load('./data/test.npy')
print(a)
