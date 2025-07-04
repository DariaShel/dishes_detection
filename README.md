# Распознавание различных блюд в ресторане с помощью YOLOv11
Этот проект решает задачу детекции различных блюд.

# Загрузка видео
Для воспроизведения нарезки видео на кадры, их необходимо скачать по [ссылке](https://disk.yandex.ru/d/-VhiX2BOWdw-rg) и сохранить рядом с ноутбуком.

# Загрузка датасета
Необходимо скачать датасет по [ссылке](https://drive.google.com/drive/folders/1MGbBY7E1w4JtK1epQ-VqvTYTfnQeF5G1?usp=sharing)

Структура датасета следующая:

```
dish-detection
|__test
   |__images
      |__frame1.png
      |__.....
   |__labels
      |__frame1.txt
      |__.....
|__train
   |__images
   |__labels
|__val
   |__images
   |__labels
|__data.yaml
```

# Воспроизведение решения
Все необходимые зависимости прописаны в [ноутбуке](dishes_detection.ipynb). Для воспроизведения решения необходимо запустить все ячейки в ноутбуке.

Чтобы не повторять процедуру обучения модели прикрепляю [архив](https://drive.google.com/drive/folders/1EV9e65IrScmN1NkVUbG3WKorA9Ve6OHt?usp=sharing) с полученными весами, а также результатами тестирования. Архив необходимо скачать и положить рядом с ноутбуком, после чего можно будет воспроизвести тестирование моделей и построение графиков по полученным метрикам.

# Тестирование модели на видео
Для запуска обученной модели на видео необходимо установить следующие библиотеки:
```bash
pip install opencv-python
pip install ultralytics
```
И запустить скрипт `testing.py`:
```bash
python testing.py
```

# Результаты
Полное видео с примером детекции можно скачать [здесь](https://drive.google.com/drive/folders/1ue_FkxTGQAqX2oDi2H4VQ19m6pTVuXCS?usp=sharing)

<img src="example/example.gif" width="600" alighn="center">