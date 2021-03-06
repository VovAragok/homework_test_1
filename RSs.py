def info_Pits_end():
    # print("""Пациенту с РС, уровень EDSS ≥ 7,0 баллов, при отсутствии обострений и радиологической
    #     активности по данным МРТ втечение не менее 2-х лет Рекомендуется отмменить терапию!!!!
    #     ПИТРС!!!""")
    # print("""При субоптимальном ответе на терапию ПИТРС первой линии у пациента с РРС
    #     с уровнем EDSS ≤ 6,5 баллов, рекомендуется сменить препарат в рамках первой линии ПИТРС""")

    # print("""При развитии резистентности на терапию ПИТРС первой линии у пациентов с РРС (ВАРС, «высокоактивный РС»)
    #      с уровнем EDSS ≤ 6,5  рекомендуется ПИТРС второй линии""")
    #
    # print("""При стойком субоптимальном ответе на терапию ПИТРС первой линии у пациентов с РРС (2 и более ПИТРС
    #     первой линии) рекомендуется ПИТРС второй линии""")

    # print("""У пациентов с быстропрогрессирующим РРС с уровнем EDSS ≤ 6,5 бал. рекомендуются ПИТРС второй линии""")
    #
    # print("""У пациентов с РС с уровнем EDSS ≤ 6,5 баллов при использовании терапии ПИТРС второй линии
    #     (натализумаб, финголимод, окрелизумаб, алемтузумаб, кладрибин, митоксантрон#) и оптимальном ответе на терапию,
    #     в случае наличия высоких рисков нежелательных побочных реакций (НПР), угрожающих жизни пациента, или при
    #     наличии риска развития тяжелой инвалидизации в условиях продолжения данной терапии ПИТРС рекомендуется смена
    #      терапии на другой ПИТРС второй линии""")


    # print("""У пациентов с РС с уровнем EDSS ≤ 6,5 баллов при использовании терапии ПИТРС второй линии , при условии
    #      высокой комплаентности пациента, достаточного времени для развития эффекта терапии ПИТРС, при отсутствии
    #      оптимального ответа на терапию ПИТРС рекомендуется смена терапии на другой ПИТРС второй линии""")
    # print("""Пациентам с ВПРС с обострениями с уровнем EDSS ≤ 6,5 баллов рекомендуется назначение ПИТРС:
    #     интерферон бета-1а (для п/к введения), интерферон бета-1b, окрелизумаб, митоксантрон""")
    # print("""Пациентам с ППРС с уровнем EDSS ≤ 6,5 баллов рекомендуется назначение
    #     окрелизумаба с целью предотвращения прогрессирования РС""")

def ss():
    print("Принимает ли пациент ПИТРС?")
    print("1- не принимает")
    print("2- принимвает ПИТРС 1-линии")
    print("3- принимает ПИТРС 2- линии")
    res_cl = int(input("введите цифру "))
    while True:
        if res_cl == 1:
            print("Какое течение болезни пациента и уровень EDSS?")
            print("1- Ремитирующий РС, уровень EDSS <= 6,5")
            print("2- ППРС , уровень EDSS <= 6,5")
            print("3- ВПРС, уровень EDSS <= 6,5")
            print("4- Быстропрогрессируйщий РРС, уровень EDSS <= 6,5 ")
            res_prim = int(input("введите цифру "))
            if res_prim == 1:
                print("Всем пациентам с ремиттирующим РС с уровнем EDSS ≤ 6,5 баллов, несоответствующих критериям "
                      "быстропрогрессирующего рассеянного склероза, при первом назначении терапии ПИТРС "
                      "рекомендуется максимально раннее назначение ПИТРС первой линии:")
                print(" 1- Получить препараты первой линии")
                print("2 - Вернуться в главное меню")
                res_res = int(input("введите цифру "))
                if res_res == 1:
                    pass  #получить препараты первой линии\
                else:
                    pass  # главное меню
            if res_prim == 2:
                print("Пациентам с ППРС с уровнем EDSS ≤ 6,5 баллов рекомендуется назначение "
                      "окрелизумаба с целью предотвращения прогрессирования РС")
                print("1- Назначить необходимые препараты")
                print("2 - Вернуться в главное меню")
                res_res1 = int(input("введите цифру "))
                if res_res1 == 1:
                    pass  #назначить препарат
                else:
                    pass  # главное меню

            if res_prim == 3:
                print("Пациентам с ВПРС с обострениями с уровнем EDSS ≤ 6,5 баллов рекомендуется назначение ПИТРС:"
                      "интерферон бета-1а (для п/к введения), интерферон бета-1b, окрелизумаб, митоксантрон")
                print("вызвать данные препараты")

            if res_prim == 4:
                print("У пациентов с быстропрогрессирующим РРС с уровнем EDSS ≤ 6,5 бал. "
                      "рекомендуются ПИТРС второй линии")
                print("вызвать ПИТРС второй линии")
        if res_cl == 2:
            print("1 - развилась резистентность у пациента с РРС (ВАРС, «высокоактивный РС») с уровнем EDSS ≤ 6,5")
            print("2 - есть стойкий субоптимальный ответ у пациентов с РРС (2 и более ПИТРС 1- линии)")
            print("3 - есть субоптимальный ответ у пациента с РРС  с уровнем EDSS ≤ 6,5 баллов")
            print("4 - отсутствие обострений и рад.активности по данным МРТ , в течение не менее 2-х лет,"
                  "у пациента  с РС и уровнем EDSS ≥ 7,0 баллов")
            print("5 - главное меню")
            res_res_cl2 = int(input("введите число "))
            if res_res_cl2 == 1:
                print("назначить ПИТРС второй линни")
            if res_res_cl2 == 2:
                print("назначитб ПИТРС второй линии")
            if res_res_cl2 ==3 :
                print("сменить на другой  ПИТРС перовй линии")
            if res_res_cl2 == 4 :
                print(" следует отменить терапию ПИТРС")
            if res_res_cl2 == 5:
                print("главное меню")




        if res_cl == 3:
            print("1 - при отсутствии оптимального ответа на терапию ПИТРС у пациентов с РС с уровнем EDSS ≤ 6,5 баллов")
            print("2 -есть оптимальный ответ на терапию у  пациентов с РС с уровнем EDSS ≤ 6,5 баллов , но есть наличие"
                  "высоких рисков нежелательных побочных реакций (НПР), угрожающих жизни пациента, и есть риск "
                  "развития тяжелой инвалидизации в условиях продолжения данной терапии ПИТРС")
            print("3 - главное меню")
            res_res_cl3 = int(input("введите цифру "))
            if res_res_cl3 == 1 or res_res_cl3 ==2:
                print(" сменить препарат 2- линии")
            if res_res_cl3 == 3:
                print("главное меню")


print ("Низкодозный интерферон бета-1а 30 мкг в/в с частотой 1 раз в неделю 3-6 месяцев")

print("""Высокодозный интерферон бета-1а 44 мкг подкожно 3 раза в неделю (с 12 лет)
и интерферон бета-1b 250 мкг подкожно через день (с 18 лет) 3-6 месяцев""")
print("Пэг-интерферон (пегилированный интерферон) бета-1а 125 мкг подкожно 1 раз в 14 дней рекомендуется пациентам с РРС"
      "3-6 месяцев (с 18 лет")






                









