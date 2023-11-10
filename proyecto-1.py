from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edad = data["age"]
edades_np = np.array(edad)

# Calcular el promedio de edad
promedio_edad = np.mean(edades_np)
print(promedio_edad)