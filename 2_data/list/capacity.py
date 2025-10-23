
# 预先分配容量 比append循环快3倍
pre_allocated = [None] * 10
for i in range(10):
    pre_allocated[i] = i * 2  # 直接按索引赋值，非append
print("pre_allocated", pre_allocated, "\n")

# 预分配+动态扩容（推荐）
def safe_preallocate(initial_size=1000, buffer_ratio=0.2):
    buffer_size = int(initial_size * buffer_ratio)
    lst = [None] * (initial_size + buffer_size) # 预分配
    current_max = initial_size  # 缓存当前有效长度

    def set_value(index, value):
        nonlocal current_max, lst
        if index >= current_max: # 通过索引+当前有效长度判断是否需要扩容
            new_size = int(current_max * 1.5)
            lst += [None] * (new_size - len(lst))
            current_max = new_size
        lst[index] = value

    return set_value, lambda: lst[:current_max]
setter, getter = safe_preallocate(10)
for i in range(15):
    setter(i, i*2)
result = getter()  # 获取有效数据
print("init+dynamic", result, "\n")

# 分块预分配（适合流式数据）
# 也就是二维数组，扩容通过增加一个列表的方式扩容，完全避免整体扩容
# 读写都先定位块，再定位元素。也就是二维数组的定位
BLOCK_SIZE = 1024
class ChunkedList:
    def __init__(self):
        self.blocks = [] # 二维数组
        self.current_block = [] # 一维下标
        self._current_index = 0 # 二维下标
    
    def append(self, value):
        if self._current_index % BLOCK_SIZE == 0: # 扩容
            self.current_block = [None] * BLOCK_SIZE
            self.blocks.append(self.current_block)
        self.current_block[self._current_index % BLOCK_SIZE] = value # 固定是最新块，提供二维下标就行
        self._current_index += 1
    
    def __getitem__(self, index):
        block_num = index // BLOCK_SIZE # 一维下标
        pos = index % BLOCK_SIZE # 二维下标
        return self.blocks[block_num][pos]
cl = ChunkedList()
for i in range(3000):
    cl.append(i*3)
print(cl[2047], cl[2048])  # 跨块访问
