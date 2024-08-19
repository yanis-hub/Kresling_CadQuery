# Installing CadQuery via pip

CadQuery can be installed via pip on Linux, MacOS, and Windows. Python versions 3.9 and newer are supported by CadQuery.

It is highly recommended to use a virtual environment when installing CadQuery, although it is not strictly required.

To install the latest version of pip:

```bash
python3 -m pip install --upgrade pip
```

Once a current version of pip is installed, CadQuery can be installed using the following command line:

```bash
pip install cadquery
```

It is also possible to install the very latest changes directly from CadQuery's GitHub repository:

```bash
pip install git+https://github.com/CadQuery/cadquery.git
```

For users who want to use CadQuery with IPython/Jupyter or set up a developer environment, additional dependencies can be installed:

```bash
pip install cadquery[ipython]
pip install cadquery[dev]
```

## Adding a Nicer GUI via CQ-editor

If you prefer to have a GUI available, your best option is to use [CQ-editor](https://github.com/CadQuery/CQ-editor).

You can download the newest build [here](https://github.com/CadQuery/CQ-editor/releases/tag/nightly).

### Linux/MacOS Installation

1. Download the installer (.sh script matching OS and platform).
2. Make the script executable: right-click, select **Properties**, go to **Permissions**, and check **Allow executing file as a program**.
3. Run the script.

```bash
curl -LO https://github.com/CadQuery/CQ-editor/releases/download/nightly/CQ-editor-master-Linux-x86_64.sh
sh CQ-editor-master-Linux-x86_64.sh

$HOME/cq-editor/run.sh
```

### Windows Installation

1. Download the installer (.exe) and double-click it.
2. Follow the prompts to accept the license and optionally change the installation location.
3. Run the **run.bat** script:

```bash
C:\Users\<username>\cq-editor\run.bat
```

## Jupyter Integration

Viewing models in Jupyter is another good option for a GUI. Models are rendered in the browser.

First install CadQuery, then install JupyterLab:

### Using conda

```bash
mamba install jupyterlab
```

### Using pip

```bash
pip install jupyterlab
```

Start JupyterLab:

```bash
jupyter lab
```

Create a Notebook to interactively edit/view CadQuery models. Use `display` to show the model:

```python
display(<Workplane, Shape, or Assembly object>)
```

## Test Your Installation

If all has gone well, you can open a command line/prompt, and type:

```python
python
>>> import cadquery
>>> cadquery.Workplane('XY').box(1,2,3).toSvg()
```

You should see raw SVG output displayed on the command line if the CadQuery installation was successful.
