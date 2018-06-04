from open_seq2seq.models import Image2Label
from open_seq2seq.encoders.alexnet_encoder import AlexNetEncoder
from open_seq2seq.decoders import FullyConnectedDecoder
from open_seq2seq.losses import CrossEntropyLoss
from open_seq2seq.data import ImagenetDataLayer
from open_seq2seq.optimizers.lr_policies import poly_decay
import tensorflow as tf


base_model = Image2Label

base_params = {
  "random_seed": 0,
  "use_horovod": False,
  "num_epochs": 100,

  "num_gpus": 8,
  "batch_size_per_gpu": 128,
  "dtype": tf.float32,

  "save_summaries_steps": 2000,
  "print_loss_steps": 100,
  "print_samples_steps": 2000,
  "eval_steps": 5000,
  "save_checkpoint_steps": 5000,
  "logdir": "experiments/alexnet-imagenet",

  "optimizer": "Momentum",
  "optimizer_params": {
    "momentum": 0.90,
  },
  "lr_policy": poly_decay,
  "lr_policy_params": {
    "learning_rate": 0.02,
    "power": 1.0,
  },

  "initializer": tf.variance_scaling_initializer,

  "regularizer": tf.contrib.layers.l2_regularizer,
  "regularizer_params": {
    'scale': 0.0005,
  },
  "summaries": ['learning_rate', 'variables', 'gradients', 'larc_summaries',
                'variable_norm', 'gradient_norm', 'global_gradient_norm'],
  "encoder": AlexNetEncoder,
  "encoder_params": {},

  "decoder": FullyConnectedDecoder,
  "decoder_params": {
    "output_dim": 1000,
  },
  "loss": CrossEntropyLoss,
  "data_layer": ImagenetDataLayer,
  "data_layer_params": {
    "data_dir": "data/tf-imagenet",
    "image_size": 227,
  },
}
