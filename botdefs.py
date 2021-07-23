import requests
from pint import UnitRegistry

ureg = UnitRegistry()

G = 6.67259e-11 * ureg.newton * ureg.meter*ureg.meter / ureg.kilogram**2 
c=2.99792458e8 * ureg.meter / ureg.second
Na=6.0221367e23 * ureg.mole
R=8.314510 * ureg.joule / (ureg.kelvin * ureg.mole)
k=1.380658e-23 * ureg.joule / ureg.kelvin
sb=5.67051e-8 * ureg.weber / (ureg.meter**2 *  ureg.kelvin**4)
b=2.897756e-3 * ureg.meter *  ureg.kelvin
e=1.60217733e-19 * ureg.coulomb
me=9.1093897e-31 * ureg.kilogram
mp=1.6726231e-27 * ureg.kilogram
mn=1.6749286e-27 * ureg.kilogram
mu0=1.2566370614359173e-6 * ureg.newton / ureg.ampere**2
E0=8.854187817e-12 * ureg.coulomb**2 / (ureg.newton * ureg.meter**2)
F=96485.3029 * ureg.coulomb / ureg.mole
h=6.6260755e-34 * ureg.joule * ureg.second
Ry=1.0973731534e7 / ureg.meter
h0=13.605698 * ureg.eV
a0=5.29177249e-11 * ureg.metre

const_unit = {"G":G,"c":c,"Na":Na,"R":R,"k":k,"sb":sb,"b":b,"e":e,"me":me,
"mp":mp,"mn":mn,"mu0":mu0,"E0":E0,"F":F,"h":h,"Ry":Ry,"h0":h0,"a0":a0}

def covid_state():
	cl = []
	data = requests.get('https://disease.sh/v3/covid-19/all').json()
	for x, y in data.items():
		cl.append(f"{x}-{y}")
	return (cl)

constants = {"G":('6.67259 ⨯ 10⁻¹¹','Nm²kg⁻²'),"c":('2.99792458 ⨯ 10⁸','ms⁻¹'),"Na":('6.0221367⨯ 10²³', 'mol⁻¹'),
"R":(8.314510,"JK⁻¹mol⁻¹"),"k":('1.380658 ⨯ 10⁻²³',"JK⁻¹"),"sb":('5.67051 ⨯ 10⁻⁸',"Wm⁻²K⁻⁴"),
"b":('2.897756 ⨯ 10⁻³','mK'),"e":('1.60217733 ⨯ 10⁻¹⁹',"C"),"me":('9.1093897 ⨯ 10⁻³¹',"kg"),
"mp":('1.6726231 ⨯ 10⁻²⁷','kg'),"mn":('1.6749286 ⨯ 10⁻²⁷','kg'),"mu0":('1.2566370614359173 ⨯ 10⁻⁰⁶',"NA⁻²"),
"E0":('8.854187817 ⨯ 10⁻¹²',"C²N⁻¹m⁻²"),"F":(96485.3029,'Cmol⁻¹'),"h":('6.6260755 ⨯ 10⁻³⁴',"Js"),
"Ry":('1.0973731534⨯ 10⁷','m⁻¹'),"h0":(13.605698,"eV"),"a0":('5.29177249 ⨯ 10⁻¹¹',"m")}
