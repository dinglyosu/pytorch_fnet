FROM pytorch/pytorch:v0.2

RUN pip install --upgrade pip

RUN apt update && apt install -y \
    libx11-6 \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    quilt

RUN quilt install \
    aics/label_free

RUN pip install \
    git+https://github.com/AllenCellModeling/aicsimage.git

RUN pip install --no-cache-dir --upgrade --force-reinstall --no-deps \
    git+https://github.com/JacksonMaxfield/pytorch_fnet.git
