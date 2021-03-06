# round-robin-generator

[![Codeship Status for avadavat/round-robin-generator](https://app.codeship.com/projects/deb1b7b0-6962-0138-9e23-22c0d1c6829f/status?branch=master)](https://app.codeship.com/projects/394216)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Efficiently creates incomplete/complete round robin matchups.

## Installation

```
git clone https://github.com/avadavat/round-robin-generator
cd round-robin-generator
pip install -r requirements.txt
```

## Usage

```
python round_robin_generator.py -p tests/players.txt -r 3
```

## Options

Use `-i` to specify the algorithm used for round robin generation.
Options are `CIRCLE` and `DEFAULT_SCRAMBLE`. Default_Scramble is run when the `-i` parameter is omitted.

<p align="center">
  <img src=branding/Robin_Logo.png? alt="Custom Logo" width="200" />
</p>
