"""spring rates"""


class KgMm:
    def to_lb(self, kg):
        lb = kg * 56
        print(round(lb, 3), "lbs/in")

    def to_nm(self, kg):
        nm = kg * 981
        print(round(nm, 3), "N/m")

    def to_nmm(self, kg):
        nmm = kg * 9.81
        print(round(nmm, 3), "N/mm")

    def to_kn(self, kg):
        knm = kg * 9.81
        print(round(knm, 3), "kN/m")


class LbIn:
    def to_kg(self, lb):
        kg = lb * 0.017858
        print(round(kg, 3), "kg/m")

    def to_nm(self, lb):
        nm = lb * 8.85075
        print(round(nm, 3), "N/m")

    def to_nmm(self, lb):
        nmm = lb * 0.1751
        print(round(nmm, 3), "N/mm")

    def to_kn(self, lb):
        kn = lb * 0.1751
        print(round(lb, 3), "kN/m")


class Nm:
    def to_kg(self, nm):
        kg =  nm * 0.00010197
        print(round(kg, 3), "kg/mm")

    def to_lb(self, nm):
        lb = nm * 0.00571015
        print(round(lb, 3), "lb/in")

    def to_nmm(self, nm):
        nmm = nm * 0.001
        print(round(nmm, 3), "N/mm")

    def to_kn(self, nm):
        kn = nm * 0.001
        print(round(kn, 3), "kN/m")


class Nmm:
    def to_kg(self, nmm):
        kg = nmm * 0.10197
        print(round(kg, 3), "kg/mm")

    def to_lb(self, nmm):
        lb = nmm * 5.7099
        print(round(lb, 3), "lb/in")

    def to_nm(self, nmm):
        nm = nmm * 1000
        print(round(nm, 3), "N/mm")

    def to_kn(self, nmm):
        kn = nmm * 1
        print(round(kn, 3), "kN/m")


class kNm:
    def to_kg(self, kn):
        kg = kn * 0.10197
        print(round(kg, 3), "kg/mm")

    def to_lb(self, kn):
        lb = kn * 5.71015
        print(round(lb, 3), "kN/m")

    def to_nm(self, kn):
        nm = kn * 1000
        print(round(nm, 3), "N/m")

    def to_nmm(self, kn):
        nmm = kn * 1
        print(round(nmm, 3), "N/mm")

nm_converter = Nm()
lb_in_converter = LbIn()
kg_mm_converter = KgMm()

nm_converter.to_lb(60000)
lb_in_converter.to_nm(448)
kg_mm_converter.to_lb(12)