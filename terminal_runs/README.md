# Using Cluster for Label Free Predictions

## Changing Prediction Options
You will have to copy the `config.json` and `run.sh` to the directory you want
predictions for. Then edit those files to generate the predictions you want.

#### `config.json`
There are four attributes in the `config.json` that are needed.
* `structure`: Corresponds to which structure you want to be predicted.
   * `"dna"`
   * `"tom20"`
   * `"membrane"`
   * `"lamin_b1"`
   * `"sec61_beta"`
   * `"fibrillarin"`
* `brightfield`: Corresponds to which channel the brightfield is located at.
Usually it is okay to keep this at `-1` because this will tell the script to
use the last channel in the image, which is usually the brightfield. If you
need to change it however, use zero-indexing. If the brightfield is the third
channel, put `2`.
* `files`: Corresponds to which directories or specific files you want
predictions for. Provide a comma separated list with paths in `"quotes"` and
the entire list needs to be wrapped in `[brackets]`. Ex:
`["/path/to/directory/1/", "/path/to/directory/2/"]`.
* `gpu_ids`: Corresponds to which gpu the prediction should be run on. This
should really be kept on `0` unless told otherwise.

#### `run.sh`
The `run.sh` file is how you actually tell the cluster to generate the
predictions. You will have to change two things in this file. The drive mount
point and the path to the `config.json` file.

The drive mount point should be replaced with the highest common directory of
all the paths provided in the `config.json` file.

Ex: `/path/to/directory/config.json`
```json
{
    "structure": "dna",
    "brightfield": -1,
    "files": [
        "/path/to/directory/1/",
        "/path/to/directory/2/",
        "/path/to/directory/3/"],
    "gpu_ids": 0
}
```

If you notice all the directories provided in the `files` attribute of
`config.json` and the `config.json` file itself all have a shared parent
directory of `/path/to/directory/` so we will point our mount path to there.

Additionally we will put the path to the `config.json` file at the end.

Ex: `/path/to/directory/run.sh`
```
nvidia-docker run -t \
	-v /path/to/directory/:/path/to/directory/ \
	lf_predict label_free_predict \
	/path/to/directory/config.json
```

## Generating Predictions

After creating your versions of the `config.json` and `run.sh` files navigate
to where the `run.sh` file is located and simple:

```
. run.sh
```

All predictions will be saved in a predictions folder inside each of the
directories given / if a file was given it will be in a predictions directory
that is a sibling of the file. Prediction file names will be the same file name
followed by `_structure` where structure is which structure was predicted,
`example_file_100X_zstack_dna.ome.tif`.
