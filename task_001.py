import numpy as np
import matplotlib.pyplot as plt
import os
import xml.etree.ElementTree as ET

# 1. Définition de la fonction f(x)
def f(x):
    return -np.cos(x) * np.cos(np.pi) * np.exp(-(x - np.pi)**2)

# 2. Générer les valeurs de x avec un pas assez petit pour lisser le graphe
x_values = np.linspace(-100, 100, 2000)  # 2000 points pour un graphe lisse
y_values = f(x_values)

# 3. Réduire la plage à sauvegarder dans le fichier XML (autour de pi pour lisibilité)
x_export = x_values[(x_values > (np.pi - 5)) & (x_values < (np.pi + 5))]
y_export = f(x_export)

# 4. Créer le dossier "results" s'il n'existe pas
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

# 5. Sauvegarde des données dans un fichier XML
root = ET.Element("data")
xdata = ET.SubElement(root, "xdata")
ydata = ET.SubElement(root, "ydata")

# Ajouter les valeurs de x
for x in x_export:
    x_elem = ET.SubElement(xdata, "x")
    x_elem.text = f"{x:.6f}"  # 6 chiffres après la virgule

# Ajouter les valeurs de y
for y in y_export:
    y_elem = ET.SubElement(ydata, "y")
    y_elem.text = f"{y:.6f}"

# Écrire le fichier XML
xml_file_path = os.path.join(results_dir, "resultat_fonction.xml")
tree = ET.ElementTree(root)
tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)

print(f"Résultats sauvegardés dans : {xml_file_path}")

# 6. Tracer la courbe pour toute la plage
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label="f(x)", color='orange')
plt.title("Graphique de la fonction f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Sauvegarde de l'image du graphique
plot_file_path = os.path.join(results_dir, "graphique.png")
plt.savefig(plot_file_path)
plt.show()

print(f"Graphique sauvegardé dans : {plot_file_path}")