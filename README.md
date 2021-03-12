# Deepracer_api Rewirt
This project base on https://github.com/thu2004/deepracer-vehicle-api rewrite to support the new version Deepracer Console `Software version 1.0.606.0`

# Directory Tree
```
deepracer_api/
├── config.yml
├── core
│   ├── deepracer_cam.py
│   ├── __init__.py
│   └── logger.py
├── docker
│   └── cam
│       └── Dockerfile
├── docker-compose.yml
├── g29_mode.py
├── logs
├── README.md
├── requirements.txt
├── setup.sh
├── show_cam.py
└── test
    ├── os_test.py
    └── test_g29.py
```

# Setup

```bash
Powershell
> git clone https://github.com/lshw54/deepracer_api.git
> cd deepracer_api
> python -m venv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
```

```bash
linux
> git clone https://github.com/lshw54/deepracer_api.git
> cd deepracer_api
> python3 -m venv venv
> . venv/bin/activate
> pip install -r requirements.txt
```