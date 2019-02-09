import os


def get_all_dataloaders(
    dataset_cls, bert_model, train_dev_split_prop=0.8, max_len=512, dl_kwargs={}
):
    """ Initializes train/dev/test dataloaders given dataset_class"""

    # split train -> artificial train/dev
    train_ds = dataset_cls(split="train", bert_model=bert_model, max_len=max_len)
    train_dl, dev_dl = train_ds.get_dataloader(
        split_prop=train_dev_split_prop, **dl_kwargs
    )

    # treat dev -> test
    test_ds = dataset_cls(split="dev", bert_model=bert_model, max_len=max_len)
    test_dl = test_ds.get_dataloader(**dl_kwargs)

    return {"train": train_dl, "dev": dev_dl, "test": test_dl}


def tsv_path_for_dataset(dataset_name, dataset_split):
    return os.path.join(
        os.environ["GLUEDATA"], "{}/{}.tsv".format(dataset_name, dataset_split)
    )