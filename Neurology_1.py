base_disease = ["Мигрень"]



class Neurology:
    def __init__(self, disease, phase, drugs):
        self.disease = disease
        self.phase = phase
        self.drugs = drugs


class Migraine(Neurology):
    def triptans(self):
        print("Суматриптан таб.50 мг 100мг, Элетриптан таб.40 мг, Золмитриптан таб.2.5 мг, Наратриптан таб 2.5 мг")
    def antiemetics(self):
        print("Метоклопрамид 10-20 мг внутрь, Домперидон 20-30 мг внутрь")
    def  NSAID(self):
        print("Ацетилсалициловая кислота 1000, Ибупрофен 200 - 800, Напроксен 500-1000 внутрь, "
              "Диклофенак 50-100, Парацетамол 1000 внутрь")
    def info(self):
        print(self.disease, self.phase, self.drugs)


migraine = Migraine(disease="Мигрень", phase="Обострение", drugs=["Триптаны", "НПВС", " Противорвотные"])
migraine.info()
migraine.triptans()
migraine.antiemetics()
migraine.NSAID()

if 