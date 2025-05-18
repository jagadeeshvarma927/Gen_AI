conda create -p venv python=3.10 -y

pip install -r requirements.txt

pip install ipykernel


```
 conda create -p env python=3.10 -y
```
```
conda activate env
```
```
uvicorn main:app --reload --port 8001
```