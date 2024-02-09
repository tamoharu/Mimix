Dope
==========

Some functions are not available due to under development.

Preview
-------

![Dope-preview](https://github.com/tamoharu/Dope/assets/133945583/6507e101-f2cf-4581-b82a-8869f1ebdd74)

Installation
------------

1. Create Virtual Environment


```
python3 -m venv venv
```

2. Activate


```
source venv/bin/activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```


Usage
-----

Run the command:

```
python run.py [options]
```

```
options:
  -api
  -webcam
```


API Reference
-----

Required

```
sources: List[str]
target: [str]
```

Please refer to `main/globals` for other available settings.

Reference
-------------

FaceFusion: https://github.com/facefusion/facefusion

InsightFace: https://github.com/deepinsight/insightface

YOLOv8: https://github.com/ultralytics/ultralytics