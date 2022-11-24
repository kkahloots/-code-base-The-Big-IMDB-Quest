### 1. To conda env, type:
```
conda create -n env-imdb python=3.9 -y && conda activate env-imdb
```

### 2. To install requirments, type:
```
pip install -r requirements.txt
```

### 3. To invididual unittest, type:
```
cd tests
python -m unittest test_valid_page -vvv
cd -
```

### 4. To all unittests, type:
```
python -m unittests
```

### 5. To all The pipeline, type:
```
python -m main
```
