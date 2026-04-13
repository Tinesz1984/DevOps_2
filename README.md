# DevOps_2
Лабораторная работа №2
---
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

и запускаем все одной командой 'kubectl apply -f k8s/' : 

<img width="742" height="223" alt="image" src="https://github.com/user-attachments/assets/1e73d2be-8c9d-4aaa-9811-f59cd48333ef" />

Кажется, все заработало! 

<img width="868" height="481" alt="image" src="https://github.com/user-attachments/assets/d5d03ddb-68e9-4c1d-b0b5-1bff46ca290c" />


