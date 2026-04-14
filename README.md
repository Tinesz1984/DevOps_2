# Лабораторная работа №2
Выполнила Шишкова Арина, 502547 
# Часть первая 
Поднять kubernets кластер локально. 
Для выполнения этого задания я использовала три ресурса: 
  1.	ConfigMap — хранит текст сообщения.
  2.	Deployment — запускает контейнеры приложения.
  3.	Service — делает приложение доступным.

Напишем приложение, которое содержиться в файле `app.py`. Этот код обитает на порте 8080: создает простой веб сервер и при открытии возвращает текст из перменной окружения APP_MESSAGE. 

Напишем докерфайл, который просто берет готовую версию питон, ставит фласк, копирует приложение внутрь контейнера и запускает его на порте. 

Поднимаем minikube кластер(`minikube start`):

![telegram-cloud-photo-size-2-5397814597701538298-y](https://github.com/user-attachments/assets/8eb601f4-837b-4466-849c-cfd5ba344b8e)

С третьего раза собираем образ: 

![telegram-cloud-photo-size-2-5397814597701538340-y](https://github.com/user-attachments/assets/91183169-1e0b-42b6-a9fb-57283d205646)

Поднимем кластер командой `kubectl apply -f k8s/` и запустим: 

<img width="742" height="223" alt="image" src="https://github.com/user-attachments/assets/1e73d2be-8c9d-4aaa-9811-f59cd48333ef" />

Кажется, все заработало! 

<img width="868" height="481" alt="image" src="https://github.com/user-attachments/assets/d5d03ddb-68e9-4c1d-b0b5-1bff46ca290c" />

---

# Часть вторая 
Создадим helm chart вручную, как папку в папке `kuber`, содержащую обязательные файлы. 

<img width="817" height="420" alt="image" src="https://github.com/user-attachments/assets/cc44f6dc-a1e4-46b0-a560-55b24dd822b8" />

Убедимся, что образ приложения собран: 

<img width="873" height="368" alt="image" src="https://github.com/user-attachments/assets/352dabb6-e55e-4514-86b8-4235c24aa23a" />

Установим helm-chart в кластер: 

<img width="548" height="155" alt="image" src="https://github.com/user-attachments/assets/f8ce554f-e2b5-4ab4-87b6-e0da7382f665" />

Узнаем имя сервиса: 

<img width="730" height="107" alt="image" src="https://github.com/user-attachments/assets/7f2eba3b-896c-498c-8d2f-055f3c09294d" />

Получим url 

<img width="708" height="69" alt="image" src="https://github.com/user-attachments/assets/7b70d72f-51a8-4354-ad1e-12081439400b" />

и убедимся, что все работает 

<img width="636" height="273" alt="image" src="https://github.com/user-attachments/assets/e7680963-9023-4b79-82ca-f67b046aa9e5" />

Поменяем сервис с помощью апдейта релиза. Самое простое - изменить текст в `chart/values.yaml`. Заменим приветственное сообщение на анекдот про девопс. Выполним udate релиз. 

<img width="736" height="303" alt="image" src="https://github.com/user-attachments/assets/8d1f48c8-01dc-44ac-87ff-7b2d40cc2a29" />

Не знаю, противоречит это лабе или нет, но по старому url я не смогла попасть на страницу. Пришлось запросить новый. И получить: 

<img width="810" height="293" alt="image" src="https://github.com/user-attachments/assets/29524095-478b-4952-a845-6a92c117a5ec" />

---

# Причины, почему helm удобнее, чем классический деплой  

  **1. Все то, что мы изменяем расположено в одном месте**

   В первой части у нас были отдельные Kubernetes-манифесты `configmap.yaml`, `deployment.yaml`, `service.yaml`, а во второй все собрано в файле `values.yaml.` Нам не надо переписывать несколько файлов вручную, а просто изменить то, что нам нужно в одном

  **2. Обновление сервиса происходит одной командой**

Во второй части мы установили приложение как релиз: 
  ```
  helm install hello-release ./chart
  ```
  и потом обновляли его через:
  
  ```
  helm upgrade hello-release ./chart
  ```
С обычными манифестами мы бы несколько раз повторяли `kubectl apply`.

  **3. Манифесты теперь - шаблоны**

В первой части наши yaml-ки были написаны под конкретный случай. Во второй части они стали шаблонами - значит один и тот же чарт можно использовать и дальше, просто меняя параметры.


Честно, kuber оказался очень понятной и логичной структурой. Оказывается, существуют даже российские аналоги, но насколько я поняла, они просто на основе того же самого кубера интегрируют какие то новые системы, или просто дистрибутивы (VMware Tanzu, Red Hat Openshift) 
