# madm-non-compensatory-solvers

Multi Attribute Decision Making project: Weighting a sample problem attributes using methods taught in the class.

# Methods implemented:
* Least Square Function

* Eigenvectors

# How to run
First of all, you need [pypoetry](https://python-poetry.org/) to install project dependencies (also you can simply use `pip` and the `requirements.txt` provided file; however, it is recomended to use pypoetry)

after installing dependencies using `poetry install` you can use the `run.py` to start the project:
```bash
run -m {METHOD} -f {PRIORITY_SET_CSV_FILE} -p {PROBLEM_PARAMETERS_CSV_FILE} -o {OUTPUT_CSV_FILE}
```

For more information, please check `run.py`

# Contributors

With special thanks to [Amirreza Salehi](https://github.com/AmirrezaSLH)
