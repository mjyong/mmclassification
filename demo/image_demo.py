# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser

import mmcv
from rich import print_json

from mmcls.apis import inference_model, init_model


def main():
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    model = init_model(args.config, args.checkpoint, device=args.device)
    # test a single image
    result = inference_model(model, args.img)
    # show the results
    print_json(mmcv.dump(result, file_format='json', indent=4))


if __name__ == '__main__':
    main()
