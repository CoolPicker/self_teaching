import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# First way to call the 2 group Venn diagram:
venn2(subsets=(10, 5, 2), set_labels=('Group A', 'Group B'))
plt.show()

# Second way
venn2([set(['A', 'B', 'C', 'D']), set(['D', 'E', 'F'])])
plt.show()
