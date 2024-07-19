import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de prueba
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear un gráfico simple
plt.plot(x, y)
plt.title("Gráfico de prueba")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame de prueba
data = {'A': np.random.rand(10), 'B': np.random.rand(10)}
df = pd.DataFrame(data)

# Imprimir el DataFrame
print(df)

# Crear un gráfico simple
df.plot(kind='bar')
plt.title("Gráfico de prueba")
plt.xlabel("Índice")
plt.ylabel("Valores")
plt.show()
