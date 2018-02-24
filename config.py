
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