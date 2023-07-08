# Food Doctor for Travlers

Travelling means going out to new places and it can be very unfortunate if you happen to eat the wrong food.

We decided to build a project that leverages Google Palm 2 and Text-to-Image model to provide users with food knowledge to avoid allergies.

A safe journey is the best journey.

# How to run

You'll need a _service account JSON file_ provided by Google Cloud. And do the following cmd.

```bash
# At the parent directory
mkdir .google
cp <your_service_account>.json ./google/service_account.json
```

Install python packages.
```
pip install -r requirements.txt
```

# Project overall process

The overall process of this project, from the start to the end.

![Overall process](./doc/pate_travel.png)
