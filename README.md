# Dir_monitoring
Сервер мониторинга изменений в папках

## Описание
Сервер отслеживает изменение файлов в папках (изменение, создвание, удаление).
При изменении выводит что изменилось и новое дерево файлов и папок:


<img width="75%" alt="image" src="https://github.com/Ivan-Dorofeev/Dir_monitoring/blob/master/gif.gif">

## Установка
Для постоянного мониторинга используется библиотека --> [watchdog](https://github.com/gorakhargosh/watchdog)

## Запуск
 
  ```python monitoring_console.py ./1```

  >(./1 - указываем путь для мониторинга. По умолчанию './')
