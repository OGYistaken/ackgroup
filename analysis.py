import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hospital.csv")

toplam_gelir = df["Gelir"].sum()
toplam_gider = df["Gider"].sum()



kar = toplam_gelir - toplam_gider
df.plot(kind="bar", x="Ay", y=["Gelir", "Gider"])
plt.title("Gelirler ve Giderler")
plt.xlabel("Ay")
plt.ylabel("Tutar")
plt.show()


if kar > 0:
    print(f"Kar: {kar} TL")
else:
    print(f"Zarar: {kar} TL")