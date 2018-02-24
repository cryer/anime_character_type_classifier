# anime_character_type_classifier

这是我闲来无事做的一个小项目，根据输入的动漫女性图片，可以判断女性的类别，暂时只是大概做了三类：萝莉，御姐，成熟女性。如果你们感兴趣的话，
可以添加更多的分类，比如黑长直，金发等，当然也可以是隐藏属性等等，比如天然呆，傲娇，腹黑，病娇等等，当然做到这些需要你好好的准备数据集。

## 数据集

我的数据集其实没有花太多时间，简单的用爬虫爬取百度图片，三种类型，其中前两种比较好爬，爬取完后进行筛选，去除背景较大的，
尽量让人物填满整个图片，当然如果你有心的话，可以手动截取，去除多余的背景，我每一类只留下了50张图片，所以截取工作量也能接受。
当然你如果想获得更好的效果，就需要更多的数据。第三类图片爬取成熟女性的动漫角色的话，出来的基本都是很奇妙的东西。。
我试了下爬取K站的图，也都是不太合适的图片，因此我不得不手动从百度图片找，大致让我满意的就找了30张。。也懒得再找了，
就这样吧。（真的是懒）


PS：因为动漫角色不是人脸和真实物体，所以我暂时不太清楚有什么办法可以程序式的识别出图片中的角色，如果是人脸的话，有很多的程序方法
可以直接将人脸从图片中扣出。所以稳妥点还是手动截取角色吧，但是我比较懒2333我直接用了爬虫爬取后的图片，然后简单筛选一下，留下50张，
之后我会上传到百度云盘。`所以我这个数据集不管在数量还是质量上都是很差的，你们有很大的提升空间`

## 数据增强

要训练神经网络，一共130张图片肯定是不够的，因此需要数据增强。我提供了一些利用PIL模块数据增强的方法，放在了process.py中，
你们可以自行修改，也可以直接用。

最后我增强到了1040张图片，勉勉强强合格了。

## 训练

```
git clone https://github.com/cryer/anime_character_type_classifier.git
cd anime_character_type_classifier/
python train.py
```
训练相关的配置都在Config中：

```
class Config(object):
    model_saved_path='checkpoints/anime_type.pkl'
    train_path='data/'
    img_size = 128
    batch_size=20
    shuffle = True
    num_workers = 2
    lr=1e-3
    use_gpu=False
    epoch = 20
    test_img = 'test/luo1.jpg'
```
你们可以根据实际情况进行修改。我这里只训练了20轮，又因为图片数量不大，所以只用了10分钟不到就训练好了，
因此我就不给出checkpoints文件了，你们可以修改配置，增加epoch，制作更大更好的数据集，这样效果会更好。

## 结果

尽管我的数据集不是很好，训练时间也很短，但是效果却还可以，我测试了几张图片基本都可以准确分类。

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/luo5.jpg)

测试输出：`这个妹子是： 萝莉`

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/luo6.jpg)

测试输出：`这个妹子是： 萝莉`

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/yu3.jpg)

测试输出：`这个妹子是： 御姐`

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/yu4.jpg)

测试输出：`这个妹子是： 御姐`

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/yu6.jpg)

测试输出：`这个妹子是： 御姐`

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/shu1.jpg)

测试输出：`这个妹子是： 成熟女性`

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/shu2.jpg)

测试输出：`这个妹子是： 成熟女性`

emmmm，你问我成熟女性和御姐有啥区别？？ emmmm，我也没看出来，只能交给百度了，搜索御姐出来的图片我都认为是御姐了，
搜索成熟女性出来的图片，我就认为为是成熟女性了。。上面最后两个在百度眼里的确就是成熟女性，可能成熟女性不一定是
要结过婚的吧emmm

或者是我的分类不太明确，你们可以做数据集的时候设置更分明的分类。

当然也有错误分类的，比如下面这张：

![](https://github.com/cryer/anime_character_type_classifier/raw/master/image/yu1.jpg)

测试输出：`这个妹子是： 萝莉`

。。。。What？不过这也没办法，在这个不怎么样的数据集上，只训练了几分钟就有这个效果我已经很满意了。。不过话说这个妹子
是不是颜艺之渊的学生会长？



