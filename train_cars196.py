import argparse
import torch
from hdml import train
from hdml import dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='train hdml with triplet loss.')
    parser.add_argument('-b', '--batch_size', type=int, default=120, help="Batch size.")
    parser.add_argument('-s', '--image_size', type=int, default=227, help="The size of input images.")
    parser.add_argument('-l', '--lr_init', type=float, default=7e-5, help="Initial learning rate.")
    parser.add_argument('-m', '--max_steps', type=int, default=80000, help="The maximum step number.")
    args = parser.parse_args()
    streams = dataset.get_streams('data/CARS196/cars196.hdf5', args.batch_size, 'cars196', 'triplet', crop_size=args.image_size)
    train.triplet_train(streams, args.max_steps, args.lr_init,
                        device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))