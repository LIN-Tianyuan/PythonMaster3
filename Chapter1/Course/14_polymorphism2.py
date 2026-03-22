# Air conditioner
class AC:
    def cool_wind(self):
        """Réfrigération"""
        pass

    def hot_wind(self):
        """Chaleur"""
        pass

    def swing_l_r(self):
        """La vent souffle à droite et à gauche"""
        pass

class Midea_MC(AC):
    def cool_wind(self):
        """Réfrigération"""
        print("Climatisation et refroidissement par Midea.")

    def hot_wind(self):
        """Chaleur"""
        print("Chauffage par Midea.")

    def swing_l_r(self):
        """La vent souffle à droite et à gauche"""
        print("Les climatiseurs Midea se balancent de gauche à droite.")

class Gree_MC(AC):
    def cool_wind(self):
        """Réfrigération"""
        print("Climatisation et refroidissement par Gree.")

    def hot_wind(self):
        """Chaleur"""
        print("Chauffage par Gree.")

    def swing_l_r(self):
        """La vent souffle à droite et à gauche"""
        print("Les climatiseurs Gree se balancent de gauche à droite.")

def make_cool(ac: AC):
    ac.cool_wind()

midea_ac = Midea_MC()
gree_ac = Gree_MC()

make_cool(midea_ac)
make_cool(gree_ac)


# 抽象类：抽象类不能实例化，只能继承
# 抽象类：类里只有抽象方法的类就叫抽象类
# 抽象方法：抽象方法没有方法体，没有实现，只有方法名