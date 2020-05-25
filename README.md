## 提取语料中的句式，分别针对不同的实体类型扩展相应的语料

## data
* data/raw 中初始的横向的少量数据集data.json
* mapping.json 是一个字典，分别为需要扩展的实体名与对应的实体列表名
* data/dict 人物_企业家国内.json, 城市.json等json文件是需要扩展实体的list
* configure.json 是文件与超参数配置，
  其中max_list_expend是data实体list扩展的限度，低于限度的实体全部保留，超过限度的实体数量：按照限度阈值随机抽取限度数量的个数进行扩展

## code
### 1.读取并转换原始的 json 格式的语料
* json_to_conllx.py 将初始的json格式的语料转换成 conllx 格式语料
* merge_data.py 将文件中所有的 json格式转换的 conllx 格式的语料都合并成一个总的语料

### 2. 对转换后的语料根据mapping，dict字典进行扩展（可选）
* meta_generate.py 将 data/dict 中所有的实体list 提取成需要扩展的 k,v 字典格式，保存为meta.json文件
* generate_seq.py 读取生成的 data.conllx 语料，根据mapping.json字典映射表，寻找data文件夹里面需要扩展的实体list进行语料扩充，依赖configure.json配置文件
* generate_seq2.py 功能与 generate_seq.py 一样，区别是不依赖 configure.json 配置文件，超参数都是固定的。

all_run_expend.py 顺序执行上面的1、2, 生成的扩展后的语料保存在'./data/expend/data_expend.conllx'

### 3. 对扩充后的语料（可选）进行比例划分，收集实体列表等处理，用作 ner 模型训练

* split_data.py 对数据集进行 train 与 test 比例划分（一般 8：2）
* collect_tag.py 收集数据集的实体列表 entity.txt
* collect_label.py 收集数据集的意图列表 label.txt
* write_metadata.py 统计语料比例的数量，以及生产的日期等

all_run.py 一键顺序执行 1，2，3 中的所有脚本，生成ner模型训练需要的数据格式