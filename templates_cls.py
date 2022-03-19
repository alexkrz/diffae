from templates import *


def cls_ffhq128_autoenc():
    conf = ffhq128_autoenc_130M()
    conf.train_mode = TrainMode.manipulate
    conf.manipulate_mode = ManipulateMode.celebahq_all
    conf.manipulate_znormalize = True
    conf.latent_infer_path = f'checkpoints/{ffhq128_autoenc_130M().name}.pkl'
    conf.batch_size = 32
    conf.lr = 1e-3
    conf.total_samples = 300_000
    # use the pretraining trick instead of contiuning trick
    conf.pretrain = PretrainConfig(
        '130M',
        f'checkpoints/{ffhq128_autoenc_130M().name}/last.ckpt',
    )
    conf.name = 'ffhq128_autoenc_cls'
    return conf


def cls_ffhq256_autoenc():
    '''We first train the encoder on FFHQ dataset then use it as a pretrained to train a linear classifer on CelebA dataset with attribute labels'''
    conf = ffhq256_autoenc()
    conf.train_mode = TrainMode.manipulate
    conf.manipulate_mode = ManipulateMode.celebahq_all
    conf.manipulate_znormalize = True
    conf.latent_infer_path = f'checkpoints/{ffhq256_autoenc().name}/latent.pkl'  # we train on Celeb dataset, not FFHQ
    conf.batch_size = 32
    conf.lr = 1e-3
    conf.total_samples = 300_000
    # use the pretraining trick instead of contiuning trick
    conf.pretrain = PretrainConfig(
        '130M',
        f'checkpoints/{ffhq256_autoenc().name}/last.ckpt',
    )
    conf.name = 'ffhq256_autoenc_cls'
    return conf