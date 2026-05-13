# AI Agro Bot v0.1 — Python version

def nomi_moh(m):
    mohho = {
        1: "Январ", 2: "Феврал", 3: "Март", 4: "Апрел",
        5: "Май", 6: "Июн", 7: "Июл", 8: "Август",
        9: "Сентябр", 10: "Октябр", 11: "Ноябр", 12: "Декабр"
    }
    return mohho.get(m, "Номаълум")


def nomi_ziroat(c):
    ziroatho = {
        1: "Картошка",
        2: "Пахта",
        3: "Гандум"
    }
    return ziroatho.get(c, "Номаълум")


def nomi_mintaqa(r):
    mintaqaho = {
        1: "Шимол",
        2: "Марказ",
        3: "Ҷануб"
    }
    return mintaqaho.get(r, "Номаълум")


def dar_diapazon(x, a, b):
    return a <= x <= b


def harorati_taqribi(region, month):
    data = {
        1: [0, 3, 10, 16, 22, 28, 34, 33, 25, 16, 8, 2],
        2: [1, 4, 9, 15, 20, 26, 31, 30, 22, 15, 7, 3],
        3: [5, 8, 13, 18, 24, 30, 36, 35, 28, 20, 12, 7]
    }

    if region in data and 1 <= month <= 12:
        return data[region][month - 1]

    return 20


def chopi_khat():
    print("------------------------------------------------------------")


def maslihat_kartoshka(month, temp, rain_mm, soil):
    if dar_diapazon(month, 3, 4):
        marhila = "Кишт ва оғози рушд"
    elif dar_diapazon(month, 5, 6):
        marhila = "Рушди фаъол"
    elif month == 7:
        marhila = "Дарав"
    else:
        marhila = "Берун аз мавсим"

    print("Марҳила:", marhila)

    if temp >= 30:
        print("ОГОҲӢ: Ҳарорат баланд аст (>30°C). Хатар: рушд суст, сифати лунда паст мешавад.")
    elif temp < 5:
        print("ОГОҲӢ: Ҳарорат паст аст (<5°C). Хатар: сармо ва суст сабзидан.")

    if dar_diapazon(month, 3, 4):
        if temp < 8:
            print("КИШТ: Беҳтараш интизор шав, то ҳарорат ~8–10°C шавад.")
        else:
            print("КИШТ: Вақт мувофиқ аст (агар хок аз ҳад тар набошад).")

    if dar_diapazon(month, 5, 6):
        if rain_mm >= 30:
            print("ОБДИҲӢ: Борон кофист, обро кам кун (пӯсидагӣ нашавад).")
        else:
            print("ОБДИҲӢ: Намиро баробар нигоҳ дор; субҳ/шом об деҳ.")

    if dar_diapazon(month, 4, 5):
        print("НУРӢ: Дар оғоз каме нитроген + NPK (бе зиёдатӣ).")
    elif month == 6:
        print("НУРӢ: Барои лунда калий муфид аст (агар дошта бошӣ).")

    soil_text = {
        1: "ХОК: гилолуд — обро зиёд накун, ботлоқшавӣ хатар дорад.",
        2: "ХОК: регдор — зуд хушк мешавад, кам-кам вале бештар об деҳ.",
        3: "ХОК: сергумус — хуб, тартиби об ва нуриро нигоҳ дор.",
        4: "ХОК: лойдор/миёна — барои картошка беҳтарин, реҷаи оддӣ."
    }

    print(soil_text.get(soil, "ХОК: Номаълум"))


def maslihat_pakhta(month, temp, rain_mm, soil, nav):
    if month == 4:
        marhila = "Кишт"
    elif dar_diapazon(month, 5, 6):
        marhila = "Рушди сабз"
    elif month == 7:
        marhila = "Гулкунӣ"
    elif month == 8:
        marhila = "Қуттагирӣ"
    elif dar_diapazon(month, 9, 10):
        marhila = "Пухтарасӣ ва дарав"
    else:
        marhila = "Берун аз мавсим"

    print("Марҳила:", marhila)

    if temp < 12:
        print("ОГОҲӢ: Ҳарорат паст аст (<12°C). Барои пахта хатарнок.")
    elif temp > 40:
        print("ОГОҲӢ: Гармии шадид (>40°C). Стресс ва талафи намӣ зиёд мешавад.")

    if month == 4:
        if temp < 14:
            print("КИШТ: Интизор шав то ~14°C+ шавад, то тухм хуб сабзад.")
        else:
            print("КИШТ: Вақти кишт мувофиқ аст (намии хокро таъмин кун).")

    if dar_diapazon(month, 6, 8):
        if rain_mm >= 30:
            print("ОБДИҲӢ: Борон ҳаст, обро танзим кун (зиёдатӣ нашавад).")
        else:
            if month in [7, 8]:
                print("ОБДИҲӢ: Марҳилаи муҳим (гул/қутта). Хокро хушк мондан намон!")
            else:
                print("ОБДИҲӢ: Реҷаи мунтазам; танаффуси дароз накун.")

            if temp >= 32:
                print("МАСЛИҲАТ: Субҳи барвақт ё шом об деҳ (испариш кам мешавад).")

    if dar_diapazon(month, 5, 6):
        print("НУРӢ: Нитрогенро мӯътадил деҳ (зиёдатӣ = барг зиёд, ҳосил кам).")
    elif dar_diapazon(month, 7, 8):
        print("НУРӢ: Фосфор/калий беҳтар аст; нитрогени дерро кам кун.")

    if nav == 3:
        print("НАВЪ: Дерпаз — мумкин аст то сардии тирамоҳ дер монад (хатар).")

    soil_text = {
        1: "ХОК: гилолуд — дренаж лозим, аз обдиҳии зиёдатӣ эҳтиёт.",
        2: "ХОК: регдор — об бештар, нурӣ зуд шуста мешавад.",
        3: "ХОК: сергумус — хуб, тартиби нуриро нигоҳ дор.",
        4: "ХОК: лойдор — устувор, реҷаи стандартӣ кор мекунад."
    }

    print(soil_text.get(soil, "ХОК: Номаълум"))


def maslihat_gandum(month, temp, rain_mm, soil, namud):
    if namud == 1:
        if dar_diapazon(month, 9, 10):
            marhila = "Кишт"
        elif dar_diapazon(month, 11, 12) or dar_diapazon(month, 1, 2):
            marhila = "Зимистонгузаронӣ"
        elif dar_diapazon(month, 3, 5):
            marhila = "Рушди баҳорӣ"
        elif month == 6:
            marhila = "Дарав"
        else:
            marhila = "Берун аз мавсим"
    else:
        if dar_diapazon(month, 3, 4):
            marhila = "Кишт"
        elif dar_diapazon(month, 5, 6):
            marhila = "Рушд"
        elif month == 7:
            marhila = "Дарав"
        else:
            marhila = "Берун аз мавсим"

    print("Марҳила:", marhila)

    if namud == 2 and dar_diapazon(month, 3, 4) and temp < 5:
        print("ОГОҲӢ: Барои кишти баҳорӣ ҳаво сард аст, сабзидан суст мешавад.")

    if dar_diapazon(month, 3, 5):
        if rain_mm >= 40:
            print("ОБДИҲӢ: Борон кофист, обро кам кун (касалӣ зиёд нашавад).")
        else:
            print("ОБДИҲӢ: Мӯътадил; ботлоқ накун.")

    if namud == 1 and dar_diapazon(month, 3, 4):
        print("НУРӢ: Дар баҳор нитрогенро мӯътадил ҳамчун “подкормка” деҳ.")
    elif namud == 2 and dar_diapazon(month, 4, 5):
        print("НУРӢ: Дар оғоз нитроген; агар хок камқувват бошад, фосфор/калий ҳам деҳ.")

    soil_text = {
        1: "ХОК: гилолуд — аз намии зиёдатӣ эҳтиёт (занбӯруғ хатар).",
        2: "ХОК: регдор — об ва нуриро бодиққат деҳ (зуд меравад).",
        3: "ХОК: сергумус — имкони ҳосили хуб зиёд.",
        4: "ХОК: лойдор — беҳтарин, реҷаи оддӣ."
    }

    print(soil_text.get(soil, "ХОК: Номаълум"))


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("ХАТО: Лутфан рақам ворид кун!")
        exit()


def main():
    print("АГРО-МАСЛИҲАТ (версияи 0.1) — Картошка / Пахта / Гандум")
    chopi_khat()

    print("Зироатро интихоб кун: 1=Картошка  2=Пахта  3=Гандум")
    ziroat = get_int("Ворид кун (1..3): ")

    if ziroat < 1 or ziroat > 3:
        print("ХАТО: зироат бояд 1..3 бошад!")
        return

    chopi_khat()
    print("Минтақаро интихоб кун: 1=Шимол  2=Марказ  3=Ҷануб")
    region = get_int("Ворид кун (1..3): ")

    if region < 1 or region > 3:
        print("ХАТО: минтақа бояд 1..3 бошад!")
        return

    chopi_khat()
    month = get_int("Моҳро ворид кун (1..12): ")

    if month < 1 or month > 12:
        print("ХАТО: моҳ бояд 1..12 бошад!")
        return

    chopi_khat()
    print("Навъи хок: 1=гилолуд  2=регдор  3=сергумус  4=лойдор/миёна")
    soil = get_int("Ворид кун (1..4): ")

    if soil < 1 or soil > 4:
        print("ХАТО: хок бояд 1..4 бошад!")
        return

    chopi_khat()
    temp_user = get_int("Ҳарорати миёна (°C). Агар намедонӣ 0 навис (авто): ")

    if temp_user == 0:
        temp = harorati_taqribi(region, month)
    else:
        temp = temp_user

    rain_mm = get_int("Миқдори бориш (мм) дар ин моҳ (0..300): ")

    if rain_mm < 0:
        rain_mm = 0
    elif rain_mm > 300:
        rain_mm = 300

    chopi_khat()
    print("ХУЛОСА:")
    print("  Зироат :", nomi_ziroat(ziroat))
    print("  Минтақа:", nomi_mintaqa(region))
    print("  Моҳ    :", month, f"({nomi_moh(month)})")
    print("  Ҳарорат:", temp, "°C")
    print("  Бориш  :", rain_mm, "мм")
    chopi_khat()

    if ziroat == 1:
        maslihat_kartoshka(month, temp, rain_mm, soil)

    elif ziroat == 2:
        print("Навъи пахта: 1=барвақт  2=миёнапаз  3=дерпаз")
        nav_pakhta = get_int("Ворид кун (1..3): ")

        if nav_pakhta < 1 or nav_pakhta > 3:
            print("ХАТО: навъи пахта бояд 1..3 бошад!")
            return

        chopi_khat()
        maslihat_pakhta(month, temp, rain_mm, soil, nav_pakhta)

    elif ziroat == 3:
        print("Навъи гандум: 1=тирамоҳӣ  2=баҳорӣ")
        namud_gandum = get_int("Ворид кун (1..2): ")

        if namud_gandum < 1 or namud_gandum > 2:
            print("ХАТО: навъи гандум бояд 1..2 бошад!")
            return

        chopi_khat()
        maslihat_gandum(month, temp, rain_mm, soil, namud_gandum)

    chopi_khat()
    input("Тайёр. Барои баромадан ENTER пахш кун...")


if __name__ == "__main__":
    main()
