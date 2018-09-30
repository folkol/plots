import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

Ship = namedtuple('Ship', ['name', 'begin', 'end'])

regalskepp = [
        Ship('Äpplet', 1622, 1625),
        Ship('Vasa', 1627, 1627),
        Ship('Äpplet', 1628, 1659),
        Ship('Kronan', 1632, 1675),
        Ship('Scepter', 1636, 1675),
        Ship('Draken', 1656, 1677),
        Ship('Viktoria', 1658, 1686),
        Ship('Saturnus', 1662, 1707),
        Ship('Riksäpplet', 1663, 1676),
        Ship('Svärdet', 1662, 1676),
        Ship('Wrangel', 1664, 1713),
        Ship('Nyckeln', 1665, 1679),
        Ship('Mars', 1665, 1677),
        Ship('Jupiter', 1665, 1710),
        Ship('Venus', 1667, 1706),
        Ship('Kronan', 1668, 1676),
        Ship('Solen', 1669, 1694),
        Ship('Mercurius', 1672, 1720),
]

begin = np.array([begin for _, begin, _ in regalskepp])
end = np.array([end for _, _, end in regalskepp])
event = [name for name, _, _ in regalskepp]

plt.style.use('seaborn-paper')

plt.barh(range(len(begin)), end-begin+0.1, left=begin)
plt.yticks(range(len(begin)), event)
plt.title(f'Regalskeppens tjänstgöringsperioder')

plt.show()
