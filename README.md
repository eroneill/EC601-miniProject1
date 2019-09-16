# EC601 Mini Project 1
Course Mini Project 1 for ENG EC 601

## Requirements

* Python >= 3.5
* *Twitter* API access keys
* *Google Cloud Platform* API access keys

----

## Setup and Runing Tests

### Basic

For develop mode (editable), copy and paste following commands into the terminal.
```bash
python setup.py develop
pytest # with stdin capture (no stdin output)
pytest -s # without any capture (with stdin output)
```
To test the API access, please provide the access key in Test Config File as described below.



### Test Config File

Please put a config file named `test.conf` in the project root directory, with following format:
```config
[PATH]
twitter_keys_path = YOUR_PATH_HERE
gcp_keys_path = YOUR_PATH_HERE
```
Note that the key file of GCP should be download directly from the offical site (your console).

----

## Sprint 1

[User stories](./docs/user_stories.md) and [architecture](./docs/architecture.md) are placed in `docs` directory.

For the demo part, please check out the JSON serialized Twitter response object [here](./home_timeline_sample.json),
as well as the Google Cloud Platform sentiment analyze result of a simple sentence [here](./gcp_sentiment_sample).

To reproduce these result, please set up `test.conf` file, and then follow the instruction in **Setup and Running Test** section.

----

### Formatting

We simply use the default configuration of [black](https://github.com/psf/black). To be simple, we don't use `pytset-black` to check the formatting, but in order to keep the uniform, please formatting the code styple under the guidance of `black`.

----

## License
[MIT](./LICENSE)
